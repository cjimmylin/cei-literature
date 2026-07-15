#!/usr/bin/env python3
"""Empirical-data gate and neutral Pilot 2 supplement renderers."""

from __future__ import annotations

import argparse
import html
import json
from pathlib import Path
from typing import Any, Dict, Mapping, Sequence

import pilot2_preflight as preflight


class ReportError(RuntimeError):
    """A Pilot 2 supplement cannot be emitted from the supplied evidence."""


def _require_complete_empirical(dataset: Mapping[str, Any]) -> list:
    """Fail closed unless all five scalar surfaces meet the registered gate."""
    cells = dataset.get("cells")
    rows = dataset.get("per_sut")
    if not isinstance(cells, list) or len(cells) != 222 * len(preflight.SUTS):
        raise ReportError("complete empirical scalar evidence is required")
    if not isinstance(rows, list) or len(rows) != len(preflight.SUTS):
        raise ReportError("complete empirical per-SUT summaries are required")
    keyed = {row.get("sut"): row for row in rows if isinstance(row, Mapping)}
    if set(keyed) != set(preflight.SUTS):
        raise ReportError("complete empirical exact-roster summaries are required")
    ordered = []
    for slug in preflight.SUTS:
        row = dict(keyed[slug])
        if row.get("scalar_denominator") != 222:
            raise ReportError(f"complete empirical denominator missing for {slug}")
        numeric = row.get("numeric")
        if not isinstance(numeric, int) or isinstance(numeric, bool) or numeric < 200:
            raise ReportError(f"complete empirical coverage gate failed for {slug}")
        if any(row.get(field) is None for field in ("mean", "ci_low", "ci_high")):
            raise ReportError(f"complete empirical interval missing for {slug}")
        ordered.append(row)
    return ordered


def _number(value: Any) -> str:
    return "missing" if value is None else f"{float(value):.4f}"


def _markdown(dataset: Mapping[str, Any], per_sut: Sequence[Mapping[str, Any]]) -> str:
    lines = [
        f"# {preflight.VALIDITY_LABEL}",
        "",
        "This immutable supplement is a descriptive exploratory snapshot. It makes "
        "no ranking, reasoning-effect, release, gate, universal-score, publication, "
        "or accepted-paper claim.",
        "",
        "## Per-SUT descriptive scalar summaries (frozen roster order)",
        "",
        "| SUT | Numeric / 222 | Mean | 95% item-bootstrap interval | Errors / missing |",
        "|---|---:|---:|---:|---:|",
    ]
    for row in per_sut:
        lines.append(
            f"| `{row['sut']}` | {row['numeric']} / 222 | {_number(row['mean'])} | "
            f"[{_number(row['ci_low'])}, {_number(row['ci_high'])}] | "
            f"{row.get('errors_missing', 222 - row['numeric'])} |")
    lines.extend([
        "",
        "## Separate reporting surfaces",
        "",
        "Matter, Manner, End, refusal behavior, contested positions, coverage, errors, "
        "and the four diagnostic-only development items remain separate. Errors are "
        "missing, never zero. Diagnostic development items are not judged or aggregated.",
        "",
        "### Axis coverage",
        "",
        "| Axis | Numeric | Mean |",
        "|---|---:|---:|",
    ])
    for axis in ("matter", "manner", "end"):
        row = dataset.get("axis_summary", {}).get(axis, {})
        lines.append(f"| {axis.title()} | {row.get('numeric', 0)} | "
                     f"{_number(row.get('mean'))} |")
    lines.extend([
        "",
        f"Refusal classes: `{json.dumps(dataset.get('refusal_summary', {}), sort_keys=True)}`",
        "",
        f"Contested cells reported separately: {len(dataset.get('contested_summary', []))}",
        "",
        f"Errors or missing cells: {len(dataset.get('errors_missing', []))}",
        "",
        f"Diagnostic-only development cells: {len(dataset.get('diagnostic_dev_cells', []))}",
        "",
        "## Interpretation boundary",
        "",
        "No ranking is reported. No reasoning-effect estimate is possible. This single "
        "unqualified Codex-OAuth judge result is non-quotable and does not replace PPP-1.",
        "",
    ])
    return "\n".join(lines)


def _html(markdown_text: str, per_sut: Sequence[Mapping[str, Any]]) -> str:
    rows = "".join(
        "<tr><td><code>{}</code></td><td>{}/222</td><td>{}</td>"
        "<td>[{}, {}]</td><td>{}</td></tr>".format(
            html.escape(str(row["sut"])), row["numeric"], _number(row["mean"]),
            _number(row["ci_low"]), _number(row["ci_high"]),
            row.get("errors_missing", 222 - row["numeric"]))
        for row in per_sut)
    return """<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><style>
:root{{color-scheme:light;--ink:#18212b;--muted:#586474;--line:#cbd3dc;--paper:#fff;--wash:#eef3f7}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--wash);color:var(--ink);font:16px/1.55 system-ui,sans-serif}}
main{{max-width:980px;margin:2rem auto;padding:2.5rem;background:var(--paper);box-shadow:0 8px 28px #1a27351a}}
h1{{font-size:1.55rem;line-height:1.25}}.label{{border:2px solid #8a301f;padding:1rem;background:#fff5f1}}
table{{width:100%;border-collapse:collapse;margin:1rem 0}}th,td{{border:1px solid var(--line);padding:.55rem;text-align:left}}
th{{background:#f4f6f8}}code{{overflow-wrap:anywhere}}.boundary{{border-left:5px solid #8a301f;padding:.75rem 1rem;background:#fff5f1}}
@media(max-width:600px){{main{{margin:0;padding:1rem}}table{{font-size:.78rem}}th,td{{padding:.35rem}}}}
@media print{{body{{background:#fff}}main{{max-width:none;margin:0;padding:0;box-shadow:none}}}}
</style></head><body><main>
<h1 class="label">{title}</h1>
<p>This immutable supplement is a descriptive exploratory snapshot. It makes no ranking, reasoning-effect, release, gate, universal-score, publication, or accepted-paper claim.</p>
<h2>Per-SUT descriptive scalar summaries</h2><p>Frozen roster order; errors remain missing, never zero.</p>
<table><thead><tr><th>SUT</th><th>Numeric</th><th>Mean</th><th>95% item-bootstrap interval</th><th>Errors / missing</th></tr></thead><tbody>{rows}</tbody></table>
<h2>Separate reporting surfaces</h2><p>Matter, Manner, End, refusal behavior, contested positions, coverage, errors, and diagnostic-only development items remain separate. Development items are not judged or aggregated.</p>
<h2>Interpretation boundary</h2><p class="boundary">No ranking is reported. No reasoning-effect estimate is possible. This single unqualified Codex-OAuth judge result is non-quotable and does not replace PPP-1.</p>
</main></body></html>""".format(title=html.escape(preflight.VALIDITY_LABEL), rows=rows)


def _pdf(path: Path, per_sut: Sequence[Mapping[str, Any]]) -> None:
    try:
        from reportlab.lib.pagesizes import letter
        from reportlab.lib.styles import getSampleStyleSheet
        from reportlab.lib.units import inch
        from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle
        from reportlab.lib import colors
    except ImportError as exc:  # pragma: no cover - dependency is part of harness env
        raise ReportError("reportlab is required for Pilot 2 PDF output") from exc
    styles = getSampleStyleSheet()
    doc = SimpleDocTemplate(
        str(path), pagesize=letter, rightMargin=.65 * inch, leftMargin=.65 * inch,
        topMargin=.65 * inch, bottomMargin=.65 * inch,
        title=preflight.VALIDITY_LABEL)
    title = preflight.VALIDITY_LABEL.replace(" · ", " - ")
    story = [Paragraph(title, styles["Title"]), Spacer(1, 12),
             Paragraph(
                 "Descriptive exploratory snapshot only. No ranking, reasoning-effect, "
                 "release, gate, universal-score, publication, or accepted-paper claim.",
                 styles["BodyText"]), Spacer(1, 12)]
    data = [["SUT", "Numeric", "Mean", "95% interval", "Missing"]]
    for row in per_sut:
        data.append([
            row["sut"], f"{row['numeric']}/222", _number(row["mean"]),
            f"[{_number(row['ci_low'])}, {_number(row['ci_high'])}]",
            str(row.get("errors_missing", 222 - row["numeric"]))])
    table = Table(data, colWidths=[2.35 * inch, .65 * inch, .65 * inch, 1.35 * inch, .65 * inch],
                  repeatRows=1)
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#e8edf2")),
        ("GRID", (0, 0), (-1, -1), .5, colors.HexColor("#9aa6b2")),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
        ("FONTSIZE", (0, 0), (-1, -1), 8),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
    ]))
    story.extend([Paragraph("Per-SUT descriptive scalar summaries", styles["Heading2"]),
                  table, Spacer(1, 12),
                  Paragraph("Separate reporting surfaces", styles["Heading2"]),
                  Paragraph(
                      "Matter, Manner, End, refusal behavior, contested positions, "
                      "coverage, errors, and diagnostic-only development items remain "
                      "separate. Errors are missing, never zero.", styles["BodyText"]),
                  Spacer(1, 10), Paragraph("Interpretation boundary", styles["Heading2"]),
                  Paragraph(
                      "No ranking is reported. No reasoning-effect estimate is possible. "
                      "This single unqualified Codex-OAuth judge result is non-quotable "
                      "and does not replace PPP-1.", styles["BodyText"])])
    doc.build(story)


def render_supplement(dataset: Mapping[str, Any], output_dir: Path) -> Dict[str, Path]:
    """Render one append-only supplement from complete immutable empirical data."""
    per_sut = _require_complete_empirical(dataset)
    if dataset.get("validity_label") != preflight.VALIDITY_LABEL:
        raise ReportError("complete empirical Pilot 2 validity label is required")
    output_dir = Path(output_dir)
    try:
        output_dir.mkdir(parents=True, exist_ok=False)
    except FileExistsError as exc:
        raise ReportError("supplement output directory already exists") from exc
    outputs = {
        "markdown": output_dir / "pilot2-supplement.md",
        "html": output_dir / "pilot2-supplement.html",
        "pdf": output_dir / "pilot2-supplement.pdf",
    }
    markdown_text = _markdown(dataset, per_sut)
    outputs["markdown"].write_text(markdown_text, encoding="utf-8")
    outputs["html"].write_text(_html(markdown_text, per_sut), encoding="utf-8")
    _pdf(outputs["pdf"], per_sut)
    return outputs


def build_supplement_payload(
    manifest: Mapping[str, Any], rows: Sequence[Mapping[str, Any]],
) -> Dict[str, Any]:
    if not rows:
        raise ReportError("empirical results are required; no empty supplement")
    if manifest.get("validity_label") != preflight.VALIDITY_LABEL:
        raise ReportError("manifest validity label is not Pilot 2")
    keyed = {row.get("sut"): dict(row) for row in rows}
    if set(keyed) != set(preflight.SUTS) or len(rows) != len(preflight.SUTS):
        raise ReportError("empirical results must cover each exact SUT once")
    ordered = []
    for slug in preflight.SUTS:
        row = keyed[slug]
        numeric = row.get("numeric_scores")
        if not isinstance(numeric, int) or isinstance(numeric, bool) \
                or not 0 <= numeric <= 222:
            raise ReportError(f"invalid scalar coverage: {slug}")
        row["coverage_status"] = (
            "SUFFICIENT_DESCRIPTIVE" if numeric >= 200 else "INCOMPLETE")
        if numeric < 200:
            row["scalar_mean"] = None
        ordered.append(row)
    return {
        "validity_label": preflight.VALIDITY_LABEL,
        "presentation_order": "FROZEN_ROSTER_NOT_SCORE_ORDER",
        "per_sut": ordered,
        "separate_surfaces": [
            "matter", "manner", "end", "refusal", "contested",
            "coverage", "errors", "diagnostic_dev_set"],
        "claims": {
            "ranking": False,
            "reasoning_effect": False,
            "release": False,
            "universal_score": False,
            "paper_replacement": False,
        },
    }


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--analysis-json", type=Path)
    parser.add_argument("--output-dir", type=Path)
    args = parser.parse_args(argv)
    if not args.analysis_json or not args.output_dir:
        print("Pilot 2 supplement generation requires immutable empirical analysis.")
        return 2
    try:
        dataset = json.loads(args.analysis_json.read_text(encoding="utf-8"))
        render_supplement(dataset, args.output_dir)
    except (OSError, json.JSONDecodeError, ReportError) as exc:
        print(f"Pilot 2 supplement blocked: {exc}")
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
