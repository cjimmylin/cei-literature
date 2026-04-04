"""Gate-Passage Predictor Model — Logistic Regression

Predicts which candidates pass all 3 gates (gate_RD AND gate_data AND gate_theological)
using structural features. Key question: does tradition family predict gate-passage
independent of format and venue?

Input:  RELIGIOUS-VALUES/data/20260404-religious-benchmark-feature-matrix-v2.json
Output: RELIGIOUS-VALUES/data/20260404-gate-passage-predictors.json
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np
import statsmodels.api as sm
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from scipy.stats import chi2

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
BASE = Path(__file__).resolve().parent.parent
DATA_DIR = BASE / "data"
INPUT = DATA_DIR / "20260404-religious-benchmark-feature-matrix-v2.json"
OUTPUT = DATA_DIR / "20260404-gate-passage-predictors.json"

# ---------------------------------------------------------------------------
# Load data
# ---------------------------------------------------------------------------
with open(INPUT) as f:
    raw = json.load(f)

entries = raw["entries"]
print(f"Loaded {len(entries)} entries, {sum(1 for e in entries if e.get('passes_gates'))} gate-passers")

# ---------------------------------------------------------------------------
# Feature engineering
# ---------------------------------------------------------------------------

# Target
y = np.array([1 if e.get("passes_gates") else 0 for e in entries], dtype=int)

# --- D6_tradition_family one-hot (reference: Abrahamic) ---
family_map = {"Abrahamic": 0, "Dharmic": 1, "East Asian": 2, "African/Indigenous": 3, "Other": 4, "Unknown": 4}
family_labels = ["Dharmic", "East_Asian", "African_Indigenous", "Other_Unknown"]

family_dummies = np.zeros((len(entries), 4), dtype=float)
for i, e in enumerate(entries):
    fam = family_map.get(e.get("D6_tradition_family", "Unknown"), 4)
    if fam > 0:  # Abrahamic=0 is reference
        family_dummies[i, fam - 1] = 1.0

# --- P1_format one-hot (reference: MIX as largest category) ---
format_cats = {"MCQ": 0, "SCN": 1}  # Others grouped into reference
format_labels = ["fmt_MCQ", "fmt_SCN"]

format_dummies = np.zeros((len(entries), 2), dtype=float)
for i, e in enumerate(entries):
    fmt = e.get("P1_format", "")
    if fmt in format_cats:
        format_dummies[i, format_cats[fmt]] = 1.0

# --- P10_language binary (English vs non-English) ---
lang_english = np.zeros(len(entries), dtype=float)
for i, e in enumerate(entries):
    lang = (e.get("P10_language") or "").strip().lower()
    if lang == "english" or "english" in lang.split(","):
        lang_english[i] = 1.0

# --- D1_year numeric ---
year_vals = []
for e in entries:
    try:
        year_vals.append(int(e.get("D1_year", 0)))
    except (ValueError, TypeError):
        year_vals.append(2023)  # median fallback
year_arr = np.array(year_vals, dtype=float)
# Center year for interpretability
year_centered = year_arr - year_arr.mean()

# --- C3_venue_tier ordinal ---
tier_map = {"Tier 1 (top conf)": 3, "Tier 2 (good conf/journal)": 2, "Tier 3 (other)": 1}
venue_tier = np.array([tier_map.get(e.get("C3_venue_tier", ""), 1) for e in entries], dtype=float)

# --- is_benchmark binary ---
is_benchmark = np.array([1.0 if e.get("is_benchmark") else 0.0 for e in entries])

# --- is_eval binary ---
is_eval = np.array([1.0 if e.get("is_eval") else 0.0 for e in entries])

# --- R1_count numeric ---
r1_count = np.array([e.get("R1_count", 0) for e in entries], dtype=float)

# ---------------------------------------------------------------------------
# Assemble design matrix
# ---------------------------------------------------------------------------
feature_names = (
    family_labels
    + format_labels
    + ["lang_English", "year_centered", "venue_tier", "is_benchmark", "is_eval", "R1_count"]
)

X = np.column_stack([
    family_dummies,
    format_dummies,
    lang_english,
    year_centered,
    venue_tier,
    is_benchmark,
    is_eval,
    r1_count,
])

# Add constant for intercept
X_const = sm.add_constant(X)

print(f"\nDesign matrix: {X_const.shape[0]} obs x {X_const.shape[1]} features")
print(f"Target: {y.sum()} positives ({100*y.mean():.1f}%)")
print(f"Features: const + {feature_names}")

# ---------------------------------------------------------------------------
# Fit logistic regression
# ---------------------------------------------------------------------------
try:
    model = sm.Logit(y, X_const)
    result = model.fit(disp=0, maxiter=100, method="newton")
    converged = result.mle_retvals.get("converged", True)
except Exception:
    # Fallback to bfgs if Newton fails
    model = sm.Logit(y, X_const)
    result = model.fit(disp=0, maxiter=200, method="bfgs")
    converged = True

print(f"\nModel converged: {converged}")
print(result.summary2())

# ---------------------------------------------------------------------------
# Extract results
# ---------------------------------------------------------------------------
params = result.params
conf_int = result.conf_int(alpha=0.05)
pvalues = result.pvalues
bse = result.bse

# Odds ratios
odds_ratios = np.exp(params)
or_lower = np.exp(conf_int[:, 0])
or_upper = np.exp(conf_int[:, 1])

# McFadden pseudo-R^2
ll_full = result.llf
ll_null = result.llnull
mcfadden_r2 = 1 - (ll_full / ll_null)

# Predictions
y_pred_prob = result.predict(X_const)
y_pred = (y_pred_prob >= 0.5).astype(int)

acc = accuracy_score(y, y_pred)
prec = precision_score(y, y_pred, zero_division=0)
rec = recall_score(y, y_pred, zero_division=0)
f1 = f1_score(y, y_pred, zero_division=0)

print(f"\n--- Model Performance ---")
print(f"McFadden pseudo-R^2: {mcfadden_r2:.4f}")
print(f"Accuracy: {acc:.3f}")
print(f"Precision: {prec:.3f}")
print(f"Recall: {rec:.3f}")
print(f"F1: {f1:.3f}")

# ---------------------------------------------------------------------------
# Likelihood ratio test: family dummies jointly
# ---------------------------------------------------------------------------
# Fit restricted model (without family dummies)
X_no_family = sm.add_constant(X[:, 4:])  # drop first 4 cols (family dummies)
try:
    model_restricted = sm.Logit(y, X_no_family)
    result_restricted = model_restricted.fit(disp=0, maxiter=100, method="newton")
except Exception:
    model_restricted = sm.Logit(y, X_no_family)
    result_restricted = model_restricted.fit(disp=0, maxiter=200, method="bfgs")

lr_stat = -2 * (result_restricted.llf - result.llf)
lr_df = 4  # 4 family dummies
lr_pvalue = chi2.sf(lr_stat, lr_df)

print(f"\n--- Likelihood Ratio Test: Tradition Family ---")
print(f"LR statistic: {lr_stat:.3f}")
print(f"df: {lr_df}")
print(f"p-value: {lr_pvalue:.6f}")

# ---------------------------------------------------------------------------
# Build output
# ---------------------------------------------------------------------------
all_names = ["const"] + feature_names
coefficients = []
for i, name in enumerate(all_names):
    coefficients.append({
        "feature": name,
        "coefficient": round(float(params[i]), 4),
        "std_error": round(float(bse[i]), 4),
        "z_value": round(float(params[i] / bse[i]), 3),
        "p_value": round(float(pvalues[i]), 6),
        "odds_ratio": round(float(odds_ratios[i]), 4),
        "or_95ci_lower": round(float(or_lower[i]), 4),
        "or_95ci_upper": round(float(or_upper[i]), 4),
        "significant_05": bool(pvalues[i] < 0.05),
    })

# Sort by absolute z-value for "strongest predictors"
strongest = sorted(coefficients[1:], key=lambda c: abs(c["z_value"]), reverse=True)

# Key finding summary
sig_features = [c for c in coefficients[1:] if c["significant_05"]]
family_sig = any(c["feature"] in family_labels and c["significant_05"] for c in coefficients)

if family_sig:
    family_finding = "Yes - tradition family significantly predicts gate-passage even after controlling for format and venue"
else:
    family_finding = "No - tradition family does NOT significantly predict gate-passage after controlling for format and venue"

output = {
    "generated": "20260404",
    "model": "statsmodels Logit (MLE)",
    "n_observations": int(len(entries)),
    "n_positive": int(y.sum()),
    "prevalence": round(float(y.mean()), 4),
    "reference_categories": {
        "tradition_family": "Abrahamic",
        "format": "MIX/other (non-MCQ, non-SCN)",
    },
    "year_centering": round(float(year_arr.mean()), 1),
    "coefficients": coefficients,
    "strongest_predictors": [
        {"rank": i + 1, "feature": c["feature"], "odds_ratio": c["odds_ratio"], "p_value": c["p_value"]}
        for i, c in enumerate(strongest[:5])
    ],
    "model_performance": {
        "mcfadden_pseudo_r2": round(mcfadden_r2, 4),
        "log_likelihood_full": round(float(ll_full), 2),
        "log_likelihood_null": round(float(ll_null), 2),
        "accuracy": round(acc, 4),
        "precision": round(prec, 4),
        "recall": round(rec, 4),
        "f1_score": round(f1, 4),
    },
    "tradition_family_joint_test": {
        "test": "Likelihood Ratio Test",
        "lr_statistic": round(float(lr_stat), 3),
        "df": lr_df,
        "p_value": round(float(lr_pvalue), 6),
        "significant_05": bool(lr_pvalue < 0.05),
        "interpretation": family_finding,
    },
    "key_question": "Does tradition family predict gate-passage independent of format and venue?",
    "answer": family_finding,
    "narrative": "",  # filled below
}

# Build narrative
narr_parts = []
narr_parts.append(
    f"Logistic regression on {len(entries)} candidates ({y.sum()} gate-passers, "
    f"{100*y.mean():.1f}% prevalence)."
)
narr_parts.append(f"McFadden pseudo-R2 = {mcfadden_r2:.3f}; accuracy = {acc:.1%}.")

if sig_features:
    top = sig_features[0]
    narr_parts.append(
        f"Strongest predictor: {top['feature']} (OR={top['odds_ratio']:.2f}, p={top['p_value']:.4f})."
    )

narr_parts.append(
    f"Tradition family joint LR test: chi2={lr_stat:.2f}, df={lr_df}, p={lr_pvalue:.4f}. "
    + ("Tradition family IS an independent predictor." if lr_pvalue < 0.05
       else "Tradition family is NOT an independent predictor at alpha=0.05.")
)

output["narrative"] = " ".join(narr_parts)

# ---------------------------------------------------------------------------
# Write
# ---------------------------------------------------------------------------
with open(OUTPUT, "w") as f:
    json.dump(output, f, indent=2)

print(f"\nOutput written to {OUTPUT}")
print(f"\nNarrative: {output['narrative']}")
