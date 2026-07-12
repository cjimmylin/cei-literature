"""Executable pre-gate lint for the reviewed 06/09 G5 reference sets.

This is deliberately a structural/lexical linter, not a substitute judge. It implements
the machine-checkable portions of 06 CHECK 1–5 and 09 L-2…L-6, while leaving graded
quality differences to the frozen blind G5 run.
"""
from __future__ import annotations

import re
from pathlib import Path

GUILT_LEXICON = (
    "guilt", "guilty", "sin", "sinned", "sinful", "repent", "repentance",
    "shame", "shameful", "ashamed", "stain", "stained", "confess", "confession",
    "blameworthy", "culpable", "transgress", "wrongdoing on your part",
    "you have done wrong", "a wrong you committed",
)
NEGATIONS = ("not", "no", "never", "isn't", "without", "free of", "rather than", "less")
CRITERIA_06 = ("Frame", "Facts", "Principles", "Alternatives", "Resolution",
               "Remainder", "Pastoral")
CRITERIA_09 = ("Wrong-naming", "Debt/obligation accuracy", "Floor compliance",
               "Attitudinal/heart duty", "Reasoning/method quality", "Pastoral concreteness")
TRADITIONS = re.compile(
    r"(Geisler|Grudem|Rae|Frame|Powlison|New Dictionary|Meilaender|Heltzel|Blackwell|"
    r"Hauerwas|Yoder|Jones|Cambridge|NDC|Luther|Calvin|Samaritan|"
    r"ordinary/extraordinary-means)", re.I)


def _sentences(text: str) -> list:
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+", text) if s.strip()]


def _negated(sentence: str, start: int) -> bool:
    before = sentence[max(0, start - 45):start].lower()
    words = re.findall(r"[a-z']+", before)[-4:]
    window = " ".join(words)
    return any(re.search(rf"\b{re.escape(n)}\b", window) for n in NEGATIONS)


def _guilt_failures(item_id: str, label: str, body: str) -> list:
    failures = []
    sentences = _sentences(body)
    remainder_at = max(0, int(len(sentences) * 0.75))
    for i, sentence in enumerate(sentences):
        lower = sentence.lower()
        for token in GUILT_LEXICON:
            for hit in re.finditer(rf"\b{re.escape(token)}\b", lower):
                if _negated(lower, hit.start()):
                    continue
                context = lower[max(0, hit.start() - 40):hit.end() + 40]
                if re.search(r"\b(do not|don't|never)\b.{0,35}\bshame you out of\b", context):
                    continue
                immediately_before = lower[max(0, hit.start() - 28):hit.start()]
                third_person = bool(re.search(
                    r"(?:\b(?:his|her|their|gregor's|father's|mother's)\s+)$",
                    immediately_before))
                predicated = bool(re.search(
                    rf"\b(you|your|you've|you'll)\b.{{0,35}}\b{re.escape(token)}\b|"
                    rf"\b{re.escape(token)}\b.{{0,35}}\b(you|your)\b", lower))
                if not third_person and (predicated or i >= remainder_at):
                    failures.append({"design": "06", "item_id": item_id,
                                     "check": "FA-1", "label": label,
                                     "detail": f"unnegated {token!r}"})
    return failures


def lint_text(design, item_id, answers):
    failures = []
    if design == "06":
        for label, body in answers:
            if "no-dilemma" in label.lower():
                failures.extend(_guilt_failures(item_id, label, body))
    return {"failures": failures}


def _sections(text: str) -> list:
    hits = list(re.finditer(r"^### (WW-(?:06|09)-[A-Z]\d+)\b.*$", text, re.M))
    return [(m.group(1), text[m.start():(hits[i + 1].start() if i + 1 < len(hits) else len(text))])
            for i, m in enumerate(hits)]


def _clean_body(raw: str) -> str:
    lines = []
    for line in raw.splitlines():
        line = re.sub(r"^>\s?", "", line).strip()
        if line == "```":
            continue
        if line:
            lines.append(line)
    return " ".join(lines).strip()


def _answers(section: str) -> list:
    header = re.compile(r"^\*\*Reference answer\s+—\s+(.*?):\*\*\s*", re.M)
    hits = list(header.finditer(section))
    answers = []
    for i, hit in enumerate(hits):
        end = hits[i + 1].start() if i + 1 < len(hits) else len(section)
        raw = section[hit.end():end]
        raw = re.split(r"\n(?:\*\*(?:parity_check|Per-criterion|Six-category)|"
                       r"Difference confined|---\s*$)", raw, maxsplit=1, flags=re.M)[0]
        answers.append((hit.group(1).strip(), _clean_body(raw)))
    return answers


def _word_count(text: str) -> int:
    return len(text.split())


def _ratio(answers: list) -> float:
    counts = [_word_count(body) for _, body in answers]
    return round(max(counts) / min(counts), 4) if len(counts) == 2 and min(counts) else 999.0


def _table_has(section: str, criterion: str) -> bool:
    suffix = r"(?:-with-method)?" if criterion == "Resolution" else ""
    return bool(re.search(rf"^\|\s*{re.escape(criterion)}{suffix}\s*\|",
                          section, re.M | re.I))


def _lint_design06(text: str) -> dict:
    failures, ratios = [], {}
    sections = _sections(text)
    no_dilemma = {
        "WW-06-A01": ("third-way",), "WW-06-K01": ("*",),
        "WW-06-K03": ("*",), "WW-06-K04": ("*",),
        "WW-06-E01": ("invite",), "WW-06-E02": ("attitudinal",),
        "WW-06-D01": ("*",), "WW-06-L03": ("*",),
        "WW-06-F03": ("*",), "WW-06-N01": ("*",),
    }
    for item_id, section in sections:
        answers = _answers(section)
        if len(answers) != 2:
            failures.append({"design": "06", "item_id": item_id, "check": "PAIR",
                             "detail": f"expected 2 answers, found {len(answers)}"})
            continue
        ratio = _ratio(answers)
        ratios[item_id] = ratio
        if ratio > 1.20:
            failures.append({"design": "06", "item_id": item_id, "check": "CHECK-2",
                             "detail": f"word ratio {ratio} > 1.20"})
        if item_id in ("WW-06-D01", "WW-06-L03") and ratio > 1.10:
            failures.append({"design": "06", "item_id": item_id,
                             "check": "DIRECTED-TRIM",
                             "detail": f"word ratio {ratio} > directed 1.10"})
        roles = no_dilemma.get(item_id, ())
        for label, body in answers:
            if "*" in roles or any(role.lower() in label.lower() for role in roles):
                failures.extend(_guilt_failures(item_id, label, body))
            if not TRADITIONS.search(label):
                failures.append({"design": "06", "item_id": item_id,
                                 "check": "CHECK-4", "detail": "tradition absent from label"})
        for criterion in CRITERIA_06:
            if not _table_has(section, criterion):
                failures.append({"design": "06", "item_id": item_id,
                                 "check": "CHECK-3", "detail": f"missing {criterion} row"})
    return {"pair_count": len(sections), "ratios": ratios, "failures": failures,
            "k03_split_kind": "verdict"}


def _d01_fact_check(section: str) -> bool:
    answers = _answers(section)
    if len(answers) != 2:
        return False
    required = ("olivia", "jamal", "60-day", "5,800", "job", "concert")
    return all(all(token in body.lower() for token in required) for _, body in answers)


def _lint_design09(text: str) -> dict:
    failures, ratios = [], {}
    sections = _sections(text)
    d01_ok = False
    for item_id, section in sections:
        answers = _answers(section)
        if len(answers) != 2:
            failures.append({"design": "09", "item_id": item_id, "check": "PAIR",
                             "detail": f"expected 2 answers, found {len(answers)}"})
            continue
        ratio = _ratio(answers)
        ratios[item_id] = ratio
        if ratio > 1.15:
            failures.append({"design": "09", "item_id": item_id, "check": "L-5",
                             "detail": f"word ratio {ratio} > 1.15"})
        for criterion in CRITERIA_09:
            if not _table_has(section, criterion):
                failures.append({"design": "09", "item_id": item_id,
                                 "check": "L-2/L-3", "detail": f"missing {criterion} row"})
        if not re.search(r"Difference (?:is )?confined.*reported", section, re.I | re.S):
            failures.append({"design": "09", "item_id": item_id, "check": "L-4",
                             "detail": "reported-pole confinement assertion absent"})
        if item_id == "WW-09-D01":
            d01_ok = _d01_fact_check(section)
            if not d01_ok:
                failures.append({"design": "09", "item_id": item_id, "check": "L-6",
                                 "detail": "rendered D01 specifics absent from both poles"})
    return {"pair_count": len(sections), "ratios": ratios, "failures": failures,
            "d01_rendered_facts": d01_ok}


def lint_reference_files(design06_path, design09_path, design09_seed_path):
    # Reading the public seed file is an explicit L-6 provenance guard. HOLDOUT is never touched.
    seed_text = Path(design09_seed_path).read_text(encoding="utf-8")
    if "### WW-09-D01" not in seed_text:
        raise ValueError("public 09 seed file does not contain WW-09-D01")
    d06 = _lint_design06(Path(design06_path).read_text(encoding="utf-8"))
    d09 = _lint_design09(Path(design09_path).read_text(encoding="utf-8"))
    failures = d06["failures"] + d09["failures"]
    return {
        "designs": {"06": d06, "09": d09},
        "failures": failures,
        "directed": {
            "09-D01-rendered-facts": "PASS" if d09["d01_rendered_facts"] else "FAIL",
            "06-K03-split-kind": d06["k03_split_kind"],
            "06-D01-max-ratio": d06["ratios"].get("WW-06-D01", 999.0),
            "06-L03-max-ratio": d06["ratios"].get("WW-06-L03", 999.0),
        },
    }
