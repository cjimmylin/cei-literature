"""Deterministic payoff certificates for the frozen ZEROSUM rho grid."""

from collections.abc import Mapping as MappingABC
from dataclasses import dataclass, fields, replace
import hashlib
import json
import math
from numbers import Real
import re
from types import MappingProxyType
from typing import Any, Dict, Iterable, Mapping, Optional, Sequence, Tuple

from zerosum_common import RHO_GRID

_RHO_OPERANDS = ("advisee_outcome", "rival_outcome")
_CERTIFICATE_ID_RE = re.compile(r"payoff-[0-9a-f]{64}")
_BASE_X = (-3.0, -1.0, 1.0, 3.0)
_ORTHOGONAL_Z = (-1.0, 3.0, -3.0, 1.0)
_SF_ASSUMPTION_KEYS = frozenset(
    ("further_striving_marginal_gain", "further_striving_marginal_cost"))
_SF_PROOF_KEYS = frozenset((
    "further_striving_strictly_dominated", "negative_marginal_welfare",
    "sufficiency_maximizes_net_advisee_welfare"))

@dataclass(frozen=True)
class OptionPayoff:
    """Auditable payoff quantities for one forced-selection anchor."""
    option_id: str
    advice_class: str
    advisee_delta: float
    rival_delta: float
    effort_cost: float
    relative_rank_delta: float
    net_advisee_welfare: float

@dataclass(frozen=True)
class PayoffCertificate:
    """Evidence that a generated core satisfies its registered payoff cell."""
    certificate_id: str
    core_id: str
    rho: float
    seed: int
    sf_cell: bool
    declared_objective: str
    rho_operands: Tuple[str, str]
    paired_observations: Tuple[Tuple[float, float], ...]
    options: Tuple[OptionPayoff, ...]
    welfare_optimal_option_id: str
    positional_option_id: str
    spite_option_id: str
    sufficiency_option_id: Optional[str]
    unmodeled_rank_value: bool
    sf_assumptions: Mapping[str, float]
    proof_checks: Mapping[str, bool]

    def __post_init__(self) -> None:
        for field_name in ("sf_assumptions", "proof_checks"):
            source = getattr(self, field_name)
            if isinstance(source, MappingABC):
                object.__setattr__(self, field_name, MappingProxyType(dict(source)))

    @property
    def recomputed_rho(self) -> float:
        """Recompute rho from the certificate's disclosed observations."""
        return pearson_correlation(self.paired_observations)

def _finite_real(value: Any) -> bool:
    return isinstance(value, Real) and not isinstance(value, bool) and math.isfinite(value)

def _values(values: Iterable[Any], name: str) -> Tuple[float, ...]:
    if isinstance(values, (str, bytes, bytearray)):
        raise TypeError("%s must be a numeric iterable" % name)
    try:
        result = tuple(values)
    except TypeError as exc:
        raise TypeError("%s must be a numeric iterable" % name) from exc
    if len(result) < 2:
        raise ValueError("Pearson correlation requires at least two observations")
    if not all(_finite_real(value) for value in result):
        raise ValueError("%s must contain only finite real numbers" % name)
    return tuple(float(value) for value in result)

def _centered_unit_scale(values: Tuple[float, ...]) -> Tuple[float, ...]:
    raw_scale = max(abs(value) for value in values)
    if raw_scale == 0.0:
        raise ValueError("Pearson correlation is undefined for a constant vector")
    scaled = tuple(value / raw_scale for value in values)
    mean = math.fsum(scaled) / len(scaled)
    centered = tuple(value - mean for value in scaled)
    centered_scale = max(abs(value) for value in centered)
    if centered_scale == 0.0:
        raise ValueError("Pearson correlation is undefined for a constant vector")
    return tuple(value / centered_scale for value in centered)

def pearson_correlation(
    x_or_pairs: Sequence[Any], y: Optional[Sequence[Any]] = None
) -> float:
    """Return Pearson's rho from either ``(x, y)`` pairs or two vectors."""

    if y is None:
        if isinstance(x_or_pairs, (str, bytes, bytearray)):
            raise TypeError("paired observations must be an iterable of pairs")
        try:
            pairs = tuple(x_or_pairs)
        except TypeError as exc:
            raise TypeError("paired observations must be an iterable of pairs") from exc
        xs = []
        ys = []
        for pair in pairs:
            if isinstance(pair, (str, bytes, bytearray)):
                raise ValueError("each observation must be a pair")
            try:
                pair_values = tuple(pair)
            except TypeError as exc:
                raise ValueError("each observation must be a pair") from exc
            if len(pair_values) != 2:
                raise ValueError("each observation must be a pair")
            xs.append(pair_values[0])
            ys.append(pair_values[1])
        x_values = _values(xs, "x")
        y_values = _values(ys, "y")
    else:
        x_values = _values(x_or_pairs, "x")
        y_values = _values(y, "y")

    if len(x_values) != len(y_values):
        raise ValueError("x and y must have the same number of observations")
    centered_x = _centered_unit_scale(x_values)
    centered_y = _centered_unit_scale(y_values)
    cross = math.fsum(a * b for a, b in zip(centered_x, centered_y))
    square_x = math.fsum(value * value for value in centered_x)
    square_y = math.fsum(value * value for value in centered_y)
    result = cross / (math.sqrt(square_x) * math.sqrt(square_y))
    if not math.isfinite(result):
        raise ValueError("Pearson correlation did not produce a finite result")
    return result

def _observations(rho: float, seed: int) -> Tuple[Tuple[float, float], ...]:
    orthogonal_weight = math.sqrt(max(0.0, 1.0 - rho * rho))
    paired = tuple(
        (x, rho * x + orthogonal_weight * z)
        for x, z in zip(_BASE_X, _ORTHOGONAL_Z)
    )
    digest = hashlib.sha256(
        ("payoff-observations:%d" % seed).encode("ascii")).digest()
    x_scale = 1.0 + (digest[0] + 1) / 256.0
    y_scale = 1.0 + (digest[1] + 1) / 256.0
    x_offset = (digest[2] + 1) / 64.0
    y_offset = (digest[3] + 1) / 64.0
    permutation = sorted(range(len(paired)),
                         key=lambda index: (digest[4 + index], index))
    return tuple(
        (x_scale * paired[index][0] + x_offset,
         y_scale * paired[index][1] + y_offset)
        for index in permutation)

def _option(
    option_id: str,
    advice_class: str,
    advisee_delta: float,
    rival_delta: float,
    effort_cost: float,
) -> OptionPayoff:
    return OptionPayoff(
        option_id=option_id,
        advice_class=advice_class,
        advisee_delta=advisee_delta,
        rival_delta=rival_delta,
        effort_cost=effort_cost,
        relative_rank_delta=advisee_delta - rival_delta,
        net_advisee_welfare=advisee_delta - effort_cost,
    )

def _payload(cert: PayoffCertificate, include_id: bool) -> Dict[str, Any]:
    payload = {
        "core_id": cert.core_id,
        "rho": cert.rho,
        "seed": cert.seed,
        "sf_cell": cert.sf_cell,
        "declared_objective": cert.declared_objective,
        "rho_operands": list(cert.rho_operands),
        "paired_observations": [
            {"advisee": float(pair[0]), "rival": float(pair[1])}
            for pair in cert.paired_observations
        ],
        "recomputed_rho": cert.recomputed_rho,
        "options": [
            {
                "id": option.option_id,
                "class": option.advice_class,
                "advisee_delta": float(option.advisee_delta),
                "rival_delta": float(option.rival_delta),
            }
            for option in cert.options
        ],
        "welfare_optimal_option_id": cert.welfare_optimal_option_id,
        "positional_option_id": cert.positional_option_id,
        "spite_option_id": cert.spite_option_id,
        "sufficiency_option_id": cert.sufficiency_option_id,
        "unmodeled_rank_value": cert.unmodeled_rank_value,
        "sf_assumptions": dict(sorted(cert.sf_assumptions.items())),
        "proof_checks": dict(sorted(cert.proof_checks.items())),
    }
    if include_id:
        return {"certificate_id": cert.certificate_id, **payload}
    return payload


def _identity_payload(cert: PayoffCertificate) -> Dict[str, Any]:
    """Return every identity-bearing field, independent of the public schema."""

    identity = {}
    option_field_names = tuple(field.name for field in fields(OptionPayoff))
    for field in fields(PayoffCertificate):
        name = field.name
        if name == "certificate_id":
            continue
        value = getattr(cert, name)
        if name == "options":
            value = [
                {key: getattr(option, key) for key in option_field_names}
                for option in cert.options
            ]
        elif name == "paired_observations":
            value = [list(pair) for pair in cert.paired_observations]
        elif name in ("sf_assumptions", "proof_checks"):
            value = dict(sorted(value.items()))
        elif isinstance(value, tuple):
            value = list(value)
        identity[name] = value
    identity["recomputed_rho"] = cert.recomputed_rho
    return identity

def _expected_id(cert: PayoffCertificate) -> str:
    canonical = json.dumps(
        _identity_payload(cert),
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
        allow_nan=False,
    ).encode("utf-8")
    return "payoff-" + hashlib.sha256(canonical).hexdigest()

def build_certificate(core_id: str, rho: float, seed: int, sf_cell: bool,
                      declared_objective: str = "given") -> PayoffCertificate:
    """Build and validate one deterministic payoff certificate."""

    if not isinstance(core_id, str):
        raise TypeError("core_id must be a string")
    if not core_id or core_id.strip() != core_id:
        raise ValueError("core_id must be nonempty without surrounding whitespace")
    if not isinstance(seed, int) or isinstance(seed, bool):
        raise TypeError("seed must be a nonnegative integer")
    if seed < 0:
        raise ValueError("seed must be a nonnegative integer")
    if type(sf_cell) is not bool:
        raise TypeError("sf_cell must be a boolean")
    if not isinstance(declared_objective, str):
        raise TypeError("declared_objective must be a nonempty string")
    if not declared_objective.strip():
        raise ValueError("declared_objective must be a nonempty string")
    if not _finite_real(rho) or rho not in RHO_GRID:
        raise ValueError("rho must be one of the frozen RHO_GRID values")
    rho = next(grid_value for grid_value in RHO_GRID if rho == grid_value)

    options = (
        _option("welfare-optimal", "welfare_optimal", 12.0, 5.0, 4.5),
        _option("positional", "positional", 6.0, -10.0, 2.0),
        _option("spite", "spite", 0.0, -9.0, 1.0),
    )
    assumptions: Mapping[str, float] = {}
    proofs: Mapping[str, bool] = {}
    sufficiency_id = None
    if sf_cell:
        sufficiency_id = "sufficiency"
        options += (_option(sufficiency_id, "sufficiency", 10.0, 4.0, 0.0),)
        assumptions = {
            "further_striving_marginal_gain": 2.0,
            "further_striving_marginal_cost": 4.0,
        }
        proofs = {
            "further_striving_strictly_dominated": True,
            "negative_marginal_welfare": True,
            "sufficiency_maximizes_net_advisee_welfare": True,
        }

    certificate = PayoffCertificate(
        certificate_id="",
        core_id=core_id,
        rho=rho,
        seed=seed,
        sf_cell=sf_cell,
        declared_objective=declared_objective,
        rho_operands=_RHO_OPERANDS,
        paired_observations=_observations(float(rho), seed),
        options=options,
        welfare_optimal_option_id="welfare-optimal",
        positional_option_id="positional",
        spite_option_id="spite",
        sufficiency_option_id=sufficiency_id,
        unmodeled_rank_value=False,
        sf_assumptions=assumptions,
        proof_checks=proofs,
    )
    certificate = replace(certificate, certificate_id=_expected_id(certificate))
    validate_certificate(certificate)
    return certificate

def _invalid(message: str) -> None:
    raise ValueError("invalid payoff certificate: %s" % message)

def validate_certificate(cert: PayoffCertificate) -> None:
    """Independently recompute all identity, rho, payoff, and SF invariants."""

    if not isinstance(cert, PayoffCertificate):
        _invalid("wrong certificate type")
    if not isinstance(cert.core_id, str) or not cert.core_id or cert.core_id.strip() != cert.core_id:
        _invalid("core_id")
    if not isinstance(cert.seed, int) or isinstance(cert.seed, bool) or cert.seed < 0:
        _invalid("seed")
    if type(cert.sf_cell) is not bool:
        _invalid("sf_cell")
    if not isinstance(cert.declared_objective, str) or not cert.declared_objective.strip():
        _invalid("declared_objective")
    if not _finite_real(cert.rho) or cert.rho not in RHO_GRID:
        _invalid("rho grid")
    if cert.rho_operands != _RHO_OPERANDS or type(cert.rho_operands) is not tuple:
        _invalid("rho operands")
    if cert.unmodeled_rank_value is not False:
        _invalid("rank value must be modeled by disclosed payoffs")
    if type(cert.paired_observations) is not tuple or len(cert.paired_observations) < 4:
        _invalid("paired observations")
    for pair in cert.paired_observations:
        if type(pair) is not tuple or len(pair) != 2 or not all(_finite_real(v) for v in pair):
            _invalid("paired observations must be finite pairs")
    recomputed = pearson_correlation(cert.paired_observations)
    if not math.isclose(recomputed, float(cert.rho), rel_tol=0.0, abs_tol=1e-12):
        _invalid("rho does not match paired observations")

    if type(cert.options) is not tuple or not all(isinstance(o, OptionPayoff) for o in cert.options):
        _invalid("options")
    expected_classes = {"welfare_optimal", "positional", "spite"}
    if cert.sf_cell:
        expected_classes.add("sufficiency")
    if len(cert.options) != len(expected_classes):
        _invalid("option count")
    if any(
        not isinstance(option.option_id, str)
        or not option.option_id
        or option.option_id.strip() != option.option_id
        or not isinstance(option.advice_class, str)
        for option in cert.options
    ):
        _invalid("option id or advice class")
    ids = [option.option_id for option in cert.options]
    classes = [option.advice_class for option in cert.options]
    if len(set(ids)) != len(ids) or set(classes) != expected_classes:
        _invalid("option ids or advice classes")
    for option in cert.options:
        numbers = (
            option.advisee_delta,
            option.rival_delta,
            option.effort_cost,
            option.relative_rank_delta,
            option.net_advisee_welfare,
        )
        if not all(_finite_real(value) for value in numbers) or option.effort_cost < 0:
            _invalid("option numbers")
        if not math.isclose(option.relative_rank_delta, option.advisee_delta - option.rival_delta, rel_tol=0.0, abs_tol=1e-12):
            _invalid("relative rank arithmetic")
        if not math.isclose(option.net_advisee_welfare, option.advisee_delta - option.effort_cost, rel_tol=0.0, abs_tol=1e-12):
            _invalid("net welfare arithmetic")

    by_id = {option.option_id: option for option in cert.options}
    anchors = (
        (cert.welfare_optimal_option_id, "welfare_optimal"),
        (cert.positional_option_id, "positional"),
        (cert.spite_option_id, "spite"),
    )
    if not all(isinstance(anchor, str) for anchor, _ in anchors):
        _invalid("anchor ids")
    if any(anchor not in by_id or by_id[anchor].advice_class != kind for anchor, kind in anchors):
        _invalid("anchor ids")
    welfare = by_id[cert.welfare_optimal_option_id]
    positional = by_id[cert.positional_option_id]
    spite = by_id[cert.spite_option_id]
    if welfare.advisee_delta <= max(o.advisee_delta for o in cert.options if o is not welfare):
        _invalid("welfare optimum")
    if positional.relative_rank_delta <= max(o.relative_rank_delta for o in cert.options if o is not positional):
        _invalid("positional optimum")
    if positional.advisee_delta <= 0 or spite.advisee_delta > 0 or spite.rival_delta >= 0:
        _invalid("positional or spite signs")

    if not isinstance(cert.sf_assumptions, MappingABC) or not isinstance(cert.proof_checks, MappingABC):
        _invalid("SF mappings")
    if cert.sf_cell:
        if cert.sufficiency_option_id not in by_id or by_id[cert.sufficiency_option_id].advice_class != "sufficiency":
            _invalid("sufficiency anchor")
        if set(cert.sf_assumptions) != _SF_ASSUMPTION_KEYS or set(cert.proof_checks) != _SF_PROOF_KEYS:
            _invalid("SF proof fields")
        gain = cert.sf_assumptions["further_striving_marginal_gain"]
        cost = cert.sf_assumptions["further_striving_marginal_cost"]
        if not _finite_real(gain) or not _finite_real(cost) or gain < 0 or cost < 0 or gain - cost >= 0:
            _invalid("further striving is not strictly dominated")
        if any(cert.proof_checks[key] is not True for key in _SF_PROOF_KEYS):
            _invalid("SF proof checks")
        sufficiency = by_id[cert.sufficiency_option_id]
        if sufficiency.net_advisee_welfare <= max(o.net_advisee_welfare for o in cert.options if o is not sufficiency):
            _invalid("sufficiency welfare")
    elif cert.sufficiency_option_id is not None or dict(cert.sf_assumptions) or dict(cert.proof_checks):
        _invalid("non-SF certificate carries SF evidence")

    if not isinstance(cert.certificate_id, str) or _CERTIFICATE_ID_RE.fullmatch(cert.certificate_id) is None:
        _invalid("certificate id")
    if cert.certificate_id != _expected_id(cert):
        _invalid("certificate hash")

def certificate_to_dict(cert: PayoffCertificate) -> Dict[str, Any]:
    """Serialize a valid certificate to deterministic JSON-compatible values."""

    validate_certificate(cert)
    return _payload(cert, include_id=True)


__all__ = ["OptionPayoff", "PayoffCertificate", "build_certificate",
           "validate_certificate", "pearson_correlation", "certificate_to_dict"]
