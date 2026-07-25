#!/usr/bin/env python3
"""Claims-discipline linter for the WALKWORTHY phase-6 manuscripts.

Checks every .md under the given paths against the binding rules in
RULINGS-APPLIED-20260725b.md and 06-messaging.md section 5.  Prints a report and
exits non-zero if any BLOCKER fires.

Run:  .venv/bin/python REPORTS/20260725-manuscripts/lint_claims.py REPORTS/20260725-manuscripts
"""
import re
import sys
from pathlib import Path

CANARY = "WALKWORTHY-CANARY-7f3e2026"

# (severity, label, compiled pattern, note)
RULES = [
    ("BLOCKER", "R3 significance-as-adjective",
     re.compile(r"\bsignifican(?:t|tly|ce)\b", re.I),
     "R3: use 'excludes zero' / 'crosses zero'; never significance language."),
    # A significance star is adjacent to a numeral or a p-value operator.  Markdown
    # bold/italic is the same token class, so anchoring on the neighbour is the only
    # way to tell them apart without a full markdown parse.
    ("BLOCKER", "significance stars / p-values",
     re.compile(r"\d\s*\*{1,3}(?![\w*])|\bp\s*[<>=≤≥]\s*0?\.\d+"),
     "R3: no significance stars, no p-values."),
    ("BLOCKER", "corrected 'judge dominates' framing",
     re.compile(r"judges?\s+(?:\w+\s+){0,3}dominat|dominat\w*\s+(?:\w+\s+){0,3}judge", re.I),
     "Corrected framing: models differ, judges disagree about the ORDERING."),
    ("BLOCKER", "theological-truth claim",
     re.compile(r"correctly\s+christian|theologically\s+(?:true|correct)|"
                r"fidelity\s+to\s+(?:christianity|scripture)", re.I),
     "Concordance with the named registry corpus only."),
    ("BLOCKER", "referees-prove-truth claim",
     re.compile(r"referees?\s+(?:\w+\s+){0,3}(?:prove|proves|proved|confirm\w*\s+that\s+judge|"
                r"establish\w*\s+that\s+judge)|ground[- ]truth\s+(?:from|by)\s+the\s+referees?", re.I),
     "Referees establish reference-model concordance, not ground truth."),
    ("BLOCKER", "security-hook forbidden token",
     re.compile(r"(?:eval|exec)\("),
     "The write hook blocks these byte sequences even inside prose."),
    ("WARN", "possible leaderboard / ranking language",
     re.compile(r"\bleaderboard\b|\b(?:out|under)performs?\b|\bbest[- ]performing\b|"
                r"\branked?\s+(?:first|second|third|highest|lowest|top)\b|\bwinner\b", re.I),
     "No SUT rankings. Check each hit reads as a non-claim or a description of what is NOT done."),
    ("WARN", "venue / author leakage",
     re.compile(r"\b(?:NeurIPS|ICLR|ICML|ACL|EMNLP|AAAI|arXiv|OSF|preprint)\b|"
                r"\backnowledg(?:e?ments?)\b|\bfunding\b|\bcorresponding author\b", re.I),
     "Manuscript stays venue-generic and author-generic."),
    ("WARN", "pushback_rate promoted",
     re.compile(r"pushback[_ ]rate[^.\n]{0,60}\bheadline\b", re.I),
     "break_turn is the sole design-02 headline; pushback_rate is SECONDARY."),
    # Only the REFEREE sample is un-poolable: it is disagreement-enriched by
    # construction, so an overall figure is meaningless.  Pooled item-rater
    # reliability (the IVR-1.1 double-rating) is an ordinary, legitimate statistic —
    # requiring 'referee' nearby keeps the rule from firing on it.
    ("WARN", "possible pooled referee agreement",
     re.compile(r"(?:overall|pooled)\s+(?:\w+\s+){0,2}agreement(?=(?:.|\n){0,200}?referee)"
                r"|referee(?:.|\n){0,200}?(?:overall|pooled)\s+(?:\w+\s+){0,2}agreement", re.I),
     "Referee sample is disagreement-enriched; strata are never pooled."),
]

# Negation / disclaimer cues.  A flagged phrase inside a sentence that STATES the
# non-claim ("never as correctly Christian", "no significance language is used") is
# exactly the prose the rules require, not a violation.
#
# This is matched against a CHARACTER WINDOW around the hit, not the hit's own line:
# manuscript prose hard-wraps at ~90 chars, so the negation cue routinely lands on a
# different line than the word it negates.
ALLOW = re.compile(
    r"\bno\b|\bnot\b|\bnever\b|\bwithout\b|\bavoid\w*\b|\bforbid\w*\b|\brefrain\b|"
    r"\bdisallow\w*\b|\brather\s+than\b|\binstead\s+of\b|\bwould\s+be\s+invalid\b|"
    r"\bis\s+invalid\b|\bmust\s+not\b|\bcannot\b|\bdeclines?\s+to\b|\bdeferred\b|"
    r"venue-generic|author-generic|\bdiscipline\b|\bcaveat\b|\bnon-claim\b",
    re.I)

# Allowance is SENTENCE-scoped, not window-scoped.
#
# An earlier version searched a +/-260 character window.  An adversarial review showed
# that was so permissive it suppressed nearly every hit in a manuscript -- prose of
# this kind contains "no", "not" or "never" within 260 characters almost everywhere,
# so the linter reported clean while real defects stood.  Scoping to the sentence
# containing the hit keeps the hard-wrap fix (sentences span line breaks) without
# swallowing the whole page.
SENT_END = re.compile(r"(?<=[.!?])\s+(?=[A-Z(\"'*|])|\n\s*\n|\n(?=[|#-])")


def sentence_around(text, start, end):
    """The sentence containing a match, so a negation three sentences away can't excuse it."""
    left = 0
    for m in SENT_END.finditer(text, 0, start):
        left = m.end()
    nxt = SENT_END.search(text, end)
    return text[left:nxt.start() if nxt else min(len(text), end + 400)]

# Rules that must run against emphasis-blanked text rather than the raw source.
STAR_RULE = "significance stars / p-values"

_EMPHASIS = re.compile(r"(?<!\*)(\*{1,3})(?!\s)(.+?)(?<!\s)\1(?!\*)", re.S)


def blank_emphasis(text):
    """Replace balanced markdown emphasis markers with spaces, preserving offsets.

    A closing ``**`` after a numeral ("**8 of 8**") is byte-identical to a
    significance star ("0.42**").  Blanking balanced pairs first — without changing
    string length, so line numbers stay exact — leaves only unbalanced stars, which
    is what a significance marker actually is.
    """
    out = list(text)
    for m in _EMPHASIS.finditer(text):
        for i in list(range(m.start(1), m.end(1))) + list(range(m.end(2), m.end(0))):
            out[i] = " "
    return "".join(out)


def lint(paths):
    files = []
    for p in paths:
        p = Path(p)
        files.extend(sorted(p.rglob("*.md")) if p.is_dir() else [p])

    blockers = warns = 0
    for f in files:
        text = f.read_text(encoding="utf-8")
        lines = text.splitlines()
        hits = []

        if text.count(CANARY) < 2:
            hits.append(("BLOCKER", "canary", 0,
                         f"canary appears {text.count(CANARY)}x, need >= 2 (top and bottom)"))

        deemphasised = blank_emphasis(text)

        for sev, label, pat, note in RULES:
            scan = deemphasised if label == STAR_RULE else text
            for m in pat.finditer(scan):
                ln = text[:m.start()].count("\n")
                ln0 = scan[:m.start()].count("\n")
                line = lines[ln0] if ln0 < len(lines) else ""
                # The venue/author rule guards THIS manuscript's front matter.  A
                # reference-list row or a vault path legitimately names other people's
                # venues and authors, so those lines are out of its scope.
                if label == "venue / author leakage" and (
                        line.lstrip().startswith("|") or "CEI-Lit-WS/" in line
                        or "arxiv.org" in line.lower()):
                    continue
                scope = sentence_around(scan, m.start(), m.end())
                # The forbidden-token rule is byte-level: no prose can excuse it.
                if label != "security-hook forbidden token" and ALLOW.search(scope):
                    continue
                ctx = lines[ln] if ln < len(lines) else ""
                hits.append((sev, label, ln + 1, ctx.strip()[:150]))

        for m in re.finditer(r"\[NUMBER NOT IN SOURCE\]|NEEDS-[A-Z]+", text):
            ln = text[:m.start()].count("\n")
            hits.append(("BLOCKER", "unresolved marker", ln + 1,
                         lines[ln].strip()[:150] if ln < len(lines) else ""))

        if hits:
            print(f"\n=== {f.name} ===")
            for sev, label, ln, ctx in hits:
                print(f"  [{sev}] {label}  L{ln}: {ctx}")
                if sev == "BLOCKER":
                    blockers += 1
                else:
                    warns += 1
        else:
            print(f"  OK  {f.name}")

    print(f"\n{len(files)} file(s) checked - {blockers} blocker(s), {warns} warning(s)")
    return 1 if blockers else 0


if __name__ == "__main__":
    sys.exit(lint(sys.argv[1:] or ["."]))
