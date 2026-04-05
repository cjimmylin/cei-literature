# Moral Psychology Dashboard v2 — Bug Fix Spec

**Date:** 2026-04-05
**Scope:** Address 4 known issues from Session 15 handoff (dashboard code fixes + data transparency UX)

---

## Fix 1: Theme Re-render on Inactive Tabs

**Problem:** Toggling light/dark theme only re-renders charts on the active tab. Inactive tabs show stale-themed charts until the user switches tabs and back.

**Solution:** Version-counter pattern in ThemeManager.

- Add `_version: 0` and `_paneVersions: {}` to ThemeManager
- `toggle()` increments `_version`; `_refreshCharts()` records active pane's version
- `initCharts(paneId)` already runs on `shown.bs.tab` — after it runs, record `_paneVersions[paneId] = ThemeManager._version`
- On tab show, charts are always disposed+recreated (existing behavior), so they automatically pick up current theme. The version tracking ensures this happens even if the tab was previously rendered with a stale theme.

**Files:** `app.js` (~10 lines changed)

---

## Fix 2: Print Improvements

**Problem:** Print stylesheet dumps all 12+ tabs sequentially (30+ pages). No print button exists. `data-print-date` attribute is never set.

**Solution:** Print button with current-tab/all-tabs modes.

**HTML:** Add dropdown button to navbar (next to theme toggle):
```html
<div class="dropdown d-inline-block ms-2">
  <button class="btn btn-sm btn-outline-secondary dropdown-toggle" data-bs-toggle="dropdown">
    Print
  </button>
  <ul class="dropdown-menu dropdown-menu-end">
    <li><a class="dropdown-item" href="#" id="print-current">Print Current Tab</a></li>
    <li><a class="dropdown-item" href="#" id="print-all">Print All Tabs</a></li>
  </ul>
</div>
```

**JS:** 
- `#print-current`: set `body.dataset.printMode = 'current'`, add `.print-target` to active `.tab-pane`, set `body.dataset.printDate`, call `window.print()`
- `#print-all`: set `body.dataset.printMode = 'all'`, set `body.dataset.printDate`, call `window.print()`
- `window.addEventListener('afterprint', cleanup)` — remove `.print-target`, delete `data-print-mode`

**CSS:**
- Add `@page { margin: 1.5cm; }`
- Add `body[data-print-mode="current"] .tab-pane:not(.print-target) { display: none !important; }`
- Existing "show all panes" rules apply when `data-print-mode="all"` (default print behavior)

**Files:** `index.html` (~8 lines), `app.js` (~30 lines), `style.css` (~10 lines)

---

## Fix 3: Gemini Cloned Data Transparency

**Problem:** 21/23 Gemini benchmarks are Opus clones. Provenance badges exist but no explanatory context.

**Solution:** Add an alert callout at the top of Tab 9 (Cross-Vendor Analysis tab).

**Content:** Warning-styled alert explaining:
- 21/23 Gemini benchmarks reflect Opus values (not independently administered)
- Only MP4 (MF Vignettes) and MP9 (MFTC) have real Gemini data
- Independent Gemini API trials are needed to validate cross-vendor claims
- Existing provenance badges in the trial table flag affected rows

**Files:** `index.html` (~8 lines), `style.css` (~5 lines for theme-aware alert styling)

---

## Fix 4: MFQ Radar + Moral Machine Opus-Only Context

**Problem:** Two charts only have Opus data but the "(Opus only)" label doesn't explain why.

**Solution:** Add info callouts directly above each chart container.

**Content:** Brief methodological note explaining these benchmarks produce rich multi-dimensional data (15 MFT foundation scores, 9 dimension preference rates) that was only collected for the initial Opus trial. Extending requires dedicated per-model trial administration.

**Files:** `index.html` (~8 lines), shared callout CSS from Fix 3

---

## Out of Scope

- Running actual Gemini trials (deferred)
- Running MFQ/Moral Machine trials for non-Opus models (deferred)
- Data splitting of data.js (deferred — gzip makes effective transfer ~800KB)
- LaTeX conversion

---

*Spec filed: 2026-04-05*
