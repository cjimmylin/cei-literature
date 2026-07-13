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
REFERENCES = PAPER_ROOT / "references.bib"
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
        "reference": ParagraphStyle(
            "BBReference",
            parent=base["BodyText"],
            fontName="BBArial",
            fontSize=7.7,
            leading=10.1,
            textColor=colors.HexColor("#243746"),
            leftIndent=13,
            firstLineIndent=-13,
            spaceAfter=5,
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


def _parse_bibliography(text: str) -> dict[str, dict[str, str]]:
    """Parse the deliberately bounded BibTeX subset used by this manuscript."""
    entries: dict[str, dict[str, str]] = {}
    entry_pattern = re.compile(
        r"^@(?P<type>[A-Za-z]+)\{(?P<key>[^,\s]+),(?P<body>.*?)(?=^@|\Z)",
        re.MULTILINE | re.DOTALL,
    )
    for match in entry_pattern.finditer(text):
        body = match.group("body").rstrip()
        if not body.endswith("}"):
            raise ValueError(f"unterminated bibliography entry: {match.group('key')}")
        body = body[:-1]
        fields: dict[str, str] = {"entry_type": match.group("type").lower()}
        position = 0
        while position < len(body):
            separator = re.match(r"[\s,]*", body[position:])
            position += separator.end()
            if position >= len(body):
                break
            field_match = re.match(r"([A-Za-z][A-Za-z0-9_]*)\s*=\s*", body[position:])
            if not field_match:
                raise ValueError(
                    f"invalid bibliography field in {match.group('key')}: "
                    f"{body[position:position + 24]!r}"
                )
            field = field_match.group(1).lower()
            position += field_match.end()
            if body[position] == "{":
                depth = 1
                start = position + 1
                position += 1
                while position < len(body) and depth:
                    if body[position] == "{":
                        depth += 1
                    elif body[position] == "}":
                        depth -= 1
                    position += 1
                if depth:
                    raise ValueError(
                        f"unterminated bibliography field {field} in {match.group('key')}"
                    )
                value = body[start : position - 1]
            elif body[position] == '"':
                start = position + 1
                position = body.find('"', start)
                if position < 0:
                    raise ValueError(
                        f"unterminated bibliography field {field} in {match.group('key')}"
                    )
                value = body[start:position]
                position += 1
            else:
                end = body.find(",", position)
                if end < 0:
                    end = len(body)
                value = body[position:end].strip()
                position = end
            fields[field] = value.strip()
        key = match.group("key")
        if key in entries:
            raise ValueError(f"duplicate bibliography key: {key}")
        entries[key] = fields
    if not entries:
        raise ValueError("bibliography contains no entries")
    return entries


def _plain_bibtex(value: str) -> str:
    return value.replace("{", "").replace("}", "").replace("--", "-").strip()


def _authors(entry: dict[str, str]) -> tuple[list[str], bool]:
    raw = entry.get("author", "").strip()
    corporate = raw.startswith("{") and raw.endswith("}")
    if corporate:
        return [_plain_bibtex(raw)], True
    return [
        _plain_bibtex(name)
        for name in re.split(r"\s+and\s+", raw)
        if name.strip()
    ], False


def _author_year(entry: dict[str, str]) -> tuple[str, str]:
    authors, corporate = _authors(entry)
    if not authors:
        label = "Anonymous"
    elif corporate:
        label = authors[0]
    elif len(authors) == 1:
        label = authors[0].split()[-1]
    elif len(authors) == 2:
        label = f"{authors[0].split()[-1]} and {authors[1].split()[-1]}"
    else:
        label = f"{authors[0].split()[-1]} et al."
    return label, _plain_bibtex(entry.get("year", "n.d."))


def _citation_labels(entries: dict[str, dict[str, str]]) -> dict[str, str]:
    bases: dict[str, tuple[str, str]] = {
        key: _author_year(entry) for key, entry in entries.items()
    }
    grouped: dict[tuple[str, str], list[str]] = {}
    for key, base in bases.items():
        grouped.setdefault(base, []).append(key)
    labels: dict[str, str] = {}
    for key, (author, year) in bases.items():
        siblings = grouped[(author, year)]
        suffix = chr(ord("a") + siblings.index(key)) if len(siblings) > 1 else ""
        labels[key] = f"{author}, {year}{suffix}"
    return labels


def _resolve_citations(
    markdown: str, entries: dict[str, dict[str, str]]
) -> tuple[str, list[str]]:
    labels = _citation_labels(entries)
    cited: list[str] = []
    citation_pattern = re.compile(
        r"\[(?P<items>@[A-Za-z][A-Za-z0-9]*(?:\s*;\s*@[A-Za-z][A-Za-z0-9]*)*)\]"
    )

    def replace(match: re.Match[str]) -> str:
        keys = re.findall(r"@([A-Za-z][A-Za-z0-9]*)", match.group("items"))
        missing = [key for key in keys if key not in entries]
        if missing:
            raise ValueError(f"unresolved bibliography citation(s): {', '.join(missing)}")
        for key in keys:
            if key not in cited:
                cited.append(key)
        return "(" + "; ".join(labels[key] for key in keys) + ")"

    resolved = citation_pattern.sub(replace, markdown)
    unresolved = re.search(r"\[@[A-Za-z][A-Za-z0-9]*", resolved)
    if unresolved:
        raise ValueError(f"unresolved bibliography token: {unresolved.group(0)}")
    return resolved, cited


def _bibliography_entry(entry: dict[str, str], citation_year: str) -> str:
    authors, _ = _authors(entry)
    if not authors:
        author_text = "Anonymous"
    elif len(authors) > 4:
        author_text = f"{authors[0]} et al."
    elif len(authors) == 1:
        author_text = authors[0]
    else:
        author_text = ", ".join(authors[:-1]) + f", and {authors[-1]}"
    title = _plain_bibtex(entry.get("title", "Untitled"))
    parts = [f"{author_text} ({citation_year}). {title}."]
    container = entry.get("journal") or entry.get("booktitle")
    if container:
        parts.append(_plain_bibtex(container) + ".")
    series = entry.get("series")
    if series:
        parts.append(_plain_bibtex(series) + ".")
    publisher = entry.get("publisher")
    if publisher:
        parts.append(_plain_bibtex(publisher) + ".")
    volume = _plain_bibtex(entry.get("volume", ""))
    number = _plain_bibtex(entry.get("number", ""))
    pages = _plain_bibtex(entry.get("pages", ""))
    if volume:
        parts.append(f"Volume {volume}" + (f"({number})" if number else "") + ".")
    if pages:
        parts.append(f"Pages {pages}.")
    isbn = _plain_bibtex(entry.get("isbn", ""))
    if isbn:
        parts.append(f"ISBN {isbn}.")
    howpublished = entry.get("howpublished")
    if howpublished:
        parts.append(_plain_bibtex(howpublished) + ".")
    doi = _plain_bibtex(entry.get("doi", ""))
    if doi:
        parts.append(f"[DOI](https://doi.org/{doi}).")
    url = _plain_bibtex(entry.get("url", ""))
    if url:
        parts.append(f"[Source]({url}).")
    note = entry.get("note")
    if note:
        parts.append(_plain_bibtex(note))
    return " ".join(parts)


def _bibliography_story(
    entries: dict[str, dict[str, str]],
    cited: list[str],
    styles: dict[str, ParagraphStyle],
) -> list:
    labels = _citation_labels(entries)
    external = [key for key in cited if entries[key].get("keywords") != "local-provenance"]
    local = [key for key in cited if entries[key].get("keywords") == "local-provenance"]
    story: list = [
        PageBreak(),
        Paragraph("Bibliography", styles["h1"]),
        Paragraph(
            "External scholarship and local design provenance are separated below. "
            "The bibliography resolves every author-year citation in the manuscript; "
            "repository entries document design lineage rather than external validation.",
            styles["body"],
        ),
    ]
    for heading, keys in (("External scholarship", external), ("Local design provenance", local)):
        if not keys:
            continue
        story.append(Paragraph(heading, styles["h2"]))
        for key in keys:
            citation_year = labels[key].rsplit(", ", 1)[-1]
            story.append(
                Paragraph(
                    _inline(_bibliography_entry(entries[key], citation_year)),
                    styles["reference"],
                )
            )
    return story


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
    bibliography = _parse_bibliography(REFERENCES.read_text(encoding="utf-8"))
    markdown, cited = _resolve_citations(markdown, bibliography)
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
    doc.build(
        cover
        + _body_story(markdown, styles)
        + _bibliography_story(bibliography, cited, styles)
    )
    return OUTPUT


if __name__ == "__main__":
    print(build())
