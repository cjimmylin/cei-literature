"""Private occurrence-level issuance for blinded follow-through judging.

Authoring ``JSEED`` values authorize issuance but never cross the judge
boundary.  A fresh cryptographic UUIDv4 ``JCASE`` is created for one exact
scoring occurrence and bound to the response hash in an append-only,
hash-chained private registry.
"""
from __future__ import annotations

from collections.abc import Callable, Mapping
from copy import deepcopy
import fcntl
import hashlib
import json
import os
from pathlib import Path
import re
import stat
import uuid


_UUID4_BODY = (
    r"[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-"
    r"[89ab][0-9a-f]{3}-[0-9a-f]{12}"
)
JSEED_RE = re.compile(rf"^JSEED-{_UUID4_BODY}$")
JCASE_RE = re.compile(rf"^JCASE-{_UUID4_BODY}$")
JUDGE_RE = re.compile(rf"^JUDGE-{_UUID4_BODY}$")
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
SCHEMA_VERSION = "crossroads-jcase-registry-v1"
_ZERO_HASH = "0" * 64
_RECORD_FIELDS = {
    "schema_version", "sequence", "judge_case_id", "authoring_seed",
    "item_id", "run_id", "execution_id", "candidate_model_snapshot",
    "candidate_family", "response_sha256", "scoring_occurrence",
    "previous_record_sha256", "record_sha256",
}


def _canonical_bytes(value: object) -> bytes:
    try:
        text = json.dumps(
            value, sort_keys=True, separators=(",", ":"),
            ensure_ascii=False, allow_nan=False,
        )
    except (TypeError, ValueError):
        raise ValueError("judge registry values must be canonical JSON") from None
    return text.encode("utf-8")


def canonical_response_sha256(transcript: list, observable_artifacts: list) -> str:
    """Hash the exact observable candidate output sent to a judge."""
    if type(transcript) is not list or type(observable_artifacts) is not list:
        raise TypeError("response observables must be lists")
    return hashlib.sha256(_canonical_bytes({
        "observable_artifacts": observable_artifacts,
        "transcript": transcript,
    })).hexdigest()


def _nonempty(value: object, label: str) -> str:
    if type(value) is not str or not value.strip():
        raise ValueError(f"{label} must be non-empty text")
    return value


def _occurrence_key(record: Mapping) -> tuple:
    return (
        record["run_id"], record["execution_id"],
        record["candidate_model_snapshot"], record["item_id"],
        record["response_sha256"], record["scoring_occurrence"],
    )


class OccurrenceCaseRegistry:
    """Append-only private JCASE crosswalk for one or more scoring runs."""

    def __init__(
        self,
        path: Path,
        authoring_seed_map: Mapping[str, str],
        *,
        uuid_factory: Callable[[], object] = uuid.uuid4,
    ) -> None:
        self.path = Path(path)
        if self.path.is_symlink():
            raise ValueError("judge case registry must not be a symlink")
        if (self.path.exists()
                and stat.S_IMODE(self.path.stat().st_mode) != 0o600):
            raise ValueError("existing judge case registry must use mode 0600")
        if not isinstance(authoring_seed_map, Mapping) or not authoring_seed_map:
            raise ValueError("authoring seed map must be non-empty")
        seeds: dict[str, str] = {}
        items: dict[str, str] = {}
        for seed, item_id in authoring_seed_map.items():
            if type(seed) is not str or JSEED_RE.fullmatch(seed) is None:
                raise ValueError("authoring tokens must use JSEED-<UUIDv4>")
            _nonempty(item_id, "authoring seed item_id")
            if seed in seeds or item_id in items:
                raise ValueError("authoring JSEED mappings must be one-to-one")
            seeds[seed] = item_id
            items[item_id] = seed
        if not callable(uuid_factory):
            raise TypeError("uuid_factory must be callable")
        self._seed_map = seeds
        self._uuid_factory = uuid_factory
        self._records: dict[str, dict] = {}
        self._occurrences: set[tuple] = set()
        self._tail_hash = _ZERO_HASH
        if self.path.exists():
            self._load_text(self.path.read_text(encoding="utf-8"))

    def _record_hash(self, record: Mapping) -> str:
        body = {key: value for key, value in record.items()
                if key != "record_sha256"}
        return hashlib.sha256(_canonical_bytes(body)).hexdigest()

    def _validate_record(
        self, record: object, *, expected_sequence: int, previous_hash: str,
    ) -> dict:
        if type(record) is not dict or set(record) != _RECORD_FIELDS:
            raise ValueError("judge case registry record fields differ")
        if record["schema_version"] != SCHEMA_VERSION:
            raise ValueError("judge case registry schema version differs")
        if record["sequence"] != expected_sequence:
            raise ValueError("judge case registry sequence differs")
        case_id = record["judge_case_id"]
        if type(case_id) is not str or JCASE_RE.fullmatch(case_id) is None:
            raise ValueError("registry judge_case_id must be JCASE-<UUIDv4>")
        seed = record["authoring_seed"]
        if self._seed_map.get(seed) != record["item_id"]:
            raise ValueError("registry JSEED/item binding differs from authoring map")
        for field in (
            "run_id", "execution_id", "candidate_model_snapshot",
            "candidate_family", "item_id",
        ):
            _nonempty(record[field], f"registry {field}")
        if (type(record["response_sha256"]) is not str
                or SHA256_RE.fullmatch(record["response_sha256"]) is None):
            raise ValueError("registry response_sha256 must be lowercase SHA-256")
        if (type(record["scoring_occurrence"]) is not int
                or record["scoring_occurrence"] < 0):
            raise ValueError("scoring_occurrence must be a nonnegative integer")
        if record["previous_record_sha256"] != previous_hash:
            raise ValueError("judge case registry hash chain differs")
        if record["record_sha256"] != self._record_hash(record):
            raise ValueError("judge case registry record hash differs")
        return record

    def _load_text(self, text: str) -> None:
        records: dict[str, dict] = {}
        occurrences: set[tuple] = set()
        previous = _ZERO_HASH
        if text and not text.endswith("\n"):
            raise ValueError("judge case registry has a truncated final record")
        for sequence, line in enumerate(text.splitlines(), 1):
            if not line:
                raise ValueError("judge case registry contains a blank record")
            try:
                decoded = json.loads(line)
            except json.JSONDecodeError:
                raise ValueError("judge case registry contains invalid JSON") from None
            record = self._validate_record(
                decoded, expected_sequence=sequence, previous_hash=previous,
            )
            case_id = record["judge_case_id"]
            occurrence = _occurrence_key(record)
            if case_id in records:
                raise ValueError("judge case registry reuses a JCASE token")
            if occurrence in occurrences:
                raise ValueError("judge case registry reuses a scoring occurrence")
            records[case_id] = record
            occurrences.add(occurrence)
            previous = record["record_sha256"]
        self._records = records
        self._occurrences = occurrences
        self._tail_hash = previous

    def _new_case_id(self) -> str:
        raw = self._uuid_factory()
        try:
            parsed = raw if isinstance(raw, uuid.UUID) else uuid.UUID(str(raw))
        except (ValueError, AttributeError, TypeError):
            raise ValueError("uuid_factory must return an RFC-4122 UUIDv4") from None
        if parsed.version != 4 or parsed.variant != uuid.RFC_4122:
            raise ValueError("uuid_factory must return an RFC-4122 UUIDv4")
        value = f"JCASE-{parsed}"
        if JCASE_RE.fullmatch(value) is None:
            raise AssertionError("generated JCASE failed namespace validation")
        return value

    def issue_case(
        self,
        *,
        authoring_seed: str,
        run_id: str,
        execution_id: str,
        candidate_model_snapshot: str,
        candidate_family: str,
        response_sha256: str,
        scoring_occurrence: int,
    ) -> str:
        """Create one fresh blind token and durably bind its occurrence."""
        if authoring_seed not in self._seed_map:
            raise ValueError("unknown authoring JSEED")
        for value, label in (
            (run_id, "run_id"), (execution_id, "execution_id"),
            (candidate_model_snapshot, "candidate_model_snapshot"),
            (candidate_family, "candidate_family"),
        ):
            _nonempty(value, label)
        if type(response_sha256) is not str or SHA256_RE.fullmatch(
                response_sha256) is None:
            raise ValueError("response_sha256 must be lowercase SHA-256")
        if type(scoring_occurrence) is not int or scoring_occurrence < 0:
            raise ValueError("scoring_occurrence must be a nonnegative integer")
        self.path.parent.mkdir(parents=True, exist_ok=True)
        flags = os.O_CREAT | os.O_APPEND | os.O_RDWR
        if hasattr(os, "O_NOFOLLOW"):
            flags |= os.O_NOFOLLOW
        fd = os.open(self.path, flags, 0o600)
        os.fchmod(fd, 0o600)
        with os.fdopen(fd, "a+", encoding="utf-8") as handle:
            fcntl.flock(handle.fileno(), fcntl.LOCK_EX)
            handle.seek(0)
            self._load_text(handle.read())
            item_id = self._seed_map[authoring_seed]
            provisional = {
                "schema_version": SCHEMA_VERSION,
                "sequence": len(self._records) + 1,
                "judge_case_id": "",
                "authoring_seed": authoring_seed,
                "item_id": item_id,
                "run_id": run_id,
                "execution_id": execution_id,
                "candidate_model_snapshot": candidate_model_snapshot,
                "candidate_family": candidate_family,
                "response_sha256": response_sha256,
                "scoring_occurrence": scoring_occurrence,
                "previous_record_sha256": self._tail_hash,
                "record_sha256": "",
            }
            occurrence = _occurrence_key(provisional)
            if occurrence in self._occurrences:
                raise ValueError("scoring occurrence was already issued a JCASE")
            case_id = self._new_case_id()
            if case_id in self._records:
                raise ValueError("JCASE collision; refusing token reuse")
            provisional["judge_case_id"] = case_id
            provisional["record_sha256"] = self._record_hash(provisional)
            handle.seek(0, os.SEEK_END)
            handle.write(_canonical_bytes(provisional).decode("utf-8") + "\n")
            handle.flush()
            os.fsync(handle.fileno())
            self._records[case_id] = provisional
            self._occurrences.add(occurrence)
            self._tail_hash = provisional["record_sha256"]
            fcntl.flock(handle.fileno(), fcntl.LOCK_UN)
        return case_id

    def lookup(self, judge_case_id: str) -> dict:
        if type(judge_case_id) is not str or JCASE_RE.fullmatch(
                judge_case_id) is None:
            raise ValueError("case lookup requires JCASE-<UUIDv4>")
        try:
            return deepcopy(self._records[judge_case_id])
        except KeyError:
            raise ValueError("unknown JCASE in private occurrence registry") from None

    def assert_response_binding(
        self, judge_case_id: str, response_sha256: str,
    ) -> dict:
        record = self.lookup(judge_case_id)
        if record["response_sha256"] != response_sha256:
            raise ValueError("response hash does not match the issued JCASE")
        return record
