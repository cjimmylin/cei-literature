#!/usr/bin/env python3
"""Assemble the WALKWORTHY phase-6 manuscripts from their part files.

Per RULINGS-APPLIED-20260725b.md: paper (a) and paper (b) are both live targets.
Paper (a) transplants its already-drafted, adversarially-reviewed sections 3, 4 and 8
from existing report files rather than redrafting them.

Two structural wrinkles this handles:

1. Two part files hold NON-ADJACENT sections.  ``pa-01`` carries 1 and 5; ``pb-01``
   carries 1, 6 and 7.  Sections are therefore extracted individually by heading and
   re-emitted in manuscript order, not concatenated file-by-file.

2. The transplants need surgery.  The validity draft numbers its sections ``X.1``..
   ``X.8`` as a placeholder, so X becomes 8; its X.8 limitations were already merged
   into section 9 and must not be transplanted twice.  Both drafts carry inline
   ``<!-- src: ... -->`` provenance comments that the owner ruled are stripped at
   final transplant.

Run from the project root:
    ./.venv/bin/python REPORTS/20260725-manuscripts/assemble.py
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PARTS = Path(__file__).resolve().parent / "parts"
OUT = Path(__file__).resolve().parent

CANARY = "**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content"

# Section headings we never carry into a manuscript.  Provenance blocks from the
# feeder reports are working records, not manuscript content.
DROP_HEADINGS = re.compile(r"^\s*(?:source map|sources|part file|assembly note)\b", re.I)

# The related-work parts end with a citation ledger mapping every cited work to the
# vault file it was verified against.  That is not dropped — without it the inline
# citations resolve to nothing — but it is re-titled and moved to the end as a
# provisional reference list.
LEDGER_HEADING = re.compile(r"^\s*citation ledger\b", re.I)

# ---------------------------------------------------------------------------
# Post-transplant patches (paper (a) sections 3, 4 and 8).
#
# The two feeder drafts are DATED REPORTS and therefore immutable — they are not
# edited.  These patches are applied to the transplanted copy at assembly time, so
# the divergence from source is explicit, reviewable and reproducible rather than a
# silent hand-edit of a generated file.
#
# Each entry: (source file key, reason, exact old text, new text).  Every patch
# asserts a single match, so prose drift in a source fails the build loudly.
# ---------------------------------------------------------------------------
TRANSPLANT_PATCHES = {
    "design": [
        # RULING 2 moved the pilot to a development-history subsection (5.7); the
        # draft predates that ruling and still routes the reader to section 7,
        # which is now the full-bank run.
        ("stale pilot cross-reference (RULING 2)",
         "is reported separately as instrument readings (see §7); no pilot number "
         "appears in this section.",
         "is reported as development history in §5.7; no pilot number appears in "
         "this section."),
        # The stratum-a discipline is not pilot-only; section 6.3 states it runs at
        # full bank, so the pilot attribution now reads as a narrower scope than
        # the instrument actually has.
        ("stratum scope no longer pilot-specific",
         "the pilot's headline scope is stratum-`a` only",
         "the headline scope is stratum-`a` only"),
    ],
    "validity": [
        # RULINGS-APPLIED-20260725 requires every pushback_rate cell to name its
        # judge.  The smoke figures are judge-A inline.
        ("pushback_rate cell must name its judge (A-prime ruling)",
         "sub-metric (PE-18) was nonzero and SUT-differentiated (means 0.04–0.29)",
         "sub-metric (PE-18) was nonzero and varied across systems under judge-A "
         "(means 0.04–0.29)"),
        # RULING 2: pilot-era per-system spreads are not reproduced.  The pooled
        # 32.7% is a property of the old metric, not a system reading, so it stays.
        ("pilot-era per-system spread removed (RULING 2)",
         "**32.7% of the turns the old metric had pooled into undifferentiated hold-mass —\n"
         "between 21.8% and 45.8% across the five pilot SUTs — were in fact",
         "**32.7% of the turns the old metric had pooled into undifferentiated hold-mass\n"
         "were in fact"),
    ],
}


def patch(text, key):
    """Apply the documented post-transplant patches for one feeder draft."""
    for reason, old, new in TRANSPLANT_PATCHES.get(key, []):
        if text.count(old) != 1:
            raise SystemExit(
                f"ASSEMBLY ERROR: transplant patch [{key}: {reason}] matched "
                f"{text.count(old)}x, expected 1. The source draft has changed; "
                f"re-verify the patch before rebuilding.")
        text = text.replace(old, new)
    return text


def sections(path, strip_comments=False, renumber=None, patch_key=None):
    """Return {heading_text: full_section_markdown} for every '## ' section."""
    text = Path(path).read_text(encoding="utf-8")
    if patch_key:
        text = patch(text, patch_key)
    if strip_comments:
        text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
        text = re.sub(r"[ \t]+\n", "\n", text)
    if renumber:
        old, new = renumber
        text = re.sub(rf"^(#+\s*){re.escape(old)}\.", rf"\g<1>{new}.", text, flags=re.M)
        # No \b before the section sign: '§' is not a word character, so \b would
        # only match after a letter or digit, which is never how a cross-reference
        # is written.  Catch both '§X.4' and a bare 'X.4'.
        text = re.sub(rf"§\s*{re.escape(old)}\.(\d)", rf"§{new}.\1", text)
        text = re.sub(rf"(?<![\w.]){re.escape(old)}\.(\d)", rf"{new}.\1", text)

    out, chunks = {}, re.split(r"^(?=## )", text, flags=re.M)
    for chunk in chunks:
        m = re.match(r"## +(.+)", chunk)
        if not m:
            continue
        head = m.group(1).strip()
        if DROP_HEADINGS.match(head):
            continue
        out[head] = chunk.rstrip() + "\n"
    return out


def pick(secs, prefix):
    """Grab the one section whose heading starts with `prefix` (e.g. '3 ' or '8.')."""
    hits = [h for h in secs if h.startswith(prefix)]
    if not hits:
        raise SystemExit(f"ASSEMBLY ERROR: no section starting {prefix!r}. "
                         f"Available: {sorted(secs)[:12]}")
    return "\n".join(secs[h] for h in hits)


def frontmatter(path):
    """Title + abstract + keywords, minus the part-file banner and canary lines."""
    text = Path(path).read_text(encoding="utf-8")
    text = text[text.index("\n# "):] if "\n# " in text else text
    return re.sub(re.escape(CANARY), "", text).strip() + "\n"


def split_related(path):
    """Return (section-2 markdown, reference-list markdown) for a related-work part.

    The two related-work drafters emitted their ledgers at different heading levels
    (## vs ###), so this matches any level rather than relying on the section split.
    Without this the ledger stays buried inside section 2 in one paper and moves to
    the end matter in the other — same content, inconsistent placement.
    """
    path = Path(path)
    if not path.exists():
        return "", ""
    text = path.read_text(encoding="utf-8")
    m = re.search(r"^(#{2,4})\s*citation ledger\b.*$", text, re.I | re.M)
    if not m:
        secs = sections(path)
        return (pick(secs, "2 ") if any(h.startswith("2 ") for h in secs) else ""), ""

    level = len(m.group(1))
    rest = text[m.end():]
    nxt = re.search(rf"^#{{1,{level}}}\s", rest, re.M)
    table = (rest[:nxt.start()] if nxt else rest).strip()

    body = text[:m.start()] + (rest[nxt.start():] if nxt else "")
    secs = {}
    for chunk in re.split(r"^(?=## )", body, flags=re.M):
        hm = re.match(r"## +(.+)", chunk)
        if hm and not DROP_HEADINGS.match(hm.group(1).strip()):
            secs[hm.group(1).strip()] = chunk.rstrip() + "\n"
    sec2 = pick(secs, "2 ") if any(h.startswith("2 ") for h in secs) else ""
    return sec2, table


def format_refs(table):
    """Re-title a citation ledger as the manuscript's provisional reference list."""
    if not table.strip():
        return ""
    # Absolute paths are a drafting artefact; the vault-relative form is portable.
    table = table.replace("/Users/jimmy.lin/Documents/CEI-Literature-Vault/", "")
    return (
        "## Provisional reference list\n\n"
        "*v0.1. Every entry below was verified against one of two channels: a file in the "
        "project literature vault, or — for the works added by the 2026-07-29 citation "
        "sweep — an external record retrieved and inspected directly. Both channels are "
        "itemised in the citation ledger of the relevant §2 part file, and vault paths are "
        "retained so each citation can be re-checked. Bibliographic details are to be "
        "reconciled against the canonical records before submission: several vault "
        "filenames carry an author token that disagrees with the work's printed byline, so "
        "a bibliography build must resolve against the documents themselves rather than "
        "against filenames. The `[CITATION NEEDED]` gap markers carried in §2 at assembly "
        "are now closed; one candidate source was inspected and rejected as unverifiable, "
        "and is recorded as rejected in the paper (b) ledger so it is not silently "
        "rediscovered.*\n\n"
        + table.rstrip() + "\n")


def build(name, title_part, blocks, outfile, refs=""):
    body = [frontmatter(PARTS / title_part), "\n---\n"]
    for label, chunk in blocks:
        if not chunk.strip():
            raise SystemExit(f"ASSEMBLY ERROR: {name} section {label} came back empty")
        body.append(chunk.rstrip() + "\n\n---\n")
    if refs:
        body.append(refs.rstrip() + "\n\n---\n")
    body.append(f"\n{CANARY}\n")
    doc = "\n".join(body)
    doc = re.sub(r"\n{4,}", "\n\n\n", doc)
    Path(outfile).write_text(doc, encoding="utf-8")
    words = len(doc.split())
    print(f"  {Path(outfile).name}: {words:,} words, {len(blocks)} sections")
    return words


def main():
    # ---- paper (b): the judge-sensitivity methods note -----------------------
    pb1 = sections(PARTS / "pb-01-intro-limitations-future.md")
    pb2 = sections(PARTS / "pb-02-testbed-method.md")
    pb3 = sections(PARTS / "pb-03-results.md")
    pb_sec2, pb_refs = split_related(PARTS / "pb-04-related-work.md")

    print("paper (b):")
    build("paper (b)", "pb-00-frontmatter.md", [
        ("1", pick(pb1, "1 ")),
        ("2", pb_sec2 or "## 2 Related work\n\n*[SECTION PENDING]*\n"),
        ("3", pick(pb2, "3 ")),
        ("4", pick(pb2, "4 ")),
        ("5", pick(pb3, "5 ")),
        ("6", pick(pb1, "6 ")),
        ("7", pick(pb1, "7 ")),
    ], OUT / "20260725-paper-b-judging-the-judges-v0.1.md", refs=format_refs(pb_refs))

    # ---- paper (a): the benchmark / instrument paper -------------------------
    pa1 = sections(PARTS / "pa-01-intro-itemdev.md")
    pa2 = sections(PARTS / "pa-02-methods-fullbank.md")
    pa3 = sections(PARTS / "pa-03-limitations-future.md")
    pa_sec2, pa_refs = split_related(PARTS / "pa-04-related-work.md")

    # Transplants: adversarially reviewed, carried near-verbatim.
    design = sections(ROOT / "REPORTS/20260724c-paper-design-section-draft.md",
                      strip_comments=True, patch_key="design")
    validity = sections(ROOT / "REPORTS/20260724-paper-validity-section-draft.md",
                        strip_comments=True, renumber=("X", "8"), patch_key="validity")
    # X.8 limitations were merged into section 9 by the pa-03 drafter; do not repeat.
    validity = {h: v for h, v in validity.items() if not h.startswith("8.8")}
    # The feeder draft numbers its subsections at H2 because it stood alone.  Inside
    # the manuscript they are children of section 8, and sections 3-7 use H3 for
    # subsections -- demote so the heading tree is consistent throughout.
    validity = {h: re.sub(r"^## (8\.\d)", r"### \1", v, flags=re.M)
                for h, v in validity.items()}

    print("paper (a):")
    build("paper (a)", "pa-00-frontmatter.md", [
        ("1", pick(pa1, "1 ")),
        ("2", pa_sec2 or "## 2 Related work\n\n*[SECTION PENDING]*\n"),
        ("3", pick(design, "3 ")),
        ("4", pick(design, "4 ")),
        ("5", pick(pa1, "5 ")),
        ("6", pick(pa2, "6 ")),
        ("7", pick(pa2, "7 ")),
        ("8", "## 8 Item quality and validity evidence\n\n" + pick(validity, "8.")),
        ("9", pick(pa3, "9 ")),
        ("10", pick(pa3, "10 ")),
    ], OUT / "20260725-paper-a-walkworthy-benchmark-v0.1.md", refs=format_refs(pa_refs))


if __name__ == "__main__":
    main()
