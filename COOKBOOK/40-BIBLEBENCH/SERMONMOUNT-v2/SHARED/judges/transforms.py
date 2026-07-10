"""Deterministic identity masking with exact parent and span-map lineage."""
from __future__ import annotations

from collections import defaultdict
from typing import Any, Mapping, Sequence
import unicodedata

from canonical import CanonicalSnapshot, content_hash, evidence_hash


class IdentityMaskError(ValueError):
    """An identity-mask transform is malformed or does not reproduce its view."""


VIEW_FIELDS = {"parent_evidence_hash", "transform", "task", "response"}
SPAN_INPUT_FIELDS = {"path", "source_start", "source_end", "replacement"}
SPAN_FIELDS = SPAN_INPUT_FIELDS | {"derived_start", "derived_end"}
ALLOWED_IDENTITY_PLACEHOLDERS = frozenset(
    {
        "<MODEL_ID>",
        "<PROVIDER_ID>",
        "<FAMILY_ID>",
        "<ARM_ID>",
        "<CONDITION_ID>",
    }
)


def _object(value: Mapping[str, Any], field: str) -> dict:
    if not isinstance(value, Mapping):
        raise IdentityMaskError(f"{field} must be an object")
    copied = CanonicalSnapshot.capture(dict(value)).to_object()
    if not isinstance(copied, dict):  # pragma: no cover
        raise AssertionError("mapping snapshot invariant")
    return copied


def _validate_raw_view(raw: dict) -> None:
    if set(raw) != VIEW_FIELDS:
        raise IdentityMaskError("raw parent view fields are not exact")
    if raw["parent_evidence_hash"] is not None or raw["transform"] is not None:
        raise IdentityMaskError("raw parent must have null parent/transform lineage")
    if not isinstance(raw["task"], dict) or not isinstance(raw["response"], dict):
        raise IdentityMaskError("raw parent task/response must be objects")


def _text_at(view: dict, path: str) -> str:
    if not isinstance(path, str) or not path or path.split(".")[0] not in {"task", "response"}:
        raise IdentityMaskError(f"unsupported span path:{path}")
    current: Any = view
    for part in path.split("."):
        if not isinstance(current, dict) or part not in current:
            raise IdentityMaskError(f"span path missing:{path}")
        current = current[part]
    if not isinstance(current, str):
        raise IdentityMaskError(f"span path is not text:{path}")
    return current


def _set_text(view: dict, path: str, text: str) -> None:
    parts = path.split(".")
    current = view
    for part in parts[:-1]:
        current = current[part]
    current[parts[-1]] = text


def _normalize_identity_tokens(
    identity_tokens: Mapping[str, Sequence[str]],
) -> dict:
    if not isinstance(identity_tokens, Mapping) or not identity_tokens:
        raise IdentityMaskError("identity token authorization is required")
    normalized = {}
    token_owner = {}
    for placeholder, values in identity_tokens.items():
        if placeholder not in ALLOWED_IDENTITY_PLACEHOLDERS:
            raise IdentityMaskError(f"unsupported typed identity placeholder:{placeholder}")
        if not isinstance(values, (list, tuple)) or not values:
            raise IdentityMaskError(f"identity tokens missing for {placeholder}")
        normalized_values = []
        for value in values:
            if not isinstance(value, str) or not value.strip():
                raise IdentityMaskError("expected source identity tokens must be nonblank")
            token = unicodedata.normalize("NFKC", value).casefold()
            if token in token_owner and token_owner[token] != placeholder:
                raise IdentityMaskError("identity token maps to multiple placeholder types")
            token_owner[token] = placeholder
            normalized_values.append(token)
        normalized[placeholder] = tuple(sorted(set(normalized_values)))
    return normalized


def mask_identity_spans(
    raw_view: Mapping[str, Any],
    spans: Sequence[Mapping[str, Any]],
    *,
    transform_version: str,
    identity_tokens: Mapping[str, Sequence[str]],
) -> dict:
    """Return a derived copy; the raw parent is never modified."""

    raw = _object(raw_view, "raw_view")
    _validate_raw_view(raw)
    if not isinstance(transform_version, str) or not transform_version.strip():
        raise IdentityMaskError("transform_version must be nonblank")
    if not isinstance(spans, (list, tuple)) or not spans:
        raise IdentityMaskError("span_map must be a non-empty sequence")
    authorized_tokens = _normalize_identity_tokens(identity_tokens)

    grouped = defaultdict(list)
    for index, span_value in enumerate(spans):
        span = _object(span_value, f"spans[{index}]")
        if set(span) != SPAN_INPUT_FIELDS:
            raise IdentityMaskError(f"spans[{index}] fields are not exact")
        path = span["path"]
        source = _text_at(raw, path)
        start, end = span["source_start"], span["source_end"]
        if (
            isinstance(start, bool)
            or isinstance(end, bool)
            or not isinstance(start, int)
            or not isinstance(end, int)
            or start < 0
            or end <= start
            or end > len(source)
        ):
            raise IdentityMaskError(f"spans[{index}] bounds are invalid")
        if not isinstance(span["replacement"], str) or not span["replacement"]:
            raise IdentityMaskError(f"spans[{index}] replacement must be non-empty")
        grouped[path].append(span)

    derived = _object(raw, "raw_view")
    output_spans = []
    for path in sorted(grouped):
        source = _text_at(raw, path)
        ordered = sorted(grouped[path], key=lambda row: row["source_start"])
        previous_end = -1
        for span in ordered:
            if span["source_start"] < previous_end:
                raise IdentityMaskError(
                    f"span overlap at {path}:{span['source_start']}"
                )
            previous_end = span["source_end"]

        delta = 0
        fragments = []
        cursor = 0
        for span in ordered:
            start, end = span["source_start"], span["source_end"]
            placeholder = span["replacement"]
            if placeholder not in ALLOWED_IDENTITY_PLACEHOLDERS:
                raise IdentityMaskError(
                    f"replacement is not an allowed typed identity placeholder:{placeholder}"
                )
            selected = unicodedata.normalize("NFKC", source[start:end]).casefold()
            if selected not in authorized_tokens.get(placeholder, ()):
                raise IdentityMaskError(
                    f"selected span is not an authorized identity-bearing token:{path}:{start}"
                )
            fragments.extend((source[cursor:start], span["replacement"]))
            derived_start = start + delta
            derived_end = derived_start + len(span["replacement"])
            output_spans.append(
                {
                    **span,
                    "derived_start": derived_start,
                    "derived_end": derived_end,
                }
            )
            delta += len(span["replacement"]) - (end - start)
            cursor = end
        fragments.append(source[cursor:])
        _set_text(derived, path, "".join(fragments))

    parent_hash = evidence_hash(raw)
    transform = {
        "transform_type": "identity_mask",
        "transform_version": transform_version,
        "identity_token_commitment": content_hash(
            {
                placeholder: list(tokens)
                for placeholder, tokens in sorted(authorized_tokens.items())
            }
        ),
        "span_map": output_spans,
    }
    transform["transform_hash"] = content_hash(
        {"parent_evidence_hash": parent_hash, **transform}
    )
    derived["parent_evidence_hash"] = parent_hash
    derived["transform"] = transform
    return derived


def validate_transformed_view(
    derived_view: Mapping[str, Any],
    raw_parent_view: Mapping[str, Any],
    *,
    identity_tokens: Mapping[str, Sequence[str]],
) -> bool:
    """Reproduce every replacement and reject any unregistered neighboring edit."""

    derived = _object(derived_view, "derived_view")
    raw = _object(raw_parent_view, "raw_parent_view")
    _validate_raw_view(raw)
    if set(derived) != VIEW_FIELDS:
        raise IdentityMaskError("derived view fields are not exact")
    if derived.get("parent_evidence_hash") != evidence_hash(raw):
        raise IdentityMaskError("parent evidence hash does not match raw parent")
    transform = derived.get("transform")
    if not isinstance(transform, dict) or set(transform) != {
        "transform_type",
        "transform_version",
        "identity_token_commitment",
        "span_map",
        "transform_hash",
    }:
        raise IdentityMaskError("transform envelope fields are not exact")
    if transform["transform_type"] != "identity_mask":
        raise IdentityMaskError("unsupported transform type")
    authorized_tokens = _normalize_identity_tokens(identity_tokens)
    expected_commitment = content_hash(
        {
            placeholder: list(tokens)
            for placeholder, tokens in sorted(authorized_tokens.items())
        }
    )
    if transform["identity_token_commitment"] != expected_commitment:
        raise IdentityMaskError("identity token commitment mismatch")
    span_map = transform["span_map"]
    if not isinstance(span_map, list) or not span_map:
        raise IdentityMaskError("span_map must be non-empty")
    for index, span in enumerate(span_map):
        if not isinstance(span, dict) or set(span) != SPAN_FIELDS:
            raise IdentityMaskError(f"span_map[{index}] fields are not exact")
    supplied_hash = transform["transform_hash"]
    payload = {key: value for key, value in transform.items() if key != "transform_hash"}
    expected_hash = content_hash(
        {"parent_evidence_hash": evidence_hash(raw), **payload}
    )
    if supplied_hash != expected_hash:
        raise IdentityMaskError("transform hash mismatch")

    input_spans = [
        {key: span[key] for key in SPAN_INPUT_FIELDS}
        for span in span_map
    ]
    reproduced = mask_identity_spans(
        raw,
        input_spans,
        transform_version=transform["transform_version"],
        identity_tokens=identity_tokens,
    )
    if reproduced != derived:
        raise IdentityMaskError("span coverage does not reproduce the derived view")
    return True
