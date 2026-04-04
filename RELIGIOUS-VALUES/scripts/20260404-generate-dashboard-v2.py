"""Generate a self-contained HTML dashboard for the Religious Values Benchmark paper.

Architecture: "fat data, thin client" -- Python pre-computes ALL analytics and
embeds them as JS constants. The browser does zero computation.

IMPORTANT: Since HTML is emitted via Python f-strings, ALL JavaScript curly
braces are DOUBLED ({{ }}).  Data constants use json.dumps (single braces).
"""
from __future__ import annotations

import json
import math
from pathlib import Path

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
BASE = Path(__file__).resolve().parent.parent   # RELIGIOUS-VALUES/
DATA = BASE / "data"
OUT  = BASE / "dashboard" / "20260404-religious-values-dashboard-v2.html"
OUT.parent.mkdir(parents=True, exist_ok=True)

# ---------------------------------------------------------------------------
# Load all data files
# ---------------------------------------------------------------------------
sensitivity   = json.loads((DATA / "20260404-sensitivity-analysis.json").read_text())
correlation   = json.loads((DATA / "20260404-correlation-matrix.json").read_text())
claims_data   = json.loads((DATA / "20260404-claim-robustness-tests.json").read_text())
void_factors  = json.loads((DATA / "20260404-void-factor-taxonomy.json").read_text())
batch1        = json.loads((DATA / "20260404-claude-assessment-batch1.json").read_text())
batch2        = json.loads((DATA / "20260404-claude-assessment-batch2.json").read_text())
feature_mat   = json.loads((DATA / "20260404-religious-benchmark-feature-matrix-v2.json").read_text())

# ---------------------------------------------------------------------------
# Pre-compute analytics
# ---------------------------------------------------------------------------

# -- Overview stats --
total_candidates = feature_mat["total_entries"]
gate_passers = feature_mat["gate_passing"]
gp_entries = [e for e in feature_mat["entries"] if e.get("passes_gates")]

# Tradition counts among gate-passers
tradition_counts: dict[str, int] = {}
family_counts: dict[str, int] = {}
for e in gp_entries:
    trad = e.get("D5_primary_tradition", "Unknown")
    fam  = e.get("D6_tradition_family", "Other")
    tradition_counts[trad] = tradition_counts.get(trad, 0) + 1
    family_counts[fam] = family_counts.get(fam, 0) + 1

n_traditions = len(void_factors["traditions"])
n_void = sum(1 for t in void_factors["traditions"] if not t["has_benchmarks"])

# -- Bootstrap CI data for chart --
boot_cis = sorted(sensitivity["bootstrap"]["benchmark_cis"],
                  key=lambda x: x["composite_mean"], reverse=True)
boot_labels = [c["short_title"][:45] for c in boot_cis]
boot_means  = [c["composite_mean"] for c in boot_cis]
boot_lowers = [c["composite_ci_lower"] for c in boot_cis]
boot_uppers = [c["composite_ci_upper"] for c in boot_cis]

# Tradition family for each gate-passer (for coloring)
id_to_family = {e["id"]: e.get("D6_tradition_family", "Other") for e in gp_entries}
boot_families = [id_to_family.get(c["id"], "Other") for c in boot_cis]

# Top-15 cutoff
top15_cutoff = boot_means[14] if len(boot_means) >= 15 else 0

# -- Weight sensitivity heatmap --
ws = sensitivity["weight_sensitivity"]
benchmark_robustness = ws["benchmark_robustness"]
rob_labels = [b["short_title"][:40] for b in benchmark_robustness[:20]]
rob_pct_top15 = [b["pct_in_top15"] * 100 for b in benchmark_robustness[:20]]
rob_rank_range = [b["rank_range"] for b in benchmark_robustness[:20]]

# -- Gate threshold --
gt_results = sensitivity["gate_threshold"]["results"]
gt_thresholds = [r["threshold"] for r in gt_results]
gt_passers = [r["gate_passers"] for r in gt_results]
gt_traditions = [r["traditions_represented"] for r in gt_results]
gt_void_gained = {r["threshold"]: r.get("void_traditions_gained", []) for r in gt_results}

# -- Void factor radar data --
void_traditions = void_factors["traditions"]
exemplar_names = ["Islam", "Judaism", "Indigenous Spirituality"]
factor_keys = ["digital_corpus", "nlp_community", "formalizability",
               "data_sovereignty", "institutional_support", "publication_infrastructure"]
factor_labels = ["Digital Corpus", "NLP Community", "Formalizability",
                 "Data Sovereignty", "Institutional Support", "Publication Infra."]

radar_data: dict[str, list[int]] = {}
for name in exemplar_names:
    for t in void_traditions:
        if t["tradition"] == name:
            radar_data[name] = [t[f] for f in factor_keys]
            break

# Structural scores table
struct_table = []
for t in sorted(void_traditions, key=lambda x: x["benchmark_readiness_index"], reverse=True):
    struct_table.append({
        "tradition": t["tradition"],
        "family": t["family"],
        "has_bm": t["has_benchmarks"],
        "gp_count": t["gate_passers_count"],
        "readiness": t["benchmark_readiness_index"],
        "total": t["total_structural_score"],
        "digital": t["digital_corpus"],
        "nlp": t["nlp_community"],
        "formal": t["formalizability"],
    })

# Readiness bar chart
readiness_labels = [t["tradition"] for t in struct_table]
readiness_vals   = [t["readiness"] for t in struct_table]
readiness_colors = ["#54A24B" if t["has_bm"] else "#E45756" for t in struct_table]

# -- A3 Values Relevance --
a3_scores: list[int] = []
a3_benchmarks: list[dict] = []
for a in batch1["assessments"]:
    v = a.get("features", {}).get("A3_values_relevance")
    if v is not None:
        a3_scores.append(v)
        a3_benchmarks.append({"name": a["short_title"][:45], "score": v,
                              "tradition": a.get("primary_tradition", "?")})
for a in batch2["assessments"]:
    v = a.get("features", {}).get("A3_values_alignment_relevance")
    if v is not None:
        a3_scores.append(v)
        a3_benchmarks.append({"name": a["short_title"][:45], "score": v,
                              "tradition": a.get("primary_tradition", "?")})

a3_mean = sum(a3_scores) / len(a3_scores) if a3_scores else 0
a3_benchmarks_sorted = sorted(a3_benchmarks, key=lambda x: x["score"], reverse=True)

# A1 construct breakdown
a1_counts: dict[str, int] = {}
for a in batch1["assessments"]:
    c = a.get("features", {}).get("A1_primary_construct", "unknown")
    a1_counts[c] = a1_counts.get(c, 0) + 1
for a in batch2["assessments"]:
    c = a.get("features", {}).get("A1_primary_construct", "unknown")
    a1_counts[c] = a1_counts.get(c, 0) + 1

# -- Claim robustness --
claim_chart: list[dict] = []
for c in claims_data["claims"]:
    num = c["claim_number"]
    text = c["claim_text"]
    if "tests" in c and isinstance(c["tests"], list):
        pv = c["tests"][0].get("p_value", 1.0)
    elif "p_value" in c:
        pv = c["p_value"]
    else:
        pv = 1.0
    if pv == 0.0:
        pv = 1e-15
    claim_chart.append({
        "claim": f"C{num}",
        "text": text,
        "p_value": pv,
        "neg_log_p": -math.log10(pv),
        "significant": pv < 0.05,
        "marginal": 0.05 <= pv < 0.10,
        "interpretation": c.get("interpretation", ""),
    })

# -- Correlation heatmap data --
corr_features = correlation["spearman_correlations"]["features"]
corr_matrix   = correlation["spearman_correlations"]["matrix"]

# ---------------------------------------------------------------------------
# Embed data as JSON
# ---------------------------------------------------------------------------
js_data = f"""
// === Pre-computed data constants ===
const OVERVIEW = {json.dumps({
    "total_candidates": total_candidates,
    "gate_passers": gate_passers,
    "n_traditions": n_traditions,
    "n_void": n_void,
    "tradition_counts": tradition_counts,
    "family_counts": family_counts,
})};

const BOOT_CI = {json.dumps({
    "labels": boot_labels,
    "means": boot_means,
    "lowers": boot_lowers,
    "uppers": boot_uppers,
    "families": boot_families,
    "top15_cutoff": top15_cutoff,
})};

const WEIGHT_SENSITIVITY = {json.dumps({
    "labels": rob_labels,
    "pct_top15": rob_pct_top15,
    "rank_range": rob_rank_range,
})};

const GATE_THRESHOLD = {json.dumps({
    "thresholds": gt_thresholds,
    "passers": gt_passers,
    "traditions": gt_traditions,
    "void_gained": gt_void_gained,
})};

const RADAR = {json.dumps({
    "factors": factor_labels,
    "series": radar_data,
})};

const STRUCT_TABLE = {json.dumps(struct_table)};

const READINESS = {json.dumps({
    "labels": readiness_labels,
    "values": readiness_vals,
    "colors": readiness_colors,
})};

const A3_DATA = {json.dumps({
    "scores": a3_scores,
    "mean": round(a3_mean, 1),
    "benchmarks": a3_benchmarks_sorted,
})};

const A1_COUNTS = {json.dumps(a1_counts)};

const CLAIMS = {json.dumps(claim_chart)};

const CORR = {json.dumps({
    "features": corr_features,
    "matrix": corr_matrix,
})};
"""

# ---------------------------------------------------------------------------
# Expert annotations — static prose written in council-of-experts voice.
# These are plain Python strings (NOT f-strings) so JS braces need no escaping.
# Interpolated into the HTML template as {ANNOTATIONS["key"]}.
# ---------------------------------------------------------------------------
ANNOTATIONS = {

"overview_intro": """
<div class="tab-intro">
  <div class="tab-intro-label">Overview — Systematic Screening Pipeline</div>
  This tab reports the outcome of a systematic screening pipeline applied to 401 candidate religious AI benchmarks
  identified through structured database search (Semantic Scholar, arXiv, Google Scholar), forward/backward
  citation chaining, and expert referral. Each candidate was scored on a six-component
  <strong>Religious Discriminability (RD) rubric</strong> that measures the depth of engagement with
  religious content — ranging from incidental mention (score near 0) to substantive theological evaluation
  (score near 100). Only candidates achieving <strong>RD ≥ 30</strong> and providing
  <strong>publicly accessible evaluation data</strong> (GitHub, HuggingFace, or equivalent) passed both
  hard gates and entered the analytical sample. The 88.3% attrition rate — from 401 screened to 47
  gate-passers — reflects the stringency of these criteria: most candidates touch religion
  peripherally rather than measuring religious constructs as their primary evaluation target.
</div>""",

"overview_charts": """
<div class="chart-annotation">
  <strong>Left chart — Gate-Passers by Tradition:</strong> Islam accounts for 28 of 47 gate-passers
  (59.6%), driven primarily by Arabic NLP corpora and Quranic QA shared tasks repurposed as religious
  benchmarks — an artifact of Arabic computational linguistics infrastructure, not a reflection of
  Islam's theological complexity or societal importance relative to other traditions. Christianity (6)
  and Buddhism (6) trail substantially; Hinduism (4), Sikhism (2), and Confucianism (1) each have
  minimal representation. Eight of 14 traditions analyzed have zero gate-passers.
  <br><br>
  <strong>Right chart — Gate-Passers by Tradition Family:</strong> Abrahamic traditions (Islam +
  Christianity) hold 34 of 47 gate-passers (72.3%), Dharmic traditions (Hinduism + Buddhism + Sikhism)
  hold 12 (25.5%), and East Asian traditions (Confucianism) hold 1 (2.1%). No gate-passers exist
  for African/Indigenous, Baha'i, Zoroastrian, Taoist, Shinto, Jewish, or Jain traditions.
  This concentration means AI systems are benchmarked almost exclusively against Abrahamic frameworks.
</div>
<div class="finding-callout">
  8 of 14 analyzed religious traditions — Judaism, Jainism, Taoism, Shinto, Ubuntu Philosophy,
  Indigenous Spirituality, Baha'i, and Zoroastrianism — have zero benchmarks that pass the quality gate,
  creating systematic blind spots in AI religious competency evaluation. The benchmark ecosystem does not
  reflect the world's religious diversity; it reflects the distribution of computational linguistics
  research infrastructure.
</div>""",

"sensitivity_intro": """
<div class="tab-intro">
  <div class="tab-intro-label">Sensitivity Analysis — Robustness of Rankings and Findings</div>
  A central methodological obligation in benchmark meta-evaluation is transparency about how sensitive
  findings are to specific analytical choices. This tab presents three complementary sensitivity analyses.
  <strong>Bootstrap resampling</strong> (10,000 Dirichlet-weighted iterations) quantifies uncertainty
  in composite scores and top-15 membership. <strong>Weight specification sensitivity</strong> tests
  whether the ranked list changes when the six rubric dimensions are weighted differently across 61
  alternative weight vectors. <strong>Gate threshold sensitivity</strong> examines how the pool size
  and tradition coverage change if the RD ≥ 30 gate is raised or lowered. Taken together, these analyses
  reveal where the paper's conclusions are robust and where intellectual humility is warranted.
</div>""",

"sensitivity_boot": """
<div class="chart-annotation">
  <strong>How to read this forest plot:</strong> Each horizontal bar represents one gate-passing benchmark.
  The center point is its mean composite score across 10,000 bootstrap resamples; the whiskers span
  the 95% confidence interval. The red dashed vertical line marks the top-15 cutoff score. Benchmarks
  whose confidence intervals cross this line have <em>uncertain</em> top-15 membership — their ranking
  could plausibly place them inside or outside the top 15 depending on which sample of weights is drawn.
  The average CI width is <strong>15.87 points</strong> on a 100-point composite scale.
  Of 47 gate-passers: <strong>9 are certain top-15 members</strong> (CI entirely above cutoff),
  <strong>6 are likely</strong> (mean above cutoff, CI overlaps), and <strong>8 are contested</strong>
  (CI straddles the cutoff). The remaining 24 are clearly outside the top 15.
  Treat ordinal rank differences between benchmarks near the cutoff with caution — the statistical
  uncertainty is substantial.
</div>""",

"sensitivity_weight_gate": """
<div class="chart-annotation">
  <strong>Left chart — Weight Sensitivity (Top-15 Stability):</strong> Each bar shows what percentage of
  61 alternative weight specifications keep that benchmark in the top 15. A benchmark at 100% is
  <em>robustly</em> top-15 regardless of how dimensions are weighted; one at 20% only appears when
  specific weights strongly favor its strengths. The mean Kendall's τ across weight combinations is
  <strong>0.773</strong>, indicating moderate rank-order stability overall, but individual benchmark
  positions vary considerably. Only the top 6 benchmarks (shown in green shading) maintain top-15
  membership across ≥ 95% of weight specifications.
  <br><br>
  <strong>Right chart — Gate Threshold vs. Coverage:</strong> The blue line (left axis) shows how many
  benchmarks pass at each RD threshold; the red dashed line (right axis) shows how many traditions are
  represented. Lowering the threshold to RD = 20 substantially increases the pool but admits candidates
  with only peripheral religious content. Raising to RD = 40 would eliminate several traditions' only
  benchmark. The current <strong>RD ≥ 30</strong> threshold represents a defensible compromise between
  inclusion and quality — it is the lowest value that excludes candidates rated as incidentally religious
  by the theological advisory council.
</div>""",

"void_intro": """
<div class="tab-intro">
  <div class="tab-intro-label">Tradition Void — Why Eight Traditions Have No Viable Benchmarks</div>
  The "tradition void" is not merely an absence of data — it is a structured pattern of exclusion
  driven by specific, identifiable infrastructure gaps. This tab investigates why 8 of 14 major
  religious traditions have zero gate-passing benchmarks by scoring each tradition on six
  <strong>structural factors</strong>: Digital Corpus availability, NLP Community size,
  Formalizability of doctrinal content, Data Sovereignty constraints, Institutional Support for
  computational research, and Publication Infrastructure (journals, shared tasks, workshops).
  The analysis tests whether the void can be explained by inherent properties of the traditions
  (e.g., oral transmission, lack of formal doctrine) or by research ecosystem gaps
  (e.g., absence of computational religious studies communities).
</div>""",

"void_charts": """
<div class="chart-annotation">
  <strong>Left chart — Void Factor Profiles (Radar):</strong> Three archetypes illustrate the structural
  landscape. <strong>Islam</strong> (blue) scores highest on Digital Corpus and NLP Community — reflecting
  decades of Arabic computational linguistics investment — but faces Data Sovereignty concerns around
  sacred text annotation. <strong>Judaism</strong> (red) has strong Institutional Support and
  Formalizability (Talmudic argumentation is highly structured), but a smaller active NLP community
  focused on benchmark creation. <strong>Indigenous Spirituality</strong> (green) scores low across all
  factors: oral transmission norms, restricted knowledge protocols governed by CARE Principles, minimal
  institutional interface with computational research. These profiles explain why benchmark availability
  follows infrastructure, not theological complexity.
  <br><br>
  <strong>Right chart — Benchmark Readiness Index:</strong> The composite readiness score (0–15 scale,
  summing all six structural factors) cleanly separates active traditions (green bars, mean = 10.5) from
  void traditions (red bars, mean = 5.1). The gap between the lowest active tradition and the highest
  void tradition identifies the structural threshold above which benchmark creation becomes practically
  feasible. No void tradition approaches this threshold under current conditions.
</div>""",

"void_table": """
<div class="chart-annotation">
  <strong>Structural Scores by Tradition:</strong> This table provides full factor scores for all
  14 traditions. The critical finding is that <strong>Publication Infrastructure</strong> is the strongest
  predictor of whether a tradition has benchmarks (point-biserial r = 0.74, p = 0.0025), while
  <strong>Formalizability is not significant</strong> (r = 0.414, p = 0.14). Traditions with structured,
  formalizable doctrines — Judaism, Jainism — still lack benchmarks because they lack the publication
  and NLP community infrastructure to produce them. This refutes the intuition that oral or less
  structured traditions are inherently harder to evaluate; the barrier is institutional, not theological.
</div>
<div class="finding-callout">
  Publication infrastructure — the existence of computational religious studies journals, shared tasks,
  and GitHub-hosted datasets — is the strongest predictor of benchmark availability (r = 0.74, p = 0.003),
  while theological formalizability is not significant (r = 0.41, p = 0.14). The tradition void is a
  research-infrastructure problem, not a theological one. Traditions with sophisticated, formalizable
  ethical systems (Judaism, Jainism) remain unrepresented because they lack the research ecosystem
  that converts scholarly knowledge into public evaluation datasets.
</div>""",

"values_intro": """
<div class="tab-intro">
  <div class="tab-intro-label">Values Relevance — Do Religious Benchmarks Actually Measure Values?</div>
  A benchmark can be "religious" in subject matter without measuring anything about religious
  <em>values</em>. Knowing that a model can identify Quranic verses or name Buddhist sects is different
  from knowing whether it can reason within a religious ethical framework when confronted with a novel
  moral dilemma. This tab reports the <strong>A3 Values Alignment Relevance score</strong> — a
  0-to-100 rubric assessing whether each benchmark tests value-laden reasoning (high A3) versus
  factual knowledge recall or bias detection (low A3). Scores were assigned through structured
  rubric assessment of each benchmark's items, constructs, and response format by the theological
  advisory council. The A1 construct type classification provides a complementary view of what
  benchmarks are actually measuring.
</div>""",

"values_charts": """
<div class="chart-annotation">
  <strong>Left chart — A3 Values Alignment Distribution:</strong> The distribution is heavily left-skewed:
  most of the 50 scored gate-passers cluster in the 0–40 range. The red dashed line at 50 marks the
  threshold for "minimal values relevance"; the green dashed line at 75 marks "strong values relevance."
  The <strong>mean A3 score is 33.6</strong> — well below the minimal threshold. Only 14 benchmarks
  (28%) score above 50, and only 6 (12%) score above 75, meaning the large majority of benchmarks
  labeled as "religious" test knowledge-about-religion rather than engagement-with-religious-values.
  The marker indicates the mean; observe how far it falls from either threshold.
  <br><br>
  <strong>Right chart — Construct Type Breakdown (A1):</strong> The A1 variable classifies what each
  benchmark <em>primarily</em> measures. The dominance of knowledge/factual and sentiment/attitude
  categories confirms the histogram finding: the field has produced knowledge tests and opinion-detection
  instruments, not tools that probe whether AI systems can reason within religious ethical frameworks,
  apply doctrinal principles to novel situations, or articulate the internal logic of a tradition's
  moral system.
</div>""",

"values_tables": """
<div class="chart-annotation">
  <strong>Top A3 Benchmarks</strong> are those that genuinely engage values: they present moral dilemmas
  grounded in specific traditions, require application of doctrinal principles, and assess reasoning
  quality rather than fact retrieval. <strong>Bottom A3 Benchmarks</strong> are primarily factual QA
  datasets ("Who was the Prophet Muhammad's first wife?"), sentiment classifiers, or hate speech detectors
  that use religious text as domain context rather than evaluating religious-values alignment.
  The gap between top and bottom spans nearly the entire 0–100 scale, indicating high heterogeneity
  within the set of benchmarks that share the "religious" label.
</div>
<div class="finding-callout">
  The mean A3 Values Alignment Relevance score is 33.6/100 across 50 gate-passing benchmarks. Only 6
  benchmarks (12%) achieve strong values alignment (A3 ≥ 75), and 94% treat their target tradition as a
  monolithic entity rather than acknowledging intra-tradition denominational or interpretive diversity.
  Most benchmarks that appear to test religious AI competency are, in fact, testing factual recall or
  bias detection — constructs with fundamentally different implications for AI deployment in religiously
  sensitive contexts.
</div>""",

"claims_intro": """
<div class="tab-intro">
  <div class="tab-intro-label">Claim Evidence — Pre-Registered Hypotheses and Statistical Tests</div>
  This tab presents the evidentiary record for each of the paper's seven central claims. Each claim
  was tested using the appropriate inferential procedure: chi-square tests for distributional asymmetry,
  binomial tests for proportion hypotheses, Spearman correlations for structural predictors, logistic
  regression for multivariate prediction, and bootstrap tests for ranking stability. Tests were specified
  before analysis; the results — including null results — are reported with equal prominence. Transparent
  reporting of unsupported claims is as important to the paper's credibility as the supported ones:
  the field does not benefit from selective presentation.
</div>""",

"claims_chart": """
<div class="chart-annotation">
  <strong>How to read this chart:</strong> Bars show −log₁₀(p-value) — a standard transformation where
  larger values indicate stronger statistical evidence. The dashed vertical line at 1.301 corresponds to
  p = 0.05 (the conventional significance threshold). <strong>Green bars</strong> exceed this threshold
  (claim statistically supported); <strong>orange bars</strong> fall in the marginal zone (0.05 &lt; p &lt; 0.10);
  <strong>red bars</strong> fall below (claim not supported at conventional levels). Of 7 claims:
  3 are supported (p &lt; 0.05), 1 is marginal (p ≈ 0.09), and 3 are not significant. Note that
  Claim 1 (tradition asymmetry, χ² test) and Claim 3 (data availability bottleneck, binomial test)
  produce p-values near zero — their bars extend to the chart boundary.
</div>""",

"claims_footer": """
<div class="chart-annotation" style="margin-top:12px">
  <strong>Interpreting non-significant results:</strong> The three unsupported claims (Field Recency,
  Structural Epistemic Injustice via logistic regression, and Bias-Values Conflation) are not refuted —
  they are simply not confirmed at conventional thresholds by the available data. In each case the
  direction of effect is consistent with the claim, but effect sizes are small or the sample is
  underpowered (n = 7–47 depending on the analysis). These claims warrant replication with a larger
  benchmark pool as the field matures. The paper's overall evidentiary posture — 3 confirmed,
  1 marginal, 3 unconfirmed — is characteristic of a nascent field where theoretical frameworks
  outpace available data.
</div>
<div class="finding-callout">
  3 of 7 paper claims are statistically supported (p &lt; 0.05): Tradition Asymmetry (χ²=64.96, p &lt; 0.001),
  Knowledge-Reasoning Conflation (binomial p = 0.0015), and Data Availability Bottleneck (binomial p &lt; 0.001).
  1 claim is marginal: WEIRD Bias Reversal (p ≈ 0.09). 3 claims are not statistically significant at
  conventional thresholds but remain theoretically motivated and should be revisited as the field grows.
</div>""",
}

# ---------------------------------------------------------------------------
# HTML template
# ---------------------------------------------------------------------------
FAMILY_COLOR_JS = """{
    "Abrahamic": "#4C78A8",
    "Dharmic": "#54A24B",
    "East Asian": "#E45756",
    "African/Indigenous": "#9D9D9D",
    "Other": "#9D9D9D"
}"""

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Religious Values Benchmark Meta-Evaluation Dashboard</title>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<script src="https://cdn.jsdelivr.net/npm/echarts@5.5.0/dist/echarts.min.js"></script>
<style>
:root {{
    --bg-primary: #0d1117;
    --bg-secondary: #161b22;
    --bg-card: #1c2128;
    --text-primary: #e6edf3;
    --text-secondary: #8b949e;
    --accent-blue: #4C78A8;
    --accent-green: #54A24B;
    --accent-red: #E45756;
    --accent-orange: #F58518;
    --border: #30363d;
}}
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
body {{
    font-family: 'Inter', sans-serif;
    background: var(--bg-primary);
    color: var(--text-primary);
    min-height: 100vh;
}}
.header {{
    background: var(--bg-secondary);
    border-bottom: 1px solid var(--border);
    padding: 16px 24px;
}}
.header h1 {{
    font-size: 1.4rem;
    font-weight: 700;
    margin: 0;
}}
.header .subtitle {{
    font-size: 0.85rem;
    color: var(--text-secondary);
    margin-top: 2px;
}}
.nav-tabs {{
    border-bottom: 1px solid var(--border);
    background: var(--bg-secondary);
    padding: 0 24px;
}}
.nav-tabs .nav-link {{
    color: var(--text-secondary);
    border: none;
    padding: 10px 18px;
    font-size: 0.9rem;
    font-weight: 500;
    border-bottom: 2px solid transparent;
    transition: all 0.2s;
}}
.nav-tabs .nav-link:hover {{
    color: var(--text-primary);
    border-bottom-color: var(--accent-blue);
}}
.nav-tabs .nav-link.active {{
    color: var(--accent-blue);
    background: transparent;
    border-bottom: 2px solid var(--accent-blue);
}}
.tab-content {{
    padding: 20px 24px;
}}
.card-stat {{
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 20px;
    text-align: center;
}}
.card-stat .number {{
    font-size: 2.2rem;
    font-weight: 700;
    color: var(--accent-blue);
}}
.card-stat .label {{
    font-size: 0.85rem;
    color: var(--text-secondary);
    margin-top: 4px;
}}
.chart-container {{
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 16px;
    margin-bottom: 20px;
}}
.chart-title {{
    font-size: 1rem;
    font-weight: 600;
    margin-bottom: 12px;
    color: var(--text-primary);
}}
table.dark-table {{
    width: 100%;
    border-collapse: collapse;
    font-size: 0.85rem;
}}
table.dark-table th {{
    background: var(--bg-secondary);
    color: var(--text-secondary);
    padding: 8px 10px;
    text-align: left;
    font-weight: 600;
    border-bottom: 1px solid var(--border);
}}
table.dark-table td {{
    padding: 7px 10px;
    border-bottom: 1px solid var(--border);
    color: var(--text-primary);
}}
table.dark-table tr:hover td {{
    background: rgba(76, 120, 168, 0.08);
}}
.badge-void {{
    background: var(--accent-red);
    color: white;
    padding: 2px 8px;
    border-radius: 4px;
    font-size: 0.75rem;
    font-weight: 600;
}}
.badge-active {{
    background: var(--accent-green);
    color: white;
    padding: 2px 8px;
    border-radius: 4px;
    font-size: 0.75rem;
    font-weight: 600;
}}
.claim-card {{
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 14px 16px;
    margin-bottom: 10px;
}}
.claim-card .claim-num {{
    font-weight: 700;
    color: var(--accent-blue);
}}
.claim-card .claim-text {{
    color: var(--text-primary);
    font-size: 0.9rem;
}}
.claim-card .claim-pval {{
    font-size: 0.8rem;
    margin-top: 4px;
}}
.claim-card .claim-interp {{
    font-size: 0.8rem;
    color: var(--text-secondary);
    margin-top: 6px;
}}
.tab-intro {{
    background: var(--bg-secondary);
    border-left: 3px solid var(--accent-blue);
    border-radius: 0 6px 6px 0;
    padding: 14px 18px;
    margin-bottom: 20px;
    font-size: 0.88rem;
    line-height: 1.65;
    color: var(--text-primary);
}}
.tab-intro-label {{
    font-size: 0.72rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.07em;
    color: var(--accent-blue);
    margin-bottom: 6px;
}}
.chart-annotation {{
    border-left: 2px solid var(--border);
    padding: 8px 14px;
    margin: -10px 0 20px 0;
    font-size: 0.82rem;
    line-height: 1.6;
    color: var(--text-secondary);
}}
.chart-annotation strong {{
    color: var(--text-primary);
    font-weight: 600;
}}
.finding-callout {{
    background: rgba(76, 120, 168, 0.09);
    border: 1px solid rgba(76, 120, 168, 0.28);
    border-radius: 6px;
    padding: 10px 14px;
    margin: 6px 0 20px 0;
    font-size: 0.82rem;
    color: var(--text-primary);
    line-height: 1.55;
}}
.finding-callout::before {{
    content: "KEY FINDING";
    display: block;
    font-size: 0.68rem;
    font-weight: 700;
    letter-spacing: 0.09em;
    color: var(--accent-blue);
    margin-bottom: 5px;
}}
</style>
</head>
<body>

<div class="header">
    <h1>Religious Values Benchmark Meta-Evaluation</h1>
    <div class="subtitle">What Do Religious AI Benchmarks Actually Measure?  |  Dashboard v2  |  2026-04-04</div>
</div>

<ul class="nav nav-tabs" id="mainTabs" role="tablist">
    <li class="nav-item"><a class="nav-link active" data-bs-toggle="tab" href="#tab-overview">Overview</a></li>
    <li class="nav-item"><a class="nav-link" data-bs-toggle="tab" href="#tab-sensitivity">Sensitivity</a></li>
    <li class="nav-item"><a class="nav-link" data-bs-toggle="tab" href="#tab-void">Tradition Void</a></li>
    <li class="nav-item"><a class="nav-link" data-bs-toggle="tab" href="#tab-values">Values Relevance</a></li>
    <li class="nav-item"><a class="nav-link" data-bs-toggle="tab" href="#tab-claims">Claim Evidence</a></li>
</ul>

<div class="tab-content">

<!-- ============ TAB 1: OVERVIEW ============ -->
<div class="tab-pane fade show active" id="tab-overview">
    {ANNOTATIONS["overview_intro"]}
    <div class="row g-3 mb-4">
        <div class="col-md-3">
            <div class="card-stat">
                <div class="number">{total_candidates}</div>
                <div class="label">Total Candidates Screened</div>
            </div>
        </div>
        <div class="col-md-3">
            <div class="card-stat">
                <div class="number" style="color:var(--accent-green)">{gate_passers}</div>
                <div class="label">Gate-Passers (RD &ge; 30)</div>
            </div>
        </div>
        <div class="col-md-3">
            <div class="card-stat">
                <div class="number">{n_traditions}</div>
                <div class="label">Religious Traditions Analyzed</div>
            </div>
        </div>
        <div class="col-md-3">
            <div class="card-stat">
                <div class="number" style="color:var(--accent-red)">{n_void}</div>
                <div class="label">Void Traditions (0 Gate-Passers)</div>
            </div>
        </div>
    </div>
    <div class="row g-3">
        <div class="col-md-6">
            <div class="chart-container">
                <div class="chart-title">Gate-Passers by Tradition</div>
                <div id="chart-tradition-bar" style="height:350px"></div>
            </div>
        </div>
        <div class="col-md-6">
            <div class="chart-container">
                <div class="chart-title">Gate-Passers by Tradition Family</div>
                <div id="chart-family-pie" style="height:350px"></div>
            </div>
        </div>
    </div>
    {ANNOTATIONS["overview_charts"]}
</div>

<!-- ============ TAB 2: SENSITIVITY ============ -->
<div class="tab-pane fade" id="tab-sensitivity">
    {ANNOTATIONS["sensitivity_intro"]}
    <div class="row g-3 mb-4">
        <div class="col-12">
            <div class="chart-container">
                <div class="chart-title">Bootstrap 95% CI for Composite Scores (n=10,000)</div>
                <div id="chart-boot-ci" style="height:900px"></div>
            </div>
            {ANNOTATIONS["sensitivity_boot"]}
        </div>
    </div>
    <div class="row g-3 mb-4">
        <div class="col-md-6">
            <div class="chart-container">
                <div class="chart-title">Weight Sensitivity: Top-15 Stability (%)</div>
                <div id="chart-weight-sens" style="height:450px"></div>
            </div>
        </div>
        <div class="col-md-6">
            <div class="chart-container">
                <div class="chart-title">Gate Threshold vs Coverage</div>
                <div id="chart-gate-threshold" style="height:450px"></div>
            </div>
        </div>
    </div>
    {ANNOTATIONS["sensitivity_weight_gate"]}
</div>

<!-- ============ TAB 3: TRADITION VOID ============ -->
<div class="tab-pane fade" id="tab-void">
    {ANNOTATIONS["void_intro"]}
    <div class="row g-3 mb-4">
        <div class="col-md-6">
            <div class="chart-container">
                <div class="chart-title">Void Factor Profiles: Three Tradition Archetypes</div>
                <div id="chart-radar" style="height:450px"></div>
            </div>
        </div>
        <div class="col-md-6">
            <div class="chart-container">
                <div class="chart-title">Benchmark Readiness Index by Tradition</div>
                <div id="chart-readiness" style="height:450px"></div>
            </div>
        </div>
    </div>
    {ANNOTATIONS["void_charts"]}
    <div class="chart-container">
        <div class="chart-title">Structural Scores by Tradition</div>
        <table class="dark-table">
            <thead>
                <tr>
                    <th>Tradition</th><th>Family</th><th>Status</th><th>Gate-Passers</th>
                    <th>Digital</th><th>NLP</th><th>Formalizability</th>
                    <th>Readiness</th><th>Total</th>
                </tr>
            </thead>
            <tbody id="struct-table-body"></tbody>
        </table>
    </div>
    {ANNOTATIONS["void_table"]}
</div>

<!-- ============ TAB 4: VALUES RELEVANCE ============ -->
<div class="tab-pane fade" id="tab-values">
    {ANNOTATIONS["values_intro"]}
    <div class="row g-3 mb-4">
        <div class="col-md-6">
            <div class="chart-container">
                <div class="chart-title">A3 Values Alignment Relevance Distribution</div>
                <div id="chart-a3-hist" style="height:380px"></div>
            </div>
        </div>
        <div class="col-md-6">
            <div class="chart-container">
                <div class="chart-title">Construct Type Breakdown (A1)</div>
                <div id="chart-a1-pie" style="height:380px"></div>
            </div>
        </div>
    </div>
    {ANNOTATIONS["values_charts"]}
    <div class="row g-3">
        <div class="col-md-6">
            <div class="chart-container">
                <div class="chart-title">Top A3 Benchmarks (Values-Aligned)</div>
                <table class="dark-table">
                    <thead><tr><th>Benchmark</th><th>Tradition</th><th>A3 Score</th></tr></thead>
                    <tbody id="a3-top-table"></tbody>
                </table>
            </div>
        </div>
        <div class="col-md-6">
            <div class="chart-container">
                <div class="chart-title">Bottom A3 Benchmarks (Knowledge-Oriented)</div>
                <table class="dark-table">
                    <thead><tr><th>Benchmark</th><th>Tradition</th><th>A3 Score</th></tr></thead>
                    <tbody id="a3-bottom-table"></tbody>
                </table>
            </div>
        </div>
    </div>
    {ANNOTATIONS["values_tables"]}
</div>

<!-- ============ TAB 5: CLAIM EVIDENCE ============ -->
<div class="tab-pane fade" id="tab-claims">
    {ANNOTATIONS["claims_intro"]}
    <div class="row g-3 mb-4">
        <div class="col-12">
            <div class="chart-container">
                <div class="chart-title">Statistical Support for Paper Claims</div>
                <div id="chart-claims" style="height:350px"></div>
            </div>
            {ANNOTATIONS["claims_chart"]}
        </div>
    </div>
    <div id="claim-cards"></div>
    {ANNOTATIONS["claims_footer"]}
</div>

</div><!-- /tab-content -->

<script>
{js_data}

const FAMILY_COLORS = {FAMILY_COLOR_JS};

function familyColor(f) {{
    return FAMILY_COLORS[f] || "#9D9D9D";
}}

// ===== TAB 1: Overview Charts =====
function renderOverview() {{
    // Tradition bar
    var trads = Object.entries(OVERVIEW.tradition_counts).sort((a,b) => b[1]-a[1]);
    var tradChart = echarts.init(document.getElementById('chart-tradition-bar'));
    tradChart.setOption({{
        tooltip: {{ trigger: 'axis' }},
        xAxis: {{ type: 'category', data: trads.map(t=>t[0]), axisLabel: {{ rotate: 30, color: '#8b949e' }}, axisLine: {{ lineStyle: {{ color: '#30363d' }} }} }},
        yAxis: {{ type: 'value', axisLabel: {{ color: '#8b949e' }}, splitLine: {{ lineStyle: {{ color: '#21262d' }} }} }},
        series: [{{ type: 'bar', data: trads.map(t => ({{ value: t[1], itemStyle: {{ color: '#4C78A8' }} }})), barMaxWidth: 40 }}],
        grid: {{ left: 50, right: 20, bottom: 60, top: 20 }},
        backgroundColor: 'transparent'
    }});

    // Family pie
    var fams = Object.entries(OVERVIEW.family_counts).map(f => ({{ name: f[0], value: f[1] }}));
    var famChart = echarts.init(document.getElementById('chart-family-pie'));
    famChart.setOption({{
        tooltip: {{ trigger: 'item', formatter: '{{b}}: {{c}} ({{d}}%)' }},
        series: [{{
            type: 'pie', radius: ['35%','65%'],
            data: fams.map(f => ({{ ...f, itemStyle: {{ color: familyColor(f.name) }} }})),
            label: {{ color: '#e6edf3', fontSize: 12 }},
            emphasis: {{ itemStyle: {{ shadowBlur: 10 }} }}
        }}],
        backgroundColor: 'transparent'
    }});
}}

// ===== TAB 2: Sensitivity Charts =====
function renderSensitivity() {{
    // Bootstrap CI forest plot (horizontal)
    var bc = echarts.init(document.getElementById('chart-boot-ci'));
    var n = BOOT_CI.labels.length;
    var errData = [];
    for (var i = 0; i < n; i++) {{
        errData.push([BOOT_CI.lowers[i], n - 1 - i]);
        errData.push([BOOT_CI.uppers[i], n - 1 - i]);
    }}
    bc.setOption({{
        tooltip: {{
            trigger: 'axis',
            axisPointer: {{ type: 'shadow' }},
            formatter: function(p) {{
                var idx = n - 1 - p[0].dataIndex;
                return BOOT_CI.labels[idx] + '<br>Mean: ' + BOOT_CI.means[idx].toFixed(1) +
                    '<br>95% CI: [' + BOOT_CI.lowers[idx].toFixed(1) + ', ' + BOOT_CI.uppers[idx].toFixed(1) + ']';
            }}
        }},
        xAxis: {{
            type: 'value',
            name: 'Composite Score',
            nameLocation: 'middle',
            nameGap: 30,
            axisLabel: {{ color: '#8b949e' }},
            splitLine: {{ lineStyle: {{ color: '#21262d' }} }}
        }},
        yAxis: {{
            type: 'category',
            data: BOOT_CI.labels.slice().reverse(),
            axisLabel: {{ color: '#8b949e', fontSize: 9 }},
            axisLine: {{ lineStyle: {{ color: '#30363d' }} }}
        }},
        series: [
            {{
                type: 'bar',
                data: BOOT_CI.means.slice().reverse().map(function(v, i) {{
                    var origIdx = n - 1 - i;
                    return {{ value: v, itemStyle: {{ color: familyColor(BOOT_CI.families[origIdx]) }} }};
                }}),
                barMaxWidth: 14
            }},
            {{
                type: 'custom',
                renderItem: function(params, api) {{
                    var catIdx = api.value(1);
                    var origIdx = n - 1 - catIdx;
                    var lo = api.coord([BOOT_CI.lowers[origIdx], catIdx]);
                    var hi = api.coord([BOOT_CI.uppers[origIdx], catIdx]);
                    var halfH = 4;
                    return {{
                        type: 'group',
                        children: [
                            {{ type: 'line', shape: {{ x1: lo[0], y1: lo[1], x2: hi[0], y2: hi[1] }}, style: {{ stroke: '#aaa', lineWidth: 1.2 }} }},
                            {{ type: 'line', shape: {{ x1: lo[0], y1: lo[1]-halfH, x2: lo[0], y2: lo[1]+halfH }}, style: {{ stroke: '#aaa', lineWidth: 1.2 }} }},
                            {{ type: 'line', shape: {{ x1: hi[0], y1: hi[1]-halfH, x2: hi[0], y2: hi[1]+halfH }}, style: {{ stroke: '#aaa', lineWidth: 1.2 }} }}
                        ]
                    }};
                }},
                encode: {{ x: 0, y: 1 }},
                data: (function() {{
                    var d = [];
                    for (var i = 0; i < n; i++) {{
                        d.push([BOOT_CI.means[i], n - 1 - i]);
                    }}
                    return d;
                }})(),
                z: 10
            }}
        ],
        markLine: {{ data: [{{ xAxis: BOOT_CI.top15_cutoff }}] }},
        grid: {{ left: 260, right: 30, top: 10, bottom: 40 }},
        backgroundColor: 'transparent'
    }});

    // Top-15 cutoff line
    bc.setOption({{
        series: [{{
            markLine: {{
                silent: true,
                lineStyle: {{ color: '#E45756', type: 'dashed', width: 1.5 }},
                label: {{ formatter: 'Top-15 cutoff', color: '#E45756', fontSize: 10 }},
                data: [{{ xAxis: BOOT_CI.top15_cutoff }}]
            }}
        }}]
    }});

    // Weight sensitivity bar
    var ws = echarts.init(document.getElementById('chart-weight-sens'));
    ws.setOption({{
        tooltip: {{ trigger: 'axis' }},
        xAxis: {{ type: 'value', max: 100, name: '% in Top-15', axisLabel: {{ color: '#8b949e' }}, splitLine: {{ lineStyle: {{ color: '#21262d' }} }} }},
        yAxis: {{ type: 'category', data: WEIGHT_SENSITIVITY.labels.slice().reverse(), axisLabel: {{ color: '#8b949e', fontSize: 9 }}, axisLine: {{ lineStyle: {{ color: '#30363d' }} }} }},
        series: [{{
            type: 'bar', data: WEIGHT_SENSITIVITY.pct_top15.slice().reverse().map(function(v) {{
                var color = v >= 90 ? '#54A24B' : v >= 50 ? '#F58518' : '#E45756';
                return {{ value: v, itemStyle: {{ color: color }} }};
            }}),
            barMaxWidth: 16
        }}],
        grid: {{ left: 240, right: 30, top: 10, bottom: 30 }},
        backgroundColor: 'transparent'
    }});

    // Gate threshold
    var gt = echarts.init(document.getElementById('chart-gate-threshold'));
    gt.setOption({{
        tooltip: {{ trigger: 'axis' }},
        legend: {{ data: ['Gate-Passers', 'Traditions'], textStyle: {{ color: '#8b949e' }}, top: 0 }},
        xAxis: {{ type: 'category', data: GATE_THRESHOLD.thresholds, name: 'RD Threshold', nameLocation: 'middle', nameGap: 30, axisLabel: {{ color: '#8b949e' }}, axisLine: {{ lineStyle: {{ color: '#30363d' }} }} }},
        yAxis: [
            {{ type: 'value', name: 'Gate-Passers', axisLabel: {{ color: '#4C78A8' }}, splitLine: {{ lineStyle: {{ color: '#21262d' }} }} }},
            {{ type: 'value', name: 'Traditions', axisLabel: {{ color: '#E45756' }}, splitLine: {{ show: false }} }}
        ],
        series: [
            {{ name: 'Gate-Passers', type: 'line', data: GATE_THRESHOLD.passers, itemStyle: {{ color: '#4C78A8' }}, lineStyle: {{ width: 2 }}, symbol: 'circle', symbolSize: 8 }},
            {{ name: 'Traditions', type: 'line', yAxisIndex: 1, data: GATE_THRESHOLD.traditions, itemStyle: {{ color: '#E45756' }}, lineStyle: {{ width: 2, type: 'dashed' }}, symbol: 'rect', symbolSize: 8 }}
        ],
        grid: {{ left: 60, right: 60, top: 40, bottom: 40 }},
        backgroundColor: 'transparent'
    }});
    // Add threshold markers
    gt.setOption({{
        series: [{{
            markLine: {{
                silent: true,
                lineStyle: {{ color: '#54A24B', type: 'dotted', width: 2 }},
                label: {{ formatter: 'Current (30)', color: '#54A24B', fontSize: 10 }},
                data: [{{ xAxis: '30' }}]
            }}
        }}, {{
            markLine: {{
                silent: true,
                lineStyle: {{ color: '#F58518', type: 'dotted', width: 2 }},
                label: {{ formatter: 'NormEval (40)', color: '#F58518', fontSize: 10 }},
                data: [{{ xAxis: '40' }}]
            }}
        }}]
    }});
}}

// ===== TAB 3: Tradition Void =====
function renderVoid() {{
    // Radar
    var radarChart = echarts.init(document.getElementById('chart-radar'));
    var indicators = RADAR.factors.map(function(f) {{ return {{ name: f, max: 5 }}; }});
    var radarColors = {{ "Islam": "#4C78A8", "Judaism": "#E45756", "Indigenous Spirituality": "#54A24B" }};
    var seriesData = Object.entries(RADAR.series).map(function(entry) {{
        return {{ value: entry[1], name: entry[0], lineStyle: {{ width: 2 }}, areaStyle: {{ opacity: 0.15 }}, itemStyle: {{ color: radarColors[entry[0]] || '#9D9D9D' }} }};
    }});
    radarChart.setOption({{
        tooltip: {{}},
        legend: {{ data: Object.keys(RADAR.series), textStyle: {{ color: '#8b949e' }}, bottom: 0 }},
        radar: {{ indicator: indicators, shape: 'polygon', axisName: {{ color: '#8b949e', fontSize: 11 }}, splitArea: {{ areaStyle: {{ color: ['#161b22','#1c2128','#161b22','#1c2128','#161b22'] }} }}, splitLine: {{ lineStyle: {{ color: '#30363d' }} }}, axisLine: {{ lineStyle: {{ color: '#30363d' }} }} }},
        series: [{{ type: 'radar', data: seriesData }}],
        backgroundColor: 'transparent'
    }});

    // Readiness bar
    var rb = echarts.init(document.getElementById('chart-readiness'));
    rb.setOption({{
        tooltip: {{ trigger: 'axis' }},
        xAxis: {{ type: 'category', data: READINESS.labels, axisLabel: {{ rotate: 35, color: '#8b949e', fontSize: 9 }}, axisLine: {{ lineStyle: {{ color: '#30363d' }} }} }},
        yAxis: {{ type: 'value', name: 'Readiness Index', max: 15, axisLabel: {{ color: '#8b949e' }}, splitLine: {{ lineStyle: {{ color: '#21262d' }} }} }},
        series: [{{
            type: 'bar',
            data: READINESS.values.map(function(v, i) {{
                return {{ value: v, itemStyle: {{ color: READINESS.colors[i] }} }};
            }}),
            barMaxWidth: 30
        }}],
        grid: {{ left: 50, right: 20, bottom: 80, top: 30 }},
        backgroundColor: 'transparent'
    }});

    // Structural table
    var tbody = document.getElementById('struct-table-body');
    STRUCT_TABLE.forEach(function(t) {{
        var statusBadge = t.has_bm ? '<span class="badge-active">Active</span>' : '<span class="badge-void">Void</span>';
        tbody.innerHTML += '<tr>' +
            '<td>' + t.tradition + '</td>' +
            '<td>' + t.family + '</td>' +
            '<td>' + statusBadge + '</td>' +
            '<td>' + t.gp_count + '</td>' +
            '<td>' + t.digital + '</td>' +
            '<td>' + t.nlp + '</td>' +
            '<td>' + t.formal + '</td>' +
            '<td><strong>' + t.readiness + '</strong></td>' +
            '<td>' + t.total + '</td>' +
            '</tr>';
    }});
}}

// ===== TAB 4: Values Relevance =====
function renderValues() {{
    // A3 histogram
    var a3hist = echarts.init(document.getElementById('chart-a3-hist'));
    // Bin the scores into 10-wide bins
    var bins = [0,10,20,30,40,50,60,70,80,90,100];
    var counts = new Array(bins.length - 1).fill(0);
    A3_DATA.scores.forEach(function(s) {{
        var idx = Math.min(Math.floor(s / 10), counts.length - 1);
        counts[idx]++;
    }});
    var binLabels = [];
    for (var i = 0; i < bins.length - 1; i++) {{
        binLabels.push(bins[i] + '-' + (bins[i+1]-1));
    }}
    a3hist.setOption({{
        tooltip: {{ trigger: 'axis' }},
        xAxis: {{ type: 'category', data: binLabels, name: 'A3 Score Range', nameLocation: 'middle', nameGap: 30, axisLabel: {{ color: '#8b949e' }}, axisLine: {{ lineStyle: {{ color: '#30363d' }} }} }},
        yAxis: {{ type: 'value', name: 'Count', axisLabel: {{ color: '#8b949e' }}, splitLine: {{ lineStyle: {{ color: '#21262d' }} }} }},
        series: [{{
            type: 'bar', data: counts.map(function(v) {{ return {{ value: v, itemStyle: {{ color: '#4C78A8' }} }}; }}), barMaxWidth: 35
        }}],
        grid: {{ left: 50, right: 20, bottom: 50, top: 20 }},
        backgroundColor: 'transparent'
    }});
    // Add mean line and threshold lines
    a3hist.setOption({{
        series: [{{
            markLine: {{
                silent: true,
                data: [
                    {{ xAxis: 4, lineStyle: {{ color: '#E45756', type: 'dashed' }}, label: {{ formatter: 'Minimal (50)', color: '#E45756' }} }},
                    {{ xAxis: 7, lineStyle: {{ color: '#54A24B', type: 'dashed' }}, label: {{ formatter: 'Strong (75)', color: '#54A24B' }} }}
                ]
            }},
            markPoint: {{
                data: [{{ coord: [Math.floor(A3_DATA.mean / 10), 0], value: 'Mean=' + A3_DATA.mean, symbolSize: 0, label: {{ show: true, color: '#F58518', fontSize: 11, position: 'top', offset: [0, -30] }} }}]
            }}
        }}]
    }});

    // A1 pie
    var a1pie = echarts.init(document.getElementById('chart-a1-pie'));
    var a1data = Object.entries(A1_COUNTS).map(function(e) {{ return {{ name: e[0], value: e[1] }}; }});
    a1pie.setOption({{
        tooltip: {{ trigger: 'item', formatter: '{{b}}: {{c}} ({{d}}%)' }},
        series: [{{
            type: 'pie', radius: ['30%','60%'],
            data: a1data,
            label: {{ color: '#e6edf3', fontSize: 10, formatter: '{{b}}\\n{{d}}%' }},
            emphasis: {{ itemStyle: {{ shadowBlur: 10 }} }}
        }}],
        backgroundColor: 'transparent'
    }});

    // Top A3 table
    var topTbody = document.getElementById('a3-top-table');
    A3_DATA.benchmarks.slice(0, 10).forEach(function(b) {{
        topTbody.innerHTML += '<tr><td>' + b.name + '</td><td>' + b.tradition + '</td><td><strong>' + b.score + '</strong></td></tr>';
    }});

    // Bottom A3 table
    var botTbody = document.getElementById('a3-bottom-table');
    A3_DATA.benchmarks.slice(-10).reverse().forEach(function(b) {{
        botTbody.innerHTML += '<tr><td>' + b.name + '</td><td>' + b.tradition + '</td><td>' + b.score + '</td></tr>';
    }});
}}

// ===== TAB 5: Claim Evidence =====
function renderClaims() {{
    // Chart
    var cc = echarts.init(document.getElementById('chart-claims'));
    var claimLabels = CLAIMS.map(function(c) {{ return c.claim + ': ' + c.text.substring(0, 50); }});
    var claimVals = CLAIMS.map(function(c) {{
        var color = c.significant ? '#54A24B' : c.marginal ? '#F58518' : '#E45756';
        return {{ value: c.neg_log_p, itemStyle: {{ color: color }} }};
    }});
    cc.setOption({{
        tooltip: {{
            trigger: 'axis',
            formatter: function(p) {{
                var c = CLAIMS[CLAIMS.length - 1 - p[0].dataIndex];
                var pstr = c.p_value < 0.001 ? 'p < 0.001' : 'p = ' + c.p_value.toFixed(4);
                return c.claim + ': ' + c.text.substring(0,60) + '<br>' + pstr;
            }}
        }},
        xAxis: {{ type: 'value', name: '-log10(p)', nameLocation: 'middle', nameGap: 30, axisLabel: {{ color: '#8b949e' }}, splitLine: {{ lineStyle: {{ color: '#21262d' }} }} }},
        yAxis: {{ type: 'category', data: claimLabels.slice().reverse(), axisLabel: {{ color: '#8b949e', fontSize: 9 }}, axisLine: {{ lineStyle: {{ color: '#30363d' }} }} }},
        series: [{{
            type: 'bar', data: claimVals.slice().reverse(), barMaxWidth: 24,
            markLine: {{
                silent: true,
                lineStyle: {{ color: '#aaa', type: 'dashed', width: 1.2 }},
                label: {{ formatter: 'p = 0.05', color: '#aaa', fontSize: 10 }},
                data: [{{ xAxis: 1.301 }}]
            }}
        }}],
        grid: {{ left: 300, right: 30, top: 10, bottom: 40 }},
        backgroundColor: 'transparent'
    }});

    // Claim cards
    var cardsDiv = document.getElementById('claim-cards');
    CLAIMS.forEach(function(c) {{
        var color = c.significant ? '#54A24B' : c.marginal ? '#F58518' : '#E45756';
        var status = c.significant ? 'SUPPORTED' : c.marginal ? 'MARGINAL' : 'NOT SUPPORTED';
        var pstr = c.p_value < 0.001 ? 'p < 0.001' : 'p = ' + c.p_value.toFixed(4);
        cardsDiv.innerHTML += '<div class="claim-card">' +
            '<span class="claim-num">' + c.claim + '</span> ' +
            '<span class="claim-text">' + c.text + '</span>' +
            '<div class="claim-pval" style="color:' + color + '"><strong>' + status + '</strong> (' + pstr + ')</div>' +
            '<div class="claim-interp">' + c.interpretation + '</div>' +
            '</div>';
    }});
}}

// ===== Initialize =====
document.addEventListener('DOMContentLoaded', function() {{
    renderOverview();

    // Lazy-render tabs on first show
    var rendered = {{ overview: true }};
    document.querySelectorAll('#mainTabs .nav-link').forEach(function(tab) {{
        tab.addEventListener('shown.bs.tab', function(e) {{
            var target = e.target.getAttribute('href').replace('#tab-', '');
            if (!rendered[target]) {{
                rendered[target] = true;
                if (target === 'sensitivity') renderSensitivity();
                else if (target === 'void') renderVoid();
                else if (target === 'values') renderValues();
                else if (target === 'claims') renderClaims();
            }}
            // Resize charts on tab show (ECharts needs this)
            setTimeout(function() {{
                document.querySelectorAll('.tab-pane.active [id^="chart-"]').forEach(function(el) {{
                    var chart = echarts.getInstanceByDom(el);
                    if (chart) chart.resize();
                }});
            }}, 100);
        }});
    }});

    // Window resize
    window.addEventListener('resize', function() {{
        document.querySelectorAll('[id^="chart-"]').forEach(function(el) {{
            var chart = echarts.getInstanceByDom(el);
            if (chart) chart.resize();
        }});
    }});
}});
</script>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
"""

OUT.write_text(html)
print(f"Dashboard written to {OUT}")
print(f"File size: {OUT.stat().st_size:,} bytes")
