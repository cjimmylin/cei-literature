#!/usr/bin/env python3
"""Render the nine-fruit V0–V3 response surface as an accessible SVG."""
from __future__ import annotations

from html import escape


ARMS = ["V0", "V1", "V2", "V3"]


def svg_text(result: dict) -> str:
    width, height = 960, 780
    panel_w, panel_h = 280, 190
    x0, y0, gap_x, gap_y = 70, 120, 20, 30
    basis = escape(result["banner"])
    chunks = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">',
        f'<title id="title">UNFENCED {escape(result["mode"])} per-fruit V0–V3 response surface</title>',
        '<desc id="desc">Nine small-multiple line charts compare fitting, noticing, and acting rates '
        f'across rule arms V0 through V3, separating attention from initiative. {basis}.</desc>',
        '<rect width="100%" height="100%" fill="#ffffff"/>',
        '<style>text{font-family:ui-sans-serif,system-ui,sans-serif;fill:#172033}'
        '.small{font-size:11px}.label{font-size:13px;font-weight:600}.title{font-size:20px;font-weight:600}'
        '.grid{stroke:#d7dce5;stroke-width:1}.axis{stroke:#7b8494;stroke-width:1.2}'
        '.fit{stroke:#2864dc;fill:none;stroke-width:2.5}.notice{stroke:#d97706;fill:none;stroke-width:2.5}'
        '.action{stroke:#16865b;fill:none;stroke-width:2.5}.fit-dot{fill:#2864dc}'
        '.notice-dot{fill:#d97706}.action-dot{fill:#16865b}</style>',
        '<text x="70" y="42" class="title">UNFENCED P1 — per-fruit rule-arm response surface</text>',
        f'<text x="70" y="66" class="small">{basis}</text>',
        '<line x1="585" y1="58" x2="615" y2="58" class="fit"/><text x="622" y="62" class="small">fit for arm</text>',
        '<line x1="710" y1="58" x2="740" y2="58" class="notice"/><text x="747" y="62" class="small">noticed</text>',
        '<line x1="830" y1="58" x2="860" y2="58" class="action"/><text x="867" y="62" class="small">acted</text>',
    ]
    surface = result["fruit_response_surface"]
    for index, fruit in enumerate(sorted(surface, key=lambda x: int(x[1:]))):
        row, col = divmod(index, 3)
        px, py = x0 + col * (panel_w + gap_x), y0 + row * (panel_h + gap_y)
        left, top, plot_w, plot_h = px + 36, py + 24, panel_w - 52, panel_h - 54
        chunks.append(f'<text x="{px}" y="{py + 12}" class="label">{escape(fruit)}</text>')
        for frac in (0, .5, 1):
            y = top + plot_h * (1 - frac)
            chunks.append(f'<line x1="{left}" y1="{y:.1f}" x2="{left + plot_w}" y2="{y:.1f}" class="grid"/>')
            chunks.append(f'<text x="{left - 7}" y="{y + 4:.1f}" text-anchor="end" class="small">{int(frac*100)}</text>')
        chunks.append(f'<line x1="{left}" y1="{top}" x2="{left}" y2="{top + plot_h}" class="axis"/>')
        chunks.append(f'<line x1="{left}" y1="{top + plot_h}" x2="{left + plot_w}" y2="{top + plot_h}" class="axis"/>')
        xs = [left + i * plot_w / 3 for i in range(4)]
        fit_points, notice_points, action_points = [], [], []
        for arm, x in zip(ARMS, xs):
            fit = surface[fruit][arm]["fit_rate"]
            notice = surface[fruit][arm]["noticing_rate"]
            action = surface[fruit][arm]["acting_rate"]
            fy, ny, ay = (
                top + (1 - fit) * plot_h,
                top + (1 - notice) * plot_h,
                top + (1 - action) * plot_h,
            )
            fit_points.append(f"{x:.1f},{fy:.1f}")
            notice_points.append(f"{x:.1f},{ny:.1f}")
            action_points.append(f"{x:.1f},{ay:.1f}")
            chunks.append(f'<text x="{x:.1f}" y="{top + plot_h + 17}" text-anchor="middle" class="small">{arm}</text>')
            chunks.append(f'<circle cx="{x:.1f}" cy="{fy:.1f}" r="3.2" class="fit-dot"><title>{fruit} {arm} fit {fit:.1%}</title></circle>')
            chunks.append(f'<circle cx="{x:.1f}" cy="{ny:.1f}" r="3.2" class="notice-dot"><title>{fruit} {arm} noticed {notice:.1%}</title></circle>')
            chunks.append(f'<circle cx="{x:.1f}" cy="{ay:.1f}" r="3.2" class="action-dot"><title>{fruit} {arm} acted {action:.1%}</title></circle>')
        chunks.append(f'<polyline points="{" ".join(fit_points)}" class="fit"/>')
        chunks.append(f'<polyline points="{" ".join(notice_points)}" class="notice"/>')
        chunks.append(f'<polyline points="{" ".join(action_points)}" class="action"/>')
    chunks.append('</svg>')
    return "\n".join(chunks) + "\n"
