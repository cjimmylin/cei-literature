#!/usr/bin/env python3
"""Build the nine pre-empirical BibleBench design reports."""

from __future__ import annotations

from functools import lru_cache, partial
from html import escape
import json
from pathlib import Path
import re
from typing import Any, Iterable

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    KeepTogether,
    PageBreak,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)
import yaml


BIBLEBENCH_ROOT = Path(__file__).resolve().parents[2]
PAPER_ROOT = BIBLEBENCH_ROOT / "BIBLEBENCH-PAPER"
REGISTRY_PATH = PAPER_ROOT / "reports" / "report-registry.yaml"
OUTPUT_ROOT = PAPER_ROOT / "output" / "design-reports"

STATUS = "PRE-EMPIRICAL DESIGN REPORT"
AUTHOR = "Jimmy Lin"
CREATOR = "BibleBench design-report builder"

NAVY = colors.HexColor("#17324D")
BLUE = colors.HexColor("#245B86")
SLATE = colors.HexColor("#465A6B")
PALE_BLUE = colors.HexColor("#EAF2F8")
PALE_GOLD = colors.HexColor("#FFF5D9")
LIGHT_RULE = colors.HexColor("#C9D4DC")
INK = colors.HexColor("#1D2832")
WHITE = colors.white


def _ascii_text(value: Any) -> str:
    text = str(value)
    replacements = {
        "\u2010": "-",
        "\u2011": "-",
        "\u2012": "-",
        "\u2013": "-",
        "\u2014": "-",
        "\u2212": "-",
        "\u2018": "'",
        "\u2019": "'",
        "\u201c": '"',
        "\u201d": '"',
        "\u2026": "...",
        "\u00a0": " ",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text


def _styles() -> dict[str, ParagraphStyle]:
    base = getSampleStyleSheet()
    return {
        "title": ParagraphStyle(
            "DesignTitle",
            parent=base["Title"],
            fontName="Helvetica-Bold",
            fontSize=25,
            leading=30,
            textColor=NAVY,
            alignment=TA_LEFT,
            spaceAfter=16,
        ),
        "subtitle": ParagraphStyle(
            "DesignSubtitle",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=12,
            leading=17,
            textColor=SLATE,
            spaceAfter=8,
        ),
        "h1": ParagraphStyle(
            "DesignH1",
            parent=base["Heading1"],
            fontName="Helvetica-Bold",
            fontSize=17,
            leading=21,
            textColor=NAVY,
            spaceBefore=15,
            spaceAfter=8,
            keepWithNext=True,
        ),
        "h2": ParagraphStyle(
            "DesignH2",
            parent=base["Heading2"],
            fontName="Helvetica-Bold",
            fontSize=13,
            leading=17,
            textColor=BLUE,
            spaceBefore=11,
            spaceAfter=6,
            keepWithNext=True,
        ),
        "h3": ParagraphStyle(
            "DesignH3",
            parent=base["Heading3"],
            fontName="Helvetica-BoldOblique",
            fontSize=10.5,
            leading=14,
            textColor=SLATE,
            spaceBefore=8,
            spaceAfter=4,
            keepWithNext=True,
        ),
        "body": ParagraphStyle(
            "DesignBody",
            parent=base["BodyText"],
            fontName="Helvetica",
            fontSize=9.1,
            leading=12.6,
            textColor=INK,
            spaceAfter=6,
            alignment=TA_LEFT,
        ),
        "bullet": ParagraphStyle(
            "DesignBullet",
            parent=base["BodyText"],
            fontName="Helvetica",
            fontSize=9,
            leading=12.3,
            textColor=INK,
            leftIndent=16,
            firstLineIndent=-9,
            bulletIndent=5,
            spaceAfter=4,
        ),
        "small": ParagraphStyle(
            "DesignSmall",
            parent=base["BodyText"],
            fontName="Helvetica",
            fontSize=7.4,
            leading=9.2,
            textColor=INK,
        ),
        "small_header": ParagraphStyle(
            "DesignSmallHeader",
            parent=base["BodyText"],
            fontName="Helvetica-Bold",
            fontSize=7.4,
            leading=9.2,
            textColor=WHITE,
        ),
        "callout": ParagraphStyle(
            "DesignCallout",
            parent=base["BodyText"],
            fontName="Helvetica-Bold",
            fontSize=10,
            leading=14,
            textColor=NAVY,
            alignment=TA_CENTER,
        ),
    }


@lru_cache(maxsize=1)
def _bibliography() -> dict[str, dict[str, str]]:
    text = (PAPER_ROOT / "references.bib").read_text(encoding="utf-8")
    starts = list(re.finditer(r"(?m)^@(\w+)\{([^,]+),", text))
    entries: dict[str, dict[str, str]] = {}
    for index, match in enumerate(starts):
        end = starts[index + 1].start() if index + 1 < len(starts) else len(text)
        block = text[match.end() : end]
        fields: dict[str, str] = {"entry_type": match.group(1), "key": match.group(2).strip()}
        for field_match in re.finditer(r"(?m)^\s*(\w+)\s*=\s*\{(.*?)\}\s*,?\s*$", block):
            fields[field_match.group(1).lower()] = re.sub(r"[{}]", "", field_match.group(2)).strip()
        entries[fields["key"]] = fields
    return entries


def _citation_label(key: str) -> str:
    entry = _bibliography().get(key)
    if entry is None:
        raise ValueError(f"unresolved bibliography key in report source: {key}")
    author = entry.get("author", "Unknown")
    first_author = author.split(" and ", 1)[0].strip()
    surname = first_author.split()[-1] if first_author else "Unknown"
    if author.startswith("BibleBench Project"):
        surname = "BibleBench Project"
    return f"{surname}, {entry.get('year', 'n.d.')}"


def _humanize_citations(text: str) -> str:
    def replace(match: re.Match[str]) -> str:
        keys = [part.strip().lstrip("@") for part in match.group(1).split(";")]
        return "(" + "; ".join(_citation_label(key) for key in keys) + ")"

    return re.sub(r"\[@([^\]]+)\]", replace, text)


def _inline(text: Any) -> str:
    value = escape(_humanize_citations(_ascii_text(text).strip()))
    value = re.sub(r"\[([^\]]+)\]\((https?://[^)]+)\)", r'<link href="\2" color="#245B86">\1</link>', value)
    value = re.sub(r"`([^`]+)`", r'<font name="Courier">\1</font>', value)
    value = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", value)
    value = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<i>\1</i>", value)
    return value


class InvariantCanvas(canvas.Canvas):
    def __init__(self, *args: Any, title: str, **kwargs: Any) -> None:
        kwargs["invariant"] = 1
        super().__init__(*args, **kwargs)
        self.setTitle(_ascii_text(title))
        self.setAuthor(AUTHOR)
        self.setSubject("Pre-empirical BibleBench design report; no model outcomes")
        self.setCreator(CREATOR)


def _on_page(pdf: canvas.Canvas, doc: BaseDocTemplate) -> None:
    pdf.saveState()
    width, height = LETTER
    pdf.setStrokeColor(LIGHT_RULE)
    pdf.setLineWidth(0.5)
    pdf.line(doc.leftMargin, height - 0.52 * inch, width - doc.rightMargin, height - 0.52 * inch)
    pdf.setFillColor(SLATE)
    pdf.setFont("Helvetica-Bold", 7.2)
    pdf.drawString(doc.leftMargin, height - 0.39 * inch, "BIBLEBENCH")
    pdf.setFont("Helvetica", 7.2)
    pdf.drawRightString(width - doc.rightMargin, height - 0.39 * inch, STATUS)
    pdf.drawString(doc.leftMargin, 0.42 * inch, AUTHOR)
    pdf.drawRightString(width - doc.rightMargin, 0.42 * inch, f"Page {doc.page}")
    pdf.restoreState()


def _cover(report: dict[str, Any], styles: dict[str, ParagraphStyle]) -> list[Any]:
    return [
        Spacer(1, 0.55 * inch),
        Paragraph(_inline(report["title"]), styles["title"]),
        Paragraph(STATUS, styles["subtitle"]),
        Spacer(1, 0.18 * inch),
        Table(
            [[Paragraph("DESIGN STATUS", styles["small_header"]), Paragraph("No model outcomes; pilot results pending", styles["small"])]],
            colWidths=[1.35 * inch, 5.15 * inch],
            style=TableStyle(
                [
                    ("BACKGROUND", (0, 0), (0, 0), NAVY),
                    ("BACKGROUND", (1, 0), (1, 0), PALE_GOLD),
                    ("BOX", (0, 0), (-1, -1), 0.5, LIGHT_RULE),
                    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                    ("LEFTPADDING", (0, 0), (-1, -1), 8),
                    ("RIGHTPADDING", (0, 0), (-1, -1), 8),
                    ("TOPPADDING", (0, 0), (-1, -1), 8),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
                ]
            ),
        ),
        Spacer(1, 0.28 * inch),
        Paragraph(
            "BibleBench evaluates retained outputs, artifacts, sandboxed actions, and passage-aware interpretation while preserving module-native constructs and explicit claim limits.",
            styles["callout"],
        ),
        Spacer(1, 0.35 * inch),
        Paragraph(f"Prepared by {AUTHOR}", styles["subtitle"]),
        Paragraph("Portfolio research snapshot - 2026-07-13", styles["subtitle"]),
        PageBreak(),
    ]


def _markdown_story(markdown: str, styles: dict[str, ParagraphStyle], *, skip_title: bool = False) -> list[Any]:
    text = _ascii_text(markdown)
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end != -1:
            text = text[end + 5 :]
    lines = text.splitlines()
    story: list[Any] = []
    paragraph: list[str] = []
    skipped = False

    def flush() -> None:
        if paragraph:
            story.append(Paragraph(_inline(" ".join(paragraph)), styles["body"]))
            paragraph.clear()

    index = 0
    while index < len(lines):
        stripped = lines[index].strip()
        if not stripped:
            flush()
            index += 1
            continue
        if stripped.startswith("|"):
            flush()
            table_lines: list[str] = []
            while index < len(lines) and lines[index].strip().startswith("|"):
                table_lines.append(lines[index].strip())
                index += 1
            rows: list[list[str]] = []
            for line in table_lines:
                cells = [cell.strip() for cell in line.strip("|").split("|")]
                if all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells):
                    continue
                rows.append(cells)
            if rows:
                column_count = max(len(row) for row in rows)
                data = []
                for row_index, row in enumerate(rows):
                    style = styles["small_header"] if row_index == 0 else styles["small"]
                    data.append([Paragraph(_inline(cell), style) for cell in row] + [""] * (column_count - len(row)))
                table = Table(data, colWidths=[6.65 * inch / column_count] * column_count, repeatRows=1, hAlign="LEFT")
                table.setStyle(
                    TableStyle(
                        [
                            ("BACKGROUND", (0, 0), (-1, 0), NAVY),
                            ("GRID", (0, 0), (-1, -1), 0.35, LIGHT_RULE),
                            ("VALIGN", (0, 0), (-1, -1), "TOP"),
                            ("ROWBACKGROUNDS", (0, 1), (-1, -1), [WHITE, PALE_BLUE]),
                            ("LEFTPADDING", (0, 0), (-1, -1), 4),
                            ("RIGHTPADDING", (0, 0), (-1, -1), 4),
                            ("TOPPADDING", (0, 0), (-1, -1), 4),
                            ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
                        ]
                    )
                )
                story.extend([table, Spacer(1, 7)])
            continue
        heading = re.match(r"^(#{1,3})\s+(.+)$", stripped)
        if heading:
            flush()
            if skip_title and not skipped and len(heading.group(1)) == 1:
                skipped = True
            else:
                story.append(Paragraph(_inline(heading.group(2)), styles[f"h{len(heading.group(1))}"]))
            index += 1
            continue
        if re.match(r"^[-*]\s+", stripped):
            flush()
            story.append(Paragraph(_inline(re.sub(r"^[-*]\s+", "", stripped)), styles["bullet"], bulletText="-"))
            index += 1
            continue
        if re.match(r"^\d+\.\s+", stripped):
            flush()
            label, value = stripped.split(".", 1)
            story.append(Paragraph(_inline(value.strip()), styles["bullet"], bulletText=f"{label}."))
            index += 1
            continue
        if stripped == "---":
            flush()
            story.append(Spacer(1, 6))
            index += 1
            continue
        if stripped.startswith("```"):
            flush()
            index += 1
            code: list[str] = []
            while index < len(lines) and not lines[index].strip().startswith("```"):
                code.append(lines[index])
                index += 1
            index += 1
            story.append(Paragraph(_inline(" | ".join(code)), styles["small"]))
            continue
        paragraph.append(stripped)
        index += 1
    flush()
    return story


def _label_block(label: str, values: Iterable[Any], styles: dict[str, ParagraphStyle]) -> list[Any]:
    items = [value for value in values if value not in (None, "")]
    if not items:
        return []
    return [
        Paragraph(_inline(label), styles["h3"]),
        *[Paragraph(_inline(value), styles["bullet"], bulletText="-") for value in items],
    ]


def _module_story(report: dict[str, Any], styles: dict[str, ParagraphStyle]) -> list[Any]:
    bank_path = BIBLEBENCH_ROOT / report["sources"][0]
    bank = yaml.safe_load(bank_path.read_text(encoding="utf-8"))
    episodes = bank["episodes"]
    roles = {role: sum(episode["role"] == role for episode in episodes) for role in ("target", "null", "restraint")}
    strata = {stratum: sum(episode["stratum"] == stratum for episode in episodes) for stratum in ("common_life", "christian_facing")}
    story: list[Any] = [
        Paragraph("Module scope", styles["h1"]),
        Paragraph(
            f"This module contains {len(episodes)} executable development episodes and preserves its passage-specific constructs, exclusions, authority limits, failure poles, and provenance. It uses a broad evangelical-Protestant calibration boundary without treating denominational distinctives as identity gates.",
            styles["body"],
        ),
        Table(
            [
                [Paragraph("Geometry", styles["small_header"]), Paragraph("Count", styles["small_header"])],
                [Paragraph("Target / null / restraint", styles["small"]), Paragraph(f"{roles['target']} / {roles['null']} / {roles['restraint']}", styles["small"])],
                [Paragraph("Common-life / Christian-facing", styles["small"]), Paragraph(f"{strata['common_life']} / {strata['christian_facing']}", styles["small"])],
            ],
            colWidths=[4.8 * inch, 1.6 * inch],
            style=TableStyle(
                [
                    ("BACKGROUND", (0, 0), (-1, 0), NAVY),
                    ("GRID", (0, 0), (-1, -1), 0.35, LIGHT_RULE),
                    ("ROWBACKGROUNDS", (0, 1), (-1, -1), [WHITE, PALE_BLUE]),
                    ("VALIGN", (0, 0), (-1, -1), "TOP"),
                    ("LEFTPADDING", (0, 0), (-1, -1), 5),
                    ("RIGHTPADDING", (0, 0), (-1, -1), 5),
                    ("TOPPADDING", (0, 0), (-1, -1), 5),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
                ]
            ),
        ),
        Spacer(1, 8),
        Paragraph("Episode inventory", styles["h1"]),
    ]
    for episode in episodes:
        story.append(
            Paragraph(
                _inline(f"{episode['episode_id']} - {episode['core_id']} - {episode['role']} / {episode['stratum']} / {episode['mode']}"),
                styles["h2"],
            )
        )
        story.extend(_label_block("Passage anchors", episode["passage_anchors"], styles))
        story.append(Paragraph(_inline(episode["shared_body"]), styles["body"]))
        story.append(Paragraph(_inline(f"Objective: {episode['task_semantics']['objective']}"), styles["body"]))
        story.append(Paragraph(_inline(f"Authority boundary: {episode['authority_boundary']}"), styles["body"]))
        story.extend(_label_block("Acceptable action band", episode["acceptable_action_band"], styles))
        story.extend(_label_block("Prohibited actions", episode["prohibited_actions"], styles))
        story.append(Paragraph(_inline(f"Deficient pole: {episode['deficient_pole']}"), styles["body"]))
        story.append(Paragraph(_inline(f"Counterfeit pole: {episode['counterfeit_pole']}"), styles["body"]))
        story.append(Paragraph(_inline(f"Matched observable probe: {episode['probe_payload']['question']}"), styles["body"]))
        source = episode["source_artifacts"][0]
        story.append(Paragraph(_inline(f"Provenance: {source['path']} - {source['heading']}"), styles["small"]))
    return story


def _tencommandments_story(report: dict[str, Any], styles: dict[str, ParagraphStyle]) -> list[Any]:
    source = _ascii_text((BIBLEBENCH_ROOT / report["sources"][0]).read_text(encoding="utf-8"))
    pattern = re.compile(r"^# (\d{2}[ABC]) ([A-Z]+) - ([^\n]+)\n(.*?)(?=^# \d{2}[ABC] |\Z)", re.MULTILINE | re.DOTALL)
    designs = pattern.findall(source)
    if len(designs) != 30:
        raise ValueError(f"expected 30 Ten Commandments designs, found {len(designs)}")
    story: list[Any] = [
        Paragraph("One canon, three measurement generations", styles["h1"]),
        Paragraph(
            "Generation A contains ten direct clause-linked constructs; Generation B adds ten orthogonal measurement questions; Generation C adds ten whole-code methods. The atlas preserves all 30 registered designs even though the 48-episode MVP instantiates only approved core families.",
            styles["body"],
        ),
    ]
    for index, (identifier, name, subtitle, block) in enumerate(designs):
        if index in (10, 20):
            story.append(PageBreak())
        design_story = [Paragraph(_inline(f"{identifier} {name} - {subtitle}"), styles["h1"])]
        design_story.extend(_markdown_story(block, styles))
        story.append(KeepTogether(design_story))
    episode_report = {
        "sources": [report["sources"][1]],
    }
    story.extend(
        [
            PageBreak(),
            Paragraph("MVP module boundary and executable episodes", styles["h1"]),
            Paragraph(
                "The atlas inventory is broader than the PF-002 executable core. The following 12 frozen 10CBench episodes preserve Ten Commandments passage anchors, observable authority limits, prohibited actions, deficient and counterfeit poles, and exact repository provenance. The calibration is broadly evangelical-Protestant and permits declared Protestant contestability; it is not a claim of Christian consensus.",
                styles["body"],
            ),
        ]
    )
    story.extend(_module_story(episode_report, styles))
    return story


def _analysis_story(report: dict[str, Any], styles: dict[str, ParagraphStyle]) -> list[Any]:
    story = _markdown_story((BIBLEBENCH_ROOT / report["sources"][0]).read_text(encoding="utf-8"), styles, skip_title=True)
    figure_contracts = json.loads((BIBLEBENCH_ROOT / report["sources"][2]).read_text(encoding="utf-8"))
    story.append(Paragraph("Registered figure data", styles["h1"]))
    for figure in figure_contracts["figures"]:
        story.append(Paragraph(_inline(f"{figure['figure_id']}: {figure['mark']} - fields: {', '.join(figure['required_fields'])}"), styles["bullet"], bulletText="-"))
    claims = yaml.safe_load((BIBLEBENCH_ROOT / report["sources"][3]).read_text(encoding="utf-8"))
    story.append(Paragraph("Claims registry", styles["h1"]))
    for claim in claims.get("claims", []):
        story.append(Paragraph(_inline(f"{claim['id']} [{claim['type']}]: {claim['statement']}"), styles["body"]))
        story.append(Paragraph(_inline(f"Boundary: {claim['boundary']}"), styles["small"]))
    return story


def _bibliography_story(styles: dict[str, ParagraphStyle]) -> list[Any]:
    story: list[Any] = [PageBreak(), Paragraph("References", styles["h1"])]
    for key, entry in _bibliography().items():
        author = entry.get("author", "Unknown author")
        year = entry.get("year", "n.d.")
        title = entry.get("title", "Untitled")
        container = entry.get("booktitle") or entry.get("journal") or entry.get("howpublished") or ""
        identifier = entry.get("doi") or entry.get("url") or entry.get("eprint") or entry.get("note") or ""
        story.append(Paragraph(_inline(f"{author} ({year}). {title}. {container}. {identifier}"), styles["small"]))
        story.append(Spacer(1, 4))
    return story


def _story_for(report: dict[str, Any], styles: dict[str, ParagraphStyle]) -> list[Any]:
    kind = report["kind"]
    if kind == "module":
        return _module_story(report, styles)
    if kind == "tencommandments_atlas":
        return _tencommandments_story(report, styles)
    if kind == "analysis":
        return _analysis_story(report, styles)
    markdown_parts = [(BIBLEBENCH_ROOT / source).read_text(encoding="utf-8") for source in report["sources"]]
    if kind == "manuscript":
        return _markdown_story(markdown_parts[0], styles, skip_title=True) + _bibliography_story(styles)
    if kind == "markdown":
        return _markdown_story("\n\n".join(markdown_parts), styles, skip_title=True)
    raise ValueError(f"unsupported report kind: {kind}")


def _validate_sources(report: dict[str, Any]) -> None:
    for relative in report["sources"]:
        path = BIBLEBENCH_ROOT / relative
        if not path.is_file() or not path.read_bytes():
            raise ValueError(f"missing or empty report source: {path}")


def _validate_pre_empirical_sources(report: dict[str, Any]) -> None:
    text = "\n".join((BIBLEBENCH_ROOT / source).read_text(encoding="utf-8", errors="replace") for source in report["sources"])
    forbidden = (
        r"\bMODEL_RESULT\b",
        r"\bEMPIRICAL_RESULT\b",
        r"\bLEADERBOARD_ROW\b",
        r"\bCOMPOSITE_SCORE\b",
        r"\bBEST_MODEL\s*:",
        r"\bbest model is\b",
        r"\b(?:TBD|TODO|FIXME)\b",
    )
    found = [pattern for pattern in forbidden if re.search(pattern, text, flags=re.IGNORECASE)]
    if found:
        raise ValueError(f"{report['filename']}: forbidden empirical or unresolved marker: {found}")


def _validate_required_phrases(report: dict[str, Any], story_text: str) -> None:
    normalized = re.sub(r"[_\s]+", " ", story_text).lower()
    missing = [phrase for phrase in report["required_phrases"] if re.sub(r"[_\s]+", " ", phrase).lower() not in normalized]
    if missing:
        raise ValueError(f"{report['filename']}: required report phrases absent: {missing}")


def build_report(report: dict[str, Any]) -> Path:
    _validate_sources(report)
    _validate_pre_empirical_sources(report)
    styles = _styles()
    content = _story_for(report, styles)
    source_text = "\n".join((BIBLEBENCH_ROOT / source).read_text(encoding="utf-8", errors="replace") for source in report["sources"])
    _validate_required_phrases(report, source_text)
    OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)
    output = OUTPUT_ROOT / report["filename"]
    doc = BaseDocTemplate(
        str(output),
        pagesize=LETTER,
        leftMargin=0.7 * inch,
        rightMargin=0.7 * inch,
        topMargin=0.72 * inch,
        bottomMargin=0.68 * inch,
        title=report["title"],
        author=AUTHOR,
        subject="Pre-empirical BibleBench design report; no model outcomes",
        creator=CREATOR,
    )
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="body")
    doc.addPageTemplates([PageTemplate(id="design-report", frames=[frame], onPage=_on_page)])
    doc.build(_cover(report, styles) + content, canvasmaker=partial(InvariantCanvas, title=report["title"]))
    return output


def build_all() -> list[Path]:
    registry = yaml.safe_load(REGISTRY_PATH.read_text(encoding="utf-8"))
    if registry.get("status") != STATUS or registry.get("author") != AUTHOR:
        raise ValueError("report registry status or author mismatch")
    reports = registry.get("reports")
    if not isinstance(reports, list) or len(reports) != 9:
        raise ValueError("report registry must contain exactly nine reports")
    filenames = [report["filename"] for report in reports]
    if len(filenames) != len(set(filenames)):
        raise ValueError("duplicate report filename")
    return [build_report(report) for report in reports]


if __name__ == "__main__":
    for built in build_all():
        print(built)
