"""Attempt the preregistered WITNESS B5 mixed-logit robustness model."""
from __future__ import annotations

import csv
import math
import shutil
import subprocess
import tempfile
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable, Mapping, Protocol, Sequence

from stats_util import AnalysisError, filter_non_holdout, finite_number


FORMULA = "gold ~ format * content_type + (1|core) + (1|base)"
COEFFICIENT_NAME = "formatEND:content_typemoral"
_STATUSES = {"FIT", "CONVERGENCE_FAILURE", "UNAVAILABLE"}


@dataclass(frozen=True)
class GlmmFitResult:
    status: str
    logit_corrected_gap: float | None
    convergence: bool | None
    message: str

    def to_dict(self) -> dict:
        if self.status not in _STATUSES:
            raise AnalysisError(f"unknown GLMM status: {self.status}")
        if self.logit_corrected_gap is not None and not math.isfinite(
            self.logit_corrected_gap
        ):
            raise AnalysisError("GLMM coefficient must be finite when present")
        if self.status == "FIT" and (
            self.logit_corrected_gap is None or self.convergence is not True
        ):
            raise AnalysisError("FIT requires a finite coefficient and convergence=True")
        if not isinstance(self.message, str) or not self.message.strip():
            raise AnalysisError("GLMM result requires a non-empty message")
        return asdict(self)


class GlmmRunner(Protocol):
    def fit(self, model: str, rows: Sequence[Mapping]) -> GlmmFitResult:
        """Fit one model's normalized END/ACT item-level rows."""


_R_SCRIPT = r'''
args <- commandArgs(trailingOnly=TRUE)
d <- read.csv(args[[1]], stringsAsFactors=FALSE)
d$format <- relevel(factor(d$format), ref="ACT")
d$content_type <- relevel(factor(d$content_type), ref="control")
d$core <- factor(d$core)
d$base <- factor(d$base)
fit <- tryCatch(
  lme4::glmer(
    gold ~ format * content_type + (1|core) + (1|base),
    data=d,
    family=stats::binomial()
  ),
  error=function(e) e
)
sanitize <- function(x) gsub("[\\t\\r\\n]+", " ", paste(x, collapse="; "))
if (inherits(fit, "error")) {
  cat("RESULT\tCONVERGENCE_FAILURE\tNA\tFALSE\t", sanitize(conditionMessage(fit)), "\n", sep="")
  quit(status=0)
}
messages <- fit@optinfo$conv$lme4$messages
opt_code <- fit@optinfo$conv$opt
converged <- (is.null(messages) || length(messages) == 0) &&
             (is.null(opt_code) || all(opt_code == 0)) &&
             !lme4::isSingular(fit, tol=1e-4)
coef_name <- "formatEND:content_typemoral"
coefs <- lme4::fixef(fit)
if (!(coef_name %in% names(coefs))) {
  cat("RESULT\tCONVERGENCE_FAILURE\tNA\tFALSE\tmissing coefficient ", coef_name, "\n", sep="")
} else if (!converged) {
  detail <- if (lme4::isSingular(fit, tol=1e-4)) "singular fit" else sanitize(messages)
  cat("RESULT\tCONVERGENCE_FAILURE\tNA\tFALSE\t", detail, "\n", sep="")
} else {
  cat("RESULT\tFIT\t", format(unname(coefs[[coef_name]]), digits=17),
      "\tTRUE\tconverged\n", sep="")
}
'''


class SubprocessRGlmmRunner:
    """Real R/lme4 adapter; absence and convergence failures remain data, not gates."""

    def __init__(self, rscript: str | None = None, timeout_seconds: float = 55.0):
        self.rscript = rscript or shutil.which("Rscript")
        if timeout_seconds <= 0 or not math.isfinite(timeout_seconds):
            raise AnalysisError("GLMM timeout_seconds must be finite and positive")
        self.timeout_seconds = timeout_seconds

    def fit(self, model: str, rows: Sequence[Mapping]) -> GlmmFitResult:
        if not self.rscript:
            return GlmmFitResult(
                status="UNAVAILABLE",
                logit_corrected_gap=None,
                convergence=None,
                message="Rscript not found on PATH; real lme4 fit was attempted but unavailable",
            )
        try:
            check = subprocess.run(
                [
                    self.rscript,
                    "--vanilla",
                    "-e",
                    "quit(status=ifelse(requireNamespace('lme4', quietly=TRUE), 0, 42))",
                ],
                capture_output=True,
                text=True,
                check=False,
                timeout=self.timeout_seconds,
            )
        except subprocess.TimeoutExpired:
            return GlmmFitResult(
                status="UNAVAILABLE",
                logit_corrected_gap=None,
                convergence=None,
                message=f"Rscript/lme4 availability attempt timed out after {self.timeout_seconds}s",
            )
        except OSError as exc:
            return GlmmFitResult(
                status="UNAVAILABLE",
                logit_corrected_gap=None,
                convergence=None,
                message=f"Rscript execution unavailable: {exc}",
            )
        if check.returncode == 42:
            return GlmmFitResult(
                status="UNAVAILABLE",
                logit_corrected_gap=None,
                convergence=None,
                message=f"Rscript={self.rscript}; R package lme4 is unavailable",
            )
        if check.returncode != 0:
            message = (check.stderr or check.stdout or "Rscript availability check failed").strip()
            return GlmmFitResult(
                status="UNAVAILABLE",
                logit_corrected_gap=None,
                convergence=None,
                message=f"Rscript={self.rscript}; {message}",
            )
        with tempfile.TemporaryDirectory(prefix="witness-glmm-") as directory:
            directory_path = Path(directory)
            csv_path = directory_path / "items.csv"
            script_path = directory_path / "fit.R"
            with csv_path.open("w", encoding="utf-8", newline="") as handle:
                writer = csv.DictWriter(
                    handle,
                    fieldnames=("gold", "format", "content_type", "core", "base"),
                )
                writer.writeheader()
                writer.writerows(rows)
            script_path.write_text(_R_SCRIPT, encoding="utf-8")
            try:
                completed = subprocess.run(
                    [self.rscript, "--vanilla", str(script_path), str(csv_path)],
                    capture_output=True,
                    text=True,
                    check=False,
                    timeout=self.timeout_seconds,
                )
            except subprocess.TimeoutExpired:
                return GlmmFitResult(
                    status="CONVERGENCE_FAILURE",
                    logit_corrected_gap=None,
                    convergence=False,
                    message=f"R/lme4 fit timed out after {self.timeout_seconds}s",
                )
        if completed.returncode != 0:
            message = (completed.stderr or completed.stdout or "R GLMM process failed").strip()
            return GlmmFitResult(
                status="CONVERGENCE_FAILURE",
                logit_corrected_gap=None,
                convergence=False,
                message=message,
            )
        result_lines = [
            line for line in completed.stdout.splitlines() if line.startswith("RESULT\t")
        ]
        if len(result_lines) != 1:
            return GlmmFitResult(
                status="CONVERGENCE_FAILURE",
                logit_corrected_gap=None,
                convergence=False,
                message="R GLMM adapter returned no unique RESULT record",
            )
        parts = result_lines[0].split("\t", 4)
        if len(parts) != 5 or parts[1] not in _STATUSES:
            raise AnalysisError("malformed RESULT record from R GLMM adapter")
        status, coefficient_text, convergence_text, message = parts[1:]
        coefficient = None if coefficient_text == "NA" else float(coefficient_text)
        convergence = {"TRUE": True, "FALSE": False, "NA": None}.get(convergence_text)
        return GlmmFitResult(status, coefficient, convergence, message)


def _sign(value: float) -> str:
    if not math.isfinite(value):
        raise AnalysisError("cannot take the sign of a non-finite value")
    return "positive" if value > 0 else "negative" if value < 0 else "zero"


def normalize_glmm_rows(rows: Sequence[dict], model: str) -> list[dict]:
    normalized = []
    for row in rows:
        if row.get("model") != model or row.get("modality") not in {"END", "ACT"}:
            continue
        monitored = row.get("monitored", True)
        is_control = row.get("is_control")
        if not isinstance(monitored, bool) or not isinstance(is_control, bool):
            raise AnalysisError("GLMM monitored/is_control fields must be boolean")
        if not monitored:
            continue
        core_id = row.get("core_id")
        if not isinstance(core_id, str) or not core_id:
            raise AnalysisError("GLMM rows require core_id")
        if is_control:
            base_id = row.get("control_base_id")
            if not isinstance(base_id, str) or not base_id:
                raise AnalysisError("GLMM control rows require control_base_id")
            core_group = "NO_MORAL_CORE"
            base_group = base_id
            content_type = "control"
        else:
            core_group = core_id
            base_group = "NO_CONTROL_BASE"
            content_type = "moral"
        normalized.append({
            "gold": finite_number(row.get("gold"), field="gold"),
            "format": row["modality"],
            "content_type": content_type,
            "core": core_group,
            "base": base_group,
        })
    if not normalized:
        raise AnalysisError(f"GLMM has no END/ACT rows for model {model}")
    if {row["format"] for row in normalized} != {"END", "ACT"}:
        raise AnalysisError(f"GLMM model {model} lacks END or ACT support")
    if {row["content_type"] for row in normalized} != {"moral", "control"}:
        raise AnalysisError(f"GLMM model {model} lacks moral or control support")
    return normalized


def run_glmm_robustness(
    scored_rows: Iterable[Mapping],
    primary_rows: Iterable[Mapping],
    *,
    runner: GlmmRunner | None = None,
    holdout_core_ids: Iterable[str] = (),
) -> dict:
    """Attempt B5 per model and compare fitted sign with the probability-scale primary."""
    scored = filter_non_holdout(
        scored_rows, holdout_core_ids, require_status=True
    )
    primary = filter_non_holdout(
        primary_rows, holdout_core_ids, require_status=True
    )
    primary_by_model = {}
    for row in primary:
        if row.get("contrast") != "END-ACT":
            continue
        model = row.get("model")
        if model in primary_by_model:
            raise AnalysisError(f"duplicate aggregate primary row for {model}")
        primary_by_model[model] = row
    models = sorted({row.get("model") for row in scored})
    if any(not isinstance(model, str) or not model for model in models):
        raise AnalysisError("GLMM scored rows require non-empty model IDs")
    if set(models) != set(primary_by_model):
        raise AnalysisError("GLMM models and aggregate primary models must match")
    active_runner = runner or SubprocessRGlmmRunner()
    model_results = {}
    compared = []
    for model in models:
        normalized = normalize_glmm_rows(scored, model)
        fit = active_runner.fit(model, normalized)
        record = fit.to_dict()
        record.update({
            "formula": FORMULA,
            "coefficient_name": COEFFICIENT_NAME,
        })
        primary_value = primary_by_model[model].get("corrected_gap")
        if not isinstance(primary_value, (int, float)) or not math.isfinite(
            float(primary_value)
        ):
            raise AnalysisError("aggregate primary corrected_gap must be finite")
        primary_sign = _sign(float(primary_value))
        if fit.status == "FIT":
            fitted_sign = _sign(float(fit.logit_corrected_gap))
            disagreement = fitted_sign != primary_sign
            compared.append(disagreement)
        else:
            fitted_sign = None
            disagreement = None
        record.update({
            "sign": fitted_sign,
            "primary_probability_sign": primary_sign,
            "sign_disagreement_with_primary": disagreement,
        })
        model_results[model] = record
    return {
        "attempted": True,
        "formula": FORMULA,
        "coefficient_name": COEFFICIENT_NAME,
        "models": model_results,
        "any_sign_disagreement": any(compared) if compared else None,
        "non_gating": True,
    }
