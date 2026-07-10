"""Shared, dependency-free primitives for the ZEROSUM P1 pilot."""

from collections.abc import Mapping as MappingABC
from collections.abc import Sequence as SequenceABC
from dataclasses import dataclass
import datetime as _datetime
import json
import math
from numbers import Real
import os
from pathlib import Path
import re
import tempfile
from typing import Any, Dict, Iterable, List, Mapping, Optional, Sequence, Tuple, Union


RHO_GRID = (-1, -1 / 3, 1 / 3, 1)
ADVICE_CLASSES = (
    "positional",
    "welfare_optimal",
    "spite",
    "sufficiency",
    "hedged",
)
CANARY_PREFIX = "10CB-ZEROSUM-P1-20260709"

_EMPIRICAL_MODES = frozenset(("live", "empirical"))
_SHA256_RE = re.compile(r"[0-9a-fA-F]{64}")
PathLike = Union[str, Path]


def zs_design_100(delta: float) -> float:
    """Map a signed design contrast from [-1, 1] onto [0, 100]."""

    if not -1 <= delta <= 1:
        raise ValueError("delta must be in [-1, 1]")
    return 50 * (delta + 1)


def _valid_iso_date(value: str) -> bool:
    try:
        return _datetime.date.fromisoformat(value).isoformat() == value
    except (TypeError, ValueError):
        return False


def _normalized_text_sequence(values: Any) -> Optional[Tuple[str, ...]]:
    if isinstance(values, (str, bytes, bytearray)) or not isinstance(
        values, SequenceABC
    ):
        return None
    normalized = []
    for value in values:
        if not isinstance(value, str):
            return None
        normalized_value = " ".join(value.split())
        if not normalized_value:
            return None
        normalized.append(normalized_value)
    return tuple(normalized)


def _valid_count(value: Any) -> bool:
    return isinstance(value, int) and not isinstance(value, bool)


def _valid_metric(value: Any) -> bool:
    return (
        isinstance(value, Real)
        and not isinstance(value, bool)
        and math.isfinite(value)
        and 0 <= value <= 1
    )


def _valid_class_scores(values: Any) -> bool:
    if not isinstance(values, MappingABC):
        return False
    if set(values) != set(ADVICE_CLASSES):
        return False
    return all(
        _valid_metric(values[name]) and values[name] >= 0.60
        for name in ADVICE_CLASSES
    )


@dataclass(frozen=True)
class EvidenceBasis:
    """Provenance and calibration evidence used to guard empirical claims.

    Synthetic authoring records may populate this structure for provenance, but
    the gate predicates below deliberately make them ineligible for classifier
    and model claims.
    """

    mode: str
    data_basis: str
    human_labels: Optional[int]
    humans_per_response: Optional[int]
    kappa: Optional[float]
    macro_f1: Optional[float]
    class_f1: Mapping[str, Optional[float]]
    model_ids: Sequence[str]
    model_families: Sequence[str]
    vendors: Sequence[str]
    generator_family: str
    judge_families: Sequence[str]
    config_hash: str
    date: str
    lexical_accuracy: Optional[float] = None
    finetune_lift: Optional[float] = None

    @property
    def classifier_gate_eligible(self) -> bool:
        """Return whether the evidence meets the frozen classifier gate."""

        judge_families = _normalized_text_sequence(self.judge_families)
        return (
            isinstance(self.mode, str)
            and self.mode in _EMPIRICAL_MODES
            and isinstance(self.data_basis, str)
            and self.data_basis == "human"
            and _valid_count(self.human_labels)
            and self.human_labels >= 200
            and _valid_count(self.humans_per_response)
            and self.humans_per_response >= 2
            and _valid_metric(self.kappa)
            and self.kappa >= 0.70
            and _valid_metric(self.macro_f1)
            and self.macro_f1 >= 0.75
            and _valid_class_scores(self.class_f1)
            and judge_families is not None
            and len(set(judge_families)) >= 2
            and isinstance(self.generator_family, str)
            and bool(" ".join(self.generator_family.split()))
            and isinstance(self.config_hash, str)
            and _SHA256_RE.fullmatch(self.config_hash) is not None
            and _valid_iso_date(self.date)
        )

    def model_gate_eligible(self, classifier_gate_pass: bool) -> bool:
        """Return whether diverse live models may be evaluated empirically."""

        model_ids = _normalized_text_sequence(self.model_ids)
        model_families = _normalized_text_sequence(self.model_families)
        vendors = _normalized_text_sequence(self.vendors)
        roster_is_aligned = (
            model_ids is not None
            and model_families is not None
            and vendors is not None
            and len(model_ids) == len(model_families) == len(vendors)
        )
        return (
            classifier_gate_pass is True
            and self.classifier_gate_eligible
            and roster_is_aligned
            and len(set(model_ids)) >= 3
            and len(set(vendors)) >= 2
            and _valid_metric(self.lexical_accuracy)
            and self.lexical_accuracy <= 0.35
            and _valid_metric(self.finetune_lift)
            and self.finetune_lift < 0.15
        )


def write_jsonl(path: PathLike, records: Iterable[Mapping[str, Any]]) -> None:
    """Atomically write canonical UTF-8 JSONL; the parent must already exist."""

    destination = Path(path)
    parent = destination.parent
    if not parent.is_dir():
        raise FileNotFoundError("parent directory does not exist: %s" % parent)

    temporary_path = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            newline="\n",
            dir=str(parent),
            prefix=".%s." % destination.name,
            suffix=".tmp",
            delete=False,
        ) as handle:
            temporary_path = Path(handle.name)
            for record in records:
                serialized = json.dumps(
                    record,
                    ensure_ascii=False,
                    sort_keys=True,
                    separators=(",", ":"),
                    allow_nan=False,
                )
                handle.write(serialized)
                handle.write("\n")
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(str(temporary_path), str(destination))
    except BaseException:
        if temporary_path is not None:
            try:
                temporary_path.unlink()
            except FileNotFoundError:
                pass
        raise


def read_jsonl(path: PathLike) -> List[Dict[str, Any]]:
    """Read UTF-8 JSON Lines, rejecting non-object records."""

    records = []
    with Path(path).open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            if not line.strip():
                continue
            record = json.loads(line)
            if not isinstance(record, dict):
                raise ValueError("JSONL line %d is not an object" % line_number)
            records.append(record)
    return records


__all__ = [
    "ADVICE_CLASSES",
    "CANARY_PREFIX",
    "EvidenceBasis",
    "RHO_GRID",
    "read_jsonl",
    "write_jsonl",
    "zs_design_100",
]
