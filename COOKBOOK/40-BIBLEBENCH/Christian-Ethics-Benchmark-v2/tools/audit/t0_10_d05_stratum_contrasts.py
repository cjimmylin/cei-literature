"""T0-10: stratum-aware recompute of the design-05 C1 contrasts.

Canary: WALKWORTHY-CANARY-7f3e2026

DIAGNOSTIC RECOMPUTE -- NOT A WALKWORTHY HEADLINE.

This is a NUMBERS-ONLY companion to
`logs/fullbank-3ep-20260724/c1_design05_contrasts.py`. That script computed the
published "0 of 10 contrasts excluding zero" for design 05 pooling ALL strata
(a + c), but the pre-registration (C1, `20260716-prereg-comparisons-RATIFIED.md`)
says the C1 family is scoped to **stratum-(a) cells only**. This script does not
adjudicate which scope is correct -- it reports both, plus a stratum-cell floor
accounting, so the successor note (written elsewhere, NOT by this script) has the
raw numbers to cite.

The original script resolves its run tree via `Path(__file__).parent` (it lives
inside the run tree). This copy lives in `tools/audit/` (git-tracked; `logs/` is
gitignored) so RUN_ROOT is pinned explicitly below instead.

Statistical machinery below (epoch-averaging so n = items, not items x epochs;
Bonferroni m=30 FROZEN by RULING 1a; Acklam inverse-normal approximation;
excludes-zero / crosses-zero wording, no significance stars per R3) is copied
VERBATIM from the original script. Do not "improve" it here -- any machinery
change is a metric change and out of Tier-0 scope.

PANEL 0 is a byte-for-byte reproduction of the original script's computation
(all strata pooled, exemplars dropped) and is diffed against a live subprocess
run of the untouched original as a gate (G0). If G0 does not pass, this script
aborts before printing PANEL A / PANEL C5 -- do not trust downstream numbers
from a script whose baseline does not reproduce.

PANEL A restricts to stratum-a, non-exemplar rows only (per C1's literal scope).

PANEL C5 reports the stratum-a cell's administration/item floor accounting two
ways -- (i) scored non-exemplar ADMINS per (design, SUT) cell, i.e. raw
item x epoch score count, and (ii) epoch-averaged ITEMS per cell, i.e. the n
that panel A's contrasts actually run on -- against the C5 floor value of 20.
No verdict is printed; floor adjudication is not this script's job.
"""
import difflib
import json
import math
import statistics
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

CANARY = "WALKWORTHY-CANARY-7f3e2026"

V2 = Path("/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/COOKBOOK/"
          "40-BIBLEBENCH/Christian-Ethics-Benchmark-v2")
RUN_ROOT = V2 / "logs" / "fullbank-3ep-20260724"          # pinned explicitly (T0-10)
ORIG_SCRIPT = RUN_ROOT / "c1_design05_contrasts.py"
BANK_JSONL = V2 / "datasets" / "public" / "design05.jsonl"

assert "rescore" not in str(RUN_ROOT), "log-root path must never contain 'rescore'"
sys.path.insert(0, str(V2))

from inspect_ai.log import list_eval_logs, read_eval_log  # noqa: E402

SUTS = ["deepseek", "mistral", "gemini", "llama", "gpt41mini"]
EPS = [1, 2, 3]
M_FAMILY = 30                       # RULING 1a, FROZEN -- unchanged by this script
ALPHA = 0.05                        # RULING 1e
THRESH = ALPHA / M_FAMILY
C5_FLOOR = 20                       # C5's own n>=20 reportability floor


def _norm_ppf(p):
    """Acklam's inverse normal CDF approximation (no scipy in this venv). VERBATIM copy."""
    a = [-3.969683028665376e+01, 2.209460984245205e+02, -2.759285104469687e+02,
         1.383577518672690e+02, -3.066479806614716e+01, 2.506628277459239e+00]
    b = [-5.447609879822406e+01, 1.615858368580409e+02, -1.556989798598866e+02,
         6.680131188771972e+01, -1.328068155288572e+01]
    c = [-7.784894002430293e-03, -3.223964580411365e-01, -2.400758277161838e+00,
         -2.549732539343734e+00, 4.374664141464968e+00, 2.938163982698783e+00]
    d = [7.784695709041462e-03, 3.224671290700398e-01, 2.445134137142996e+00,
         3.754408661907416e+00]
    pl, ph = 0.02425, 1 - 0.02425
    if p < pl:
        q = math.sqrt(-2 * math.log(p))
        return (((((c[0]*q+c[1])*q+c[2])*q+c[3])*q+c[4])*q+c[5]) / ((((d[0]*q+d[1])*q+d[2])*q+d[3])*q+1)
    if p > ph:
        q = math.sqrt(-2 * math.log(1 - p))
        return -(((((c[0]*q+c[1])*q+c[2])*q+c[3])*q+c[4])*q+c[5]) / ((((d[0]*q+d[1])*q+d[2])*q+d[3])*q+1)
    q = p - 0.5
    r = q * q
    return (((((a[0]*r+a[1])*r+a[2])*r+a[3])*r+a[4])*r+a[5])*q / (((((b[0]*r+b[1])*r+b[2])*r+b[3])*r+b[4])*r+1)


Z = _norm_ppf(1 - THRESH / 2)


# ---------------------------------------------------------------------------
# 1. Stratum lookup: bank JSONL (source A) -- built independently of the eval logs
# ---------------------------------------------------------------------------
bank_stratum = {}          # item_id -> stratum (bank source)
bank_exemplar = {}         # item_id -> is_exemplar (bank source)
for line in BANK_JSONL.read_text().splitlines():
    if not line.strip():
        continue
    row = json.loads(line)
    meta = row.get("metadata", {})
    iid = meta.get("item_id")
    bank_stratum[iid] = meta.get("stratum")
    bank_exemplar[iid] = bool(meta.get("is_exemplar"))

STRATUM_A_ITEMS = sorted(i for i, s in bank_stratum.items() if s == "a" and not bank_exemplar[i])
STRATUM_C_ITEMS = sorted(i for i, s in bank_stratum.items() if s == "c" and not bank_exemplar[i])
assert len(STRATUM_A_ITEMS) == 19, f"expected 19 stratum-a non-exemplar items, got {len(STRATUM_A_ITEMS)}"
assert len(STRATUM_C_ITEMS) == 9, f"expected 9 stratum-c non-exemplar items, got {len(STRATUM_C_ITEMS)}"


# ---------------------------------------------------------------------------
# 2. Walk the eval logs ONCE. Collect per-item CSR (all epochs) plus the
#    eval-log's own stratum metadata, so we can cross-check source A vs source B.
# ---------------------------------------------------------------------------
# vals[(sut, item_id)] -> [csr per epoch]   (non-exemplar only, all strata -- PANEL 0 input)
vals = defaultdict(list)
# admins[(sut, item_id)] -> count of scored (non-NaN) administrations, i.e. item x epoch hits
admins = defaultdict(int)
eval_stratum = {}          # item_id -> stratum as seen in .eval sample metadata (source B)
eval_stratum_mismatches = []  # (item_id, eval_value, bank_value) if they ever disagree

for ep in EPS:
    for sut in SUTS:
        d = RUN_ROOT / f"ep{ep}" / sut
        if not d.exists():
            continue
        for li in list_eval_logs(str(d)):
            log = read_eval_log(li.name)
            if "design05" not in log.eval.task:
                continue
            for s in (log.samples or []):
                meta = s.metadata or {}
                item_id = meta.get("item_id") or s.id
                eval_strat = meta.get("stratum")
                if item_id in eval_stratum and eval_stratum[item_id] != eval_strat:
                    eval_stratum_mismatches.append((item_id, eval_stratum[item_id], eval_strat))
                eval_stratum[item_id] = eval_strat

                if meta.get("is_exemplar"):
                    continue
                sc = (s.scores or {})
                score = next(iter(sc.values()), None) if sc else None
                if score is None:
                    continue
                v = score.value
                csr = v.get("constraint_satisfaction_rate") if isinstance(v, dict) else None
                if isinstance(csr, (int, float)) and not (isinstance(csr, float) and math.isnan(csr)):
                    vals[(sut, item_id)].append(float(csr))
                    admins[(sut, item_id)] += 1

# cross-check source A (bank) vs source B (eval metadata) for every item seen in the logs
source_agreement_mismatches = []
for item_id, eval_strat in eval_stratum.items():
    bank_strat = bank_stratum.get(item_id)
    if bank_strat is not None and eval_strat is not None and bank_strat != eval_strat:
        source_agreement_mismatches.append((item_id, bank_strat, eval_strat))


def average_per_sut(item_filter=None):
    """Return {sut: [mean-csr-per-item]} honoring item_filter(item_id) -> bool."""
    out = defaultdict(list)
    for (sut, item_id), vs in vals.items():
        if item_filter is not None and not item_filter(item_id):
            continue
        if vs:
            out[sut].append(statistics.mean(vs))
    return out


def print_stats_and_contrasts(per_sut, out=sys.stdout):
    """VERBATIM machinery from c1_design05_contrasts.py, parameterized on per_sut."""
    print(f"{'SUT':12} {'items':>7} {'CSR mean':>10} {'sd':>9} {'95%/m CI':>26}", file=out)
    stats = {}
    for sut in SUTS:
        xs = per_sut.get(sut, [])
        if not xs:
            continue
        n = len(xs)
        m = statistics.mean(xs)
        sd = statistics.stdev(xs) if n > 1 else 0.0
        se = sd / math.sqrt(n) if n else float("nan")
        stats[sut] = (m, sd, se, n)
        print(f"{sut:12} {n:7} {m:10.4f} {sd:9.4f}   [{m-Z*se:7.4f}, {m+Z*se:7.4f}]", file=out)

    print(file=out)
    print(f"{'contrast':26} {'diff':>9} {'Bonferroni-widened CI':>26}  verdict", file=out)
    print("-" * 96, file=out)
    survivors = []
    for i, a in enumerate(SUTS):
        for b in SUTS[i+1:]:
            if a not in stats or b not in stats:
                continue
            ma, sda, sea, na = stats[a]
            mb, sdb, seb, nb = stats[b]
            diff = ma - mb
            se = math.sqrt(sea**2 + seb**2)
            lo, hi = diff - Z*se, diff + Z*se
            excludes0 = (lo > 0) or (hi < 0)
            verdict = "excludes zero" if excludes0 else "crosses zero"
            if excludes0:
                survivors.append((a, b, diff, lo, hi))
            print(f"{a+' - '+b:26} {diff:9.4f}   [{lo:8.4f}, {hi:8.4f}]  {verdict}", file=out)

    print(file=out)
    print(f"Contrasts whose Bonferroni-widened interval excludes zero: {len(survivors)} of 10", file=out)
    for a, b, diff, lo, hi in survivors:
        direction = "higher" if diff > 0 else "lower"
        print(f"  {a} {direction} than {b}: delta={diff:+.4f} [{lo:+.4f}, {hi:+.4f}]", file=out)
    return stats, survivors


print(CANARY)
print("=" * 96)
print("  T0-10: DIAGNOSTIC RECOMPUTE -- NOT A WALKWORTHY HEADLINE")
print("  Stratum-aware recompute of the design-05 C1 contrasts (constraint_satisfaction_rate)")
print("=" * 96)
print(f"  family m = {M_FAMILY} (FROZEN by RULING 1a) | alpha = {ALPHA} (RULING 1e)")
print(f"  per-contrast threshold = {THRESH:.6f} | two-sided z = {Z:.4f}")
print()

# ---------------------------------------------------------------------------
# PANEL 0 -- G0 gate: reproduce the original (all-strata) computation unchanged
# ---------------------------------------------------------------------------
print("#" * 96)
print("# PANEL 0 (G0 GATE) -- DIAGNOSTIC RECOMPUTE -- NOT A WALKWORTHY HEADLINE")
print("# All-strata computation, exemplars dropped. Must reproduce the published numbers")
print("# from logs/fullbank-3ep-20260724/c1_design05_contrasts.py EXACTLY.")
print("#" * 96)
per_sut_all = average_per_sut(item_filter=None)
stats_p0, survivors_p0 = print_stats_and_contrasts(per_sut_all)
print()

# --- G0 proof: run the untouched original script as a subprocess and diff ---
print("-" * 96)
print("G0 PROOF: diffing this panel's numeric lines against a live run of the untouched original")
print(f"  original script: {ORIG_SCRIPT}")
orig_proc = subprocess.run(
    [sys.executable, str(ORIG_SCRIPT)],
    cwd=str(RUN_ROOT), capture_output=True, text=True,
)
if orig_proc.returncode != 0:
    print(f"  ORIGINAL SCRIPT FAILED (exit {orig_proc.returncode}) -- G0 GATE: FAIL")
    print(orig_proc.stderr)
    sys.exit(1)

orig_lines = orig_proc.stdout.splitlines()
# The only lines that are expected to differ between the two runs are the
# title/banner lines above the SUT table and the "READING RULES" epilogue below
# the headline count, which this script has reworded/relabeled/omitted for the
# panel structure above. The SUT table through the headline count line -- the
# actual numbers -- must be byte-identical.
orig_numeric_start = next(i for i, l in enumerate(orig_lines) if l.startswith("SUT"))

# capture our own PANEL 0 numeric block the same way, by re-rendering it to a
# string buffer (identical function call, so it is guaranteed to match what
# was already printed above modulo the surrounding banner)
import io  # noqa: E402
buf = io.StringIO()
print_stats_and_contrasts(per_sut_all, out=buf)
our_numeric = buf.getvalue().splitlines()
# our_numeric starts with the SUT header line directly (no banner inside the buffer)
assert our_numeric[0].startswith("SUT")

# slice the original's numeric block to the SAME LENGTH as ours, so the compare
# is scoped to the shared substantive lines and does not spuriously fail on the
# original's own trailing "READING RULES" epilogue (which this script's panel
# structure intentionally does not re-print per-panel).
orig_numeric = orig_lines[orig_numeric_start:orig_numeric_start + len(our_numeric)]

diff = list(difflib.unified_diff(orig_numeric, our_numeric, lineterm="",
                                  fromfile="original(c1_design05_contrasts.py)",
                                  tofile="panel0(this script)"))
if diff:
    print("  G0 GATE: FAIL -- numeric lines differ, see diff below:")
    for l in diff:
        print("   ", l)
    print()
    print("ABORTING -- PANEL A / PANEL C5 NOT COMPUTED (G0 gate is mandatory).")
    sys.exit(1)
else:
    print(f"  G0 GATE: PASS -- {len(orig_numeric)} numeric lines identical, "
          f"headline '{len(survivors_p0)} of 10' matches original's published '0 of 10'.")
print()

# ---------------------------------------------------------------------------
# Stratum-source note
# ---------------------------------------------------------------------------
print("#" * 96)
print("# STRATUM-SOURCE NOTE -- DIAGNOSTIC RECOMPUTE -- NOT A WALKWORTHY HEADLINE")
print("#" * 96)
print(f"  Source A (bank):      {BANK_JSONL.relative_to(V2)} -- metadata.stratum per row (32 rows)")
print(f"  Source B (eval logs): sample.metadata['stratum'] carried on every .eval sample")
print(f"  Source used for PANEL A / PANEL C5 below: BANK (source A) -- read once, independent")
print(f"  of eval-log traversal, so it cannot inherit a scoring-pipeline bug.")
print(f"  Distinct item_ids observed carrying a stratum value in the eval logs: {len(eval_stratum)}")
print(f"  Within-source repeat-observation mismatches (same item_id, different stratum value")
print(f"  across epochs/SUTs within the eval logs themselves): {len(eval_stratum_mismatches)}")
for m in eval_stratum_mismatches:
    print(f"    MISMATCH within eval logs: {m}")
print(f"  Cross-source mismatches (bank stratum != eval-log stratum) for the {len(eval_stratum)}")
print(f"  items seen in both: {len(source_agreement_mismatches)}")
for m in source_agreement_mismatches:
    print(f"    MISMATCH bank-vs-eval: item={m[0]} bank={m[1]} eval={m[2]}")
if not eval_stratum_mismatches and not source_agreement_mismatches:
    print("  RESULT: bank and eval-log stratum values AGREE on every item observed. No mismatches.")
print()

# ---------------------------------------------------------------------------
# PANEL A -- stratum-a only, non-exemplar, same machinery
# ---------------------------------------------------------------------------
print("#" * 96)
print("# PANEL A -- DIAGNOSTIC RECOMPUTE -- NOT A WALKWORTHY HEADLINE")
print("# Stratum-(a) non-exemplar cells ONLY, per C1's literal pre-registered scope.")
print("#" * 96)
print(f"  bank stratum-a non-exemplar item universe: n={len(STRATUM_A_ITEMS)}")
print(f"  {STRATUM_A_ITEMS}")
print()

per_sut_a = average_per_sut(item_filter=lambda iid: bank_stratum.get(iid) == "a" and not bank_exemplar.get(iid))
print(f"{'SUT':12} {'stratum-a items scored':>24}")
missing_by_sut = {}
for sut in SUTS:
    present_items = sorted({iid for (s2, iid) in vals if s2 == sut and bank_stratum.get(iid) == "a"
                             and not bank_exemplar.get(iid)})
    missing = sorted(set(STRATUM_A_ITEMS) - set(present_items))
    missing_by_sut[sut] = missing
    n = len(per_sut_a.get(sut, []))
    print(f"{sut:12} {n:24}  (bank universe n=19; missing={len(missing)})")
print()
for sut in SUTS:
    if missing_by_sut[sut]:
        print(f"  {sut}: MISSING stratum-a item_ids ({len(missing_by_sut[sut])}): {missing_by_sut[sut]}")
        for iid in missing_by_sut[sut]:
            key = (sut, iid)
            if key in admins and admins[key] == 0:
                reason = "administration(s) found but constraint_satisfaction_rate NaN/absent every epoch"
            elif key not in admins:
                reason = "no scored administration found for this (sut, item_id) in any epoch"
            else:
                reason = f"only {admins[key]} epoch(s) scored (present but partial)"
            print(f"      {iid}: {reason}")
    else:
        print(f"  {sut}: all 19 bank stratum-a items present, none missing.")
print()

stats_pa, survivors_pa = print_stats_and_contrasts(per_sut_a)
print()
print(f"PANEL A headline: contrasts whose Bonferroni-widened interval excludes zero: "
      f"{len(survivors_pa)} of 10")
print()

# ---------------------------------------------------------------------------
# PANEL C5 -- floor accounting for the stratum-a cell, BOTH ways, vs floor=20
# ---------------------------------------------------------------------------
print("#" * 96)
print("# PANEL C5 -- DIAGNOSTIC RECOMPUTE -- NOT A WALKWORTHY HEADLINE")
print("# Floor accounting for the design-05 stratum-a cell. C5's reportability floor = "
      f"{C5_FLOOR}.")
print("# No verdict is printed here -- floor adjudication is not this script's job.")
print("#" * 96)
print(f"{'SUT':12} {'(i) admins: item x epoch':>26} {'(ii) items: epoch-avg':>24} {'floor':>7}")
for sut in SUTS:
    admin_count = sum(admins.get((sut, iid), 0) for iid in STRATUM_A_ITEMS)
    item_count = len(per_sut_a.get(sut, []))
    print(f"{sut:12} {admin_count:26} {item_count:24} {C5_FLOOR:7}")
print()
print("  (i) 'admins' = count of scored (non-NaN CSR) design-05 stratum-a non-exemplar")
print("      administrations for that SUT, summed across all 3 epochs (item x epoch count,")
print("      max possible = 19 items x 3 epochs = 57).")
print("  (ii) 'items' = number of distinct stratum-a items with an epoch-averaged CSR value")
print("      for that SUT -- this is the n each PANEL A contrast above is actually computed on")
print("      (max possible = 19).")
print()
print("#" * 96)
print("# END -- DIAGNOSTIC RECOMPUTE -- NOT A WALKWORTHY HEADLINE")
print("#" * 96)
print(CANARY)
