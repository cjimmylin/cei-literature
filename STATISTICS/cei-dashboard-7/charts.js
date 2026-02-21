/**
 * CEI Dashboard v7 — Charts Module (v6.1 Extensibility Refactor)
 * All ECharts initialization, update, and cross-filter wiring.
 *
 * Phase 2: _tabRegistry — declarative tab init/update, no switch statement.
 * Phase 3: _debug audit — localhost console warnings for missing containers.
 * Phase 4: _palette — single color source, _colors/_vtColors derived.
 * Phase 5: _deepDiveSubSection — unified method replaces 3 near-identical clones.
 */

const Charts = {
    _instances: {},
    _subFilter: {},
    _initialized: new Set(),
    _applyFns: {},

    // ═══════════════════════════════════════════════════════════════════════
    // Phase 3: Debug audit — localhost-only logging for chart container mismatches
    // ═══════════════════════════════════════════════════════════════════════

    _debug: location.hostname === 'localhost' || location.hostname === '127.0.0.1',

    _get(id) {
        if (this._instances[id]) return this._instances[id];
        const el = document.getElementById(id);
        if (!el) {
            if (this._debug) console.warn(`[Charts] Missing container: #${id}`);
            return null;
        }
        const chart = echarts.init(el, null, { renderer: 'canvas' });
        this._instances[id] = chart;
        // Auto ARIA: set role and label from parent h3
        el.setAttribute('role', 'img');
        const h3 = el.closest('.chart-card')?.querySelector('h3');
        if (h3) el.setAttribute('aria-label', h3.textContent + ' chart');
        // v7: Inject chart export button
        this._injectExportBtn(el, chart, h3 ? h3.textContent : id);
        return chart;
    },

    /** Console utility: audit HTML containers vs JS-initialized charts */
    auditContainers() {
        const htmlIds = new Set([...document.querySelectorAll('.chart-container')].map(el => el.id).filter(Boolean));
        const jsIds = new Set(Object.keys(this._instances));
        const unused = [...htmlIds].filter(id => !jsIds.has(id));
        const missing = [...jsIds].filter(id => !htmlIds.has(id));
        if (unused.length) console.warn('[Charts] HTML containers never initialized:', unused);
        if (missing.length) console.warn('[Charts] JS referenced but missing from HTML:', missing);
        else console.log(`[Charts] All ${jsIds.size} containers matched.`);
    },

    resizeAll() {
        requestAnimationFrame(() => {
            const activePane = document.querySelector('.tab-pane.active');
            if (!activePane) return;
            Object.entries(this._instances).forEach(([id, c]) => {
                const el = document.getElementById(id);
                if (c && el && activePane.contains(el) && el.offsetParent !== null) c.resize();
            });
        });
    },

    // Theme colors resolved from CSS custom properties (updated on theme toggle)
    _tc: null,

    _resolveThemeColors() {
        const s = getComputedStyle(document.body);
        const g = (v) => s.getPropertyValue(v).trim();
        this._tc = {
            textSec: g('--text-secondary') || '#94a3b8',
            textPri: g('--text-primary') || '#f1f5f9',
            bgCard: g('--bg-card') || '#1e293b',
            border: g('--border') || '#334155',
            bgPrimary: g('--bg-primary') || '#0f172a',
            textMuted: g('--text-muted') || '#64748b',
        };
        this._theme = {
            textStyle: { color: this._tc.textSec },
            title: { textStyle: { color: this._tc.textPri, fontSize: 14 } },
            legend: { textStyle: { color: this._tc.textSec }, pageTextStyle: { color: this._tc.textSec } },
            tooltip: {
                backgroundColor: this._tc.bgCard, borderColor: this._tc.border,
                textStyle: { color: this._tc.textPri, fontSize: 12 },
            },
        };
        // Re-render all active charts with new theme colors
        for (const [id, chart] of Object.entries(this._instances)) {
            const el = document.getElementById(id);
            if (el && el.offsetParent !== null) chart.resize();
        }
    },

    _theme: {
        textStyle: { color: '#94a3b8' },
        title: { textStyle: { color: '#f1f5f9', fontSize: 14 } },
        legend: { textStyle: { color: '#94a3b8' }, pageTextStyle: { color: '#94a3b8' } },
        tooltip: {
            backgroundColor: '#1e293b', borderColor: '#334155',
            textStyle: { color: '#f1f5f9', fontSize: 12 },
        },
    },

    // ═══════════════════════════════════════════════════════════════════════
    // Phase 4: Centralized color palette
    // Contract: when changing a color, update _palette AND the matching CSS
    //           custom property in style.css (see :root comments).
    // ═══════════════════════════════════════════════════════════════════════

    _palette: {
        accent: '#6366f1',  // --accent / indigo
        green: '#22c55e',   // --green
        yellow: '#f59e0b',  // --yellow
        pink: '#ec4899',    // --pink
        cyan: '#22d3ee',    // --cyan
        orange: '#f97316',  // --orange
        violet: '#a855f7',  // --violet (approx)
        teal: '#14b8a6',    // --teal
        red: '#ef4444',     // --red
        lime: '#84cc16',
        slate: '#64748b',   // --slate / --text-muted
        zinc: '#71717a',    // --zinc
        emerald: '#10b981', // --emerald
        sky: '#38bdf8',     // --sky
    },

    // Derived arrays — set by _initPalette() on first use
    _colors: null,
    _vtColors: null,

    _initPalette() {
        const p = this._palette;
        this._colors = [p.accent, p.green, p.yellow, p.pink, p.cyan, p.orange, p.violet, p.teal, p.red, p.lime];
        this._vtColors = {
            'Conference': p.accent, 'Preprint': p.zinc, 'Journal': p.emerald,
            'Findings': p.cyan, 'Workshop': p.orange, 'N/A': p.slate,
        };
        this._resolveThemeColors();
    },

    // ═══════════════════════════════════════════════════════════════════════
    // CHART FACTORIES — 7 parameterized builders replace ~55 methods
    // ═══════════════════════════════════════════════════════════════════════

    _horizontalBar(id, items, opts = {}) {
        const chart = this._get(id);
        if (!chart) return chart;
        const d = (items || []).slice(0, opts.maxItems || 30);
        if (!d.length) {
            chart.setOption({ ...this._theme, graphic: { type: 'text', left: 'center', top: 'center', style: { text: opts.emptyText || 'No data', fill: '#64748b' } } }, true);
            return chart;
        }
        const color = opts.color || this._palette.accent;
        const colorFn = opts.colorFn;
        chart.setOption({
            ...this._theme,
            grid: { left: opts.gridLeft || 130, right: opts.gridRight || 30, top: 10, bottom: 20 },
            xAxis: { type: 'value', axisLabel: { color: this._tc.textSec }, splitLine: { lineStyle: { color: this._tc.bgPrimary } } },
            yAxis: { type: 'category', data: d.map(x => x.n).reverse(), axisLabel: { color: this._tc.textSec, fontSize: opts.fontSize || 11, width: opts.labelWidth || (opts.gridLeft ? opts.gridLeft - 10 : 120), overflow: 'truncate' } },
            tooltip: { ...this._theme.tooltip, trigger: 'axis', ...(opts.tooltipFmt ? { formatter: opts.tooltipFmt } : {}) },
            series: [{
                type: 'bar',
                data: d.map(x => ({
                    value: x.c,
                    itemStyle: { color: colorFn ? colorFn(x) : color, borderRadius: [0,4,4,0] },
                })).reverse(),
                ...(opts.barMaxWidth ? { barMaxWidth: opts.barMaxWidth } : {}),
                ...(opts.label ? { label: opts.label } : {}),
            }],
        }, true);
        if (opts.onClick) {
            chart.off('click');
            chart.on('click', opts.onClick);
        }
        return chart;
    },

    _donut(id, data, opts = {}) {
        const chart = this._get(id);
        if (!chart) return chart;
        chart.setOption({
            ...this._theme,
            ...(opts.useColors ? { color: this._colors } : {}),
            tooltip: { ...this._theme.tooltip, trigger: 'item', formatter: '{b}: {c} ({d}%)' },
            series: [{
                type: 'pie', radius: opts.radius || ['40%', '70%'], center: ['50%', '50%'],
                data, label: { color: this._tc.textSec, fontSize: opts.fontSize || 12 },
                emphasis: { label: { show: true, fontSize: 14, fontWeight: 'bold' } },
            }],
        }, true);
        if (opts.onClick) {
            chart.off('click');
            chart.on('click', opts.onClick);
        }
        return chart;
    },

    _heatmap(id, config) {
        const chart = this._get(id);
        if (!chart) return chart;
        const hmData = [];
        let maxVal = 0;
        (config.matrix || []).forEach((row, i) => {
            row.forEach((val, j) => {
                hmData.push([j, i, val || '-']);
                if (val > maxVal) maxVal = val;
            });
        });
        chart.setOption({
            ...this._theme,
            grid: config.grid || { left: 120, right: 60, top: 40, bottom: 80 },
            xAxis: { type: 'category', data: config.xLabels, axisLabel: { color: this._tc.textSec, fontSize: config.xFontSize || 10, rotate: config.xRotate || 0 }, ...(config.xPos ? { position: config.xPos } : {}), splitArea: config.splitArea || undefined },
            yAxis: { type: 'category', data: config.yLabels, inverse: !!config.yInverse, axisLabel: { color: this._tc.textSec, fontSize: config.yFontSize || 10, width: config.yLabelWidth || undefined, overflow: config.yLabelWidth ? 'truncate' : undefined } },
            tooltip: { ...this._theme.tooltip, ...(config.tooltipFmt ? { formatter: config.tooltipFmt } : {}) },
            visualMap: { min: 0, max: Math.max(maxVal, 1), calculable: !!config.calculable, orient: 'vertical', right: 10, top: config.vmTop || undefined, inRange: { color: [this._tc.bgCard, config.vmColor || this._palette.accent] }, textStyle: { color: this._tc.textSec } },
            series: [{
                type: 'heatmap', data: hmData,
                label: { show: true, color: this._tc.textPri, fontSize: config.labelFontSize || 10, formatter: p => p.value[2] === '-' ? '' : p.value[2] },
            }],
        }, true);
        if (config.onClick) {
            chart.off('click');
            chart.on('click', config.onClick);
        }
        return chart;
    },

    _radar(id, config) {
        const chart = this._get(id);
        if (!chart || !config.indicators || !config.indicators.length) return chart;
        const maxVal = config.maxVal || Math.max(...config.indicators.map(i => i.max || 0), 1);
        const indicators = config.indicators.map(i => ({ name: i.name, max: i.max || maxVal }));
        chart.setOption({
            ...this._theme,
            ...(config.series.length > 1 ? { legend: { ...this._theme.legend, top: 0 } } : {}),
            radar: {
                triggerEvent: !!config.triggerEvent,
                indicator: indicators,
                axisName: { color: this._tc.textSec, fontSize: 10 },
                splitLine: { lineStyle: { color: this._tc.border } },
                splitArea: { areaStyle: { color: config.splitAreaColors || ['transparent'] } },
                axisLine: config.showAxisLine ? { lineStyle: { color: this._tc.border } } : undefined,
            },
            series: [{
                type: 'radar',
                data: config.series.map(s => ({
                    value: s.values, name: s.name,
                    areaStyle: { color: s.areaColor || s.color.replace(')', ',0.3)').replace('rgb', 'rgba') },
                    lineStyle: { color: s.color }, itemStyle: { color: s.color },
                })),
                lineStyle: config.series.length === 1 ? { color: config.series[0].color } : undefined,
                itemStyle: config.series.length === 1 ? { color: config.series[0].color } : undefined,
            }],
        }, true);
        return chart;
    },

    _stackedTimeline(id, config) {
        const chart = this._get(id);
        if (!chart) return chart;
        chart.setOption({
            ...this._theme,
            grid: { left: 50, right: 20, top: 40, bottom: 40 },
            legend: { ...this._theme.legend, top: 0, ...(config.legendType ? { type: config.legendType } : {}), data: config.series.map(s => s.name) },
            xAxis: { type: 'category', data: (config.years || []).map(String), axisLabel: { color: this._tc.textSec } },
            yAxis: { type: 'value', ...(config.yMax ? { max: config.yMax } : {}), axisLabel: { color: this._tc.textSec, ...(config.yFmt ? { formatter: config.yFmt } : {}) }, splitLine: { lineStyle: { color: this._tc.bgPrimary } } },
            tooltip: { ...this._theme.tooltip, trigger: 'axis', ...(config.tooltipFmt ? { formatter: config.tooltipFmt } : {}) },
            series: config.series.map(s => ({
                name: s.name, type: s.type || 'line', data: s.data || [], smooth: s.smooth !== false,
                stack: s.stack || undefined,
                lineStyle: s.type !== 'bar' ? { color: s.color, width: s.width || 2 } : undefined,
                itemStyle: { color: s.color },
                areaStyle: s.areaStyle || undefined,
            })),
        }, true);
        return chart;
    },

    _groupedBar(id, config) {
        const chart = this._get(id);
        if (!chart || !config.categories || !config.categories.length) return chart;
        chart.setOption({
            ...this._theme,
            grid: { left: config.gridLeft || 80, right: 20, top: 40, bottom: 40 },
            legend: { ...this._theme.legend, top: 0 },
            xAxis: { type: 'category', data: config.categories, axisLabel: { color: this._tc.textSec, rotate: config.xRotate || 0, fontSize: 10 } },
            yAxis: { type: 'value', axisLabel: { color: this._tc.textSec }, splitLine: { lineStyle: { color: this._tc.bgPrimary } } },
            tooltip: { ...this._theme.tooltip, trigger: 'axis', ...(config.axisPointer ? { axisPointer: config.axisPointer } : {}) },
            series: config.series.map(s => ({
                name: s.name, type: 'bar', data: s.data,
                stack: config.stack || undefined,
                itemStyle: { color: s.color, borderRadius: config.stack ? undefined : [4,4,0,0] },
            })),
        }, true);
        return chart;
    },

    _treemap(id, data, opts = {}) {
        const chart = this._get(id);
        if (!chart || !data || !data.length) return chart;
        chart.setOption({
            ...this._theme,
            ...(opts.useColors ? { color: this._colors } : {}),
            tooltip: { ...this._theme.tooltip, ...(opts.tooltipFmt ? { formatter: opts.tooltipFmt } : {}) },
            series: [{
                type: 'treemap', data, roam: false,
                label: { show: true, color: '#fff', fontSize: 11 },
                breadcrumb: { show: false },
                itemStyle: { borderColor: this._tc.bgPrimary, borderWidth: 2 },
                levels: opts.levels || [
                    { itemStyle: { borderColor: this._tc.bgPrimary, borderWidth: 2 } },
                    { colorSaturation: [0.3, 0.7], itemStyle: { borderColor: this._tc.bgPrimary, borderWidth: 1 } },
                ],
            }],
        }, true);
        if (opts.onClick) {
            chart.off('click');
            chart.on('click', opts.onClick);
        }
        return chart;
    },

    // ═══════════════════════════════════════════════════════════════════════
    // Phase 2: Tab Initialization Registry
    // Adding a tab = 1 registry entry + init method + HTML.
    // Making a tab filter-reactive = add `update` key.
    // ═══════════════════════════════════════════════════════════════════════

    _tabRegistry: {
        overview:   { init: '_initOverview',   update: '_updateOverview' },
        conference: { init: '_initConference' },
        taxonomy:   { init: '_initTaxonomy' },
        cultural:   { init: '_initCultural' },
        normative:  { init: '_initNormative' },
        moralpsych: { init: '_initMoralPsych' },
        religious:  { init: '_initReligious' },
        models:     { init: '_initModels' },
        intersections: { init: '_initIntersections' },
    },

    initTab(tabId) {
        if (!this._colors) this._initPalette(); // one-time palette setup
        if (this._initialized.has(tabId)) return;
        this._initialized.add(tabId);
        const reg = this._tabRegistry[tabId];
        if (!reg) {
            if (this._debug) console.warn(`[Charts] No registry entry for tab: ${tabId}`);
            return;
        }
        this[reg.init](FilterState.getFilteredPapers());
        if (reg.update) {
            FilterState.subscribe(filtered => {
                if (this._initialized.has(tabId)) this[reg.update](filtered);
            });
        }
    },

    // ═══════════════════════════════════════════════════════════════════════
    // TAB 1: OVERVIEW
    // ═══════════════════════════════════════════════════════════════════════

    _initOverview(papers) {
        const D = DATA;
        document.getElementById('kpi-papers').textContent = fmt(D.agg.total);
        document.getElementById('kpi-candidates').textContent = fmt(D.agg.candidates);
        document.getElementById('kpi-ethics').textContent = fmt(D.agg.ethicsYes);
        document.getElementById('kpi-venues').textContent = fmt(D.conf.uniqueVenues);
        document.getElementById('kpi-authors').textContent = fmt(D.agg.authorCount);
        document.getElementById('kpi-llm').textContent = fmt(D.agg.llmAssessed);
        this._chartTimeline(papers);
        this._chartVenueDonut(papers);
        this._horizontalBar('chart-category-bar', DATA.taxonomy.categories.slice(0, 10), { gridLeft: 220, labelWidth: 200, color: this._palette.accent });
        this._horizontalBar('chart-top-authors', DATA.agg.topAuthors.slice(0, 15), { gridLeft: 150, labelWidth: 140, color: this._palette.green });
        // Availability donut
        const av = DATA.agg.availability;
        const avData = Object.entries(av).filter(([,v]) => v > 0).map(([n, v]) => ({ name: n, value: v }));
        this._donut('chart-availability', avData, { useColors: true, radius: ['35%', '65%'] });
    },

    _updateOverview(papers) {
        this._chartTimeline(papers);
        this._chartVenueDonut(papers);
    },

    _chartTimeline(papers) {
        const chart = this._get('chart-timeline');
        if (!chart) return;
        const yearCount = {};
        papers.forEach(p => { if (p.y > 0) yearCount[p.y] = (yearCount[p.y]||0) + 1; });
        const years = Object.keys(yearCount).sort();
        chart.setOption({
            ...this._theme, color: this._colors,
            grid: { left: 50, right: 20, top: 30, bottom: 40 },
            xAxis: { type: 'category', data: years, axisLabel: { color: this._tc.textSec }, axisLine: { lineStyle: { color: this._tc.border } } },
            yAxis: { type: 'value', axisLabel: { color: this._tc.textSec }, splitLine: { lineStyle: { color: this._tc.bgPrimary } } },
            tooltip: { ...this._theme.tooltip, trigger: 'axis' },
            series: [{ type: 'bar', data: years.map(y => yearCount[y]), itemStyle: { color: this._palette.accent, borderRadius: [4,4,0,0] }, emphasis: { itemStyle: { color: '#818cf8' } } }],
        }, true);
        chart.off('click');
        chart.on('click', p => { if (p.name) FilterState.toggle('year', +p.name); });
        // v7: Add YoY growth labels
        this._timelineYoYLabels(chart, yearCount, years);
    },

    _chartVenueDonut(papers) {
        const vtCount = {};
        papers.forEach(p => { vtCount[p.vt] = (vtCount[p.vt]||0) + 1; });
        const data = Object.entries(vtCount).map(([n, v]) => ({ name: n, value: v, itemStyle: { color: this._vtColors[n] || this._palette.slate } }));
        this._donut('chart-venue-donut', data, { onClick: p => { if (p.name) FilterState.toggle('venueType', p.name); } });
    },

    // ═══════════════════════════════════════════════════════════════════════
    // TAB 3: CONFERENCE & VENUE
    // ═══════════════════════════════════════════════════════════════════════

    _initConference() {
        const C = DATA.conf;
        const vt = DATA.agg.vtDist || {};
        document.getElementById('kpi-conf-venues').textContent = fmt(C.uniqueVenues);
        document.getElementById('kpi-conf-conf').textContent = fmt(vt.Conference || 0);
        document.getElementById('kpi-conf-peer').textContent = fmt((vt.Conference||0) + (vt.Journal||0) + (vt.Findings||0) + (vt.Workshop||0));
        document.getElementById('kpi-conf-preprint').textContent = fmt(vt.Preprint || 0);

        // Venue type donut
        const vtData = Object.entries(vt).map(([n, v]) => ({ name: n, value: v, itemStyle: { color: this._vtColors[n] || this._palette.slate } }));
        this._donut('chart-conf-donut', vtData, { onClick: p => { if (p.name) FilterState.toggle('venueType', p.name); } });

        // Top 30 venues
        this._horizontalBar('chart-conf-top30', C.topVenues, {
            maxItems: 30, gridLeft: 200, labelWidth: 190, fontSize: 10, barMaxWidth: 20,
            colorFn: x => this._vtColors[x.vt] || this._palette.accent,
            onClick: p => { if (p.name) FilterState.toggle('venue', p.name); },
        });

        // Conference family treemap
        const ecoColors = { 'NLP/CL': this._palette.accent, 'ML/AI': this._palette.green, 'AI Ethics': this._palette.yellow, 'Other': this._palette.slate };
        const ecoGroups = {};
        C.families.forEach(f => { if (!ecoGroups[f.eco]) ecoGroups[f.eco] = []; ecoGroups[f.eco].push({ name: f.n, value: f.c }); });
        const tmData = Object.entries(ecoGroups).map(([eco, children]) => ({ name: eco, itemStyle: { color: ecoColors[eco] || this._palette.slate }, children }));
        this._treemap('chart-conf-treemap', tmData, {
            levels: [
                { itemStyle: { borderColor: this._tc.bgPrimary, borderWidth: 2 } },
                { itemStyle: { borderColor: this._tc.bgPrimary, borderWidth: 1, gapWidth: 1 }, colorSaturation: [0.3, 0.7] },
            ],
            onClick: p => { if (p.data && p.data.children === undefined) FilterState.toggle('confFamily', p.name); },
        });

        // Ecosystem donut
        const ecoData = C.ecosystem.map(e => ({ name: e.n, value: e.c, itemStyle: { color: ecoColors[e.n] } }));
        this._donut('chart-conf-ecosystem', ecoData);

        // Family x year heatmap
        const fams = C.heatmap.map(h => h.n);
        const hmMatrix = C.heatmap.map(row => C.hmYears.map((_, yi) => row.d[yi] || 0));
        this._heatmap('chart-conf-heatmap', {
            xLabels: C.hmYears.map(String), yLabels: fams, matrix: hmMatrix,
            grid: { left: 120, right: 60, top: 30, bottom: 40 }, yInverse: true, yFontSize: 11,
            calculable: true, vmTop: 30, vmColor: this._palette.accent, labelFontSize: 11,
            splitArea: { show: true, areaStyle: { color: ['transparent'] } },
            tooltipFmt: p => `${fams[p.value[1]]} ${C.hmYears[p.value[0]]}: ${p.value[2]}`,
            onClick: params => {
                if (params.value[2] === '-' || params.value[2] === 0) return;
                this._showHeatmapDrilldown(fams[params.value[1]], C.hmYears[params.value[0]]);
            },
        });

        // Journals bar
        this._horizontalBar('chart-conf-journals', C.journals, { maxItems: 20, gridLeft: 250, labelWidth: 240, fontSize: 10, color: this._palette.emerald });

        // Venue type timeline
        const vtTypes = ['Conference', 'Preprint', 'Journal', 'Findings', 'Workshop'];
        this._stackedTimeline('chart-conf-timeline', {
            years: C.timeline.years,
            series: vtTypes.map(t => ({ name: t, type: 'bar', data: C.timeline[t] || [], color: this._vtColors[t], stack: 'total', smooth: false })),
        });

        // Peer-review ratio
        this._stackedTimeline('chart-conf-peer-ratio', {
            years: C.peerRatio.map(r => r.y), yMax: 100, yFmt: '{value}%',
            tooltipFmt: p => `${p[0].name}: ${p[0].value}% peer-reviewed`,
            series: [{
                name: 'Peer-Review %', type: 'line', data: C.peerRatio.map(r => r.pct), color: this._palette.accent, width: 3,
                areaStyle: { color: { type: 'linear', x: 0, y: 0, x2: 0, y2: 1, colorStops: [{offset: 0, color: 'rgba(99,102,241,0.3)'}, {offset: 1, color: 'rgba(99,102,241,0.0)'}] } },
            }],
        });
    },

    _heatmapExpandedIdx: null,
    _heatmapPapers: null,
    _heatmapDelegated: false,

    _showHeatmapDrilldown(family, year) {
        const container = document.getElementById('heatmap-drilldown');
        if (!container) return;
        this._heatmapPapers = DATA.papers.filter(p => p.cf === family && p.y === year);
        document.getElementById('heatmap-drilldown-title').textContent = `${family} ${year} \u2014 ${this._heatmapPapers.length} paper${this._heatmapPapers.length !== 1 ? 's' : ''}`;
        this._heatmapExpandedIdx = null;

        if (!this._heatmapDelegated) {
            this._heatmapDelegated = true;
            document.getElementById('heatmap-drilldown-tbody').addEventListener('click', (e) => {
                const row = e.target.closest('.paper-row');
                if (!row) return;
                const idx = +row.dataset.idx;
                this._heatmapExpandedIdx = this._heatmapExpandedIdx === idx ? null : idx;
                this._renderHeatmapTable();
            });
        }

        this._renderHeatmapTable();
        container.style.display = 'block';
        container.scrollIntoView({ behavior: 'smooth', block: 'start' });
        document.getElementById('heatmap-drilldown-close').onclick = () => { container.style.display = 'none'; };
    },

    _renderHeatmapTable() {
        const tbody = document.getElementById('heatmap-drilldown-tbody');
        if (!tbody || !this._heatmapPapers) return;
        const sorted = [...this._heatmapPapers].sort((a, b) => a.t.localeCompare(b.t));
        let html = '';
        for (const p of sorted) {
            html += renderPaperRow(p);
            if (this._heatmapExpandedIdx === p.i) html += renderPaperDetail(p);
        }
        if (!sorted.length) html = '<tr><td colspan="8" style="color:var(--text-muted);padding:16px;">No papers found.</td></tr>';
        tbody.innerHTML = html;
    },

    // ═══════════════════════════════════════════════════════════════════════
    // TAB 4: TAXONOMY & METHODS
    // ═══════════════════════════════════════════════════════════════════════

    _initTaxonomy() {
        const T = DATA.taxonomy;

        // Category x Year heatmap
        const cats = T.categories;
        const allYears = new Set();
        cats.forEach(c => Object.keys(c.byYear).forEach(y => allYears.add(y)));
        const years = [...allYears].sort();
        const matrix = cats.map(c => years.map(y => c.byYear[y] || 0));
        this._heatmap('chart-tax-heatmap', {
            xLabels: years, yLabels: cats.map(c => c.n), matrix,
            grid: { left: 220, right: 60, top: 10, bottom: 40 }, xPos: 'bottom',
            yFontSize: 10, yLabelWidth: 210, vmColor: this._palette.accent,
        });

        // Co-occurrence
        this._heatmap('chart-tax-cooccurrence', {
            xLabels: T.catNames, yLabels: T.catNames, matrix: T.cooccurrence,
            grid: { left: 200, right: 60, top: 40, bottom: 100 },
            xRotate: 45, xFontSize: 9, yFontSize: 9, yLabelWidth: 190, vmColor: this._palette.green, labelFontSize: 9,
        });

        // Models
        this._horizontalBar('chart-tax-models', T.models, { maxItems: 15, color: this._palette.yellow });

        // v7: Benchmarks sub-tab
        this._initBenchmarks();
    },

    // ═══════════════════════════════════════════════════════════════════════
    // TAB 5: CULTURAL VALUES
    // ═══════════════════════════════════════════════════════════════════════

    _initCultural() {
        const C = DATA.cultural;

        // Region donut
        const regionData = C.regionDist.map(d => ({ name: d.n, value: d.c }));
        this._donut('chart-cult-region-donut', regionData, { useColors: true, radius: ['35%', '70%'] });

        // Region timeline
        const tl = C.timeline;
        const regions = tl.regions.filter(r => tl.series[r] && tl.series[r].some(v => v > 0));
        this._stackedTimeline('chart-cult-region-timeline', {
            years: tl.years, legendType: 'scroll',
            series: regions.slice(0, 8).map((r, i) => ({
                name: r, type: 'line', data: tl.series[r], color: this._colors[i % this._colors.length],
                stack: 'total', areaStyle: {},
            })),
        });

        // Country bar
        this._horizontalBar('chart-cult-country-bar', C.countryDist, { maxItems: 30, color: this._palette.pink });
        // Language bar
        this._horizontalBar('chart-cult-lang-bar', C.langDist, { maxItems: 20, gridLeft: 110, color: this._palette.cyan });
        // WEIRD pie
        const wColors = { WEIRD: this._palette.red, 'Non-WEIRD': this._palette.green, Mixed: this._palette.yellow };
        const wData = Object.entries(C.weird).map(([n, v]) => ({ name: n, value: v, itemStyle: { color: wColors[n] } }));
        this._donut('chart-cult-weird-pie', wData, { radius: ['35%', '70%'] });
        // Culture treemap
        const ctmData = C.treemap.map(r => ({ name: r.n, children: r.ch.map(c => ({ name: c.n, value: c.v })) }));
        this._treemap('chart-cult-treemap', ctmData, { useColors: true });
        // Paper lists
        this._cultInitPaperList('country', 'cu');
        this._cultInitPaperList('lang', 'ln');
    },

    _cultInitPaperList(key, dim) {
        const countEl = document.getElementById(`cult-${key}-count`);
        const headerH3 = countEl ? countEl.parentElement.querySelector('h3') : null;
        const baseTitle = headerH3 ? headerH3.textContent : '';
        const filterKey = `cult-${key}`;
        const containerId = `cult-${key}-papers`;
        const allPapers = DATA.papers.filter(p => p[dim] && p[dim].length);
        if (countEl) countEl.textContent = allPapers.length;
        renderPaperList(containerId, allPapers, 50);

        const applyFilter = () => {
            const f = this._subFilter[filterKey];
            let filtered;
            if (!f) { filtered = allPapers; if (headerH3) headerH3.textContent = baseTitle; }
            else { filtered = DATA.papers.filter(p => p[dim] && p[dim].includes(f.val)); if (headerH3) headerH3.textContent = `${baseTitle} \u2014 ${f.val}`; }
            if (countEl) countEl.textContent = filtered.length;
            renderPaperList(containerId, filtered, 50);
        };
        const chartId = key === 'country' ? 'chart-cult-country-bar' : 'chart-cult-lang-bar';
        const chart = this._get(chartId);
        if (chart) {
            chart.off('click');
            chart.on('click', params => {
                if (!params.name) return;
                const cur = this._subFilter[filterKey];
                if (cur && cur.val === params.name) delete this._subFilter[filterKey];
                else this._subFilter[filterKey] = { dim, val: params.name };
                applyFilter();
            });
        }
    },

    // ═══════════════════════════════════════════════════════════════════════
    // TAB 6: NORMATIVE ETHICS
    // ═══════════════════════════════════════════════════════════════════════

    _initNormative() {
        const N = DATA.normative;
        // Classification donut
        const classData = [
            { name: 'Yes', value: N.yes, itemStyle: { color: this._palette.green } },
            { name: 'Borderline', value: N.borderline, itemStyle: { color: this._palette.yellow } },
            { name: 'Excluded', value: N.excluded, itemStyle: { color: this._palette.slate } },
        ];
        this._donut('chart-norm-class-donut', classData);
        // Framework bar
        this._horizontalBar('chart-norm-fw-bar', N.frameworks, { gridLeft: 200, labelWidth: 190, fontSize: 10 });
        // Timeline
        const fwColors = { ve: this._palette.green, de: this._palette.accent, cu: this._palette.yellow };
        const fwNames = { ve: 'Virtue Ethics', de: 'Deontological', cu: 'Consequentialism' };
        this._stackedTimeline('chart-norm-timeline', {
            years: N.timelineFw.years,
            series: ['ve','de','cu'].map(k => ({ name: fwNames[k], data: N.timelineFw[k] || [], color: fwColors[k] })),
        });
        // Sub-sections via unified _deepDiveSubSection
        this._deepDiveSubSection('norm', 've', N.ve, [
            { render(data, pfx) {
                if (data.virtueKeywords) this._horizontalBar(`chart-${pfx}-virtues`, data.virtueKeywords, { maxItems: 15, color: this._palette.green });
            }},
        ]);
        this._deepDiveSubSection('norm', 'de', N.de, [
            { render(data, pfx) {
                if (data.deontConcepts) this._horizontalBar(`chart-${pfx}-concepts`, data.deontConcepts, { maxItems: 13, gridLeft: 160, color: '#818cf8', emptyText: 'No concept data' });
            }},
        ]);
        this._deepDiveSubSection('norm', 'cu', N.cu, [
            { render(data, pfx) {
                if (data.cuConcepts) this._horizontalBar(`chart-${pfx}-concepts`, data.cuConcepts, { maxItems: 13, gridLeft: 160, color: this._palette.yellow, emptyText: 'No concept data' });
            }},
        ]);
        // Overlap
        this._normOverlap(N.overlap);
    },

    _normOverlap(overlap) {
        // Overlap bar
        const oData = [
            { n: 'VE + DE', c: overlap.ve_de }, { n: 'VE + CU', c: overlap.ve_cu },
            { n: 'DE + CU', c: overlap.de_cu }, { n: 'All Three', c: overlap.all },
        ];
        const paperKeys = { 'VE + DE': 've_de_papers', 'VE + CU': 've_cu_papers', 'DE + CU': 'de_cu_papers', 'All Three': 'all_papers' };
        const countEl = document.getElementById('norm-overlap-count');
        const headerH3 = countEl ? countEl.parentElement.querySelector('h3') : null;
        let activeFilter = null;
        if (countEl) countEl.textContent = (overlap.any_papers || []).length;
        renderPaperList('norm-overlap-papers', overlap.any_papers || [], 50);

        this._horizontalBar('chart-norm-overlap', oData, {
            gridLeft: 100, color: this._palette.violet,
            onClick: params => {
                if (!params.name) return;
                const key = paperKeys[params.name];
                if (!key) return;
                if (activeFilter === params.name) {
                    activeFilter = null;
                    if (headerH3) headerH3.textContent = 'Overlapping Papers';
                    if (countEl) countEl.textContent = (overlap.any_papers || []).length;
                    renderPaperList('norm-overlap-papers', overlap.any_papers || [], 50);
                } else {
                    activeFilter = params.name;
                    const papers = overlap[key] || [];
                    if (headerH3) headerH3.textContent = `Overlapping Papers \u2014 ${params.name}`;
                    if (countEl) countEl.textContent = papers.length;
                    renderPaperList('norm-overlap-papers', papers, 50);
                }
            },
        });

        // Overlap timeline
        const oColors = { ve_de: '#f472b6', ve_cu: '#fb923c', de_cu: '#34d399', all: '#a78bfa' };
        const oNames = { ve_de: 'VE + DE', ve_cu: 'VE + CU', de_cu: 'DE + CU', all: 'All Three' };
        if (overlap.overlapTimeline) {
            this._stackedTimeline('chart-norm-overlap-timeline', {
                years: overlap.overlapTimeline.years,
                series: ['ve_de', 've_cu', 'de_cu', 'all'].map(k => ({
                    name: oNames[k], data: overlap.overlapTimeline[k] || [], color: oColors[k],
                    stack: 'overlap', areaStyle: { opacity: 0.4 },
                })),
            });
        }

        // Exclusivity sunburst
        if (overlap.exclusivity) this._normOverlapExclusivity(overlap.exclusivity);

        // Overlap models grouped bar
        if (overlap.overlapModels) {
            const totals = {};
            for (const combo of ['ve_de', 've_cu', 'de_cu', 'all']) {
                for (const m of (overlap.overlapModels[combo] || [])) totals[m.n] = (totals[m.n] || 0) + m.c;
            }
            const modelNames = Object.entries(totals).sort((a, b) => b[1] - a[1]).slice(0, 8).map(e => e[0]);
            if (modelNames.length) {
                const comboLookup = {};
                for (const combo of ['ve_de', 've_cu', 'de_cu', 'all']) {
                    const lk = {}; for (const m of (overlap.overlapModels[combo] || [])) lk[m.n] = m.c; comboLookup[combo] = lk;
                }
                this._groupedBar('chart-norm-overlap-models', {
                    categories: [...modelNames].reverse(), gridLeft: 120,
                    series: ['ve_de', 've_cu', 'de_cu', 'all'].map(combo => ({
                        name: oNames[combo], data: [...modelNames].reverse().map(n => comboLookup[combo][n] || 0), color: oColors[combo],
                    })),
                });
            }
        }

        // Region heatmap
        if (overlap.regionHeatmap) {
            this._heatmap('chart-norm-overlap-region', {
                xLabels: overlap.regionHeatmap.regionLabels || [], yLabels: overlap.regionHeatmap.comboLabels || [],
                matrix: overlap.regionHeatmap.matrix || [],
                grid: { left: 90, right: 60, top: 10, bottom: 80 }, xRotate: 30, vmColor: this._palette.violet,
            });
        }

        // Benchmark density
        this._normOverlapBench(overlap);
    },

    _normOverlapExclusivity(excl) {
        const chart = this._get('chart-norm-overlap-excl');
        if (!chart || !excl) return;
        const fwColors = { ve: this._palette.green, de: this._palette.accent, cu: this._palette.yellow };
        const fwNames = { ve: 'Virtue Ethics', de: 'Deontological', cu: 'Consequentialism' };
        const subLabels = {
            ve: [['VE only','only'],['+ DE','ve_de'],['+ CU','ve_cu'],['All 3','all']],
            de: [['DE only','only'],['+ VE','ve_de'],['+ CU','de_cu'],['All 3','all']],
            cu: [['CU only','only'],['+ VE','ve_cu'],['+ DE','de_cu'],['All 3','all']],
        };
        const data = ['ve','de','cu'].map(fw => {
            const d = excl[fw]; const base = fwColors[fw];
            const children = subLabels[fw].map(([label, key], i) => ({
                name: `${label} (${d[key]})`, value: d[key],
                itemStyle: { color: i === 0 ? base : (i === 3 ? this._palette.violet : base + '88') },
            }));
            const sum = children.reduce((s, c) => s + c.value, 0);
            return { name: `${fwNames[fw]} (${sum})`, itemStyle: { color: base }, children };
        });
        chart.setOption({
            ...this._theme,
            tooltip: { ...this._theme.tooltip },
            series: [{
                type: 'sunburst', data, radius: ['15%', '90%'],
                label: { color: this._tc.textPri, fontSize: 10, overflow: 'truncate', width: 70 },
                itemStyle: { borderColor: this._tc.bgPrimary, borderWidth: 1 },
                levels: [{}, { r0: '15%', r: '50%', label: { fontSize: 12 } }, { r0: '50%', r: '90%', label: { fontSize: 10 } }],
            }],
        }, true);
    },

    _normOverlapBench(overlap) {
        const chart = this._get('chart-norm-overlap-bench');
        if (!chart) return;
        const bars = [
            { name: 'VE + DE', count: overlap.ve_de_bench, total: overlap.ve_de, pct: overlap.ve_de_pct },
            { name: 'VE + CU', count: overlap.ve_cu_bench, total: overlap.ve_cu, pct: overlap.ve_cu_pct },
            { name: 'DE + CU', count: overlap.de_cu_bench, total: overlap.de_cu, pct: overlap.de_cu_pct },
            { name: 'All Three', count: overlap.all_bench, total: overlap.all, pct: overlap.all_pct },
            { name: 'Single FW', count: overlap.single_bench, total: overlap.single_total, pct: overlap.single_pct },
        ];
        chart.setOption({
            ...this._theme,
            grid: { left: 100, right: 60, top: 10, bottom: 20 },
            xAxis: { type: 'value', max: 100, axisLabel: { color: this._tc.textSec, formatter: '{value}%' }, splitLine: { lineStyle: { color: this._tc.bgPrimary } } },
            yAxis: { type: 'category', data: bars.map(b => b.name).reverse(), axisLabel: { color: this._tc.textSec } },
            tooltip: { ...this._theme.tooltip, trigger: 'axis', formatter: params => { const p = params[0]; const b = bars.find(x => x.name === p.name); return b ? `${b.name}: ${b.count}/${b.total} (${b.pct}%)` : ''; } },
            series: [{
                type: 'bar',
                data: bars.map(b => ({ value: b.pct, itemStyle: { color: b.name === 'Single FW' ? this._palette.slate : this._palette.teal, borderRadius: [0, 4, 4, 0] } })).reverse(),
                label: { show: true, position: 'right', color: this._tc.textSec, fontSize: 10, formatter: p => { const b = bars[bars.length - 1 - p.dataIndex]; return `${b.count}/${b.total}`; } },
            }],
        }, true);
    },

    // ═══════════════════════════════════════════════════════════════════════
    // TAB 7: MORAL PSYCHOLOGY
    // ═══════════════════════════════════════════════════════════════════════

    _initMoralPsych() {
        const M = DATA.moralPsych;

        // Theory bar (with per-item colors)
        this._horizontalBar('chart-mp-theory-bar', M.theoryDist, { gridLeft: 200, colorFn: x => x.col });

        // Timeline
        this._stackedTimeline('chart-mp-timeline', {
            years: M.timeline.years,
            series: [
                { name: 'MFT', data: M.timeline.mft, color: this._palette.accent },
                { name: 'Schwartz', data: M.timeline.schwartz, color: this._palette.cyan },
                { name: 'Developmental', data: M.timeline.dev, color: this._palette.yellow },
            ],
        });

        // Co-occurrence
        this._heatmap('chart-mp-cooccurrence', {
            xLabels: M.coLabels, yLabels: M.coLabels, matrix: M.cooccurrence,
            grid: { left: 120, right: 60, top: 40, bottom: 80 }, xRotate: 30, vmColor: this._palette.pink,
        });

        // MFT — via unified _deepDiveSubSection + MFT-specific radar
        this._deepDiveSubSection('mp', 'mft', M.mft, [
            { render(data, pfx) {
                const maxVal = Math.max(...data.foundations.map(f => f.c), 1);
                this._radar(`chart-${pfx}-radar`, {
                    indicators: data.foundations.map(f => ({ name: f.n, max: maxVal })),
                    series: [{ values: data.foundations.map(f => f.c), name: 'MFT Foundations', color: this._palette.accent, areaColor: 'rgba(99,102,241,0.3)' }],
                });
            }},
        ]);

        // Schwartz — via unified _deepDiveSubSection + Schwartz-specific radar
        this._deepDiveSubSection('mp', 'schwartz', M.schwartz, [
            { render(data, pfx) {
                if (data.valueDims) {
                    const maxVal = Math.max(...data.valueDims.map(v => v.c), 1);
                    this._radar(`chart-${pfx}-radar`, {
                        indicators: data.valueDims.map(v => ({ name: v.n, max: maxVal })),
                        series: [{ values: data.valueDims.map(v => v.c), name: 'Schwartz Values', color: this._palette.cyan, areaColor: 'rgba(34,211,238,0.3)' }],
                    });
                }
            }},
        ]);

        // Developmental — via unified _deepDiveSubSection + paradigm bar
        this._deepDiveSubSection('mp', 'dev', M.developmental, [
            { render(data, pfx) {
                if (data.subTheories) {
                    const filtered = (data.subTheories || []).filter(x => x.c > 0);
                    const paradigmColors = { 'Kohlberg': this._palette.yellow, 'Trolley': this._palette.pink };
                    this._horizontalBar(`chart-${pfx}-paradigm`, filtered, { gridLeft: 100, colorFn: x => paradigmColors[x.n] || this._palette.yellow, barMaxWidth: 30, emptyText: 'No paradigm data' });
                }
            }},
        ]);
    },

    // ═══════════════════════════════════════════════════════════════════════
    // TAB 8: RELIGIOUS VALUES
    // ═══════════════════════════════════════════════════════════════════════

    _initReligious() {
        const R = DATA.religious;

        // Tradition bar (per-item colors)
        this._horizontalBar('chart-rel-trad-bar', R.traditionDist, {
            gridLeft: 120, colorFn: x => x.col,
            onClick: p => { if (p.name) FilterState.toggle('religion', p.name); },
        });

        // Timeline
        this._stackedTimeline('chart-rel-timeline', {
            years: R.timeline.years,
            series: [
                { name: 'Abrahamic', data: R.timeline.abrahamic, color: this._palette.accent },
                { name: 'Dharmic', data: R.timeline.dharmic, color: this._palette.yellow },
                { name: 'East Asian', data: R.timeline.eastAsian, color: this._palette.cyan },
                { name: 'African/Indigenous', data: R.timeline.africanIndigenous, color: this._palette.orange },
            ],
        });

        // Co-occurrence
        this._heatmap('chart-rel-cooccurrence', {
            xLabels: R.coLabels, yLabels: R.coLabels, matrix: R.cooccurrence,
            grid: { left: 110, right: 60, top: 40, bottom: 80 }, xRotate: 30, vmColor: this._palette.orange,
        });

        // Sub-sections + extended charts via unified _deepDiveSubSection
        const relSections = [
            ['islamic', R.islamic], ['christian', R.christianJewish],
            ['dharmic', R.dharmic], ['confucian', R.confucian], ['ubuntu', R.ubuntuIndigenous],
        ];
        for (const [key, data] of relSections) {
            this._deepDiveSubSection('rel', key, data, this._relExtendedConfigs[key]);
        }
    },

    // Config-driven extended chart definitions for each religious sub-section
    _relExtendedConfigs: {
        islamic: [
            { render(data, fk) {
                // Domain treemap
                const items = (data.domainDist || []).map(d => ({ name: d.n, value: d.c }));
                this._treemap('chart-rel-islamic-domains', items, {
                    levels: [{ color: ['#166534','#15803d','#16a34a','#22c55e','#4ade80','#86efac'], colorMappingBy: 'index' }],
                    tooltipFmt: p => `${p.name}: ${p.value}`,
                });
                this._attachExtFnFilter(fk, 'chart-rel-islamic-domains', p => { const d = (data.domainDist||[]).find(x => x.n === p.name); return d ? {label: d.n, fns: d.fns} : null; });
            }},
            { render(data, fk) {
                // Language/geo bar
                const d = (data.langGeo || []).slice(0, 12);
                const regionColors = { 'Middle East': this._palette.green, 'South Asia': this._palette.yellow, 'Southeast Asia': this._palette.cyan, 'Africa': this._palette.orange, 'Global': this._palette.accent, 'Other': this._palette.slate };
                this._horizontalBar('chart-rel-islamic-langgeo', d.map(x => ({ n: x.lang, c: x.c, region: x.region })), {
                    gridLeft: 110, colorFn: x => regionColors[x.region] || this._palette.slate,
                    tooltipFmt: p => `${p[0].name}: ${p[0].value} (${d.find(x => x.lang === p[0].name)?.region || ''})`,
                });
                this._attachExtFnFilter(fk, 'chart-rel-islamic-langgeo', p => { const dd = (data.langGeo||[]).find(x => x.lang === p.name); return dd ? {label: dd.lang, fns: dd.fns} : null; });
            }},
            { render(data, fk) {
                // Resource vs Bias streams
                const sl = data.streamTimeline || {};
                if ((sl.years || []).length) {
                    this._stackedTimeline('chart-rel-islamic-streams', {
                        years: sl.years,
                        series: [
                            { name: 'Resource', data: sl.resource || [], color: this._palette.green, areaStyle: { color: 'rgba(34,197,94,0.2)' } },
                            { name: 'Bias', data: sl.bias || [], color: this._palette.red, areaStyle: { color: 'rgba(239,68,68,0.2)' } },
                        ],
                    });
                }
                this._attachExtFnFilter(fk, 'chart-rel-islamic-streams', p => { const fns = (data.streamTimelineFns||{})[p.seriesName]; return fns ? {label: p.seriesName, fns} : null; });
            }},
            { render(data, fk) {
                // Source coverage radar
                const d = data.sourceCoverage || [];
                if (d.length) {
                    const maxVal = Math.max(...d.map(x => x.val), 1);
                    this._radar('chart-rel-islamic-sources', {
                        triggerEvent: true, indicators: d.map(x => ({ name: x.axis, max: maxVal })),
                        series: [{ values: d.map(x => x.val), name: 'Source Coverage', color: this._palette.green, areaColor: 'rgba(34,197,94,0.3)' }],
                        splitAreaColors: [this._tc.bgPrimary, this._tc.bgCard], showAxisLine: true,
                    });
                }
                this._attachExtFnFilter(fk, 'chart-rel-islamic-sources', p => { const fns = (data.sourceCoverageFns||{})[p.name]; return fns ? {label: p.name, fns} : null; });
            }},
            { render(data, fk) {
                // Co-traditions bar
                const flows = data.coTraditions || [];
                if (flows.length) {
                    const tradColors = { 'Christianity': this._palette.accent, 'Judaism': this._palette.violet, 'Buddhism': this._palette.yellow, 'Hinduism': this._palette.pink, 'Confucian': this._palette.cyan, 'Ubuntu': this._palette.orange, 'Indigenous': this._palette.teal, 'Shinto': '#e879f9' };
                    const sorted = [...flows].sort((a, b) => b.value - a.value);
                    this._horizontalBar('chart-rel-islamic-sankey', sorted.map(f => ({ n: f.target, c: f.value, trad: f.target })), { colorFn: x => tradColors[x.trad] || this._palette.slate });
                }
                this._attachExtFnFilter(fk, 'chart-rel-islamic-sankey', p => { const d = (data.coTraditions||[]).find(x => x.target === p.name); return d ? {label: d.target, fns: d.fns} : null; });
            }},
        ],
        christian: [
            { render(data, fk) {
                // Tradition breakdown donut
                const tradColors = { 'Christianity only': this._palette.accent, 'Judaism only': this._palette.violet, 'Both': this._palette.sky, 'Multi-religion': this._palette.yellow };
                const pieData = (data.traditionBreakdown || []).map(d => ({ name: d.n, value: d.c, itemStyle: { color: tradColors[d.n] || this._palette.slate } }));
                if (pieData.length) this._donut('chart-rel-christian-breakdown', pieData);
                this._attachExtFnFilter(fk, 'chart-rel-christian-breakdown', p => { const d = (data.traditionBreakdown||[]).find(x => x.n === p.name); return d ? {label: d.n, fns: d.fns} : null; });
            }},
            { render(data, fk) {
                // Theological concepts radar
                const d = data.theologicalConcepts || [];
                if (d.length) {
                    const maxVal = Math.max(...d.map(x => x.val), 1);
                    this._radar('chart-rel-christian-theology', {
                        triggerEvent: true, indicators: d.map(x => ({ name: x.axis, max: maxVal })),
                        series: [{ values: d.map(x => x.val), name: 'Theological Concepts', color: this._palette.accent, areaColor: 'rgba(99,102,241,0.3)' }],
                        splitAreaColors: [this._tc.bgPrimary, this._tc.bgCard], showAxisLine: true,
                    });
                }
                this._attachExtFnFilter(fk, 'chart-rel-christian-theology', p => { const fns = (data.theologicalConceptsFns||{})[p.name]; return fns ? {label: p.name, fns} : null; });
            }},
            { render(data, fk) {
                // Focus distribution donut
                const pieColors = [this._palette.accent, this._palette.violet, this._palette.sky, this._palette.green, this._palette.yellow, this._palette.slate];
                const pieData = (data.focusDist || []).map((d, i) => ({ name: d.n, value: d.c, itemStyle: { color: pieColors[i % 6] } }));
                if (pieData.length) this._donut('chart-rel-christian-focus', pieData);
                this._attachExtFnFilter(fk, 'chart-rel-christian-focus', p => { const d = (data.focusDist||[]).find(x => x.n === p.name); return d ? {label: d.n, fns: d.fns} : null; });
            }},
            { render(data, fk) {
                // Normative cross-tradition grouped bar
                const d = data.normativeCross || [];
                if (d.length) {
                    this._groupedBar('chart-rel-christian-normative', {
                        categories: d.map(x => x.framework), xRotate: 20,
                        series: [
                            { name: 'Christianity', data: d.map(x => x.christianity), color: this._palette.accent },
                            { name: 'Judaism', data: d.map(x => x.judaism), color: this._palette.violet },
                        ],
                    });
                }
                this._attachExtFnFilter(fk, 'chart-rel-christian-normative', p => { const fns = (data.normativeCrossFns||{})[p.name]; return fns ? {label: p.name, fns} : null; });
            }},
            { render(data) {
                // Tradition comparison HTML table
                const el = document.getElementById('rel-christian-comparison');
                if (!el) return;
                const tc = data.traditionComparison || {};
                const traditions = Object.keys(tc);
                if (!traditions.length) return;
                const fields = [
                    { key: 'paperCount', label: 'Papers' }, { key: 'benchmarkCount', label: 'Benchmarks' },
                    { key: 'biasStudies', label: 'Bias Studies' }, { key: 'frameworkPapers', label: 'Framework Papers' },
                    { key: 'datasetsCount', label: 'Datasets' },
                    { key: 'languages', label: 'Languages', format: v => Array.isArray(v) ? v.join(', ') : String(v) },
                ];
                const headerCells = traditions.map(t => `<th style="padding:8px 12px;text-align:right;color:#f1f5f9;border-bottom:1px solid #334155">${t}</th>`).join('');
                const rows = fields.map(f => {
                    const cells = traditions.map(t => {
                        const raw = tc[t]?.[f.key]; const display = raw === undefined ? '\u2014' : (f.format ? f.format(raw) : String(raw));
                        return `<td style="padding:6px 12px;text-align:right;color:#94a3b8">${display}</td>`;
                    }).join('');
                    return `<tr><td style="padding:6px 12px;color:#cbd5e1;font-size:12px">${f.label}</td>${cells}</tr>`;
                }).join('');
                el.innerHTML = `<table style="width:100%;border-collapse:collapse;font-size:13px;background:#0f172a;border-radius:6px;overflow:hidden"><thead><tr style="background:#1e293b"><th style="padding:8px 12px;text-align:left;color:#94a3b8;border-bottom:1px solid #334155">Metric</th>${headerCells}</tr></thead><tbody>${rows}</tbody></table>`;
            }},
        ],
        dharmic: [
            { render(data, fk) {
                // Tradition split bar
                const d = data.traditionSplit || [];
                if (d.length) {
                    this._horizontalBar('chart-rel-dharmic-split', d, { gridLeft: 60, colorFn: (x, i) => [this._palette.yellow, this._palette.pink][d.indexOf(x)] || this._palette.yellow });
                    const chart = this._get('chart-rel-dharmic-split');
                    if (chart) {
                        chart.setOption({
                            ...this._theme,
                            grid: { left: 60, right: 20, top: 10, bottom: 40 },
                            xAxis: { type: 'category', data: d.map(x => x.n), axisLabel: { color: this._tc.textSec, fontSize: 11 } },
                            yAxis: { type: 'value', axisLabel: { color: this._tc.textSec }, splitLine: { lineStyle: { color: this._tc.bgPrimary } } },
                            tooltip: { ...this._theme.tooltip, trigger: 'axis' },
                            series: [{ type: 'bar', data: d.map((x, i) => ({ value: x.c, itemStyle: { color: i === 0 ? this._palette.yellow : this._palette.pink, borderRadius: [4,4,0,0] } })) }],
                        }, true);
                    }
                }
                this._attachExtFnFilter(fk, 'chart-rel-dharmic-split', p => { const dd = (data.traditionSplit||[]).find(x => x.n === p.name); return dd ? {label: dd.n, fns: dd.fns} : null; });
            }},
            { render(data, fk) {
                // Culture donut
                const pieColors = [this._palette.yellow, this._palette.pink, this._palette.sky, this._palette.green, this._palette.accent, this._palette.slate];
                const pieData = (data.cultureDist || []).map((d, i) => ({ name: d.n, value: d.c, itemStyle: { color: pieColors[i % 6] } }));
                if (pieData.length) this._donut('chart-rel-dharmic-cultures', pieData);
                this._attachExtFnFilter(fk, 'chart-rel-dharmic-cultures', p => { const d = (data.cultureDist||[]).find(x => x.n === p.name); return d ? {label: d.n, fns: d.fns} : null; });
            }},
            { render(data, fk) {
                // Concept radar (dual)
                const cr = data.conceptRadar || {};
                const labels = cr.labels || [];
                if (labels.length) {
                    const maxVal = Math.max(...(cr.buddhism||[]), ...(cr.hinduism||[]), 1);
                    this._radar('chart-rel-dharmic-concepts', {
                        triggerEvent: true, indicators: labels.map(l => ({ name: l, max: maxVal })),
                        series: [
                            { values: cr.buddhism || [], name: 'Buddhism', color: this._palette.yellow, areaColor: 'rgba(245,158,11,0.3)' },
                            { values: cr.hinduism || [], name: 'Hinduism', color: this._palette.pink, areaColor: 'rgba(236,72,153,0.3)' },
                        ],
                        splitAreaColors: [this._tc.bgPrimary, this._tc.bgCard], showAxisLine: true,
                    });
                }
                this._attachExtFnFilter(fk, 'chart-rel-dharmic-concepts', p => { const fns = (data.conceptRadarFns||{})[p.name]; return fns ? {label: p.name, fns} : null; });
            }},
            { render(data, fk) {
                // Research focus stacked bar
                const d = data.researchFocus || [];
                if (d.length) {
                    this._groupedBar('chart-rel-dharmic-focus', {
                        categories: d.map(x => x.category), xRotate: 20, stack: 'total',
                        axisPointer: { type: 'shadow' },
                        series: [
                            { name: 'Buddhism', data: d.map(x => x.buddhism), color: this._palette.yellow },
                            { name: 'Hinduism', data: d.map(x => x.hinduism), color: this._palette.pink },
                        ],
                    });
                }
                this._attachExtFnFilter(fk, 'chart-rel-dharmic-focus', p => { const fns = (data.researchFocusFns||{})[p.name]; return fns ? {label: p.name, fns} : null; });
            }},
            { render(data, fk) {
                // Language treemap
                const tradColors = { 'Buddhism': this._palette.yellow, 'Hinduism': this._palette.pink, 'Both': this._palette.sky, 'Other': this._palette.slate };
                const items = (data.langTreemap || []).map(d => ({ name: d.n, value: d.c, itemStyle: { color: tradColors[d.trad] || this._palette.slate } }));
                if (items.length) this._treemap('chart-rel-dharmic-langs', items, { tooltipFmt: p => `${p.name}: ${p.value}`, levels: [] });
                this._attachExtFnFilter(fk, 'chart-rel-dharmic-langs', p => { const d = (data.langTreemap||[]).find(x => x.n === p.name); return d ? {label: d.n, fns: d.fns} : null; });
            }},
        ],
        confucian: [
            { render(data, fk) {
                // Cultural footprint treemap
                const items = (data.culturalFootprint || []).map(d => ({ name: d.n, value: d.c }));
                if (items.length) this._treemap('chart-rel-confucian-cultures', items, {
                    levels: [{ color: ['#164e63','#155e75','#0e7490','#0891b2','#22d3ee','#67e8f9'], colorMappingBy: 'index' }],
                    tooltipFmt: p => `${p.name}: ${p.value}`,
                });
                this._attachExtFnFilter(fk, 'chart-rel-confucian-cultures', p => { const d = (data.culturalFootprint||[]).find(x => x.n === p.name); return d ? {label: d.n, fns: d.fns} : null; });
            }},
            { render(data, fk) {
                // Framework overlap radar
                const d = data.frameworkOverlap || [];
                if (d.length) {
                    const maxVal = Math.max(...d.map(x => x.val), 1);
                    this._radar('chart-rel-confucian-frameworks', {
                        triggerEvent: true, indicators: d.map(x => ({ name: x.axis, max: maxVal })),
                        series: [{ values: d.map(x => x.val), name: 'Framework Overlap', color: this._palette.cyan, areaColor: 'rgba(34,211,238,0.3)' }],
                        splitAreaColors: [this._tc.bgPrimary, this._tc.bgCard], showAxisLine: true,
                    });
                }
                this._attachExtFnFilter(fk, 'chart-rel-confucian-frameworks', p => { const fns = (data.frameworkOverlapFns||{})[p.name]; return fns ? {label: p.name, fns} : null; });
            }},
            { render(data, fk) {
                // Chinese vs Western LLMs grouped bar
                const d = data.chineseVsWesternLLMs || [];
                if (d.length) {
                    const chinese = d.filter(x => x.origin === 'Chinese'), western = d.filter(x => x.origin === 'Western');
                    const allNames = [...new Set(d.map(x => x.n))];
                    const lookup = (arr, name) => { const f = arr.find(x => x.n === name); return f ? f.c : 0; };
                    this._groupedBar('chart-rel-confucian-llms', {
                        categories: allNames, xRotate: 20,
                        series: [
                            { name: 'Chinese', data: allNames.map(n => lookup(chinese, n)), color: this._palette.red },
                            { name: 'Western', data: allNames.map(n => lookup(western, n)), color: this._palette.sky },
                        ],
                    });
                }
                this._attachExtFnFilter(fk, 'chart-rel-confucian-llms', p => { const d = (data.chineseVsWesternLLMs||[]).find(x => x.n === p.name); return d ? {label: d.n, fns: d.fns} : null; });
            }},
            { render(data, fk) {
                // Language distribution donut
                const pieColors = [this._palette.cyan, this._palette.accent, this._palette.yellow, this._palette.green, this._palette.pink, this._palette.slate];
                const pieData = (data.languageDist || []).map((d, i) => ({ name: d.n, value: d.c, itemStyle: { color: pieColors[i % 6] } }));
                if (pieData.length) this._donut('chart-rel-confucian-langs', pieData);
                this._attachExtFnFilter(fk, 'chart-rel-confucian-langs', p => { const d = (data.languageDist||[]).find(x => x.n === p.name); return d ? {label: d.n, fns: d.fns} : null; });
            }},
            { render(data, fk) {
                // Research trajectory stacked bar
                const rp = data.researchProfile || {};
                if ((rp.years || []).length) {
                    this._groupedBar('chart-rel-confucian-trajectory', {
                        categories: rp.years.map(String), stack: 'total',
                        axisPointer: { type: 'shadow' },
                        series: [
                            { name: 'Empirical', data: rp.empirical || [], color: this._palette.cyan },
                            { name: 'Theoretical', data: rp.theoretical || [], color: this._palette.accent },
                        ],
                    });
                }
                this._attachExtFnFilter(fk, 'chart-rel-confucian-trajectory', p => { const fns = (data.researchProfileFns||{})[p.seriesName]; return fns ? {label: p.seriesName, fns} : null; });
            }},
            { render(data, fk) {
                // Concept frequency bar
                this._horizontalBar('chart-rel-confucian-concepts', (data.conceptFreq || []), { maxItems: 15, gridLeft: 140, color: this._palette.cyan });
                this._attachExtFnFilter(fk, 'chart-rel-confucian-concepts', p => { const d = (data.conceptFreq||[]).find(x => x.n === p.name); return d ? {label: d.n, fns: d.fns} : null; });
            }},
        ],
        ubuntu: [
            { render(data, fk) {
                // Sub-tradition donut
                const UBUNTU_COLORS = { 'Ubuntu': this._palette.orange, 'Indigenous': this._palette.teal, 'Shinto': '#e879f9' };
                const pieData = (data.subTradDist || []).map(d => ({ name: d.n, value: d.c, itemStyle: { color: d.col || UBUNTU_COLORS[d.n] || this._palette.slate } }));
                if (pieData.length) this._donut('chart-rel-ubuntu-subtrad', pieData);
                this._attachExtFnFilter(fk, 'chart-rel-ubuntu-subtrad', p => { const d = (data.subTradDist||[]).find(x => x.n === p.name); return d ? {label: d.n, fns: d.fns} : null; });
            }},
            { render(data, fk) {
                // Culture distribution bar
                const UBUNTU_COLORS = { 'Ubuntu': this._palette.orange, 'Indigenous': this._palette.teal, 'Shinto': '#e879f9' };
                this._horizontalBar('chart-rel-ubuntu-cultures', (data.cultureDist || []), { maxItems: 12, colorFn: x => UBUNTU_COLORS[x.trad] || this._palette.slate });
                this._attachExtFnFilter(fk, 'chart-rel-ubuntu-cultures', p => { const d = (data.cultureDist||[]).find(x => x.n === p.name); return d ? {label: d.n, fns: d.fns} : null; });
            }},
            { render(data, fk) {
                // Eval readiness stacked bar
                const d = data.evalReadiness || [];
                if (d.length) {
                    this._groupedBar('chart-rel-ubuntu-eval', {
                        categories: d.map(x => x.tradition), stack: 'total',
                        axisPointer: { type: 'shadow' },
                        series: [
                            { name: 'Benchmarks', data: d.map(x => x.benchmark), color: this._palette.accent },
                            { name: 'Evaluation', data: d.map(x => x.evaluation), color: this._palette.green },
                            { name: 'Ethics Only', data: d.map(x => x.ethicsOnly), color: this._palette.yellow },
                        ],
                    });
                }
                this._attachExtFnFilter(fk, 'chart-rel-ubuntu-eval', p => { const fns = (data.evalReadinessFns||{})[p.name]; return fns ? {label: p.name, fns} : null; });
            }},
            { render(data, fk) {
                // Theme radar (3 traces)
                const tr = data.themeRadar || {};
                const labels = tr.labels || [];
                if (labels.length) {
                    const maxVal = Math.max(...(tr.ubuntu||[]), ...(tr.indigenous||[]), ...(tr.shinto||[]), 1);
                    this._radar('chart-rel-ubuntu-themes', {
                        triggerEvent: true, indicators: labels.map(l => ({ name: l, max: maxVal })),
                        series: [
                            { values: tr.ubuntu || [], name: 'Ubuntu', color: this._palette.orange, areaColor: 'rgba(249,115,22,0.3)' },
                            { values: tr.indigenous || [], name: 'Indigenous', color: this._palette.teal, areaColor: 'rgba(20,184,166,0.3)' },
                            { values: tr.shinto || [], name: 'Shinto', color: '#e879f9', areaColor: 'rgba(232,121,249,0.3)' },
                        ],
                        splitAreaColors: [this._tc.bgPrimary, this._tc.bgCard], showAxisLine: true,
                    });
                }
                this._attachExtFnFilter(fk, 'chart-rel-ubuntu-themes', p => { const fns = (data.themeRadarFns||{})[p.name]; return fns ? {label: p.name, fns} : null; });
            }},
            { render(data, fk) {
                // Gap comparison grouped bar
                const d = data.gapComparison || [];
                if (d.length) {
                    this._groupedBar('chart-rel-ubuntu-gap', {
                        categories: d.map(x => x.metric), gridLeft: 100, xRotate: 20,
                        series: [
                            { name: 'Subset', data: d.map(x => x.subset), color: this._palette.orange },
                            { name: 'Vault', data: d.map(x => x.vault), color: this._palette.slate },
                        ],
                    });
                }
            }},
            { render(data, fk) {
                // Language distribution bar
                this._horizontalBar('chart-rel-ubuntu-langs', (data.languageDist || []), { maxItems: 12, gridLeft: 110, color: this._palette.teal });
                this._attachExtFnFilter(fk, 'chart-rel-ubuntu-langs', p => { const d = (data.languageDist||[]).find(x => x.n === p.name); return d ? {label: d.n, fns: d.fns} : null; });
            }},
        ],
    },

    // ═══════════════════════════════════════════════════════════════════════
    // TAB 9: MODELS & LLMs
    // ═══════════════════════════════════════════════════════════════════════

    _initModels() {
        const L = DATA.llm;
        this._horizontalBar('chart-llm-models', L.llmModels, {
            maxItems: 20, fontSize: 10, color: this._palette.violet,
            onClick: p => { if (p.name) FilterState.toggle('llmModel', p.name); },
        });
        this._horizontalBar('chart-llm-families', L.modelFamilies, { maxItems: 20, fontSize: 10, color: this._palette.yellow });

        // LLM timeline
        const years = Object.keys(L.llmByYear).sort();
        this._stackedTimeline('chart-llm-timeline', {
            years,
            series: [
                { name: 'Assessed', type: 'bar', data: years.map(y => L.llmByYear[y].a), color: this._palette.green, stack: 'total', smooth: false },
                { name: 'Not Assessed', type: 'bar', data: years.map(y => L.llmByYear[y].na), color: '#475569', stack: 'total', smooth: false },
            ],
        });

        // Repo distribution donut
        const repoColors = { GitHub: this._tc.textPri, HuggingFace: this._palette.yellow, Zenodo: this._palette.green, OSF: this._palette.accent, Kaggle: this._palette.cyan, Other: this._palette.slate };
        const repoData = L.repoDist.map(d => ({ name: d.n, value: d.c, itemStyle: { color: repoColors[d.n] || this._palette.slate } }));
        this._donut('chart-llm-repos', repoData, { radius: ['35%', '65%'] });

        // v7: Model Depth sub-tab
        this._initModelDepth();
    },

    // ═══════════════════════════════════════════════════════════════════════
    // Phase 5: UNIFIED DEEP-DIVE SUB-SECTION
    // Replaces _normSubSection, _mpSubSection, _relSubSection (~80 lines saved)
    // ═══════════════════════════════════════════════════════════════════════

    /**
     * Standard deep-dive sub-section renderer.
     * Handles: count badge, year bar, models bar, optional split/venue/region donuts,
     * extraCharts for section-specific additions, paper list, and filter wiring.
     *
     * @param {string} prefix - tab prefix (e.g., 'norm', 'mp', 'rel')
     * @param {string} key - sub-section key (e.g., 've', 'mft', 'islamic')
     * @param {object} data - sub-section data (count, yearDist, topModels, papers, etc.)
     * @param {Array} [extraCharts] - section-specific chart configs: [{render(data, pfx)}]
     */
    _deepDiveSubSection(prefix, key, data, extraCharts) {
        const countEl = document.getElementById(`${prefix}-${key}-count`);
        if (countEl) countEl.textContent = data.count;
        const listCountEl = document.getElementById(`${prefix}-${key}-list-count`);
        if (listCountEl) listCountEl.textContent = data.count;

        // Standard charts
        this._yearBar(`chart-${prefix}-${key}-year`, data.yearDist);
        this._horizontalBar(`chart-${prefix}-${key}-models`, data.topModels, {
            maxItems: 10, color: this._palette.yellow, emptyText: 'No model data' });

        // Optional standard charts (present on normative/moralpsych, absent on religious)
        if (data.theoryVsEmpirical) {
            const sliceColors = { 'Benchmark / Evaluation': this._palette.green, 'Theoretical / Framework': this._palette.slate };
            const pieData = data.theoryVsEmpirical.map(d => ({ name: d.n, value: d.c, itemStyle: { color: sliceColors[d.n] || this._tc.textSec } }));
            this._donut(`chart-${prefix}-${key}-split`, pieData);
        }
        if (data.venueTypeDist) {
            const vtPie = data.venueTypeDist.map(d => ({ name: d.n, value: d.c, itemStyle: { color: this._vtColors[d.n] || this._palette.slate } }));
            this._donut(`chart-${prefix}-${key}-venue`, vtPie);
        }
        if (data.regionDist && data.regionDist.length) {
            this._horizontalBar(`chart-${prefix}-${key}-regions`, data.regionDist, { maxItems: 8, color: this._palette.pink });
        }

        // Section-specific extras (e.g., virtue keywords, Schwartz radar, Islamic domains)
        if (extraCharts) {
            const fk = `${prefix}-${key}`;
            for (const cfg of extraCharts) cfg.render.call(this, data, fk);
        }

        // Paper list + filter wiring
        renderPaperList(`${prefix}-${key}-papers`, data.papers, 50);
        this._attachSubSectionFilter(prefix, key, data, countEl);
    },

    // ═══════════════════════════════════════════════════════════════════════
    // SHARED HELPERS
    // ═══════════════════════════════════════════════════════════════════════

    _yearBar(chartId, yearDist) {
        const chart = this._get(chartId);
        if (!chart) return;
        const years = Object.keys(yearDist || {}).sort();
        chart.setOption({
            ...this._theme,
            grid: { left: 40, right: 20, top: 10, bottom: 30 },
            xAxis: { type: 'category', data: years, axisLabel: { color: this._tc.textSec, fontSize: 10 } },
            yAxis: { type: 'value', axisLabel: { color: this._tc.textSec }, splitLine: { lineStyle: { color: this._tc.bgPrimary } } },
            tooltip: { ...this._theme.tooltip, trigger: 'axis' },
            series: [{ type: 'bar', data: years.map(y => yearDist[y]), itemStyle: { color: this._palette.accent, borderRadius: [4,4,0,0] } }],
        }, true);
    },

    /**
     * Unified sub-section filter handler — replaces 8 near-identical click-handler blocks
     * with a loop over chart bindings + a dimension→filter-function lookup map.
     */
    _attachSubSectionFilter(prefix, key, data, countEl) {
        const headerH3 = countEl ? countEl.parentElement.querySelector('h3') : null;
        const baseTitle = headerH3 ? headerH3.textContent : '';
        const filterKey = `${prefix}-${key}`;
        const listHeaderEl = document.getElementById(`${prefix}-${key}-list-header`);
        const listH3 = listHeaderEl ? listHeaderEl.querySelector('h3') : null;
        const listCountEl = listHeaderEl ? listHeaderEl.querySelector('.badge') : null;

        // Resolve embedded paper → full paper from main array
        const _r = (sp) => DATA._paperByFn[sp.fn] || sp;

        // Dimension → filter function map
        const filterFns = {
            year: (sp, val) => _r(sp).y === +val,
            model: (sp, val) => (_r(sp).lm || []).includes(val),
            researchType: (sp, val) => val === 'Benchmark / Evaluation' ? _r(sp).ib === 1 : !_r(sp).ib,
            venueType: (sp, val) => _r(sp).vt === val,
            region: (sp, val) => (_r(sp).rg || []).includes(val),
            subTheory: (sp, val) => (sp.st || []).includes(val),
            concept: (sp, val) => (sp.kw || []).includes(val),
            fns: (sp, _val, f) => f._fnSet.has(sp.fn),
        };

        const applyFilter = () => {
            const f = this._subFilter[filterKey];
            let filtered;
            if (!f) {
                filtered = data.papers;
                if (headerH3) headerH3.textContent = baseTitle;
            } else {
                if (f.dim === 'fns') f._fnSet = new Set(f.fns);
                const fn = filterFns[f.dim];
                filtered = fn ? data.papers.filter(sp => fn(sp, f.val, f)) : data.papers;
                if (headerH3) headerH3.textContent = `${baseTitle} \u2014 ${f.val}`;
            }
            if (countEl) countEl.textContent = filtered.length;
            if (listH3) listH3.textContent = headerH3 ? headerH3.textContent : baseTitle;
            if (listCountEl) listCountEl.textContent = filtered.length;
            renderPaperList(`${prefix}-${key}-papers`, filtered, 50);
        };
        this._applyFns[filterKey] = applyFilter;

        // Chart bindings: [chartSuffix, dim, condition?]
        const bindings = [
            ['year', 'year'],
            ['models', 'model'],
            ['split', 'researchType', !!data.theoryVsEmpirical],
            ['venue', 'venueType', !!data.venueTypeDist],
            ['regions', 'region', !!(data.regionDist && data.regionDist.length)],
            ['paradigm', 'subTheory', !!data.subTheories],
            ['virtues', 'concept'],
            ['concepts', 'concept'],
        ];
        for (const [suffix, dim, condition] of bindings) {
            if (condition === false) continue;
            const chart = this._get(`chart-${prefix}-${key}-${suffix}`);
            if (!chart) continue;
            chart.off('click');
            chart.on('click', params => {
                if (!params.name) return;
                const cur = this._subFilter[filterKey];
                if (cur && cur.dim === dim && cur.val === params.name) delete this._subFilter[filterKey];
                else this._subFilter[filterKey] = { dim, val: params.name };
                applyFilter();
            });
        }
    },

    _attachExtFnFilter(filterKey, chartId, resolve) {
        const chart = this._get(chartId);
        if (!chart) return;
        chart.off('click');
        chart.on('click', params => {
            const r = resolve(params);
            if (!r || !r.fns || !r.fns.length) return;
            const cur = this._subFilter[filterKey];
            if (cur && cur.dim === 'fns' && cur.val === r.label) delete this._subFilter[filterKey];
            else this._subFilter[filterKey] = { dim: 'fns', val: r.label, fns: r.fns };
            if (this._applyFns[filterKey]) this._applyFns[filterKey]();
        });
    },

    // ═══════════════════════════════════════════════════════════════════════
    // v7: CHART EXPORT (Step 8)
    // ═══════════════════════════════════════════════════════════════════════

    _injectExportBtn(el, chart, title) {
        const card = el.closest('.chart-card');
        if (!card || card.querySelector('.chart-export-btn')) return;
        const btn = document.createElement('button');
        btn.className = 'chart-export-btn';
        btn.title = 'Export as PNG';
        btn.textContent = '\u2913'; // ⤓
        btn.setAttribute('aria-label', 'Export ' + title + ' as PNG');
        btn.addEventListener('click', (e) => {
            e.stopPropagation();
            const url = chart.getDataURL({ type: 'png', pixelRatio: 2, backgroundColor: getComputedStyle(document.body).getPropertyValue('--bg-card').trim() || '#1e293b' });
            const a = document.createElement('a');
            a.href = url;
            a.download = (title || 'chart').replace(/[^a-zA-Z0-9]+/g, '_').toLowerCase() + '.png';
            a.click();
        });
        card.appendChild(btn);
    },

    // ═══════════════════════════════════════════════════════════════════════
    // v7: TAB — INTERSECTIONS (Cross-Dimensional Analysis)
    // ═══════════════════════════════════════════════════════════════════════

    _initIntersections() {
        const papers = DATA.papers;

        // Helper: get top N items from a frequency map
        const topN = (map, n) => Object.entries(map).sort((a,b) => b[1] - a[1]).slice(0, n).map(e => e[0]);

        // === 1. Model x Ethical Framework ===
        const modelCounts = {};
        papers.forEach(p => (p.lm || []).forEach(m => { modelCounts[m] = (modelCounts[m] || 0) + 1; }));
        const topModels = topN(modelCounts, 15);
        const fwCols = ['VE', 'DE', 'CU', 'Ethics (General)', 'No Ethics'];
        const mfMatrix = topModels.map(m => {
            const mPapers = papers.filter(p => p.lm && p.lm.includes(m));
            return [
                mPapers.filter(p => p.ve).length,
                mPapers.filter(p => p.de).length,
                mPapers.filter(p => p.ue).length,
                mPapers.filter(p => p.eo && !p.ve && !p.de && !p.ue).length,
                mPapers.filter(p => !p.eo).length,
            ];
        });
        this._heatmap('chart-ix-model-ethics', {
            xLabels: fwCols, yLabels: topModels, matrix: mfMatrix,
            grid: { left: 130, right: 60, top: 10, bottom: 40 },
            yFontSize: 10, yLabelWidth: 120, vmColor: this._palette.accent,
            tooltipFmt: p => `${topModels[p.value[1]]} + ${fwCols[p.value[0]]}: ${p.value[2] === '-' ? 0 : p.value[2]}`,
            onClick: params => {
                if (params.value[2] === '-' || params.value[2] === 0) return;
                const model = topModels[params.value[1]];
                const fwIdx = params.value[0];
                const filtered = papers.filter(p => {
                    if (!p.lm || !p.lm.includes(model)) return false;
                    if (fwIdx === 0) return p.ve;
                    if (fwIdx === 1) return p.de;
                    if (fwIdx === 2) return p.ue;
                    if (fwIdx === 3) return p.eo && !p.ve && !p.de && !p.ue;
                    return !p.eo;
                });
                this._showIxDrilldown(`${model} + ${fwCols[fwIdx]}`, filtered);
            },
        });

        // === 2. Model x Culture/Region ===
        const regionMap = {};
        papers.forEach(p => (p.cu || []).forEach(c => {
            regionMap[c] = (regionMap[c] || 0) + 1;
        }));
        const topRegions = topN(regionMap, 10);
        const mcMatrix = topModels.map(m => {
            const mPapers = papers.filter(p => p.lm && p.lm.includes(m));
            return topRegions.map(r => mPapers.filter(p => p.cu && p.cu.includes(r)).length);
        });
        this._heatmap('chart-ix-model-culture', {
            xLabels: topRegions, yLabels: topModels, matrix: mcMatrix,
            grid: { left: 130, right: 60, top: 10, bottom: 80 },
            xRotate: 30, xFontSize: 9, yFontSize: 10, yLabelWidth: 120,
            vmColor: this._palette.pink,
            tooltipFmt: p => `${topModels[p.value[1]]} + ${topRegions[p.value[0]]}: ${p.value[2] === '-' ? 0 : p.value[2]}`,
            onClick: params => {
                if (params.value[2] === '-' || params.value[2] === 0) return;
                const model = topModels[params.value[1]];
                const region = topRegions[params.value[0]];
                const filtered = papers.filter(p => p.lm && p.lm.includes(model) && p.cu && p.cu.includes(region));
                this._showIxDrilldown(`${model} + ${region}`, filtered);
            },
        });

        // === 3. Venue x Dimension ===
        const venueCounts = {};
        papers.forEach(p => { if (p.cc) venueCounts[p.cc] = (venueCounts[p.cc] || 0) + 1; });
        const topVenues = topN(venueCounts, 15);
        const dimCols = ['Ethics', 'Cultural', 'Religious', 'Moral Psych', 'Benchmark'];
        const vdMatrix = topVenues.map(v => {
            const vPapers = papers.filter(p => p.cc === v);
            return [
                vPapers.filter(p => p.eo).length,
                vPapers.filter(p => p.cu && p.cu.length).length,
                vPapers.filter(p => p.rv && p.rv.length).length,
                vPapers.filter(p => p.mp).length,
                vPapers.filter(p => p.ib).length,
            ];
        });
        this._heatmap('chart-ix-venue-dim', {
            xLabels: dimCols, yLabels: topVenues, matrix: vdMatrix,
            grid: { left: 160, right: 60, top: 10, bottom: 40 },
            yFontSize: 10, yLabelWidth: 150, vmColor: this._palette.teal,
            tooltipFmt: p => `${topVenues[p.value[1]]} + ${dimCols[p.value[0]]}: ${p.value[2] === '-' ? 0 : p.value[2]}`,
            onClick: params => {
                if (params.value[2] === '-' || params.value[2] === 0) return;
                const venue = topVenues[params.value[1]];
                const dimIdx = params.value[0];
                const filtered = papers.filter(p => {
                    if (p.cc !== venue) return false;
                    if (dimIdx === 0) return p.eo;
                    if (dimIdx === 1) return p.cu && p.cu.length;
                    if (dimIdx === 2) return p.rv && p.rv.length;
                    if (dimIdx === 3) return p.mp;
                    return p.ib;
                });
                this._showIxDrilldown(`${venue} + ${dimCols[dimIdx]}`, filtered);
            },
        });

        // === 4. Framework x Religion ===
        const fwRows = ['Virtue Ethics', 'Deontological', 'Consequentialism', 'MFT', 'Schwartz', 'Developmental'];
        const relCols = ['Islamic', 'Christianity', 'Judaism', 'Buddhism', 'Hinduism', 'Confucian', 'Ubuntu', 'Indigenous', 'Shinto'];
        const frMatrix = fwRows.map(fw => {
            const fwPapers = papers.filter(p => {
                if (fw === 'Virtue Ethics') return p.ve;
                if (fw === 'Deontological') return p.de;
                if (fw === 'Consequentialism') return p.ue;
                if (fw === 'MFT') return p.mp && p.mp.includes('Moral Foundations');
                if (fw === 'Schwartz') return p.mp && p.mp.includes('Schwartz');
                if (fw === 'Developmental') return p.mp && p.mp.includes('Developmental');
                return false;
            });
            return relCols.map(r => fwPapers.filter(p => p.rv && p.rv.some(rv => rv.toLowerCase().includes(r.toLowerCase()))).length);
        });
        this._heatmap('chart-ix-fw-religion', {
            xLabels: relCols, yLabels: fwRows, matrix: frMatrix,
            grid: { left: 130, right: 60, top: 10, bottom: 80 },
            xRotate: 30, xFontSize: 9, yFontSize: 10, yLabelWidth: 120,
            vmColor: this._palette.orange,
            tooltipFmt: p => `${fwRows[p.value[1]]} + ${relCols[p.value[0]]}: ${p.value[2] === '-' ? 0 : p.value[2]}`,
            onClick: params => {
                if (params.value[2] === '-' || params.value[2] === 0) return;
                const fw = fwRows[params.value[1]];
                const rel = relCols[params.value[0]];
                const filtered = papers.filter(p => {
                    const hasFw = (fw === 'Virtue Ethics' && p.ve) || (fw === 'Deontological' && p.de) || (fw === 'Consequentialism' && p.ue) ||
                                  (fw === 'MFT' && p.mp && p.mp.includes('Moral Foundations')) || (fw === 'Schwartz' && p.mp && p.mp.includes('Schwartz')) ||
                                  (fw === 'Developmental' && p.mp && p.mp.includes('Developmental'));
                    const hasRel = p.rv && p.rv.some(rv => rv.toLowerCase().includes(rel.toLowerCase()));
                    return hasFw && hasRel;
                });
                this._showIxDrilldown(`${fw} + ${rel}`, filtered);
            },
        });

        // Drilldown close handler
        const closeBtn = document.getElementById('ix-drilldown-close');
        if (closeBtn) closeBtn.addEventListener('click', () => {
            document.getElementById('ix-drilldown').style.display = 'none';
        });
    },

    _showIxDrilldown(title, papers) {
        const container = document.getElementById('ix-drilldown');
        if (!container) return;
        document.getElementById('ix-drilldown-title').textContent = `${title} \u2014 ${papers.length} paper${papers.length !== 1 ? 's' : ''}`;
        renderPaperList('ix-drilldown-papers', papers.map(p => ({ fn: p.fn })), 50);
        container.style.display = 'block';
        container.scrollIntoView({ behavior: 'smooth', block: 'start' });
    },

    // ═══════════════════════════════════════════════════════════════════════
    // v7: BENCHMARK DEEP-DIVE (Step 5) — extends _initTaxonomy
    // ═══════════════════════════════════════════════════════════════════════

    _initBenchmarks() {
        const papers = DATA.papers;
        const benchPapers = papers.filter(p => p.ib);
        const total = benchPapers.length;

        // KPIs
        const _s = (id, v) => { const el = document.getElementById(id); if (el) el.textContent = fmt(v); };
        _s('kpi-bench-total', total);
        _s('bench-total', total);
        _s('kpi-bench-ethics', benchPapers.filter(p => p.eo).length);
        _s('kpi-bench-cultural', benchPapers.filter(p => p.cu && p.cu.length).length);
        _s('kpi-bench-religious', benchPapers.filter(p => p.rv && p.rv.length).length);
        _s('bench-list-count', total);

        // Benchmark x Tradition heatmap
        const traditions = [...new Set(papers.flatMap(p => p.rv || []))].sort();
        const topTrad = traditions.slice(0, 12);
        const benchYN = ['Benchmark', 'Non-Benchmark'];
        const btMatrix = benchYN.map(yn => {
            const subset = yn === 'Benchmark' ? benchPapers : papers.filter(p => !p.ib);
            return topTrad.map(t => subset.filter(p => p.rv && p.rv.includes(t)).length);
        });
        this._heatmap('chart-bench-tradition', {
            xLabels: topTrad, yLabels: benchYN, matrix: btMatrix,
            grid: { left: 120, right: 60, top: 10, bottom: 80 },
            xRotate: 30, xFontSize: 9, vmColor: this._palette.yellow,
        });

        // Benchmark language coverage
        const langCounts = {};
        benchPapers.forEach(p => (p.ln || []).forEach(l => { langCounts[l] = (langCounts[l] || 0) + 1; }));
        const langItems = Object.entries(langCounts).sort((a,b) => b[1] - a[1]).slice(0, 20).map(([n, c]) => ({ n, c }));
        this._horizontalBar('chart-bench-lang', langItems, { maxItems: 20, gridLeft: 120, color: this._palette.cyan });

        // Benchmark timeline
        const yearCount = {};
        benchPapers.forEach(p => { if (p.y > 0) yearCount[p.y] = (yearCount[p.y] || 0) + 1; });
        const years = Object.keys(yearCount).sort();
        this._stackedTimeline('chart-bench-timeline', {
            years,
            series: [{ name: 'Benchmarks', type: 'bar', data: years.map(y => yearCount[y]), color: this._palette.yellow, smooth: false }],
        });

        // Benchmark venue type donut
        const vtCount = {};
        benchPapers.forEach(p => { vtCount[p.vt] = (vtCount[p.vt] || 0) + 1; });
        const vtData = Object.entries(vtCount).map(([n, v]) => ({ name: n, value: v, itemStyle: { color: this._vtColors[n] || this._palette.slate } }));
        this._donut('chart-bench-venue', vtData);

        // Paper list
        renderPaperList('bench-papers', benchPapers.map(p => ({ fn: p.fn })), 50);
    },

    // ═══════════════════════════════════════════════════════════════════════
    // v7: MODEL DEPTH ANALYSIS (Step 4) — extends _initModels
    // ═══════════════════════════════════════════════════════════════════════

    _initModelDepth() {
        const papers = DATA.papers;

        // Model x Ethical Framework heatmap (like intersection but with more detail)
        const modelCounts = {};
        papers.forEach(p => (p.lm || []).forEach(m => { modelCounts[m] = (modelCounts[m] || 0) + 1; }));
        const topModels = Object.entries(modelCounts).sort((a,b) => b[1] - a[1]).slice(0, 15).map(e => e[0]);
        const fwCols = ['VE', 'DE', 'CU', 'MFT', 'Schwartz', 'Kohlberg'];
        const mdMatrix = topModels.map(m => {
            const mPapers = papers.filter(p => p.lm && p.lm.includes(m));
            return [
                mPapers.filter(p => p.ve).length,
                mPapers.filter(p => p.de).length,
                mPapers.filter(p => p.ue).length,
                mPapers.filter(p => p.mp && p.mp.includes('Moral Foundations')).length,
                mPapers.filter(p => p.mp && p.mp.includes('Schwartz')).length,
                mPapers.filter(p => p.mp && p.mp.includes('Developmental')).length,
            ];
        });
        this._heatmap('chart-md-model-fw', {
            xLabels: fwCols, yLabels: topModels, matrix: mdMatrix,
            grid: { left: 130, right: 60, top: 10, bottom: 40 },
            yFontSize: 10, yLabelWidth: 120, vmColor: this._palette.violet,
            tooltipFmt: p => `${topModels[p.value[1]]} + ${fwCols[p.value[0]]}: ${p.value[2] === '-' ? 0 : p.value[2]}`,
        });

        // Model cultural exposure bar — distinct cultures per model
        const cultureCounts = topModels.map(m => {
            const cultures = new Set();
            papers.forEach(p => {
                if (p.lm && p.lm.includes(m) && p.cu) p.cu.forEach(c => cultures.add(c));
            });
            return { n: m, c: cultures.size };
        }).sort((a, b) => b.c - a.c);
        this._horizontalBar('chart-md-model-culture', cultureCounts, { maxItems: 15, gridLeft: 130, labelWidth: 120, color: this._palette.pink });

        // Open vs. Closed source donut
        const openModels = ['LLaMA', 'Llama', 'Llama 2', 'Llama 3', 'Mistral', 'Mixtral', 'Falcon', 'BLOOM', 'Vicuna', 'Alpaca', 'Qwen', 'ChatGLM', 'Baichuan', 'DeepSeek', 'Yi', 'OLMo', 'Gemma', 'Phi', 'StableLM', 'MPT'];
        const closedModels = ['GPT-4', 'GPT-3.5', 'GPT-3', 'ChatGPT', 'Claude', 'Claude 2', 'Claude 3', 'Gemini', 'PaLM', 'PaLM 2', 'Bard'];
        let openCount = 0, closedCount = 0, otherCount = 0;
        papers.forEach(p => {
            (p.lm || []).forEach(m => {
                const mLower = m.toLowerCase();
                if (openModels.some(o => mLower.includes(o.toLowerCase()))) openCount++;
                else if (closedModels.some(c => mLower.includes(c.toLowerCase()))) closedCount++;
                else otherCount++;
            });
        });
        this._donut('chart-md-open-closed', [
            { name: 'Open Source', value: openCount, itemStyle: { color: this._palette.green } },
            { name: 'Closed Source', value: closedCount, itemStyle: { color: this._palette.red } },
            { name: 'Other/Unknown', value: otherCount, itemStyle: { color: this._palette.slate } },
        ]);

        // Model coverage breadth — frameworks tested per model
        const breadthData = topModels.map(m => {
            const mPapers = papers.filter(p => p.lm && p.lm.includes(m));
            let dims = 0;
            if (mPapers.some(p => p.ve)) dims++;
            if (mPapers.some(p => p.de)) dims++;
            if (mPapers.some(p => p.ue)) dims++;
            if (mPapers.some(p => p.mp)) dims++;
            if (mPapers.some(p => p.rv && p.rv.length)) dims++;
            if (mPapers.some(p => p.cu && p.cu.length)) dims++;
            return { n: m, c: dims };
        }).sort((a, b) => b.c - a.c);
        this._horizontalBar('chart-md-breadth', breadthData, {
            maxItems: 15, gridLeft: 130, labelWidth: 120, color: this._palette.accent,
            tooltipFmt: p => `${p[0].name}: ${p[0].value} dimensions tested`,
        });
    },

    // ═══════════════════════════════════════════════════════════════════════
    // v7: TIMELINE ENHANCEMENTS (Step 3)
    // ═══════════════════════════════════════════════════════════════════════

    _timelineYoYLabels(chart, yearCount, years) {
        // Add YoY growth labels as markPoints
        if (!chart || years.length < 2) return;
        const markData = [];
        for (let i = 1; i < years.length; i++) {
            const prev = yearCount[years[i-1]] || 0;
            const cur = yearCount[years[i]] || 0;
            if (prev > 0) {
                const pct = Math.round((cur - prev) / prev * 100);
                if (Math.abs(pct) >= 10) {
                    markData.push({
                        xAxis: years[i], yAxis: cur,
                        value: (pct >= 0 ? '+' : '') + pct + '%',
                        symbol: 'none',
                        label: {
                            show: true, position: 'top', fontSize: 9,
                            color: pct >= 0 ? '#22c55e' : '#ef4444',
                            formatter: '{c}',
                        },
                    });
                }
            }
        }
        if (markData.length) {
            chart.setOption({
                series: [{ markPoint: { data: markData, silent: true } }],
            });
        }
    },

};

// Global resize handler (debounced 150ms)
let _resizeTimer = null;
window.addEventListener('resize', () => {
    clearTimeout(_resizeTimer);
    _resizeTimer = setTimeout(() => Charts.resizeAll(), 150);
});
