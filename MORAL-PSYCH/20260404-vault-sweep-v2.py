"""Vault sweep v2: scan all vault papers for 11 moral-psych theory keyword patterns.
Focuses on 3 non-Western theories (Islamic maqasid, Confucian role ethics, Ubuntu)
plus underrepresented Western theories (Dual Process, Social Intuitionism, Dyadic Morality)
and secondary non-Western (Buddhist, Indigenous).

READ-ONLY — does not modify any paper files.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

# ── paths ──────────────────────────────────────────────────────────────
PAPERS_DIR = Path("/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/papers")
EXTRACTS_DIR = Path("/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/PDF Extracts")
CANDIDATES_JSON = Path("/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/MORAL-PSYCH/20260403-moral-psych-benchmark-candidates.json")
OUTPUT_JSON = Path("/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/MORAL-PSYCH/20260404-vault-sweep-v2-report.json")

# ── keyword patterns (case-insensitive) ──────────────────────────────
# Each theory maps to a single compiled regex with alternations
THEORY_PATTERNS: dict[str, re.Pattern] = {
    "islamic": re.compile(
        r"maqasid|shariah|maslaha|islamic.ethics|fiqh|halal|haram|fatwa|ijtihad|islamic.jurisprudence",
        re.IGNORECASE,
    ),
    "confucian": re.compile(
        r"confucian|filial.piety|xiao|junzi|confucius|mencius|role.ethics|chinese.ethics|ren.{0,3}benevolence",
        re.IGNORECASE,
    ),
    "ubuntu": re.compile(
        r"ubuntu|communitarian.ethics|african.ethics|relational.personhood|communal.moral|restorative.justice|harambee|ujamaa",
        re.IGNORECASE,
    ),
    "buddhist": re.compile(
        r"buddhist.ethics|dharma|karma|ahimsa|eightfold.path|dependent.origination",
        re.IGNORECASE,
    ),
    "indigenous": re.compile(
        r"indigenous.ethics|kaitiakitanga|buen.vivir|indigenous.moral|decolonial.ethics|land.based.ethics",
        re.IGNORECASE,
    ),
    "dual_process": re.compile(
        r"cognitive.load.moral|system.1.{0,5}system.2|utilitarian.vs.deontological|dual.process.moral|personal.vs.impersonal.dilemma",
        re.IGNORECASE,
    ),
    "intuitionist": re.compile(
        r"moral.dumbfounding|post.hoc.rationalization|moral.intuition|automatic.moral|intuitionist.model",
        re.IGNORECASE,
    ),
    "dyadic": re.compile(
        r"harm.perception|agent.patient.moral|moral.typecasting|dyadic.template|dyadic.morality",
        re.IGNORECASE,
    ),
}


def extract_field(text: str, field: str) -> str:
    """Pull a YAML field value from frontmatter text (safe regex, handles escaped quotes)."""
    pat = re.compile(
        rf'^{re.escape(field)}:\s*"((?:[^"\\]|\\.)*)"',
        re.MULTILINE,
    )
    hit = pat.search(text)
    if hit:
        return hit.group(1)
    # unquoted value
    pat2 = re.compile(rf'^{re.escape(field)}:\s*(.+)$', re.MULTILINE)
    hit2 = pat2.search(text)
    if hit2:
        return hit2.group(1).strip().strip('"')
    return ""


def find_extract(filename: str) -> str | None:
    """Check if a PDF extract exists for the given paper filename.
    Uses iterdir() (not rglob) for bracket safety."""
    stem = Path(filename).stem
    year_match = re.match(r"(\d{4})", stem)
    if year_match:
        year = year_match.group(1)
        candidate = EXTRACTS_DIR / year / filename
        if candidate.exists():
            return f"PDF Extracts/{year}/{filename}"
    # Fallback: search all year subdirs
    for subdir in EXTRACTS_DIR.iterdir():
        if subdir.is_dir():
            candidate = subdir / filename
            if candidate.exists():
                return f"PDF Extracts/{subdir.name}/{filename}"
    return None


def load_existing_candidates() -> set[str]:
    """Load filenames from the existing candidates JSON."""
    if not CANDIDATES_JSON.exists():
        return set()
    with open(CANDIDATES_JSON, "r", encoding="utf-8") as f:
        data = json.load(f)
    return {c["file"] for c in data.get("candidates", [])}


def main() -> None:
    existing = load_existing_candidates()
    print(f"Loaded {len(existing)} existing candidates")

    # ── scan papers ──────────────────────────────────────────────────
    theory_hits: dict[str, list[dict]] = {k: [] for k in THEORY_PATTERNS}
    papers_scanned = 0
    errors = 0

    for item in sorted(PAPERS_DIR.iterdir()):
        if not item.is_file() or item.suffix != ".md":
            continue
        papers_scanned += 1

        try:
            # Read first 2000 chars for frontmatter
            with open(item, "r", encoding="utf-8") as f:
                head = f.read(2000)
        except Exception:
            errors += 1
            continue

        short_title = extract_field(head, "short_title")
        abstract = extract_field(head, "abstract")
        search_text = f"{short_title} {abstract}".lower()

        filename = item.name

        for theory, pattern in THEORY_PATTERNS.items():
            matches = pattern.findall(search_text)
            if matches:
                # Deduplicate matched keywords
                unique_kw = sorted(set(kw.lower() for kw in matches))
                extract_path = find_extract(filename)
                theory_hits[theory].append({
                    "file": filename,
                    "short_title": short_title,
                    "keywords_matched": unique_kw,
                    "has_extract": extract_path is not None,
                    "extract_path": extract_path,
                    "already_candidate": filename in existing,
                })

    # ── summary stats ────────────────────────────────────────────────
    all_hit_files: set[str] = set()
    already_candidate_files: set[str] = set()
    for theory, hits in theory_hits.items():
        for h in hits:
            all_hit_files.add(h["file"])
            if h["already_candidate"]:
                already_candidate_files.add(h["file"])

    new_files = all_hit_files - already_candidate_files
    by_theory = {k: len(v) for k, v in theory_hits.items()}

    summary = {
        "total_new_hits": len(all_hit_files),
        "already_candidates": len(already_candidate_files),
        "new_candidates": len(new_files),
        "by_theory": by_theory,
        "papers_scanned": papers_scanned,
        "errors": errors,
    }

    report = {
        "date": "2026-04-04",
        "papers_scanned": papers_scanned,
        "theory_hits": theory_hits,
        "summary": summary,
    }

    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)

    # ── console summary ──────────────────────────────────────────────
    print(f"\nScanned {papers_scanned} papers ({errors} read errors)")
    print(f"Total unique files with hits: {len(all_hit_files)}")
    print(f"  Already in candidate list:  {len(already_candidate_files)}")
    print(f"  NEW (not in candidate list): {len(new_files)}")
    print()
    print("Hits by theory:")
    for t in ["islamic", "confucian", "ubuntu", "buddhist", "indigenous",
              "dual_process", "intuitionist", "dyadic"]:
        new_count = sum(1 for h in theory_hits[t] if not h["already_candidate"])
        print(f"  {t:16s}: {by_theory[t]:3d} total ({new_count} new)")
    print(f"\nReport written to: {OUTPUT_JSON}")


if __name__ == "__main__":
    main()
