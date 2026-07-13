#!/usr/bin/env python3
"""Build the prerelease BibleBench methods manuscript as a reviewable PDF."""

from __future__ import annotations

from html import escape
from pathlib import Path
import re

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
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


PAPER_ROOT = Path(__file__).resolve().parents[1]
MANUSCRIPT = PAPER_ROOT / "manuscript.md"
OUTPUT = PAPER_ROOT / "output" / "pdf" / "biblebench-methods-prerelease.pdf"
TITLE = (
    "BibleBench: A Passage-Preserving Design for Observable Ethical and "
    "Biblical Evaluation of Language Models"
)
AUTHOR = "Jimmy Lin"
SUBJECT = "Prerelease design and methods manuscript; no live-model evidence"

NAVY = colors.HexColor("#17324D")
BLUE = colors.HexColor("#245B86")
PALE_BLUE = colors.HexColor("#EAF2F8")
PALE_GOLD = colors.HexColor("#FFF5D9")
SLATE = colors.HexColor("#465A6B")
LIGHT_RULE = colors.HexColor("#C9D4DC")
WHITE = colors.white


def _register_fonts() -> None:
    font_dir = Path("/System/Library/Fonts/Supplemental")
    faces = {
        "BBArial": "Arial.ttf",
        "BBArial-Bold": "Arial Bold.ttf",
        "BBArial-Italic": "Arial Italic.ttf",
        "BBArial-BoldItalic": "Arial Bold Italic.ttf",
    }
    for name, filename in faces.items():
        pdfmetrics.registerFont(TTFont(name, str(font_dir / filename)))
    pdfmetrics.registerFontFamily(
        "BBArial",
        normal="BBArial",
        bold="BBArial-Bold",
        italic="BBArial-Italic",
        boldItalic="BBArial-BoldItalic",
    )


def _styles() -> dict[str, ParagraphStyle]:
    base = getSampleStyleSheet()
    return {
        "title": ParagraphStyle(
            "BBTitle",
            parent=base["Title"],
            fontName="BBArial-Bold",
            fontSize=25,
            leading=31,
            textColor=NAVY,
            alignment=TA_LEFT,
            spaceAfter=18,
        ),
        "subtitle": ParagraphStyle(
            "BBSubtitle",
            parent=base["Normal"],
            fontName="BBArial",
            fontSize=12,
            leading=17,
            textColor=SLATE,
        ),
        "h1": ParagraphStyle(
            "BBH1",
            parent=base["Heading1"],
            fontName="BBArial-Bold",
            fontSize=17,
            leading=21,
            textColor=NAVY,
            spaceBefore=15,
            spaceAfter=8,
            keepWithNext=True,
        ),
        "h2": ParagraphStyle(
            "BBH2",
            parent=base["Heading2"],
            fontName="BBArial-Bold",
            fontSize=13,
            leading=17,
            textColor=BLUE,
            spaceBefore=11,
            spaceAfter=6,
            keepWithNext=True,
        ),
        "h3": ParagraphStyle(
            "BBH3",
            parent=base["Heading3"],
            fontName="BBArial-BoldItalic",
            fontSize=11,
            leading=14,
            textColor=SLATE,
            spaceBefore=9,
            spaceAfter=4,
            keepWithNext=True,
        ),
        "body": ParagraphStyle(
            "BBBody",
            parent=base["BodyText"],
            fontName="BBArial",
            fontSize=9.1,
            leading=12.7,
            textColor=colors.HexColor("#1D2832"),
            spaceAfter=6,
            alignment=TA_LEFT,
        ),
        "bullet": ParagraphStyle(
            "BBBullet",
            parent=base["BodyText"],
            fontName="BBArial",
            fontSize=9.2,
            leading=12.8,
            textColor=colors.HexColor("#1D2832"),
            leftIndent=16,
            firstLineIndent=-10,
            bulletIndent=5,
            spaceAfter=4,
        ),
        "small": ParagraphStyle(
            "BBSmall",
            parent=base["BodyText"],
            fontName="BBArial",
            fontSize=7.5,
            leading=9.5,
            textColor=colors.HexColor("#243746"),
        ),
        "table_header": ParagraphStyle(
            "BBTableHeader",
            parent=base["BodyText"],
            fontName="BBArial-Bold",
            fontSize=7.5,
            leading=9.5,
            textColor=WHITE,
        ),
        "callout": ParagraphStyle(
            "BBCallout",
            parent=base["BodyText"],
            fontName="BBArial-Bold",
            fontSize=10,
            leading=14,
            textColor=NAVY,
            alignment=TA_CENTER,
        ),
        "footer": ParagraphStyle(
            "BBFooter",
            parent=base["Normal"],
            fontName="BBArial",
            fontSize=7.5,
            leading=9,
            textColor=SLATE,
        ),
    }


def _inline(text: str) -> str:
    """Convert a deliberately small safe Markdown subset to ReportLab markup."""
    value = escape(text.strip())
    value = re.sub(r"\[([^\]]+)\]\((https?://[^)]+)\)", r'<link href="\2" color="#245B86">\1</link>', value)
    value = re.sub(r"`([^`]+)`", r'<font name="Courier">\1</font>', value)
    value = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", value)
    value = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<i>\1</i>", value)
    return value


def _page(canvas, doc) -> None:  # noqa: ANN001
    canvas.saveState()
    width, height = LETTER
    canvas.setStrokeColor(LIGHT_RULE)
    canvas.setLineWidth(0.5)
    canvas.line(doc.leftMargin, height - 0.52 * inch, width - doc.rightMargin, height - 0.52 * inch)
    canvas.setFont("BBArial", 7.5)
    canvas.setFillColor(SLATE)
    canvas.drawString(doc.leftMargin, height - 0.39 * inch, "BIBLEBENCH · PRERELEASE METHODS")
    canvas.drawRightString(width - doc.rightMargin, 0.42 * inch, f"{doc.page}")
    canvas.drawString(doc.leftMargin, 0.42 * inch, "No live-model evidence · Proposal only")
    canvas.restoreState()


def _table(lines: list[str], styles: dict[str, ParagraphStyle]) -> Table:
    rows: list[list[str]] = []
    for line in lines:
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells):
            continue
        rows.append(cells)
    width = 6.85 * inch
    columns = max(len(row) for row in rows)
    if columns == 4:
        widths = [1.22 * inch, 1.12 * inch, 1.10 * inch, 3.41 * inch]
    else:
        widths = [width / columns] * columns
    content = []
    for row_index, row in enumerate(rows):
        cell_style = styles["table_header"] if row_index == 0 else styles["small"]
        content.append([Paragraph(_inline(cell), cell_style) for cell in row])
    table = Table(content, colWidths=widths, repeatRows=1, hAlign="LEFT")
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), NAVY),
                ("TEXTCOLOR", (0, 0), (-1, 0), WHITE),
                ("FONTNAME", (0, 0), (-1, 0), "BBArial-Bold"),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("GRID", (0, 0), (-1, -1), 0.35, LIGHT_RULE),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [WHITE, colors.HexColor("#F3F6F8")]),
                ("LEFTPADDING", (0, 0), (-1, -1), 5),
                ("RIGHTPADDING", (0, 0), (-1, -1), 5),
                ("TOPPADDING", (0, 0), (-1, -1), 4),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
            ]
        )
    )
    return table


def _body_story(markdown: str, styles: dict[str, ParagraphStyle]) -> list:
    lines = markdown.splitlines()[1:]  # The title is rendered on the cover.
    story: list = []
    paragraph: list[str] = []

    def flush() -> None:
        if paragraph:
            story.append(Paragraph(_inline(" ".join(paragraph)), styles["body"]))
            paragraph.clear()

    index = 0
    while index < len(lines):
        line = lines[index]
        stripped = line.strip()
        if not stripped:
            flush()
            index += 1
            continue
        if stripped.startswith("|"):
            flush()
            table_lines: list[str] = []
            while index < len(lines) and lines[index].strip().startswith("|"):
                table_lines.append(lines[index])
                index += 1
            story.extend([_table(table_lines, styles), Spacer(1, 8)])
            continue
        heading = re.match(r"^(#{1,3})\s+(.+)$", stripped)
        if heading:
            flush()
            level = len(heading.group(1))
            story.append(Paragraph(_inline(heading.group(2)), styles[f"h{level}"]))
            index += 1
            continue
        numbered = re.match(r"^(\d+)\.\s+(.+)$", stripped)
        if numbered:
            flush()
            story.append(
                Paragraph(
                    _inline(numbered.group(2)),
                    styles["bullet"],
                    bulletText=f"{numbered.group(1)}.",
                )
            )
            index += 1
            continue
        bullet = re.match(r"^-\s+(.+)$", stripped)
        if bullet:
            flush()
            story.append(Paragraph(_inline(bullet.group(1)), styles["bullet"], bulletText="•"))
            index += 1
            continue
        if stripped.strip("`") == "PENDING_EMPIRICAL_RUN":
            flush()
            box = Table(
                [[Paragraph("PENDING_EMPIRICAL_RUN", styles["callout"])]],
                colWidths=[6.55 * inch],
            )
            box.setStyle(
                TableStyle(
                    [
                        ("BACKGROUND", (0, 0), (-1, -1), PALE_GOLD),
                        ("BOX", (0, 0), (-1, -1), 0.8, colors.HexColor("#D39B2A")),
                        ("TOPPADDING", (0, 0), (-1, -1), 10),
                        ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
                    ]
                )
            )
            story.extend([box, Spacer(1, 8)])
            index += 1
            continue
        paragraph.append(stripped)
        index += 1
    flush()
    return story


def build() -> Path:
    _register_fonts()
    styles = _styles()
    markdown = MANUSCRIPT.read_text(encoding="utf-8")
    if markdown.splitlines()[0] != f"# {TITLE}":
        raise ValueError("manuscript title drifted from registered PDF metadata")
    if markdown.count("PENDING_EMPIRICAL_RUN") != 1:
        raise ValueError("pre-empirical sentinel must appear exactly once")

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    doc = BaseDocTemplate(
        str(OUTPUT),
        pagesize=LETTER,
        leftMargin=0.72 * inch,
        rightMargin=0.72 * inch,
        topMargin=0.73 * inch,
        bottomMargin=0.68 * inch,
        title=TITLE,
        author=AUTHOR,
        subject=SUBJECT,
        creator="BibleBench deterministic ReportLab renderer",
        invariant=True,
    )
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="body")
    doc.addPageTemplates([PageTemplate(id="methods", frames=[frame], onPage=_page)])

    status_box = Table(
        [[Paragraph("Proposal only; $0.00 authorized", styles["callout"])]],
        colWidths=[6.0 * inch],
    )
    status_box.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), PALE_BLUE),
                ("BOX", (0, 0), (-1, -1), 1, BLUE),
                ("TOPPADDING", (0, 0), (-1, -1), 11),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 11),
            ]
        )
    )
    cover = [
        Spacer(1, 0.74 * inch),
        Paragraph(TITLE, styles["title"]),
        Spacer(1, 0.12 * inch),
        Paragraph(
            "A passage-preserving, vector-first protocol for separating observable "
            "ethical behavior from biblical and pastoral interpretation.",
            styles["subtitle"],
        ),
        Spacer(1, 0.48 * inch),
        status_box,
        Spacer(1, 0.42 * inch),
        Paragraph(
            "Design and methods manuscript · 13 July 2026<br/>"
            "Four modules · 42 construct families · 48 development episodes<br/>"
            "No live model calls, outcomes, rankings, or performance claims",
            styles["subtitle"],
        ),
        Spacer(1, 0.55 * inch),
        KeepTogether(
            [
                Paragraph("Reading status", styles["h2"]),
                Paragraph(
                    "This PDF is a prerelease paper artifact. Registered design and "
                    "engineering claims are separated from provisional theological "
                    "judgment and pending empirical questions. The Results section "
                    "remains visibly unfilled until the authorized pilot is complete.",
                    styles["body"],
                ),
            ]
        ),
        PageBreak(),
    ]
    doc.build(cover + _body_story(markdown, styles))
    return OUTPUT


if __name__ == "__main__":
    print(build())
