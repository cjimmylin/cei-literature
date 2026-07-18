#!/usr/bin/env python3
"""Build the WCF-Bench-v2 Session-10 readiness deck: parse the Markdown source
into typed slides and emit ONE self-contained dark+gold HTML file (inline CSS/JS,
no network) plus a Speaker-Notes appendix.

Usage:  python3 20260717-session10-build-deck.py
Reads:  20260717-session10-readiness-deck.md   (same dir)
Writes: 20260717-session10-readiness-deck.html  (same dir)

Deliberately dependency-free (stdlib only) so it runs under system python3 or the
vault .venv without installs. The PDF is produced separately via Chrome headless.
"""
import html
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "20260717-session10-readiness-deck.md"
OUT = HERE / "20260717-session10-readiness-deck.html"


# ---------------------------------------------------------------- inline markdown
def fmt(text: str) -> str:
    """Escape HTML then apply a tiny markdown subset: `code`, **bold**, *italic*."""
    t = html.escape(text, quote=False)
    t = re.sub(r"`([^`]+)`", r"<code>\1</code>", t)
    t = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", t)
    return t


# ---------------------------------------------------------------- parse
def parse(md: str):
    lines = md.splitlines()
    # 1) consume YAML front matter (opening --- ... closing ---)
    meta = {}
    i = 0
    if lines and lines[0].strip() == "---":
        i = 1
        while i < len(lines) and lines[i].strip() != "---":
            m = re.match(r'(\w+):\s*"?(.*?)"?\s*$', lines[i])
            if m:
                meta[m.group(1)] = m.group(2)
            i += 1
        i += 1  # skip closing ---
    body = "\n".join(lines[i:])

    # 2) split remaining body on lines that are exactly ---
    blocks = re.split(r"(?m)^---\s*$", body)
    slides = []
    for b in blocks:
        b = b.strip("\n")
        if not b.strip():
            continue
        slides.append(parse_slide(b))
    return meta, slides


def parse_slide(block: str):
    s = {
        "type": "content", "title": "", "subs": [], "meta": "", "num": "",
        "nq": False, "bullets": [], "stats": [], "bars": [], "table": [],
        "caveats": [], "cta": "", "foot": "", "twocol": {}, "notes": "",
    }
    tbl = []
    for raw in block.splitlines():
        line = raw.rstrip()
        st = line.strip()
        if not st:
            continue
        m = re.match(r"<!--\s*type:\s*(\w+)\s*-->", st)
        if m:
            s["type"] = m.group(1)
            continue
        if st.startswith("# "):
            s["title"] = st[2:].strip(); continue
        if st.startswith("## "):
            s["title"] = st[3:].strip(); continue
        if st == "NQ":
            s["nq"] = True; continue
        if st.startswith("SUB:"):
            s["subs"].append(st[4:].strip()); continue
        if st.startswith("META:"):
            s["meta"] = st[5:].strip(); continue
        if st.startswith("NUM:"):
            s["num"] = st[4:].strip(); continue
        if st.startswith("STAT:"):
            parts = [p.strip() for p in st[5:].split("||")]
            s["stats"].append(parts); continue
        if st.startswith("BAR:"):
            parts = [p.strip() for p in st[4:].split("||")]
            s["bars"].append(parts); continue
        if st.startswith("FOOT:"):
            s["foot"] = st[5:].strip(); continue
        if st.startswith("CAVEAT:"):
            s["caveats"].append(st[7:].strip()); continue
        if st.startswith("CTA:"):
            s["cta"] = st[4:].strip(); continue
        if st.startswith("LEFT:"):
            s["twocol"]["left"] = st[5:].strip(); continue
        if st.startswith("GOOD:"):
            s["twocol"]["good"] = st[5:].strip(); continue
        if st.startswith("BAD:"):
            s["twocol"]["bad"] = st[4:].strip(); continue
        if st.startswith("Notes:"):
            s["notes"] = st[6:].strip(); continue
        if st.startswith("- "):
            s["bullets"].append(st[2:].strip()); continue
        if st.startswith("|"):
            cells = [c.strip() for c in st.strip("|").split("|")]
            tbl.append(cells); continue
        # anything else -> treat as a paragraph bullet
        s["bullets"].append(st)
    # keep the markdown table, dropping the |---| separator row
    s["table"] = [r for r in tbl if not all(re.fullmatch(r"-{2,}|:?-+:?", c) for c in r)]
    return s


# ---------------------------------------------------------------- render helpers
def render_bullets(bullets):
    if not bullets:
        return ""
    items = "\n".join(f"    <li>{fmt(b)}</li>" for b in bullets)
    return f'  <ul class="bul">\n{items}\n  </ul>'


def render_table(rows):
    if not rows:
        return ""
    head = rows[0]
    ths = "".join(f"<th>{fmt(c)}</th>" for c in head)
    trs = []
    for r in rows[1:]:
        tds = "".join(f"<td>{fmt(c)}</td>" for c in r)
        trs.append(f"    <tr>{tds}</tr>")
    body = "\n".join(trs)
    return (f'  <table>\n    <thead><tr>{ths}</tr></thead>\n'
            f'    <tbody>\n{body}\n    </tbody>\n  </table>')


def render_stats(stats):
    cards = []
    for parts in stats:
        n = parts[0] if parts else ""
        label = parts[1] if len(parts) > 1 else ""
        cards.append(f'    <div class="stat"><div class="n">{fmt(n)}</div>'
                     f'<div class="l">{fmt(label)}</div></div>')
    return '  <div class="callouts">\n' + "\n".join(cards) + "\n  </div>"


def render_bars(bars):
    # scale to the max declared base so widths are comparable within the slide
    rows = []
    try:
        base = max(float(b[2]) for b in bars if len(b) > 2)
    except (ValueError, IndexError):
        base = 100.0
    for b in bars:
        label = b[0] if b else ""
        val = b[1] if len(b) > 1 else ""
        flag = b[3] if len(b) > 3 else ""
        try:
            pct = max(3.0, min(100.0, float(val) / base * 100.0))
        except ValueError:
            pct = 3.0
        cls = "sig" if flag.upper() == "SIG" else "ns"
        flag_html = f'<span class="{cls}">{fmt(flag)}</span>' if flag else ""
        rows.append(
            '    <div class="barrow">\n'
            f'      <div class="barlabel">{fmt(label)}</div>\n'
            f'      <div class="bartrack"><div class="bar" style="width:{pct:.1f}%"></div>'
            f'<span class="barval">{fmt(val)}</span></div>\n'
            f'      <div class="barflag">{flag_html}</div>\n'
            '    </div>'
        )
    return '  <div class="chart">\n' + "\n".join(rows) + "\n  </div>"


def render_caveats(caveats):
    if not caveats:
        return ""
    items = "".join(f'<span class="cav">{fmt(c)}</span>' for c in caveats)
    return f'  <div class="caveatstrip">{items}</div>'


# ---------------------------------------------------------------- render slide
def render_slide(s, idx, total):
    t = s["type"]
    nq = '<div class="nq">Exploratory · Non-Quotable</div>' if s["nq"] else ""
    inner = ""

    if t == "title":
        subs = "\n".join(f'<p class="subtitle">{fmt(x)}</p>' for x in s["subs"])
        meta = f'<p class="titlemeta">{fmt(s["meta"])}</p>' if s["meta"] else ""
        inner = (f'  <div class="titlewrap">\n'
                 f'    <h1 class="title">{fmt(s["title"])}</h1>\n'
                 f'    {subs}\n    {meta}\n  </div>')
    elif t == "divider":
        inner = (f'  <div class="dividerwrap">\n'
                 f'    <div class="num">{fmt(s["num"])}</div>\n'
                 f'    <h2 class="secname">{fmt(s["title"])}</h2>\n  </div>')
    elif t == "callout":
        inner = (f'  <h2 class="stitle">{fmt(s["title"])}</h2>\n'
                 f'{render_stats(s["stats"])}')
    elif t == "table":
        inner = (f'  <h2 class="stitle">{fmt(s["title"])}</h2>\n'
                 f'{render_bullets(s["bullets"])}\n{render_table(s["table"])}')
    elif t == "chart":
        foot = f'  <div class="chartfoot">{fmt(s["foot"])}</div>' if s["foot"] else ""
        inner = (f'  <h2 class="stitle">{fmt(s["title"])}</h2>\n'
                 f'{render_bars(s["bars"])}\n{foot}')
    elif t == "twocol":
        tc = s["twocol"]
        inner = (
            f'  <h2 class="stitle">{fmt(s["title"])}</h2>\n'
            f'  <div class="twocol">\n'
            f'    <div class="col colleft"><div class="collabel">The prompt</div>'
            f'<p>{fmt(tc.get("left",""))}</p></div>\n'
            f'    <div class="col colright">\n'
            f'      <div class="panel good"><div class="ptag">GOOD</div>'
            f'<p>{fmt(tc.get("good",""))}</p></div>\n'
            f'      <div class="panel bad"><div class="ptag">BAD</div>'
            f'<p>{fmt(tc.get("bad",""))}</p></div>\n'
            f'    </div>\n  </div>'
        )
    elif t == "closing":
        cta = (f'  <div class="cta">{fmt(s["cta"])}</div>') if s["cta"] else ""
        inner = (f'  <h2 class="stitle">{fmt(s["title"])}</h2>\n'
                 f'{render_bullets(s["bullets"])}\n{cta}')
    else:  # content
        inner = (f'  <h2 class="stitle">{fmt(s["title"])}</h2>\n'
                 f'{render_bullets(s["bullets"])}\n{render_caveats(s["caveats"])}')

    chrome = (
        '  <div class="tab">WCF-BENCH-v2</div>\n'
        f'  {nq}\n'
        '  <div class="foot">internal · non-quotable</div>\n'
        f'  <div class="pg">{idx} / {total}</div>'
    )
    notes = f'  <aside class="notes">{fmt(s["notes"])}</aside>' if s["notes"] else ""
    active = " active" if idx == 1 else ""
    return (f'<section class="slide{active}" data-type="{t}">\n'
            f'{chrome}\n  <div class="body">\n{inner}\n  </div>\n{notes}\n</section>')


def render_notes_appendix(slides):
    rows = []
    for i, s in enumerate(slides, 1):
        if not s["notes"]:
            continue
        title = s["title"] or f"Slide {i}"
        rows.append(f'    <div class="noterow"><span class="notenum">{i}</span>'
                    f'<div><div class="notetitle">{fmt(title)}</div>'
                    f'<p>{fmt(s["notes"])}</p></div></div>')
    return ('<section class="appendix">\n'
            '  <h2 class="stitle">Speaker Notes</h2>\n'
            '  <div class="notelist">\n' + "\n".join(rows) + "\n  </div>\n</section>")


# ---------------------------------------------------------------- CSS + shell
CSS = """
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
:root{
  --bg:#0e1220; --bg-card:#161e30; --bg-raised:#1d2740;
  --gold:#c9a84c; --gold-dim:#8a6e2e;
  --text:#e8ecf5; --text-dim:#9aa3b8; --border:#2a3555;
  --pos:#4ea86b; --amber:#d8a23a; --neg:#c96a5c; --accent:#3a7bd5;
  --serif:"Iowan Old Style","Palatino Linotype",Palatino,Georgia,serif;
  --sans:-apple-system,BlinkMacSystemFont,"Segoe UI","Helvetica Neue",Arial,sans-serif;
  --mono:"SF Mono","Fira Code",Consolas,monospace;
}
html,body{height:100%;background:var(--bg);color:var(--text);font-family:var(--sans);overflow:hidden}
#deck{width:100vw;height:100vh;position:relative;overflow:hidden}
.slide{position:absolute;inset:0;display:flex;flex-direction:column;
  padding:56px 72px 72px;opacity:0;pointer-events:none;transition:opacity .35s ease;overflow:hidden}
.slide.active{opacity:1;pointer-events:all}
.slide::before{content:"";position:absolute;left:0;top:0;bottom:0;width:6px;background:var(--gold)}
.body{position:relative;z-index:1;display:flex;flex-direction:column;flex:1;min-height:0;justify-content:center}
.tab{position:absolute;top:26px;left:32px;font:600 11px/1 var(--sans);letter-spacing:2px;
  text-transform:uppercase;color:var(--gold-dim)}
.nq{position:absolute;top:24px;right:32px;font:600 10px/1 var(--sans);letter-spacing:1.5px;
  color:var(--amber);text-transform:uppercase;border:1px solid var(--gold-dim);
  padding:5px 9px;border-radius:4px}
.foot{position:absolute;left:72px;bottom:26px;color:var(--text-dim);font-size:11px}
.pg{position:absolute;right:32px;bottom:26px;color:var(--text-dim);font-size:11px}

h1.title{font-family:var(--serif);font-size:clamp(30px,4.4vw,58px);color:var(--gold);line-height:1.1}
h2.stitle{font-family:var(--serif);font-size:clamp(22px,2.8vw,34px);color:var(--gold);
  border-bottom:1px solid var(--border);padding-bottom:14px;margin-bottom:26px;flex:0 0 auto}
.titlewrap{margin-top:auto;margin-bottom:auto}
.subtitle{font-size:clamp(15px,1.7vw,21px);color:var(--text);margin-top:16px;max-width:60ch;line-height:1.4}
.titlemeta{margin-top:34px;color:var(--gold-dim);font:600 12px/1 var(--sans);letter-spacing:2px;text-transform:uppercase}

.dividerwrap{display:flex;align-items:center;gap:40px;margin:auto 0}
.dividerwrap .num{font-family:var(--serif);font-size:190px;color:var(--gold-dim);opacity:.55;line-height:.8}
.secname{font-family:var(--serif);font-size:clamp(30px,4vw,52px);color:var(--gold)}

ul.bul{list-style:none;display:flex;flex-direction:column;gap:14px}
ul.bul li{position:relative;padding-left:26px;font-size:clamp(14px,1.5vw,19px);line-height:1.5;color:var(--text)}
ul.bul li::before{content:"\\25B8";position:absolute;left:0;color:var(--gold);font-size:.9em;top:.15em}
ul.bul li strong{color:#fff}

.caveatstrip{display:flex;flex-wrap:wrap;gap:10px;margin-top:26px}
.cav{background:var(--bg-card);border:1px solid var(--gold-dim);border-radius:20px;
  padding:6px 14px;font-size:12px;color:var(--amber)}

.callouts{display:flex;gap:22px;flex-wrap:wrap;align-content:center}
.stat{background:var(--bg-card);border:1px solid var(--border);border-left:3px solid var(--gold);
  border-radius:8px;padding:22px 26px;flex:1 1 40%;min-width:300px}
.stat .n{font-family:var(--serif);font-size:40px;color:var(--gold);line-height:1.05}
.stat .l{color:var(--text-dim);font-size:14px;margin-top:10px;line-height:1.4}

table{border-collapse:collapse;width:100%;font-size:15px}
th,td{border:1px solid var(--border);padding:8px 12px;text-align:left}
th{background:var(--bg-raised);color:var(--gold);font-family:var(--sans);font-weight:600}
td strong{color:#fff}
.sig{color:var(--pos);font-weight:700}
.ns{color:var(--text-dim)}

.chart{display:flex;flex-direction:column;gap:12px}
.barrow{display:grid;grid-template-columns:180px 1fr 120px;align-items:center;gap:16px}
.barlabel{font-size:14px;color:var(--text);text-align:right;font-family:var(--mono)}
.bartrack{position:relative;background:var(--bg-card);border:1px solid var(--border);
  border-radius:4px;height:26px;display:flex;align-items:center}
.bar{height:100%;background:linear-gradient(90deg,var(--gold-dim),var(--gold));border-radius:3px 0 0 3px}
.barval{position:absolute;right:10px;font-size:13px;font-family:var(--mono);color:var(--text)}
.barflag{font-size:12px}
.chartfoot{margin-top:20px;color:var(--text-dim);font-size:12px;font-style:italic}

.twocol{display:grid;grid-template-columns:1fr 1fr;gap:24px;flex:1;min-height:0;align-items:stretch}
.col{background:var(--bg-card);border:1px solid var(--border);border-radius:8px;padding:22px 24px;
  display:flex;flex-direction:column;justify-content:center}
.colleft{border-left:3px solid var(--accent)}
.colright{background:none;border:none;padding:0;gap:16px}
.collabel,.ptag{font:600 11px/1 var(--sans);letter-spacing:2px;text-transform:uppercase;margin-bottom:12px}
.collabel{color:var(--accent)}
.col p,.panel p{font-size:15px;line-height:1.5;color:var(--text)}
.panel{border-radius:8px;padding:18px 22px;flex:1;display:flex;flex-direction:column;justify-content:center}
.panel.good{background:rgba(78,168,107,.10);border:1px solid var(--pos)}
.panel.good .ptag{color:var(--pos)}
.panel.bad{background:rgba(201,106,92,.10);border:1px solid var(--neg)}
.panel.bad .ptag{color:var(--neg)}

.cta{margin-top:30px;background:linear-gradient(90deg,rgba(201,168,76,.15),rgba(201,168,76,.02));
  border:1px solid var(--gold);border-left:4px solid var(--gold);border-radius:8px;
  padding:22px 26px;font-family:var(--serif);font-size:clamp(18px,2.2vw,26px);color:var(--gold)}

aside.notes{display:none}

/* appendix (screen: hidden; print: flows after the deck) */
.appendix{display:none;background:var(--bg);color:var(--text);padding:56px 72px}
.appendix .stitle{margin-bottom:24px}
.noterow{display:flex;gap:18px;padding:14px 0;border-bottom:1px solid var(--border)}
.notenum{font-family:var(--serif);font-size:26px;color:var(--gold-dim);min-width:40px}
.notetitle{color:var(--gold);font-weight:600;margin-bottom:4px}
.noterow p{color:var(--text-dim);font-size:14px;line-height:1.5}

/* nav hint */
.navhint{position:fixed;bottom:14px;left:50%;transform:translateX(-50%);color:var(--text-dim);
  font-size:11px;opacity:.5;z-index:50}

/* ── PRINT: load-bearing — one slide per page ─────────────────────────── */
body.print{overflow:visible}
body.print #deck{height:auto;overflow:visible}
body.print .slide{position:relative;inset:auto;opacity:1 !important;pointer-events:all;
  page-break-after:always;height:720px;width:1280px;transition:none;overflow:hidden}
body.print .navhint{display:none}
body.print .appendix{display:block;page-break-before:always}
@page{size:1280px 720px;margin:0}
"""

JS = """
(function(){
  var slides = Array.prototype.slice.call(document.querySelectorAll('#deck .slide'));
  var i = 0;
  function show(n){
    i = Math.max(0, Math.min(slides.length-1, n));
    slides.forEach(function(s,k){ s.classList.toggle('active', k===i); });
  }
  function isPrint(){ return document.body.classList.contains('print'); }
  document.addEventListener('keydown', function(e){
    if(isPrint()) return;
    if(e.key==='ArrowRight'||e.key==='PageDown'||e.key===' '){ show(i+1); e.preventDefault(); }
    else if(e.key==='ArrowLeft'||e.key==='PageUp'){ show(i-1); e.preventDefault(); }
    else if(e.key==='Home'){ show(0); }
    else if(e.key==='End'){ show(slides.length-1); }
  });
  document.getElementById('deck').addEventListener('click', function(e){
    if(isPrint()) return;
    var mid = window.innerWidth/2;
    show(e.clientX < mid ? i-1 : i+1);
  });
  if(!isPrint()) show(0);
})();
"""


def build():
    md = SRC.read_text(encoding="utf-8")
    meta, slides = parse(md)
    total = len(slides)
    slide_html = "\n".join(render_slide(s, idx, total) for idx, s in enumerate(slides, 1))
    appendix = render_notes_appendix(slides)
    title = meta.get("title", "WCF-Bench-v2 Readiness Deck")

    doc = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=1280, initial-scale=1">
<title>{html.escape(title)}</title>
<style>{CSS}</style>
</head>
<body>
<div id="deck">
{slide_html}
</div>
<div class="navhint">← / → or click to navigate · {total} slides · add ?print for PDF layout</div>
{appendix}
<script>
  // reveal all slides for printing when ?print is present (read by Chrome headless)
  if(location.search.indexOf('print')!==-1){{ document.documentElement.classList.add('willprint'); }}
  document.addEventListener('DOMContentLoaded', function(){{
    if(location.search.indexOf('print')!==-1){{ document.body.classList.add('print'); }}
  }});
{JS}
</script>
</body>
</html>
"""
    OUT.write_text(doc, encoding="utf-8")
    print(f"[build] {total} slides -> {OUT.name} ({len(doc):,} bytes)")
    return total


if __name__ == "__main__":
    build()
