# PRE-PARSER-FIX run (preserved audit artifact — superseded)

This subdir holds the FIRST live settled-core re-qualification run, made BEFORE a harness
parser fix. It is preserved (not deleted) as the evidence that motivated the fix; the
authoritative run is in the parent dir.

**What happened.** The R39(d) settled-core probe ran K=8 live for the three incumbent judges.
grok-4.20 scored 4/8 with cause `fail_format` on the AGG-C3-W302 fixture. Inspection of the
raw verdicts showed grok's grade was ALWAYS substantively `1: correct` (the reference verdict),
but grok intermittently wrapped the label in bold markdown — `**1: correct —** ...` — which the
settled-core line parser (`_CORE_LINE_RE`) did not strip. finish_reason was `stop` on every call
(no transport loss). This is the SAME class of gap R33.8/R32i already fixed for the numeric SCORE
token (`_NUM_SCORE_RE` tolerates `[*_]*SCORE`), but the settled-core label line was never
hardened for markdown emphasis.

Because that spurious `fail_format` dropped grok below 5/8, only gemini passed the probe (1/3),
which correctly tripped the honest-outcome STOP (< 2 families → do not improvise, report loudly).
The STOP report in this subdir is therefore an artifact of the parser gap, NOT a real judge
failure.

**Fix.** `_CORE_LINE_RE` now tolerates leading/surrounding markdown emphasis (`[*_]*` before the
number and around the verdict word), mirroring the R33.8 tolerance. A live 4/4 grok re-check
confirmed recovery. The authoritative re-run in the parent dir was made under the fixed parser.

Files: `raw_verdicts.jsonl` (the run payload with grok's bold-markdown texts), the STOP manifest,
and the STOP report. All frozen here for provenance.
