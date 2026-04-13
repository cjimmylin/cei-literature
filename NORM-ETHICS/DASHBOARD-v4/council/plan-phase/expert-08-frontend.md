# Expert 08 — Web Frontend / ECharts Review

**Role:** Frontend performance, theme robustness, mobile UX, safety  
**Scope:** v2 codebase (`app.js`, `charts.js`, `style.css`, `index.html`) + v4 CONTRACT.md  
**Date:** 2026-04-13

---

## (a) Performance

**Heatmap cell counts (v2 baseline):**
- Feature Matrix heatmap: 54 rows x 9 columns = 486 cells. Well under the 8K threshold.
- Tradition heatmap: 54 rows x 5 traditions = 270 cells.
- Cross-Vendor agreement heatmap: 9 x 9 = 81 cells.

**Verdict: No chart in v2 approaches the 8K cell threshold requiring `large: true`.** However, v4 adds 11 tabs (up from 10) and the contract mentions 54 benchmarks with 41 features. If the v4 feature matrix expands to 54 x 41 = 2,214 cells, this is still safe. The only risk would be a per-item heatmap across all 9 models x 54 benchmarks x 41 features (roughly 20K cells) -- if such a chart is planned for cross-vendor analysis, `large: true` must be added. **Recommendation:** Add a defensive check in `charts.js` -- if any heatmap dataset exceeds 5,000 data points, set `large: true` and `largeThreshold: 5000` on the series.

**Lazy rendering:** v2 already implements lazy tab rendering correctly via the `rendered` flags in `setupTabListeners()`. Each tab's charts are only initialized on first `shown.bs.tab` event. The v4 contract adds tab-0 (`tab-guide`) which contains no charts, so no change needed. **One gap:** the `rendered` object is local to `setupTabListeners()` and never reset. If the theme toggle disposes and re-creates chart instances, the `rendered` flags will prevent re-initialization. This must be addressed in v4 (see section b).

---

## (b) Theme Toggle Robustness

**Critical finding: v2 has NO theme toggle at all.** There is no `data-theme` attribute handling, no localStorage read/write, no light theme CSS variables, and no version counter pattern. The v2 CSS only defines dark-mode `:root` variables. The `baseTheme()` function in `charts.js` hardcodes dark colors (`#1c1f2e`, `#2a2d42`, etc.) directly into every chart option.

**What v4 must build from scratch:**

1. **Light-theme CSS variables.** Add `[data-theme="light"]` block overriding all `--bg-*`, `--text-*`, `--border-*` custom properties.

2. **ECharts re-render on toggle.** The version counter pattern (per project memory) requires:
   - A global `themeVersion` counter incremented on every toggle.
   - Each chart render function captures `themeVersion` at invocation start.
   - After async work (setTimeout), compare captured version to current -- if mismatched, abort (a newer render is in flight).
   - `getChart()` must `dispose()` the old instance and `init()` a new one, because ECharts does not support runtime background color changes through `setOption` alone.

3. **`rendered` flags must be reset on toggle.** Otherwise lazy-rendered tabs will show stale dark-themed charts on the light theme. The simplest pattern: on toggle, iterate `chartInstances`, call `dispose()` on each, clear the object, reset all `rendered` flags to false, then re-render the currently active tab.

4. **Non-ECharts elements.** The hardcoded hex colors in `baseTheme()` tooltip background (`#1c1f2e`) and border (`#2a2d42`) must be replaced with CSS variable references or dynamically read from computed styles at render time.

**Risk:** This is the highest-effort item in the v4 migration. Hardcoded colors appear in approximately 30 locations across `charts.js`. A `getThemeColors()` helper that reads `getComputedStyle(document.documentElement)` would centralize this.

---

## (c) Mobile Responsiveness

**Current state (v2):**
- Single `@media (max-width: 768px)` breakpoint reduces padding and metric-value font size. This is minimal.
- Tab bar has `overflow-x: auto` with gradient fade indicators -- good for horizontal scrolling on small screens.
- Chart containers use `min-height: 400px` (300px for small, 550px for large) with `width: 100%` -- charts will fill container width.
- `window.addEventListener('resize', ...)` calls `c.resize()` on all chart instances -- this handles orientation changes.

**Gaps for v4:**
- **No breakpoint below 480px.** On phones in portrait, 400px min-height charts are taller than the viewport. Add `@media (max-width: 480px)` reducing `.echarts-box` to `min-height: 280px` and `.echarts-box-lg` to `min-height: 400px`.
- **No touch-specific interaction.** ECharts handles pinch-zoom natively on touch devices for dataZoom-enabled charts, but none of the v2 charts enable `dataZoom`. The feature matrix heatmap (and its v4 expansion to 41 columns) would benefit from `dataZoom: [{ type: 'inside' }, { type: 'slider', orient: 'horizontal' }]` for horizontal scrolling on mobile.
- **Table overflow.** The papers table (12 columns) uses `overflow-x: auto` on its wrapper -- adequate but should add `-webkit-overflow-scrolling: touch` for momentum scrolling on iOS.
- **Orientation change.** The `resize` event listener is present and works. However, on iOS Safari, `resize` may not fire on orientation change until the animation completes. Adding a secondary `orientationchange` listener with a 300ms debounce would be more robust.

---

## (d) localStorage Safety

**v2 has zero localStorage usage.** The v4 contract introduces `localStorage.getItem('normeval-theme')`.

**Required safety measures for v4:**

1. **Wrap in try/catch.** In private browsing (Safari) or when storage is full, `localStorage.getItem()` can throw. Pattern:
   ```js
   function getSavedTheme() {
     try { return localStorage.getItem('normeval-theme'); }
     catch (e) { return null; }
   }
   ```

2. **Value validation.** The contract specifies: if value is exactly `"light"`, apply light theme; otherwise use dark. This is correct -- it gracefully handles `null`, `"dark"`, `"undefined"`, corrupted JSON, or any garbage string by defaulting to dark.

3. **Write safety.** `localStorage.setItem()` can throw `QuotaExceededError`. Wrap the write in try/catch as well. A failure should not block the toggle -- the theme still applies to the current session via the DOM attribute.

4. **No sensitive data.** Theme preference is the only stored value. No privacy concerns.

---

## (e) Script Loading Race Conditions

**v2 load order (from index.html):**
```html
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/echarts@5.4.3/dist/echarts.min.js"></script>
<script src="data.js"></script>
<script src="charts.js"></script>
<script src="app.js"></script>
```

All scripts are synchronous (no `async` or `defer`). Execution order is guaranteed by the HTML spec. `data.js` defines `const DATA_*` globals, `charts.js` defines functions referencing them, and `app.js` calls those functions inside `DOMContentLoaded`. **No race condition exists in this pattern.**

**v4 adds `data_cross_vendor.js`** between `data.js` and `charts.js` per the contract. This is safe as long as it remains a synchronous `<script>` tag.

**Potential v4 risks:**
- The contract states constants attach to `window` scope "implicitly via `const` at top-level in classic scripts." This is **incorrect** -- `const` does NOT attach to `window` in any script mode. The variables are in the global scope but not properties of `window`. The contract's own workaround (`typeof DATA !== 'undefined'`) is correct, but if any code uses `window.DATA`, it will fail. **Audit all references** to ensure no `window.` prefix is used.
- If SRI hashes are wrong for CDN resources, Bootstrap and ECharts will fail to load, causing `ReferenceError: echarts is not defined`. Add a guard: `if (typeof echarts === 'undefined') { /* show fallback message */ }` at the top of `charts.js`.
- The `DOMContentLoaded` listener in `app.js` fires only after all synchronous scripts execute, so data is guaranteed available. No issues here.

---

## Summary of v4 Priorities

| Priority | Issue | Effort |
|----------|-------|--------|
| P0 | Theme toggle: build from scratch, dispose/re-init all ECharts instances, reset lazy flags | High |
| P1 | Replace ~30 hardcoded hex colors in charts.js with dynamic theme-aware helper | Medium |
| P1 | Audit all `window.DATA_*` references -- use bare names or `typeof` checks | Low |
| P2 | Mobile breakpoint at 480px, touch dataZoom for wide heatmaps | Low |
| P2 | localStorage try/catch wrappers | Low |
| P3 | Orientation change listener with debounce | Low |
| P3 | Defensive `large: true` for heatmaps exceeding 5K cells | Low |
