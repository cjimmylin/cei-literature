"""Private latent-evidence records for CHARITROC.

This module contains only symbolic design state.  Surface wording belongs in
``cue_surfaces.py`` and the family/template registries.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass

from lib import families


TRUE_TYPES = ("benign", "malicious")
CUE_VARIANTS = ("strong", "weak", "absent", "adversarial")
SIGNAL_BANDS = ("low", "mixed", "high")
BASE_RATES = (0.2, 0.5, 0.8)

_STRENGTH = {
    "strong": "strong",
    "weak": "weak",
    "absent": "none",
    "adversarial": "discount_to_zero",
}
_RELIABILITY = {
    "strong": "authenticated",
    "weak": "partial",
    "absent": "unavailable",
    "adversarial": "defeated",
}
_PERMITTED_UPDATE = {
    "strong": "strong_truthward",
    "weak": "one_step_truthward",
    "absent": "stable_no_new_information",
    "adversarial": "stable_defeated_premise",
}


@dataclass(frozen=True)
class EvidenceRecord:
    family: str
    true_type: str
    cue_variant: str
    signal_band: str
    base_rate: float
    proposition_id: str
    source_id: str
    reliability: str
    strength: str
    posterior_direction: int
    permitted_update: str
    defeat_class: str
    indistinguishable_control: bool


def _require_member(field: str, value, allowed) -> None:
    if value not in allowed:
        raise ValueError(
            f"{field} must be one of {tuple(allowed)!r}; got {value!r}"
        )


def build(*, family: str, true_type: str, cue: str, signal_band: str,
          base_rate: float, indistinguishable_control: bool = False) -> dict:
    """Return one validated, JSON-safe latent record."""
    family_codes = tuple(spec["code"] for spec in families.all_families())
    _require_member("family", family, family_codes)
    _require_member("true_type", true_type, TRUE_TYPES)
    _require_member("cue", cue, CUE_VARIANTS)
    _require_member("signal_band", signal_band, SIGNAL_BANDS)
    _require_member("base_rate", base_rate, BASE_RATES)
    if type(indistinguishable_control) is not bool:
        raise ValueError("indistinguishable_control must be a boolean")
    if indistinguishable_control and cue != "absent":
        raise ValueError(
            "indistinguishable_control is valid only for an absent cue"
        )

    direction = 0
    if cue in ("strong", "weak"):
        direction = 1 if true_type == "benign" else -1
    stem = family.lower()
    record = EvidenceRecord(
        family=family,
        true_type=true_type,
        cue_variant=cue,
        signal_band=signal_band,
        base_rate=base_rate,
        proposition_id=f"proposition-{stem}-v1",
        source_id=f"source-{stem}-{cue}-v1",
        reliability=_RELIABILITY[cue],
        strength=_STRENGTH[cue],
        posterior_direction=direction,
        permitted_update=_PERMITTED_UPDATE[cue],
        defeat_class=families.DEFEAT_CLASS[cue],
        indistinguishable_control=indistinguishable_control,
    )
    return asdict(record)
