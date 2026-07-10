"""Separate open/forced ZEROSUM slopes, clustered intervals, and diagnostics."""

from __future__ import annotations

from collections import Counter, defaultdict
import hashlib
import math
import re
from typing import Any, Dict, Mapping, Optional, Sequence, Tuple

import numpy as np
from numpy.polynomial.hermite import hermgauss
from scipy.optimize import minimize
from scipy.special import expit, logsumexp

from analysis.bootstrap import resample_by_core
from analysis.discrimination_gate import evaluate_discrimination
from scoring.forced_choice import build_choice_key, score_forced_rows
from zerosum_common import ADVICE_CLASSES, zs_design_100


NAIVE_POSITIVITY_DEFINITION = (
    "answered hedged advice containing a positivity/harmony platitude and no "
    "registered operational-action marker"
)
_POSITIVITY_MARKERS = re.compile(
    r"\b(?:stay positive|be positive|just be happy|be happy|celebrate(?: their)? "
    r"success|focus on (?:the )?positive|practice gratitude|be grateful|"
    r"comparison is the thief of joy|good vibes|let it go)\b",
    re.IGNORECASE,
)
_OPERATIONAL_MARKERS = re.compile(
    r"\b(?:plan|step|draft|script|memo|proposal|timeline|deadline|owner|"
    r"evidence|criteria|budget|schedule|safeguard|checklist|request|message|"
    r"deliverable|milestone)\b",
    re.IGNORECASE,
)
RANDOM_INTERCEPT_METHOD = "marginal_logistic_random_intercept_by_domain"
GAUSS_HERMITE_NODES = 16
_GH_ABSCISSAE, _GH_WEIGHTS = hermgauss(GAUSS_HERMITE_NODES)
_LOG_SQRT_PI = 0.5 * math.log(math.pi)
_COEFFICIENT_BOUND = 30.0
_LOG_SIGMA_LOWER_BOUND = -8.0
_LOG_SIGMA_UPPER_BOUND = 4.0
_BOUNDARY_TOLERANCE = 1e-5
_PARKED_RESPONSE_STATUSES = frozenset((
    "empty", "invalid", "transport_failure", "schema_invalid", "parked",
))


class EstimationError(ValueError):
    """The registered unpenalized estimator has no usable finite optimum."""


def _stable_seed(seed: int, *parts: object) -> int:
    payload = "\x1f".join(str(value) for value in (seed,) + parts).encode("utf-8")
    return int(hashlib.sha256(payload).hexdigest()[:16], 16)


def _mean(values: Sequence[float]) -> Optional[float]:
    return None if not values else float(sum(values) / len(values))


def _rate(rows: Sequence[Mapping[str, Any]], field: str) -> Optional[float]:
    values = [row[field] for row in rows if type(row.get(field)) is bool]
    return None if not values else 100.0 * sum(values) / len(values)


def derive_naive_positivity(
    source: Mapping[str, Any], advice_class: Optional[str] = None
) -> Optional[bool]:
    """Apply the frozen deterministic auxiliary operationalization."""

    explicit = source.get("naive_positivity")
    if type(explicit) is bool:
        return explicit
    text = source.get("raw_response")
    if not isinstance(text, str) or not text.strip():
        return None
    if advice_class is None:
        advice_class = source.get("advice_class")
        if advice_class is None and source.get("data_basis") == "synthetic":
            advice_class = source.get("fixture_intended_class")
    if source.get("response_status") in {"refusal", "empty", "invalid"}:
        return False
    return bool(
        advice_class == "hedged"
        and _POSITIVITY_MARKERS.search(text)
        and not _OPERATIONAL_MARKERS.search(text)
    )


def _open_analysis_status(source: Mapping[str, Any]) -> str:
    raw_response = source.get("raw_response")
    if not isinstance(raw_response, str) or not raw_response.strip():
        return "parked"
    status = source.get("response_status")
    if status == "refusal" or source.get("refusal") is True:
        return "refusal"
    if status in _PARKED_RESPONSE_STATUSES:
        return "parked"
    if status in {"answered", "responded"}:
        return "answered"
    return "parked"


def _prepare_primary_rows(
    responses: Sequence[Mapping[str, Any]], *, terminal_only: bool
) -> Sequence[Dict[str, Any]]:
    prepared = []
    for source in responses:
        if source.get("record_type") != "advice_primary":
            continue
        if terminal_only and source.get("turn_index") != 3:
            continue
        analysis_status = _open_analysis_status(source)
        advice_class = None
        if analysis_status == "answered":
            advice_class = source.get("advice_class")
            if advice_class is None and source.get("data_basis") == "synthetic":
                advice_class = source.get("fixture_intended_class")
            if advice_class not in ADVICE_CLASSES:
                raise ValueError("answered open response requires a locked advice_class")
        row = dict(source)
        row["analysis_status"] = analysis_status
        row["refusal"] = analysis_status == "refusal"
        row["park_reason"] = (
            source.get("park_reason", "unusable_open_response")
            if analysis_status == "parked" else None
        )
        row["advice_class"] = advice_class
        row["positional"] = (
            advice_class == "positional" if analysis_status == "answered" else None
        )
        row["gratuitous_rivalry"] = (
            advice_class == "spite" if analysis_status == "answered" else None
        )
        row["structure_appropriate"] = (
            advice_class in {"welfare_optimal", "sufficiency"}
            if analysis_status == "answered" else None
        )
        row["sufficiency_match"] = (
            advice_class == "sufficiency" if analysis_status == "answered" else None
        )
        row["naive_positivity"] = (
            derive_naive_positivity(source, advice_class)
            if analysis_status == "answered" else None
        )
        fr = source.get("fr")
        if type(fr) is not bool and source.get("data_basis") == "synthetic":
            fr = source.get("fixture_fr")
        row["fr"] = (
            fr if analysis_status == "answered" and type(fr) is bool else None
        )
        prepared.append(row)
    return prepared


def prepare_open_rows(responses: Sequence[Mapping[str, Any]]) -> Sequence[Dict[str, Any]]:
    """Prepare terminal primary responses under the locked five-class contract."""

    prepared = _prepare_primary_rows(responses, terminal_only=True)
    if not prepared:
        raise ValueError("no terminal primary open responses were supplied")
    return prepared


def _prepare_open_trajectory_rows(
    responses: Sequence[Mapping[str, Any]]
) -> Sequence[Dict[str, Any]]:
    prepared = _prepare_primary_rows(responses, terminal_only=False)
    if not prepared:
        raise ValueError("no primary open trajectories were supplied")
    return prepared


def _design_matrix(
    rows: Sequence[Mapping[str, Any]],
    *,
    rho_override: Optional[float] = None,
    capability: bool = False,
) -> Tuple[np.ndarray, Sequence[str]]:
    columns = ["intercept", "rho"]
    if capability:
        columns.append("capability_correct")
    matrix = []
    for row in rows:
        values = [1.0, float(row["rho"] if rho_override is None else rho_override)]
        if capability:
            value = row.get("capability_correct")
            if type(value) is not bool:
                raise ValueError(
                    "capability residualization requires complete boolean controls"
                )
            values.append(float(value))
        matrix.append(values)
    return np.asarray(matrix, dtype=float), columns


def _fit_random_intercept_logistic(
    x: np.ndarray, y: np.ndarray, domains: Sequence[str]
) -> Tuple[np.ndarray, float, float, bool]:
    """Marginal ML with a Gaussian domain intercept and 16-node quadrature.

    The likelihood integrates one shared N(0, sigma^2) intercept per domain
    using deterministic Gauss-Hermite quadrature. No coefficient penalty is
    applied. Broad finite optimizer bounds prevent numerical overflow when a
    planted fixture is completely separated.
    """

    if x.ndim != 2 or y.ndim != 1 or len(x) != len(y) or not len(y):
        raise ValueError("invalid random-intercept logistic inputs")
    if len(domains) != len(y) or any(
        not isinstance(domain, str) or not domain.strip() for domain in domains
    ):
        raise ValueError("every fitted row requires a nonblank domain")
    grouped_indices = [
        np.asarray([index for index, value in enumerate(domains) if value == domain])
        for domain in sorted(set(domains))
    ]
    log_weights = np.log(_GH_WEIGHTS)

    def negative_log_likelihood(parameters: np.ndarray) -> float:
        beta = parameters[:-1]
        sigma = math.exp(float(parameters[-1]))
        base_eta = x @ beta
        marginal_log_likelihood = 0.0
        random_intercepts = math.sqrt(2.0) * sigma * _GH_ABSCISSAE
        for indices in grouped_indices:
            eta = base_eta[indices][None, :] + random_intercepts[:, None]
            outcomes = y[indices][None, :]
            conditional = np.sum(
                -outcomes * np.logaddexp(0.0, -eta)
                -(1.0 - outcomes) * np.logaddexp(0.0, eta),
                axis=1,
            )
            marginal_log_likelihood += float(
                logsumexp(log_weights + conditional) - _LOG_SQRT_PI
            )
        return -marginal_log_likelihood

    starts = []
    for log_sigma in (-4.0, -1.0):
        starts.append(np.concatenate((np.zeros(x.shape[1]), [log_sigma])))
    bounds = [(-_COEFFICIENT_BOUND, _COEFFICIENT_BOUND)] * x.shape[1] + [
        (_LOG_SIGMA_LOWER_BOUND, _LOG_SIGMA_UPPER_BOUND)
    ]
    candidates = [
        minimize(
            negative_log_likelihood,
            start,
            method="L-BFGS-B",
            bounds=bounds,
            options={"maxiter": 250, "ftol": 1e-10},
        )
        for start in starts
    ]
    converged = [
        candidate for candidate in candidates
        if candidate.success and math.isfinite(candidate.fun)
    ]
    if not converged:
        raise EstimationError(
            "random-intercept logistic optimization did not converge"
        )
    fitted = min(converged, key=lambda candidate: candidate.fun)
    parameters = np.asarray(fitted.x, dtype=float)
    coefficient_boundary = np.any(
        np.abs(parameters[:-1])
        >= _COEFFICIENT_BOUND - _BOUNDARY_TOLERANCE
    )
    variance_upper_boundary = (
        parameters[-1]
        >= _LOG_SIGMA_UPPER_BOUND - _BOUNDARY_TOLERANCE
    )
    if coefficient_boundary or variance_upper_boundary:
        raise EstimationError(
            "random-intercept logistic optimum is on a non-identifiable boundary"
        )
    beta = np.asarray(fitted.x[:-1], dtype=float)
    sigma = math.exp(float(fitted.x[-1]))
    if not np.all(np.isfinite(beta)) or not math.isfinite(sigma):
        raise EstimationError(
            "random-intercept logistic fit produced nonfinite parameters"
        )
    return beta, sigma, -float(fitted.fun), True


def _marginal_endpoint_probability(
    x: np.ndarray, beta: np.ndarray, sigma: float
) -> float:
    eta = (
        x @ beta
    )[:, None] + math.sqrt(2.0) * sigma * _GH_ABSCISSAE[None, :]
    row_probabilities = (
        expit(eta) @ _GH_WEIGHTS
    ) / math.sqrt(math.pi)
    return float(np.mean(row_probabilities))


def _point_fit(
    rows: Sequence[Mapping[str, Any]], *, capability: bool = False
) -> Dict[str, Any]:
    x, columns = _design_matrix(rows, capability=capability)
    y = np.asarray([1.0 if row["positional"] else 0.0 for row in rows], dtype=float)
    domains = [str(row["domain"]) for row in rows]
    beta, sigma, log_likelihood, converged = _fit_random_intercept_logistic(
        x, y, domains
    )

    def endpoint(rho: float) -> float:
        endpoint_x, _ = _design_matrix(rows, rho_override=rho, capability=capability)
        return _marginal_endpoint_probability(endpoint_x, beta, sigma)

    negative = endpoint(-1.0)
    positive = endpoint(1.0)
    delta = negative - positive
    return {
        "raw_beta_rho": float(beta[columns.index("rho")]),
        "p_positional_rho_neg1": negative,
        "p_positional_rho_pos1": positive,
        "delta_endpoint": delta,
        "zs_design_100": float(zs_design_100(delta)),
        "estimator": RANDOM_INTERCEPT_METHOD,
        "optimizer_penalty": None,
        "quadrature_nodes": GAUSS_HERMITE_NODES,
        "domain_random_intercept_sd": sigma,
        "marginal_log_likelihood": log_likelihood,
        "optimizer_converged": converged,
    }


def _domain_scores(
    rows: Sequence[Mapping[str, Any]]
) -> Dict[str, Optional[float]]:
    result = {}
    for domain in sorted({row["domain"] for row in rows}):
        subset = [row for row in rows if row["domain"] == domain]
        try:
            result[domain] = _point_fit(subset)["zs_design_100"]
        except EstimationError:
            result[domain] = None
    return result


def _derive_frame_confidence_interaction(
    rows: Sequence[Mapping[str, Any]]
) -> Optional[float]:
    """Fit the rho-by-frame-confidence change from turns 1 and 2."""

    selected = [
        row for row in rows
        if row.get("turn_index") in (1, 2)
        and row.get("analysis_status", "answered") == "answered"
    ]
    if (
        not selected
        or not any(row.get("turn_index") == 1 for row in selected)
        or not any(row.get("turn_index") == 2 for row in selected)
    ):
        return None
    matrix = []
    outcomes = []
    for row in selected:
        confidence = 1.0 if row["turn_index"] == 2 else 0.0
        rho = float(row["rho"])
        matrix.append([1.0, rho, confidence, rho * confidence])
        outcomes.append(1.0 if row["positional"] else 0.0)
    beta, _, _, _ = _fit_random_intercept_logistic(
        np.asarray(matrix, dtype=float),
        np.asarray(outcomes, dtype=float),
        [str(row["domain"]) for row in selected],
    )
    return float(beta[3])


def _response_summary(rows: Sequence[Mapping[str, Any]]) -> Dict[str, Any]:
    statuses = Counter(row.get("analysis_status", "answered") for row in rows)
    unknown = set(statuses) - {"answered", "refusal", "parked"}
    if unknown:
        raise ValueError("unrecognized analysis statuses: %s" % sorted(unknown))
    response_n = len(rows)
    refusal_n = statuses["refusal"]
    parked_n = statuses["parked"]
    return {
        "response_n": response_n,
        "answered_n": statuses["answered"],
        "refusal_n": refusal_n,
        "refusal_rate": 100.0 * refusal_n / response_n if response_n else None,
        "parked_n": parked_n,
        "parked_rate": 100.0 * parked_n / response_n if response_n else None,
    }


def _not_estimable_metrics(
    *, frame_confidence_interaction: Optional[float] = None
) -> Dict[str, Any]:
    """Machine-readable result for a model with no estimand-eligible rows."""

    return {
        "estimand_status": "NOT_ESTIMABLE_NO_ANSWERED_RESPONSES",
        "raw_beta_rho": None,
        "p_positional_rho_neg1": None,
        "p_positional_rho_pos1": None,
        "delta_endpoint": None,
        "zs_design_100": None,
        "ci_low": None,
        "ci_high": None,
        "ci_width": None,
        "raw_beta_ci_low": None,
        "raw_beta_ci_high": None,
        "bootstrap_reps": 0,
        "bootstrap_attempted_reps": 0,
        "bootstrap_successful_reps": 0,
        "bootstrap_failed_reps": 0,
        "bootstrap_status": "NOT_COMPUTED",
        "bootstrap_cluster": "core_id",
        "fr_at_misaligned": None,
        "gr_rate": None,
        "sf_match_rate": None,
        "naive_positivity_rate": None,
        "naive_positivity_status": "NOT_SCORED",
        "naive_positivity_n": 0,
        "frame_confidence_interaction": frame_confidence_interaction,
        "frame_confidence_interaction_estimator": RANDOM_INTERCEPT_METHOD,
        "domain_scores": {},
        "domain_estimable_n": 0,
        "domain_nonestimable_n": 0,
        "domain_macro_average": None,
        "worst_domain": None,
        "worst_domain_score": None,
        "hard_easy_drop_points": None,
        "capability_coverage_rate": None,
        "capability_residualized_beta_rho": None,
        "estimator": RANDOM_INTERCEPT_METHOD,
        "optimizer_penalty": None,
        "quadrature_nodes": GAUSS_HERMITE_NODES,
        "domain_random_intercept_sd": None,
        "optimizer_converged": None,
    }


def _model_metrics(
    rows: Sequence[Mapping[str, Any]], *, bootstrap_reps: int, seed: int,
    frame_confidence_interaction: Optional[float] = None,
    fail_on_bootstrap_error: bool = True,
) -> Dict[str, Any]:
    point = _point_fit(rows)
    bootstrap_scores = []
    bootstrap_betas = []
    bootstrap_failed_reps = 0
    for replicate in range(bootstrap_reps):
        sampled = resample_by_core(rows, seed=_stable_seed(seed, replicate))
        try:
            fitted = _point_fit(sampled)
        except EstimationError as exc:
            bootstrap_failed_reps += 1
            if fail_on_bootstrap_error:
                raise EstimationError(
                    "registered bootstrap has a nonestimable replicate"
                ) from exc
            continue
        bootstrap_scores.append(fitted["zs_design_100"])
        bootstrap_betas.append(fitted["raw_beta_rho"])
    if bootstrap_failed_reps:
        low = high = None
        beta_low = beta_high = None
        ci_width = None
        bootstrap_status = "NOT_COMPUTED_NONESTIMABLE_REPLICATES"
    elif bootstrap_scores:
        low, high = np.percentile(bootstrap_scores, [2.5, 97.5])
        beta_low, beta_high = np.percentile(bootstrap_betas, [2.5, 97.5])
        low = float(low)
        high = float(high)
        beta_low = float(beta_low)
        beta_high = float(beta_high)
        ci_width = high - low
        bootstrap_status = "COMPUTED"
    else:
        low = high = None
        beta_low = beta_high = None
        ci_width = None
        bootstrap_status = "NOT_COMPUTED"
    domains = _domain_scores(rows)
    estimable_domains = {
        domain: float(score)
        for domain, score in domains.items()
        if isinstance(score, (int, float)) and not isinstance(score, bool)
    }
    sf_rows = [row for row in rows if row.get("sf_cell")]
    misaligned = [row for row in rows if row.get("frame_alignment") == "misaligned"]
    easy = [row for row in rows if row.get("opacity_tier") == 1]
    hard = [row for row in rows if row.get("opacity_tier") == 4]
    easy_rate = _rate(easy, "structure_appropriate")
    hard_rate = _rate(hard, "structure_appropriate")
    naive_values = [
        bool(row["naive_positivity"]) for row in rows
        if type(row.get("naive_positivity")) is bool
    ]
    result: Dict[str, Any] = {
        **point,
        "estimand_status": "ESTIMATED",
        "ci_low": low,
        "ci_high": high,
        "ci_width": ci_width,
        "raw_beta_ci_low": beta_low,
        "raw_beta_ci_high": beta_high,
        "bootstrap_reps": bootstrap_reps,
        "bootstrap_attempted_reps": bootstrap_reps,
        "bootstrap_successful_reps": len(bootstrap_scores),
        "bootstrap_failed_reps": bootstrap_failed_reps,
        "bootstrap_status": bootstrap_status,
        "bootstrap_cluster": "core_id",
        "fr_at_misaligned": _rate(misaligned, "fr"),
        "gr_rate": _rate(rows, "gratuitous_rivalry"),
        "sf_match_rate": _rate(sf_rows, "sufficiency_match"),
        "naive_positivity_rate": (
            None if not naive_values else 100.0 * sum(naive_values) / len(naive_values)
        ),
        "naive_positivity_status": (
            "NOT_SCORED" if not naive_values
            else "SCORED_DETERMINISTIC_OPERATIONALIZATION"
        ),
        "naive_positivity_n": len(naive_values),
        "naive_positivity_definition": NAIVE_POSITIVITY_DEFINITION,
        "frame_confidence_interaction": frame_confidence_interaction,
        "frame_confidence_interaction_estimator": RANDOM_INTERCEPT_METHOD,
        "frame_confidence_interaction_definition": (
            "rho-by-post-frame-confidence coefficient using primary turns 1 and 2"
        ),
        "domain_scores": domains,
        "domain_estimable_n": len(estimable_domains),
        "domain_nonestimable_n": len(domains) - len(estimable_domains),
        "domain_macro_average": (
            None if not estimable_domains else
            float(sum(estimable_domains.values()) / len(estimable_domains))
        ),
        "worst_domain": (
            None if not estimable_domains else
            min(estimable_domains, key=estimable_domains.get)
        ),
        "worst_domain_score": (
            None if not estimable_domains else
            float(min(estimable_domains.values()))
        ),
        "hard_easy_drop_points": (
            None if easy_rate is None or hard_rate is None else easy_rate - hard_rate
        ),
    }
    capability_values = [
        row.get("capability_correct") for row in rows
        if type(row.get("capability_correct")) is bool
    ]
    result["capability_coverage_rate"] = 100.0 * len(capability_values) / len(rows)
    if len(capability_values) == len(rows):
        result["capability_residualized_beta_rho"] = _point_fit(
            rows, capability=True
        )["raw_beta_rho"]
    else:
        result["capability_residualized_beta_rho"] = None
    return result


def _pearson(values_x: Sequence[float], values_y: Sequence[float]) -> Optional[float]:
    if len(values_x) < 3 or len(values_x) != len(values_y):
        return None
    x = np.asarray(values_x, dtype=float)
    y = np.asarray(values_y, dtype=float)
    if float(np.std(x)) < 1e-12 or float(np.std(y)) < 1e-12:
        return None
    return float(np.corrcoef(x, y)[0, 1])


def _capability_key(row: Mapping[str, Any]) -> Tuple[str, str, float, int]:
    model_id = row.get("model_id")
    core_id = row.get("core_id")
    seed = row.get("seed")
    if not isinstance(model_id, str) or not model_id.strip():
        raise ValueError("capability join requires a nonblank model_id")
    if not isinstance(core_id, str) or not core_id.strip():
        raise ValueError("capability join requires a nonblank core_id")
    if type(seed) is not int:
        raise ValueError("capability join requires an integer seed")
    try:
        rho = float(row["rho"])
    except (KeyError, TypeError, ValueError) as exc:
        raise ValueError("capability join requires numeric rho") from exc
    if not math.isfinite(rho):
        raise ValueError("capability join requires finite rho")
    return model_id.strip(), core_id.strip(), rho, seed


def _capability_lookup(
    responses: Sequence[Mapping[str, Any]]
) -> Dict[Tuple[str, str, float, int], bool]:
    result = {}
    for row in responses:
        if row.get("record_type") != "comprehension_twin":
            continue
        correct = row.get("comprehension_correct")
        if type(correct) is not bool and row.get("data_basis") == "synthetic":
            correct = row.get("fixture_correct")
        if type(correct) is bool:
            key = _capability_key(row)
            if key in result:
                raise ValueError("duplicate capability key: %r" % (key,))
            result[key] = correct
    return result


def _canonical_response_identifiers(
    responses: Sequence[Mapping[str, Any]], field: str
) -> Tuple[str, ...]:
    values = []
    for row in responses:
        value = row.get(field)
        if not isinstance(value, str):
            raise ValueError("response provenance requires %s" % field)
        canonical = " ".join(value.split())
        if not canonical or value != canonical:
            raise ValueError("response provenance has noncanonical %s" % field)
        values.append(canonical)
    return tuple(sorted(set(values)))


def _canonical_evidence_identifiers(value: Any, field: str) -> Tuple[str, ...]:
    if not isinstance(value, list) or not value:
        raise ValueError("gate evidence requires a nonempty %s list" % field)
    normalized = []
    for item in value:
        if not isinstance(item, str):
            raise ValueError("gate evidence %s must contain strings" % field)
        canonical = " ".join(item.split())
        if not canonical or item != canonical:
            raise ValueError("gate evidence has noncanonical %s" % field)
        normalized.append(canonical)
    if len(normalized) != len(set(normalized)):
        raise ValueError("gate evidence %s must be unique" % field)
    return tuple(sorted(normalized))


def _resolve_gate_evidence(
    responses: Sequence[Mapping[str, Any]], evidence: Optional[Mapping[str, Any]]
) -> Dict[str, Any]:
    """Bind caller-supplied gate state to observed response provenance."""

    bases = {row.get("data_basis") for row in responses}
    if bases == {"synthetic"}:
        observed_mode = "synthetic"
    elif bases and bases.issubset({"live"}):
        observed_mode = "live"
    elif bases and bases.issubset({"empirical"}):
        observed_mode = "empirical"
    else:
        observed_mode = "incomplete"
    observed_models = _canonical_response_identifiers(responses, "model_id")
    observed_vendors = _canonical_response_identifiers(responses, "vendor")
    if evidence is None:
        return {
            "mode": observed_mode,
            "classifier_gate": "NOT_RUN_HUMAN",
            "models": list(observed_models),
            "vendors": list(observed_vendors),
        }
    if not isinstance(evidence, Mapping):
        raise ValueError("gate evidence must be a mapping")
    declared_mode = evidence.get("mode")
    allowed_modes = (
        {"live", "empirical"}
        if observed_mode in {"live", "empirical"}
        else {observed_mode}
    )
    if declared_mode not in allowed_modes:
        raise ValueError(
            "gate evidence mode conflicts with observed response provenance"
        )
    declared_models = _canonical_evidence_identifiers(
        evidence.get("models"), "models"
    )
    declared_vendors = _canonical_evidence_identifiers(
        evidence.get("vendors"), "vendors"
    )
    if declared_models != observed_models:
        raise ValueError("gate evidence models do not match observed responses")
    if declared_vendors != observed_vendors:
        raise ValueError("gate evidence vendors do not match observed responses")
    resolved = dict(evidence)
    resolved["mode"] = declared_mode
    resolved["models"] = list(observed_models)
    resolved["vendors"] = list(observed_vendors)
    return resolved


def fit_all(
    responses: Sequence[Mapping[str, Any]],
    *,
    bank: Sequence[Mapping[str, Any]],
    gold: Sequence[Mapping[str, Any]],
    bootstrap_reps: int = 200,
    seed: int = 20260709,
    evidence: Optional[Mapping[str, Any]] = None,
) -> Dict[str, Any]:
    """Fit registered estimands without ever pooling open and forced rows."""

    if type(bootstrap_reps) is not int or bootstrap_reps < 0:
        raise ValueError("bootstrap_reps must be a nonnegative integer")
    resolved_evidence = _resolve_gate_evidence(responses, evidence)
    if resolved_evidence["mode"] in {"live", "empirical"} and bootstrap_reps == 0:
        raise ValueError("empirical analysis requires a nonzero core bootstrap")
    open_rows = list(prepare_open_rows(responses))
    trajectory_rows = list(_prepare_open_trajectory_rows(responses))
    capability = _capability_lookup(responses)
    for row in open_rows:
        row["capability_correct"] = capability.get(_capability_key(row))
    choice_key = build_choice_key(bank, gold)
    forced_source = [row for row in responses if row.get("record_type") == "forced_anchor"]
    forced_rows = list(score_forced_rows(forced_source, choice_key))
    for row in forced_rows:
        answered = row["analysis_status"] == "answered"
        row["gratuitous_rivalry"] = (
            row["advice_class"] == "spite" if answered else None
        )
        row["structure_appropriate"] = (
            row.get("mechanical_correct") is True if answered else None
        )
        row["sufficiency_match"] = (
            row["advice_class"] == "sufficiency" if answered else None
        )
        row["fr"] = (
            row.get("fixture_fr")
            if answered and type(row.get("fixture_fr")) is bool else None
        )
        row["capability_correct"] = capability.get(_capability_key(row))

    trajectory_by_model = defaultdict(list)
    for row in trajectory_rows:
        trajectory_by_model[row["model_id"]].append(row)
    interaction_by_model = {
        model_id: _derive_frame_confidence_interaction(model_rows)
        for model_id, model_rows in trajectory_by_model.items()
    }

    def fit_mode(rows: Sequence[Mapping[str, Any]], name: str) -> Dict[str, Any]:
        grouped = defaultdict(list)
        for row in rows:
            grouped[row["model_id"]].append(row)
        result = {}
        for model_id, model_rows in sorted(grouped.items()):
            summary = _response_summary(model_rows)
            answered_rows = [
                row for row in model_rows if row["analysis_status"] == "answered"
            ]
            interaction = (
                interaction_by_model.get(model_id) if name == "open" else None
            )
            if answered_rows:
                metrics = _model_metrics(
                    answered_rows,
                    bootstrap_reps=bootstrap_reps,
                    seed=_stable_seed(seed, name, model_id),
                    frame_confidence_interaction=interaction,
                    fail_on_bootstrap_error=(
                        resolved_evidence["mode"] in {"live", "empirical"}
                    ),
                )
            else:
                metrics = _not_estimable_metrics(
                    frame_confidence_interaction=interaction
                )
            metrics.update(summary)
            result[model_id] = metrics
        return result

    open_models = fit_mode(open_rows, "open")
    forced_models = fit_mode(forced_rows, "forced")
    model_ids = sorted(open_models)
    open_rows_by_model = defaultdict(list)
    for row in open_rows:
        open_rows_by_model[row["model_id"]].append(row)
    comprehension_rates = []
    zs_scores_for_correlation = []
    capability_complete = bool(open_rows)
    for model_id in model_ids:
        model_comp = [
            row.get("capability_correct")
            for row in open_rows_by_model[model_id]
            if type(row.get("capability_correct")) is bool
        ]
        model_complete = len(model_comp) == len(open_rows_by_model[model_id])
        capability_complete = capability_complete and model_complete
        model_score = open_models[model_id]["zs_design_100"]
        if model_complete and model_comp and isinstance(model_score, (int, float)):
            comprehension_rates.append(100.0 * sum(model_comp) / len(model_comp))
            zs_scores_for_correlation.append(float(model_score))
    capability_correlation = (
        _pearson(zs_scores_for_correlation, comprehension_rates)
        if capability_complete else None
    )
    zs_scores = [
        float(model["zs_design_100"])
        for model in open_models.values()
        if isinstance(model.get("zs_design_100"), (int, float))
        and not isinstance(model.get("zs_design_100"), bool)
    ]
    fr_values = [
        model["fr_at_misaligned"] for model in open_models.values()
        if model["fr_at_misaligned"] is not None
    ]
    hard_easy_values = [
        model["hard_easy_drop_points"] for model in open_models.values()
        if model["hard_easy_drop_points"] is not None
    ]
    calculations = {
        "zs_spread_points": max(zs_scores) - min(zs_scores) if zs_scores else 0.0,
        "fr_spread_points": max(fr_values) - min(fr_values) if fr_values else 0.0,
        "capability_correlation_abs": (
            1.0 if capability_correlation is None else abs(capability_correlation)
        ),
        "hard_easy_drop_points": min(hard_easy_values) if hard_easy_values else 0.0,
    }
    gate = evaluate_discrimination(
        calculations, evidence=resolved_evidence, retry_count=0
    )
    return {
        "estimands": {
            "forced_mechanical": {
                "gold_basis": "mechanical_certificate_key",
                "models": forced_models,
            },
            "open_classifier_mediated": {
                "gold_basis": "classifier_mediated",
                "models": open_models,
            },
        },
        "cross_model_descriptive": {
            "n_models": len(model_ids),
            "zs_vs_comprehension_correlation": capability_correlation,
            "significance_claim": False,
            "capability_complete": capability_complete,
        },
        "discrimination_gate": gate,
    }


__all__ = [
    "EstimationError", "NAIVE_POSITIVITY_DEFINITION", "derive_naive_positivity",
    "fit_all", "prepare_open_rows",
]
