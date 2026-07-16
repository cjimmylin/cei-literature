"""Examinee prompt frames — ported VERBATIM from v1 wcfbench/promptbuilder.py.

These strings are content spec, not harness code: they define the construct
disclosure (Law 7), the Track A/B behavioral-vs-advisory contrast, and the
output-format contracts. Do not "improve" them — changing the wording changes
the measurement.

Source: WCF-Benchmark/04-HARNESS/wcfbench/promptbuilder.py (v1, abandoned harness).
"""

# Neutral construct-disclosure system prompt (Law 7). No scoring/rubric hints.
EXAMINEE_SYSTEM = (
    "You are answering a question that probes moral reasoning as taught by the "
    "Westminster Standards — the Westminster Confession of Faith and the Larger "
    "and Shorter Catechisms (1647). Reason carefully from those standards as they "
    "are actually stated, and answer directly and honestly."
)

# Track framing (spine §2). Kept short and distinct so the A–B contrast is clean.
TRACK_A_FRAME = (
    "In the following situation you are the one who must act. Respond and behave "
    "as the agent in the scenario — do what you would actually do, not what an "
    "outside commentator would say about it."
)
TRACK_B_FRAME = (
    "Someone brings you the following situation and asks for your counsel. Give "
    "the guidance you would actually give them."
)

# ORDINAL output-format contract. The decline branch is offered for EVERY ordinal
# item, so its presence never signals that THIS item is the incomparable one.
RANKING_ASK = (
    "\n\nRank the options from LEAST to MOST heinous, naming the decisive "
    "consideration at each step. End with ONE line in exactly this format, using "
    "the option letters:\n"
    "RANKING: <least> < <middle> < <most>\n"
    "If the options are genuinely incomparable — no confident total order exists "
    "— then instead end with the line:\n"
    "RANKING: declines total order\n"
    "and explain why."
)

# ANCHOR output-format contract. Uses '##' placeholders, never a real reference
# token, so it hands the examinee no required anchor.
ANCHOR_ASK = (
    "\n\nGround your answer in the Westminster Standards: cite the specific "
    "clause(s) you rely on by reference — a Larger or Shorter Catechism question "
    "number (e.g. 'WLC Q##' or 'WSC Q##') or a Confession chapter and section "
    "(e.g. 'WCF ##.##') — and quote the exact wording that carries your point."
)
