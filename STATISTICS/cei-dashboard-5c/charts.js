/**
 * CEI Dashboard v5c — Charts Module
 * All ECharts initialization, update, and cross-filter wiring.
 */

const Charts = {
    _instances: {},  // id -> echarts instance
    _subFilter: {},  // "prefix-key" -> { dim: 'year'|'model'|'researchType'|'venueType'|'region'|'concept'|'subTheory', val: string }
    _initialized: new Set(),

    // Get or create an ECharts instance
    _get(id) {
        if (this._instances[id]) return this._instances[id];
        const el = document.getElementById(id);
        if (!el) return null;
        const chart = echarts.init(el, null, { renderer: 'canvas' });
        this._instances[id] = chart;
        return chart;
    },

    resizeAll() {
        requestAnimationFrame(() => {
            Object.values(this._instances).forEach(c => c && c.resize());
        });
    },

    // Dark theme defaults
    _theme: {
        textStyle: { color: '#7d7b76' },
        title: { textStyle: { color: '#d4d2cd', fontSize: 14 } },
        legend: { textStyle: { color: '#7d7b76' }, pageTextStyle: { color: '#7d7b76' } },
        tooltip: {
            backgroundColor: '#0e1019', borderColor: '#1d2033',
            textStyle: { color: '#d4d2cd', fontSize: 12 },
        },
    },

    _colors: ['#e8a44a','#5ec291','#d6c45c','#c47586','#5cb4c9','#df8844','#9c8adb','#4fa89e','#d4605e','#a8c455'],
    _vtColors: {
        'Conference': '#e8a44a', 'Preprint': '#6b6965', 'Journal': '#5ec291',
        'Findings': '#5cb4c9', 'Workshop': '#df8844', 'N/A': '#3d3b37',
    },

    // ═════════════════════════════════════════════════════════════════════
    // TAB INITIALIZATION — Lazy loading
    // ═════════════════════════════════════════════════════════════════════

    initTab(tabId) {
        if (this._initialized.has(tabId)) return;
        this._initialized.add(tabId);

        const papers = FilterState.getFilteredPapers();
        switch (tabId) {
            case 'overview': this._initOverview(papers); break;
            case 'conference': this._initConference(); break;
            case 'taxonomy': this._initTaxonomy(); break;
            case 'cultural': this._initCultural(); break;
            case 'normative': this._initNormative(); break;
            case 'moralpsych': this._initMoralPsych(); break;
            case 'religious': this._initReligious(); break;
            case 'models': this._initModels(); break;
        }

        // Subscribe to filter updates for this tab
        FilterState.subscribe(filtered => {
            if (this._initialized.has(tabId)) {
                this._updateTab(tabId, filtered);
            }
        });
    },

    _updateTab(tabId, papers) {
        switch (tabId) {
            case 'overview': this._updateOverview(papers); break;
            // Other tabs use pre-computed data; full reactivity for overview + explorer
        }
    },

    // ═════════════════════════════════════════════════════════════════════
    // TAB 1: OVERVIEW
    // ═════════════════════════════════════════════════════════════════════

    _initOverview(papers) {
        const D = DATA;
        // KPIs
        document.getElementById('kpi-papers').textContent = fmt(D.agg.total);
        document.getElementById('kpi-candidates').textContent = fmt(D.agg.candidates);
        document.getElementById('kpi-ethics').textContent = fmt(D.agg.ethicsYes);
        document.getElementById('kpi-venues').textContent = fmt(D.conf.uniqueVenues);
        document.getElementById('kpi-authors').textContent = fmt(D.agg.authorCount);
        document.getElementById('kpi-llm').textContent = fmt(D.agg.llmAssessed);

        this._chartTimeline(papers);
        this._chartVenueDonut(papers);
        this._chartCategoryBar();
        this._chartTopAuthors();
        this._chartAvailability();
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
        const counts = years.map(y => yearCount[y]);
        chart.setOption({
            ...this._theme,
            color: this._colors,
            grid: { left: 50, right: 20, top: 30, bottom: 40 },
            xAxis: { type: 'category', data: years, axisLabel: { color: '#7d7b76' }, axisLine: { lineStyle: { color: '#1d2033' } } },
            yAxis: { type: 'value', axisLabel: { color: '#7d7b76' }, splitLine: { lineStyle: { color: '#0e1019' } } },
            tooltip: { ...this._theme.tooltip, trigger: 'axis' },
            series: [{
                type: 'bar', data: counts, itemStyle: { color: '#e8a44a', borderRadius: [4,4,0,0] },
                emphasis: { itemStyle: { color: '#f2c87d' } },
            }],
        }, true);
        chart.off('click');
        chart.on('click', params => {
            if (params.name) FilterState.toggle('year', +params.name);
        });
    },

    _chartVenueDonut(papers) {
        const chart = this._get('chart-venue-donut');
        if (!chart) return;
        const vtCount = {};
        papers.forEach(p => { vtCount[p.vt] = (vtCount[p.vt]||0) + 1; });
        const data = Object.entries(vtCount).map(([n, v]) => ({
            name: n, value: v,
            itemStyle: { color: this._vtColors[n] || '#4a4844' }
        }));
        chart.setOption({
            ...this._theme,
            tooltip: { ...this._theme.tooltip, trigger: 'item', formatter: '{b}: {c} ({d}%)' },
            series: [{
                type: 'pie', radius: ['40%', '70%'], center: ['50%', '50%'],
                data, label: { color: '#7d7b76', fontSize: 12 },
                emphasis: { label: { show: true, fontSize: 14, fontWeight: 'bold' } },
            }],
        }, true);
        chart.off('click');
        chart.on('click', params => {
            if (params.name) FilterState.toggle('venueType', params.name);
        });
    },

    _chartCategoryBar() {
        const chart = this._get('chart-category-bar');
        if (!chart) return;
        const cats = DATA.taxonomy.categories.slice(0, 10);
        chart.setOption({
            ...this._theme,
            grid: { left: 220, right: 30, top: 10, bottom: 20 },
            xAxis: { type: 'value', axisLabel: { color: '#7d7b76' }, splitLine: { lineStyle: { color: '#0e1019' } } },
            yAxis: { type: 'category', data: cats.map(c => c.n).reverse(), axisLabel: { color: '#7d7b76', fontSize: 11, width: 200, overflow: 'truncate' } },
            tooltip: { ...this._theme.tooltip, trigger: 'axis' },
            series: [{
                type: 'bar', data: cats.map(c => c.c).reverse(),
                itemStyle: { color: '#e8a44a', borderRadius: [0,4,4,0] },
            }],
        }, true);
    },

    _chartTopAuthors() {
        const chart = this._get('chart-top-authors');
        if (!chart) return;
        const authors = DATA.agg.topAuthors.slice(0, 15);
        chart.setOption({
            ...this._theme,
            grid: { left: 150, right: 30, top: 10, bottom: 20 },
            xAxis: { type: 'value', axisLabel: { color: '#7d7b76' }, splitLine: { lineStyle: { color: '#0e1019' } } },
            yAxis: { type: 'category', data: authors.map(a => a.n).reverse(), axisLabel: { color: '#7d7b76', fontSize: 11, width: 140, overflow: 'truncate' } },
            tooltip: { ...this._theme.tooltip, trigger: 'axis' },
            series: [{
                type: 'bar', data: authors.map(a => a.c).reverse(),
                itemStyle: { color: '#5ec291', borderRadius: [0,4,4,0] },
            }],
        }, true);
    },

    _chartAvailability() {
        const chart = this._get('chart-availability');
        if (!chart) return;
        const av = DATA.agg.availability;
        const data = Object.entries(av).filter(([,v]) => v > 0).map(([n, v]) => ({ name: n, value: v }));
        chart.setOption({
            ...this._theme,
            color: this._colors,
            tooltip: { ...this._theme.tooltip, trigger: 'item', formatter: '{b}: {c} ({d}%)' },
            series: [{
                type: 'pie', radius: ['35%', '65%'], center: ['50%', '50%'],
                data, label: { color: '#7d7b76', fontSize: 11 },
            }],
        }, true);
    },

    // ═════════════════════════════════════════════════════════════════════
    // TAB 3: CONFERENCE & VENUE
    // ═════════════════════════════════════════════════════════════════════

    _initConference() {
        const C = DATA.conf;

        // KPIs
        const vt = DATA.agg.vtDist || {};
        document.getElementById('kpi-conf-venues').textContent = fmt(C.uniqueVenues);
        document.getElementById('kpi-conf-conf').textContent = fmt(vt.Conference || 0);
        const peerReviewed = (vt.Conference||0) + (vt.Journal||0) + (vt.Findings||0) + (vt.Workshop||0);
        document.getElementById('kpi-conf-peer').textContent = fmt(peerReviewed);
        document.getElementById('kpi-conf-preprint').textContent = fmt(vt.Preprint || 0);

        // Venue type donut
        this._confDonut(vt);
        // Top 30 venues
        this._confTop30(C.topVenues);
        // Conference family treemap
        this._confTreemap(C.families);
        // Ecosystem donut
        this._confEcosystem(C.ecosystem);
        // Family x year heatmap
        this._confHeatmap(C.heatmap, C.hmYears);
        // Journals bar
        this._confJournals(C.journals);
        // Timeline
        this._confTimeline(C.timeline);
        // Peer-review ratio
        this._confPeerRatio(C.peerRatio);
    },

    _confDonut(vt) {
        const chart = this._get('chart-conf-donut');
        if (!chart) return;
        const data = Object.entries(vt).map(([n, v]) => ({
            name: n, value: v, itemStyle: { color: this._vtColors[n] || '#4a4844' }
        }));
        chart.setOption({
            ...this._theme,
            tooltip: { ...this._theme.tooltip, trigger: 'item', formatter: '{b}: {c} ({d}%)' },
            series: [{ type: 'pie', radius: ['40%','70%'], data, label: { color: '#7d7b76' } }],
        }, true);
        chart.off('click');
        chart.on('click', p => { if (p.name) FilterState.toggle('venueType', p.name); });
    },

    _confTop30(venues) {
        const chart = this._get('chart-conf-top30');
        if (!chart) return;
        const v = venues.slice(0, 30);
        chart.setOption({
            ...this._theme,
            grid: { left: 200, right: 30, top: 10, bottom: 20 },
            xAxis: { type: 'value', axisLabel: { color: '#7d7b76' }, splitLine: { lineStyle: { color: '#0e1019' } } },
            yAxis: { type: 'category', data: v.map(x => x.n).reverse(), axisLabel: { color: '#7d7b76', fontSize: 10, width: 190, overflow: 'truncate' } },
            tooltip: { ...this._theme.tooltip, trigger: 'axis' },
            series: [{
                type: 'bar', data: v.map(x => ({
                    value: x.c, itemStyle: { color: this._vtColors[x.vt] || '#e8a44a' }
                })).reverse(),
                barMaxWidth: 20,
            }],
        }, true);
        chart.off('click');
        chart.on('click', p => { if (p.name) FilterState.toggle('venue', p.name); });
    },

    _confTreemap(families) {
        const chart = this._get('chart-conf-treemap');
        if (!chart) return;
        const ecoColors = { 'NLP/CL': '#e8a44a', 'ML/AI': '#5ec291', 'AI Ethics': '#e8a44a', 'Other': '#4a4844' };
        const ecoGroups = {};
        families.forEach(f => {
            if (!ecoGroups[f.eco]) ecoGroups[f.eco] = [];
            ecoGroups[f.eco].push({ name: f.n, value: f.c });
        });
        const data = Object.entries(ecoGroups).map(([eco, children]) => ({
            name: eco, itemStyle: { color: ecoColors[eco] || '#4a4844' },
            children,
        }));
        chart.setOption({
            ...this._theme,
            tooltip: { ...this._theme.tooltip },
            series: [{
                type: 'treemap', data,
                label: { show: true, color: '#fff', fontSize: 11 },
                breadcrumb: { show: false },
                levels: [
                    { itemStyle: { borderColor: '#07080d', borderWidth: 2 } },
                    { itemStyle: { borderColor: '#07080d', borderWidth: 1, gapWidth: 1 },
                      colorSaturation: [0.3, 0.7] },
                ],
            }],
        }, true);
        chart.off('click');
        chart.on('click', p => {
            if (p.data && p.data.children === undefined) {
                FilterState.toggle('confFamily', p.name);
            }
        });
    },

    _confEcosystem(eco) {
        const chart = this._get('chart-conf-ecosystem');
        if (!chart) return;
        const ecoColors = { 'NLP/CL': '#e8a44a', 'ML/AI': '#5ec291', 'AI Ethics': '#e8a44a', 'Other': '#4a4844' };
        const data = eco.map(e => ({ name: e.n, value: e.c, itemStyle: { color: ecoColors[e.n] } }));
        chart.setOption({
            ...this._theme,
            tooltip: { ...this._theme.tooltip, trigger: 'item', formatter: '{b}: {c} ({d}%)' },
            series: [{ type: 'pie', radius: ['40%','70%'], data, label: { color: '#7d7b76' } }],
        }, true);
    },

    _confHeatmap(heatmap, years) {
        const chart = this._get('chart-conf-heatmap');
        if (!chart) return;
        const fams = heatmap.map(h => h.n);
        const hmData = [];
        let maxVal = 0;
        heatmap.forEach((row, fi) => {
            row.d.forEach((val, yi) => {
                hmData.push([yi, fi, val || '-']);
                if (val > maxVal) maxVal = val;
            });
        });
        chart.setOption({
            ...this._theme,
            grid: { left: 120, right: 60, top: 30, bottom: 40 },
            xAxis: { type: 'category', data: years.map(String), axisLabel: { color: '#7d7b76' }, splitArea: { show: true, areaStyle: { color: ['transparent'] } } },
            yAxis: { type: 'category', data: fams, inverse: true, axisLabel: { color: '#7d7b76', fontSize: 11 } },
            tooltip: { ...this._theme.tooltip, formatter: p => `${fams[p.value[1]]} ${years[p.value[0]]}: ${p.value[2]}` },
            visualMap: { min: 0, max: maxVal, calculable: true, orient: 'vertical', right: 10, top: 30, inRange: { color: ['#0e1019', '#e8a44a'] }, textStyle: { color: '#7d7b76' } },
            series: [{
                type: 'heatmap', data: hmData,
                label: { show: true, color: '#d4d2cd', fontSize: 11, formatter: p => p.value[2] === '-' ? '' : p.value[2] },
            }],
        }, true);
        chart.off('click');
        chart.on('click', params => {
            if (params.value[2] === '-' || params.value[2] === 0) return;
            const year = years[params.value[0]];
            const family = fams[params.value[1]];
            this._showHeatmapDrilldown(family, year);
        });
    },

    _heatmapExpandedIdx: null,

    _showHeatmapDrilldown(family, year) {
        const container = document.getElementById('heatmap-drilldown');
        if (!container) return;

        const papers = DATA.papers.filter(p => p.cf === family && p.y === year);

        document.getElementById('heatmap-drilldown-title').textContent =
            `${family} ${year} — ${papers.length} paper${papers.length !== 1 ? 's' : ''}`;

        this._heatmapExpandedIdx = null;
        this._renderHeatmapTable(papers);

        container.style.display = 'block';
        container.scrollIntoView({ behavior: 'smooth', block: 'start' });

        document.getElementById('heatmap-drilldown-close').onclick = () => {
            container.style.display = 'none';
        };
    },

    _renderHeatmapTable(papers) {
        const tbody = document.getElementById('heatmap-drilldown-tbody');
        if (!tbody) return;

        const sorted = [...papers].sort((a, b) => a.t.localeCompare(b.t));
        let html = '';
        for (const p of sorted) {
            const vtClass = `vt-${p.vt === 'N/A' ? 'NA' : p.vt}`;
            const ethBadges = _ethicsBadges(p);
            const flags = [];
            if (p.ib) flags.push('<span class="flag-badge fb-B" title="Benchmark">B</span>');
            if (p.ie) flags.push('<span class="flag-badge fb-E" title="Eval">E</span>');
            if (p.id) flags.push('<span class="flag-badge fb-D" title="Dataset">D</span>');
            if (p.cu && p.cu.length) flags.push('<span class="flag-badge fb-C" title="Cultural">C</span>');
            if (p.rv && p.rv.length) flags.push('<span class="flag-badge fb-R" title="Religious">R</span>');

            html += `<tr class="paper-row" data-idx="${p.i}">
                <td class="col-year">${p.y || '—'}</td>
                <td class="col-paper">
                    <div class="paper-title">${esc(p.t)}</div>
                    <div class="paper-authors">${esc(p.fa)}${p.la ? ', ' + esc(p.la) : ''}</div>
                </td>
                <td class="col-venue"><span class="venue-badge ${vtClass}" title="${esc(p.cc)}">${esc(p.cc)}</span></td>
                <td class="col-ethics"><div class="eth-badges">${ethBadges}</div></td>
                <td class="col-flags"><div class="flag-badges">${flags.join('')}</div></td>
            </tr>`;

            if (this._heatmapExpandedIdx === p.i) {
                html += this._renderHeatmapDetail(p);
            }
        }
        if (!sorted.length) {
            html = '<tr><td colspan="5" style="color:var(--text-muted);padding:16px;">No papers found.</td></tr>';
        }
        tbody.innerHTML = html;

        tbody.querySelectorAll('.paper-row').forEach(row => {
            row.addEventListener('click', () => {
                const idx = +row.dataset.idx;
                this._heatmapExpandedIdx = this._heatmapExpandedIdx === idx ? null : idx;
                this._renderHeatmapTable(papers);
            });
        });
    },

    _renderHeatmapDetail(p) {
        const links = [];
        if (p.url) links.push(`<a href="${esc(p.url)}" target="_blank">Paper URL</a>`);
        if (p.doi) links.push(`<a href="https://doi.org/${esc(p.doi)}" target="_blank">DOI</a>`);
        if (p.du) links.push(`<a href="${esc(p.du)}" target="_blank">Data/Code</a>`);

        const ethDetail = [];
        if (p.eo) ethDetail.push('Ethics: Yes');
        if (p.ve) ethDetail.push('Virtue Ethics');
        if (p.de) ethDetail.push('Deontological');
        if (p.ue) ethDetail.push('Consequentialism/Utilitarianism');
        if (p.mp) ethDetail.push('Moral Psych: ' + p.mp);

        return `<tr class="detail-row"><td colspan="5">
            <div class="paper-detail">
                <div class="detail-grid">
                    <div class="detail-field"><span class="detail-label">Venue</span><span class="detail-value">${esc(p.cc)} (${p.vt})</span></div>
                    <div class="detail-field"><span class="detail-label">Year</span><span class="detail-value">${p.y || '—'}</span></div>
                    <div class="detail-field"><span class="detail-label">Ethics</span><span class="detail-value">${ethDetail.join(', ') || '—'}</span></div>
                    <div class="detail-field"><span class="detail-label">Benchmark</span><span class="detail-value">${esc(p.bn) || '—'}</span></div>
                    <div class="detail-field"><span class="detail-label">Measures</span><span class="detail-value">${esc(p.wm) || '—'}</span></div>
                    <div class="detail-field"><span class="detail-label">Cultures</span><span class="detail-value">${(p.cu||[]).join(', ') || '—'}</span></div>
                    <div class="detail-field"><span class="detail-label">Languages</span><span class="detail-value">${(p.ln||[]).join(', ') || '—'}</span></div>
                    <div class="detail-field"><span class="detail-label">Religion</span><span class="detail-value">${(p.rv||[]).join(', ') || '—'}</span></div>
                    <div class="detail-field"><span class="detail-label">Models</span><span class="detail-value">${(p.lm||[]).join(', ') || '—'}</span></div>
                    <div class="detail-field"><span class="detail-label">Links</span><span class="detail-value">${links.join(' | ') || '—'}</span></div>
                    <div class="detail-field"><span class="detail-label">File</span><span class="detail-value">${esc(p.fn)}</span></div>
                </div>
                ${p.ab ? `<div class="abstract-text"><strong>Abstract:</strong> ${esc(p.ab)}</div>` : ''}
            </div>
        </td></tr>`;
    },

    _confJournals(journals) {
        const chart = this._get('chart-conf-journals');
        if (!chart) return;
        const j = journals.slice(0, 20);
        chart.setOption({
            ...this._theme,
            grid: { left: 250, right: 30, top: 10, bottom: 20 },
            xAxis: { type: 'value', axisLabel: { color: '#7d7b76' }, splitLine: { lineStyle: { color: '#0e1019' } } },
            yAxis: { type: 'category', data: j.map(x => x.n).reverse(), axisLabel: { color: '#7d7b76', fontSize: 10, width: 240, overflow: 'truncate' } },
            tooltip: { ...this._theme.tooltip, trigger: 'axis' },
            series: [{ type: 'bar', data: j.map(x => x.c).reverse(), itemStyle: { color: '#5ec291', borderRadius: [0,4,4,0] } }],
        }, true);
    },

    _confTimeline(tl) {
        const chart = this._get('chart-conf-timeline');
        if (!chart) return;
        const types = ['Conference', 'Preprint', 'Journal', 'Findings', 'Workshop'];
        const series = types.map(t => ({
            name: t, type: 'bar', stack: 'total',
            data: tl[t] || [], itemStyle: { color: this._vtColors[t] },
        }));
        chart.setOption({
            ...this._theme,
            grid: { left: 50, right: 20, top: 40, bottom: 40 },
            legend: { ...this._theme.legend, top: 0, data: types },
            xAxis: { type: 'category', data: tl.years.map(String), axisLabel: { color: '#7d7b76' } },
            yAxis: { type: 'value', axisLabel: { color: '#7d7b76' }, splitLine: { lineStyle: { color: '#0e1019' } } },
            tooltip: { ...this._theme.tooltip, trigger: 'axis' },
            series,
        }, true);
    },

    _confPeerRatio(ratio) {
        const chart = this._get('chart-conf-peer-ratio');
        if (!chart) return;
        chart.setOption({
            ...this._theme,
            grid: { left: 50, right: 20, top: 30, bottom: 40 },
            xAxis: { type: 'category', data: ratio.map(r => String(r.y)), axisLabel: { color: '#7d7b76' } },
            yAxis: { type: 'value', max: 100, axisLabel: { color: '#7d7b76', formatter: '{value}%' }, splitLine: { lineStyle: { color: '#0e1019' } } },
            tooltip: { ...this._theme.tooltip, trigger: 'axis', formatter: p => `${p[0].name}: ${p[0].value}% peer-reviewed` },
            series: [{
                type: 'line', data: ratio.map(r => r.pct), smooth: true,
                lineStyle: { color: '#e8a44a', width: 3 },
                itemStyle: { color: '#e8a44a' },
                areaStyle: { color: { type: 'linear', x: 0, y: 0, x2: 0, y2: 1, colorStops: [{offset: 0, color: 'rgba(232,164,74,0.3)'}, {offset: 1, color: 'rgba(232,164,74,0.0)'}] } },
            }],
        }, true);
    },

    // ═════════════════════════════════════════════════════════════════════
    // TAB 4: TAXONOMY & METHODS
    // ═════════════════════════════════════════════════════════════════════

    _initTaxonomy() {
        const T = DATA.taxonomy;

        // Category x Year heatmap
        this._taxHeatmap(T);
        // Co-occurrence
        this._taxCooccurrence(T);
        // Models
        this._taxModels(T);
    },

    _taxHeatmap(T) {
        const chart = this._get('chart-tax-heatmap');
        if (!chart) return;
        const cats = T.categories;
        const allYears = new Set();
        cats.forEach(c => Object.keys(c.byYear).forEach(y => allYears.add(y)));
        const years = [...allYears].sort();
        const hmData = [];
        let maxVal = 0;
        cats.forEach((c, ci) => {
            years.forEach((y, yi) => {
                const v = c.byYear[y] || 0;
                hmData.push([yi, ci, v || '-']);
                if (v > maxVal) maxVal = v;
            });
        });
        chart.setOption({
            ...this._theme,
            grid: { left: 220, right: 60, top: 10, bottom: 40 },
            xAxis: { type: 'category', data: years, axisLabel: { color: '#7d7b76' }, position: 'bottom' },
            yAxis: { type: 'category', data: cats.map(c => c.n), axisLabel: { color: '#7d7b76', fontSize: 10, width: 210, overflow: 'truncate' } },
            tooltip: { ...this._theme.tooltip },
            visualMap: { min: 0, max: maxVal, orient: 'vertical', right: 10, top: 10, inRange: { color: ['#0e1019', '#e8a44a'] }, textStyle: { color: '#7d7b76' } },
            series: [{
                type: 'heatmap', data: hmData,
                label: { show: true, color: '#d4d2cd', fontSize: 10, formatter: p => p.value[2] === '-' ? '' : p.value[2] },
            }],
        }, true);
    },

    _taxCooccurrence(T) {
        const chart = this._get('chart-tax-cooccurrence');
        if (!chart) return;
        const names = T.catNames;
        const hmData = [];
        let maxVal = 0;
        T.cooccurrence.forEach((row, i) => {
            row.forEach((val, j) => {
                hmData.push([j, i, val || '-']);
                if (val > maxVal) maxVal = val;
            });
        });
        chart.setOption({
            ...this._theme,
            grid: { left: 200, right: 60, top: 40, bottom: 100 },
            xAxis: { type: 'category', data: names, axisLabel: { color: '#7d7b76', fontSize: 9, rotate: 45 } },
            yAxis: { type: 'category', data: names, axisLabel: { color: '#7d7b76', fontSize: 9, width: 190, overflow: 'truncate' } },
            tooltip: { ...this._theme.tooltip },
            visualMap: { min: 0, max: maxVal, orient: 'vertical', right: 10, inRange: { color: ['#0e1019', '#5ec291'] }, textStyle: { color: '#7d7b76' } },
            series: [{
                type: 'heatmap', data: hmData,
                label: { show: true, color: '#d4d2cd', fontSize: 9, formatter: p => p.value[2] === '-' ? '' : p.value[2] },
            }],
        }, true);
    },

    _taxModels(T) {
        const chart = this._get('chart-tax-models');
        if (!chart) return;
        const models = T.models.slice(0, 15);
        chart.setOption({
            ...this._theme,
            grid: { left: 130, right: 30, top: 10, bottom: 20 },
            xAxis: { type: 'value', axisLabel: { color: '#7d7b76' }, splitLine: { lineStyle: { color: '#0e1019' } } },
            yAxis: { type: 'category', data: models.map(m => m.n).reverse(), axisLabel: { color: '#7d7b76', fontSize: 11 } },
            tooltip: { ...this._theme.tooltip, trigger: 'axis' },
            series: [{ type: 'bar', data: models.map(m => m.c).reverse(), itemStyle: { color: '#e8a44a', borderRadius: [0,4,4,0] } }],
        }, true);
    },

    // ═════════════════════════════════════════════════════════════════════
    // TAB 5: CULTURAL VALUES
    // ═════════════════════════════════════════════════════════════════════

    _initCultural() {
        const C = DATA.cultural;
        this._cultRegionDonut(C.regionDist);
        this._cultRegionTimeline(C.timeline);
        this._cultCountryBar(C.countryDist);
        this._cultLangBar(C.langDist);
        this._cultWeirdPie(C.weird);
        this._cultTreemap(C.treemap);
        // Paper lists for Countries and Languages sub-tabs
        this._cultInitPaperList('country', 'cu');
        this._cultInitPaperList('lang', 'ln');
    },

    _cultRegionDonut(dist) {
        const chart = this._get('chart-cult-region-donut');
        if (!chart) return;
        chart.setOption({
            ...this._theme, color: this._colors,
            tooltip: { ...this._theme.tooltip, trigger: 'item', formatter: '{b}: {c} ({d}%)' },
            series: [{ type: 'pie', radius: ['35%','70%'], data: dist.map(d => ({ name: d.n, value: d.c })), label: { color: '#7d7b76', fontSize: 11 } }],
        }, true);
    },

    _cultRegionTimeline(tl) {
        const chart = this._get('chart-cult-region-timeline');
        if (!chart) return;
        const regions = tl.regions.filter(r => tl.series[r] && tl.series[r].some(v => v > 0));
        const series = regions.slice(0, 8).map((r, i) => ({
            name: r, type: 'line', stack: 'total', areaStyle: {},
            data: tl.series[r], smooth: true,
        }));
        chart.setOption({
            ...this._theme, color: this._colors,
            grid: { left: 50, right: 20, top: 40, bottom: 40 },
            legend: { ...this._theme.legend, top: 0, type: 'scroll' },
            xAxis: { type: 'category', data: tl.years.map(String), axisLabel: { color: '#7d7b76' } },
            yAxis: { type: 'value', axisLabel: { color: '#7d7b76' }, splitLine: { lineStyle: { color: '#0e1019' } } },
            tooltip: { ...this._theme.tooltip, trigger: 'axis' },
            series,
        }, true);
    },

    _cultCountryBar(dist) {
        const chart = this._get('chart-cult-country-bar');
        if (!chart) return;
        const d = dist.slice(0, 30);
        chart.setOption({
            ...this._theme,
            grid: { left: 130, right: 30, top: 10, bottom: 20 },
            xAxis: { type: 'value', axisLabel: { color: '#7d7b76' }, splitLine: { lineStyle: { color: '#0e1019' } } },
            yAxis: { type: 'category', data: d.map(x => x.n).reverse(), axisLabel: { color: '#7d7b76', fontSize: 11 } },
            tooltip: { ...this._theme.tooltip, trigger: 'axis' },
            series: [{ type: 'bar', data: d.map(x => x.c).reverse(), itemStyle: { color: '#c47586', borderRadius: [0,4,4,0] } }],
        }, true);
    },

    _cultLangBar(dist) {
        const chart = this._get('chart-cult-lang-bar');
        if (!chart) return;
        const d = dist.slice(0, 20);
        chart.setOption({
            ...this._theme,
            grid: { left: 110, right: 30, top: 10, bottom: 20 },
            xAxis: { type: 'value', axisLabel: { color: '#7d7b76' }, splitLine: { lineStyle: { color: '#0e1019' } } },
            yAxis: { type: 'category', data: d.map(x => x.n).reverse(), axisLabel: { color: '#7d7b76', fontSize: 11 } },
            tooltip: { ...this._theme.tooltip, trigger: 'axis' },
            series: [{ type: 'bar', data: d.map(x => x.c).reverse(), itemStyle: { color: '#5cb4c9', borderRadius: [0,4,4,0] } }],
        }, true);
    },

    _cultWeirdPie(weird) {
        const chart = this._get('chart-cult-weird-pie');
        if (!chart) return;
        const wColors = { WEIRD: '#d4605e', 'Non-WEIRD': '#5ec291', Mixed: '#e8a44a' };
        const data = Object.entries(weird).map(([n, v]) => ({ name: n, value: v, itemStyle: { color: wColors[n] } }));
        chart.setOption({
            ...this._theme,
            tooltip: { ...this._theme.tooltip, trigger: 'item', formatter: '{b}: {c} ({d}%)' },
            series: [{ type: 'pie', radius: ['35%','70%'], data, label: { color: '#7d7b76' } }],
        }, true);
    },

    _cultTreemap(treemap) {
        const chart = this._get('chart-cult-treemap');
        if (!chart) return;
        const data = treemap.map(r => ({
            name: r.n,
            children: r.ch.map(c => ({ name: c.n, value: c.v })),
        }));
        chart.setOption({
            ...this._theme, color: this._colors,
            series: [{
                type: 'treemap', data,
                label: { show: true, color: '#fff', fontSize: 11 },
                breadcrumb: { show: false },
                levels: [
                    { itemStyle: { borderColor: '#07080d', borderWidth: 2 } },
                    { colorSaturation: [0.3, 0.7], itemStyle: { borderColor: '#07080d', borderWidth: 1 } },
                ],
            }],
        }, true);
    },

    _cultInitPaperList(key, dim) {
        const countEl = document.getElementById(`cult-${key}-count`);
        const headerH3 = countEl ? countEl.parentElement.querySelector('h3') : null;
        const baseTitle = headerH3 ? headerH3.textContent : '';
        const filterKey = `cult-${key}`;
        const containerId = `cult-${key}-papers`;

        // All papers that have at least one value in this dimension
        const allPapers = DATA.papers.filter(p => p[dim] && p[dim].length);

        if (countEl) countEl.textContent = allPapers.length;
        renderPaperList(containerId, allPapers, 50);

        const applyFilter = () => {
            const f = this._subFilter[filterKey];
            let filtered;
            if (!f) {
                filtered = allPapers;
                if (headerH3) headerH3.textContent = baseTitle;
            } else {
                filtered = DATA.papers.filter(p => {
                    const arr = p[dim];
                    return arr && arr.includes(f.val);
                });
                if (headerH3) headerH3.textContent = `${baseTitle} \u2014 ${f.val}`;
            }
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
                if (cur && cur.val === params.name) {
                    delete this._subFilter[filterKey];
                } else {
                    this._subFilter[filterKey] = { dim: dim, val: params.name };
                }
                applyFilter();
            });
        }
    },

    // ═════════════════════════════════════════════════════════════════════
    // TAB 6: NORMATIVE ETHICS
    // ═════════════════════════════════════════════════════════════════════

    _initNormative() {
        const N = DATA.normative;

        // Classification donut
        this._normClassDonut(N);
        // Framework bar
        this._normFwBar(N.frameworks);
        // Timeline
        this._normTimeline(N.timelineFw);
        // VE/DE/CU sub-sections
        this._normSubSection('ve', N.ve);
        if (N.ve.virtueKeywords) this._virtueBar('chart-norm-ve-virtues', N.ve.virtueKeywords);
        this._normSubSection('de', N.de);
        if (N.de.deontConcepts) this._conceptBar('chart-norm-de-concepts', N.de.deontConcepts, '#f2c87d');
        this._normSubSection('cu', N.cu);
        if (N.cu.cuConcepts) this._conceptBar('chart-norm-cu-concepts', N.cu.cuConcepts, '#e8a44a');
        // Overlap
        this._normOverlap(N.overlap);
    },

    _normClassDonut(N) {
        const chart = this._get('chart-norm-class-donut');
        if (!chart) return;
        const data = [
            { name: 'Yes', value: N.yes, itemStyle: { color: '#5ec291' } },
            { name: 'Borderline', value: N.borderline, itemStyle: { color: '#e8a44a' } },
            { name: 'Excluded', value: N.excluded, itemStyle: { color: '#4a4844' } },
        ];
        chart.setOption({
            ...this._theme,
            tooltip: { ...this._theme.tooltip, trigger: 'item', formatter: '{b}: {c} ({d}%)' },
            series: [{ type: 'pie', radius: ['40%','70%'], data, label: { color: '#7d7b76' } }],
        }, true);
    },

    _normFwBar(fws) {
        const chart = this._get('chart-norm-fw-bar');
        if (!chart) return;
        chart.setOption({
            ...this._theme,
            grid: { left: 200, right: 30, top: 10, bottom: 20 },
            xAxis: { type: 'value', axisLabel: { color: '#7d7b76' }, splitLine: { lineStyle: { color: '#0e1019' } } },
            yAxis: { type: 'category', data: fws.map(f => f.n).reverse(), axisLabel: { color: '#7d7b76', fontSize: 10, width: 190, overflow: 'truncate' } },
            tooltip: { ...this._theme.tooltip, trigger: 'axis' },
            series: [{ type: 'bar', data: fws.map(f => f.c).reverse(), itemStyle: { color: '#e8a44a', borderRadius: [0,4,4,0] } }],
        }, true);
    },

    _normTimeline(tl) {
        const chart = this._get('chart-norm-timeline');
        if (!chart) return;
        const fwColors = { ve: '#5ec291', de: '#e8a44a', cu: '#e8a44a' };
        const fwNames = { ve: 'Virtue Ethics', de: 'Deontological', cu: 'Consequentialism' };
        chart.setOption({
            ...this._theme,
            grid: { left: 50, right: 20, top: 40, bottom: 40 },
            legend: { ...this._theme.legend, top: 0, data: Object.values(fwNames) },
            xAxis: { type: 'category', data: (tl.years||[]).map(String), axisLabel: { color: '#7d7b76' } },
            yAxis: { type: 'value', axisLabel: { color: '#7d7b76' }, splitLine: { lineStyle: { color: '#0e1019' } } },
            tooltip: { ...this._theme.tooltip, trigger: 'axis' },
            series: ['ve','de','cu'].map(k => ({
                name: fwNames[k], type: 'line', data: tl[k] || [], smooth: true,
                lineStyle: { color: fwColors[k], width: 2 },
                itemStyle: { color: fwColors[k] },
            })),
        }, true);
    },

    _normSubSection(key, data) {
        // Count badge
        const countEl = document.getElementById(`norm-${key}-count`);
        if (countEl) countEl.textContent = data.count;
        const listCountEl = document.getElementById(`norm-${key}-list-count`);
        if (listCountEl) listCountEl.textContent = data.count;

        // Year chart
        this._yearBar(`chart-norm-${key}-year`, data.yearDist);
        // Models chart
        this._modelsBar(`chart-norm-${key}-models`, data.topModels);
        // Theory vs Empirical donut (container exists only for VE currently)
        if (data.theoryVsEmpirical) this._theoryDonut(`chart-norm-${key}-split`, data.theoryVsEmpirical);
        // Venue type donut
        if (data.venueTypeDist) this._venueTypeDonutSm(`chart-norm-${key}-venue`, data.venueTypeDist);
        // Region bar
        if (data.regionDist && data.regionDist.length) this._regionBarSm(`chart-norm-${key}-regions`, data.regionDist);
        // Paper list
        renderPaperList(`norm-${key}-papers`, data.papers, 50);
        this._attachSubSectionFilter('norm', key, data, countEl);
    },

    /**
     * Attach click-to-filter on Year & Model bar charts for any sub-section.
     * Clicking a bar filters the papers list; clicking the same bar toggles off.
     */
    _attachSubSectionFilter(prefix, key, data, countEl) {
        const headerH3 = countEl ? countEl.parentElement.querySelector('h3') : null;
        const baseTitle = headerH3 ? headerH3.textContent : '';
        const filterKey = `${prefix}-${key}`;
        const listHeaderEl = document.getElementById(`${prefix}-${key}-list-header`);
        const listH3 = listHeaderEl ? listHeaderEl.querySelector('h3') : null;
        const listCountEl = listHeaderEl ? listHeaderEl.querySelector('.badge') : null;

        const applyFilter = () => {
            const f = this._subFilter[filterKey];
            let filtered;
            if (!f) {
                filtered = data.papers;
                if (headerH3) headerH3.textContent = baseTitle;
            } else if (f.dim === 'year') {
                filtered = data.papers.filter(sp => sp.y === +f.val);
                if (headerH3) headerH3.textContent = `${baseTitle} — ${f.val}`;
            } else if (f.dim === 'model') {
                filtered = data.papers.filter(sp => (sp.lm || []).includes(f.val));
                if (headerH3) headerH3.textContent = `${baseTitle} — ${f.val}`;
            } else if (f.dim === 'researchType') {
                filtered = data.papers.filter(sp =>
                    f.val === 'Benchmark / Evaluation' ? sp.ib === 1 : !sp.ib
                );
                if (headerH3) headerH3.textContent = `${baseTitle} — ${f.val}`;
            } else if (f.dim === 'venueType') {
                filtered = data.papers.filter(sp => sp.vt === f.val);
                if (headerH3) headerH3.textContent = `${baseTitle} — ${f.val}`;
            } else if (f.dim === 'region') {
                filtered = data.papers.filter(sp => (sp.rg || []).includes(f.val));
                if (headerH3) headerH3.textContent = `${baseTitle} — ${f.val}`;
            } else if (f.dim === 'subTheory') {
                filtered = data.papers.filter(sp => (sp.st || []).includes(f.val));
                if (headerH3) headerH3.textContent = `${baseTitle} — ${f.val}`;
            } else if (f.dim === 'concept') {
                filtered = data.papers.filter(sp => (sp.kw || []).includes(f.val));
                if (headerH3) headerH3.textContent = `${baseTitle} — ${f.val}`;
            } else if (f.dim === 'fns') {
                const fnSet = new Set(f.fns);
                filtered = data.papers.filter(sp => fnSet.has(sp.fn));
                if (headerH3) headerH3.textContent = `${baseTitle} — ${f.val}`;
            }
            if (countEl) countEl.textContent = filtered.length;
            if (listH3) listH3.textContent = headerH3 ? headerH3.textContent : baseTitle;
            if (listCountEl) listCountEl.textContent = filtered.length;
            renderPaperList(`${prefix}-${key}-papers`, filtered, 50);
        };

        if (!this._applyFns) this._applyFns = {};
        this._applyFns[filterKey] = applyFilter;

        const yearChart = this._get(`chart-${prefix}-${key}-year`);
        if (yearChart) {
            yearChart.off('click');
            yearChart.on('click', params => {
                if (!params.name) return;
                const cur = this._subFilter[filterKey];
                if (cur && cur.dim === 'year' && cur.val === params.name) {
                    delete this._subFilter[filterKey];
                } else {
                    this._subFilter[filterKey] = { dim: 'year', val: params.name };
                }
                applyFilter();
            });
        }

        const modelsChart = this._get(`chart-${prefix}-${key}-models`);
        if (modelsChart) {
            modelsChart.off('click');
            modelsChart.on('click', params => {
                if (!params.name) return;
                const cur = this._subFilter[filterKey];
                if (cur && cur.dim === 'model' && cur.val === params.name) {
                    delete this._subFilter[filterKey];
                } else {
                    this._subFilter[filterKey] = { dim: 'model', val: params.name };
                }
                applyFilter();
            });
        }

        // Only attach research-type/venue/region handlers when the data has those fields
        if (data.theoryVsEmpirical) {
            const splitChart = this._get(`chart-${prefix}-${key}-split`);
            if (splitChart) {
                splitChart.off('click');
                splitChart.on('click', params => {
                    if (!params.name) return;
                    const cur = this._subFilter[filterKey];
                    if (cur && cur.dim === 'researchType' && cur.val === params.name) {
                        delete this._subFilter[filterKey];
                    } else {
                        this._subFilter[filterKey] = { dim: 'researchType', val: params.name };
                    }
                    applyFilter();
                });
            }
        }

        if (data.venueTypeDist) {
            const venueChart = this._get(`chart-${prefix}-${key}-venue`);
            if (venueChart) {
                venueChart.off('click');
                venueChart.on('click', params => {
                    if (!params.name) return;
                    const cur = this._subFilter[filterKey];
                    if (cur && cur.dim === 'venueType' && cur.val === params.name) {
                        delete this._subFilter[filterKey];
                    } else {
                        this._subFilter[filterKey] = { dim: 'venueType', val: params.name };
                    }
                    applyFilter();
                });
            }
        }

        if (data.regionDist && data.regionDist.length) {
            const regionChart = this._get(`chart-${prefix}-${key}-regions`);
            if (regionChart) {
                regionChart.off('click');
                regionChart.on('click', params => {
                    if (!params.name) return;
                    const cur = this._subFilter[filterKey];
                    if (cur && cur.dim === 'region' && cur.val === params.name) {
                        delete this._subFilter[filterKey];
                    } else {
                        this._subFilter[filterKey] = { dim: 'region', val: params.name };
                    }
                    applyFilter();
                });
            }
        }

        if (data.subTheories) {
            const paradigmChart = this._get(`chart-${prefix}-${key}-paradigm`);
            if (paradigmChart) {
                paradigmChart.off('click');
                paradigmChart.on('click', params => {
                    if (!params.name) return;
                    const cur = this._subFilter[filterKey];
                    if (cur && cur.dim === 'subTheory' && cur.val === params.name) {
                        delete this._subFilter[filterKey];
                    } else {
                        this._subFilter[filterKey] = { dim: 'subTheory', val: params.name };
                    }
                    applyFilter();
                });
            }
        }

        // Concepts / Virtues bar (VE uses "-virtues" suffix, DE/CU use "-concepts")
        const conceptChart = this._get(`chart-${prefix}-${key}-virtues`)
                          || this._get(`chart-${prefix}-${key}-concepts`);
        if (conceptChart) {
            conceptChart.off('click');
            conceptChart.on('click', params => {
                if (!params.name) return;
                const cur = this._subFilter[filterKey];
                if (cur && cur.dim === 'concept' && cur.val === params.name) {
                    delete this._subFilter[filterKey];
                } else {
                    this._subFilter[filterKey] = { dim: 'concept', val: params.name };
                }
                applyFilter();
            });
        }
    },

    /**
     * Attach click-to-filter on an extended chart using pre-computed fns arrays.
     * resolve(params) should return {label, fns} or null.
     */
    _attachExtFnFilter(filterKey, chartId, resolve) {
        const chart = this._get(chartId);
        if (!chart) return;
        chart.off('click');
        chart.on('click', params => {
            const r = resolve(params);
            if (!r || !r.fns || !r.fns.length) return;
            const cur = this._subFilter[filterKey];
            if (cur && cur.dim === 'fns' && cur.val === r.label) {
                delete this._subFilter[filterKey];
            } else {
                this._subFilter[filterKey] = { dim: 'fns', val: r.label, fns: r.fns };
            }
            if (this._applyFns && this._applyFns[filterKey]) {
                this._applyFns[filterKey]();
            }
        });
    },

    _normOverlap(overlap) {
        // --- Existing overlap bar chart ---
        const chart = this._get('chart-norm-overlap');
        if (chart) {
            const data = [
                { name: 'VE + DE', value: overlap.ve_de },
                { name: 'VE + CU', value: overlap.ve_cu },
                { name: 'DE + CU', value: overlap.de_cu },
                { name: 'All Three', value: overlap.all },
            ];
            chart.setOption({
                ...this._theme,
                grid: { left: 100, right: 30, top: 10, bottom: 20 },
                xAxis: { type: 'value', axisLabel: { color: '#7d7b76' }, splitLine: { lineStyle: { color: '#0e1019' } } },
                yAxis: { type: 'category', data: data.map(d => d.name).reverse(), axisLabel: { color: '#7d7b76' } },
                tooltip: { ...this._theme.tooltip, trigger: 'axis' },
                series: [{ type: 'bar', data: data.map(d => d.value).reverse(), itemStyle: { color: '#9c8adb', borderRadius: [0,4,4,0] } }],
            }, true);

            // --- Click-to-filter on overlap bar → paper list ---
            const paperKeys = { 'VE + DE': 've_de_papers', 'VE + CU': 've_cu_papers',
                                'DE + CU': 'de_cu_papers', 'All Three': 'all_papers' };
            const countEl = document.getElementById('norm-overlap-count');
            const headerH3 = countEl ? countEl.parentElement.querySelector('h3') : null;
            let activeFilter = null;

            // Default: show all overlap papers
            if (countEl) countEl.textContent = (overlap.any_papers || []).length;
            renderPaperList('norm-overlap-papers', overlap.any_papers || [], 50);

            chart.off('click');
            chart.on('click', params => {
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
            });
        }

        // --- New charts ---
        this._normOverlapTimeline(overlap.overlapTimeline);
        this._normOverlapExclusivity(overlap.exclusivity);
        this._normOverlapModels(overlap.overlapModels);
        this._normOverlapRegion(overlap.regionHeatmap);
        this._normOverlapBench(overlap);
    },

    _normOverlapTimeline(data) {
        const chart = this._get('chart-norm-overlap-timeline');
        if (!chart || !data) return;
        const colors = { ve_de: '#d487a0', ve_cu: '#e0a060', de_cu: '#7dba97', all: '#b0a0e0' };
        const names = { ve_de: 'VE + DE', ve_cu: 'VE + CU', de_cu: 'DE + CU', all: 'All Three' };
        chart.setOption({
            ...this._theme,
            grid: { left: 50, right: 20, top: 40, bottom: 40 },
            legend: { ...this._theme.legend, top: 0, data: Object.values(names) },
            xAxis: { type: 'category', data: (data.years || []).map(String), axisLabel: { color: '#7d7b76' } },
            yAxis: { type: 'value', axisLabel: { color: '#7d7b76' }, splitLine: { lineStyle: { color: '#0e1019' } } },
            tooltip: { ...this._theme.tooltip, trigger: 'axis' },
            series: ['ve_de', 've_cu', 'de_cu', 'all'].map(k => ({
                name: names[k], type: 'line', data: data[k] || [], smooth: true,
                stack: 'overlap', areaStyle: { opacity: 0.4 },
                lineStyle: { color: colors[k], width: 2 },
                itemStyle: { color: colors[k] },
            })),
        }, true);
    },

    _normOverlapExclusivity(excl) {
        const chart = this._get('chart-norm-overlap-excl');
        if (!chart || !excl) return;
        const fwColors = { ve: '#5ec291', de: '#e8a44a', cu: '#e8a44a' };
        const fwNames = { ve: 'Virtue Ethics', de: 'Deontological', cu: 'Consequentialism' };
        const subLabels = {
            ve: [['VE only','only'],['+ DE','ve_de'],['+ CU','ve_cu'],['All 3','all']],
            de: [['DE only','only'],['+ VE','ve_de'],['+ CU','de_cu'],['All 3','all']],
            cu: [['CU only','only'],['+ VE','ve_cu'],['+ DE','de_cu'],['All 3','all']],
        };
        const data = ['ve','de','cu'].map(fw => {
            const d = excl[fw];
            const base = fwColors[fw];
            const children = subLabels[fw].map(([label, key], i) => ({
                name: `${label} (${d[key]})`, value: d[key],
                itemStyle: { color: i === 0 ? base : (i === 3 ? '#9c8adb' : base + '88') },
            }));
            const sum = children.reduce((s, c) => s + c.value, 0);
            return { name: `${fwNames[fw]} (${sum})`, itemStyle: { color: base }, children };
        });
        chart.setOption({
            ...this._theme,
            tooltip: { ...this._theme.tooltip },
            series: [{
                type: 'sunburst', data, radius: ['15%', '90%'],
                label: { color: '#d4d2cd', fontSize: 10, overflow: 'truncate', width: 70 },
                itemStyle: { borderColor: '#07080d', borderWidth: 1 },
                levels: [
                    {},
                    { r0: '15%', r: '50%', label: { fontSize: 12 } },
                    { r0: '50%', r: '90%', label: { fontSize: 10 } },
                ],
            }],
        }, true);
    },

    _normOverlapModels(models) {
        const chart = this._get('chart-norm-overlap-models');
        if (!chart || !models) return;
        const colors = { ve_de: '#d487a0', ve_cu: '#e0a060', de_cu: '#7dba97', all: '#b0a0e0' };
        const names = { ve_de: 'VE + DE', ve_cu: 'VE + CU', de_cu: 'DE + CU', all: 'All Three' };
        // Union all model names, order by total count
        const totals = {};
        for (const combo of ['ve_de', 've_cu', 'de_cu', 'all']) {
            for (const m of (models[combo] || [])) {
                totals[m.n] = (totals[m.n] || 0) + m.c;
            }
        }
        const modelNames = Object.entries(totals).sort((a, b) => b[1] - a[1]).slice(0, 8).map(e => e[0]);
        if (!modelNames.length) {
            chart.setOption({ ...this._theme, graphic: { type: 'text', left: 'center', top: 'center', style: { text: 'No model data', fill: '#4a4844' } } }, true);
            return;
        }
        // Build lookup per combo
        const comboLookup = {};
        for (const combo of ['ve_de', 've_cu', 'de_cu', 'all']) {
            const lk = {};
            for (const m of (models[combo] || [])) lk[m.n] = m.c;
            comboLookup[combo] = lk;
        }
        chart.setOption({
            ...this._theme,
            grid: { left: 120, right: 20, top: 40, bottom: 20 },
            legend: { ...this._theme.legend, top: 0, data: Object.values(names) },
            xAxis: { type: 'value', axisLabel: { color: '#7d7b76' }, splitLine: { lineStyle: { color: '#0e1019' } } },
            yAxis: { type: 'category', data: [...modelNames].reverse(), axisLabel: { color: '#7d7b76', fontSize: 10 } },
            tooltip: { ...this._theme.tooltip, trigger: 'axis' },
            series: ['ve_de', 've_cu', 'de_cu', 'all'].map(combo => ({
                name: names[combo], type: 'bar',
                data: [...modelNames].reverse().map(n => comboLookup[combo][n] || 0),
                itemStyle: { color: colors[combo], borderRadius: [0, 4, 4, 0] },
            })),
        }, true);
    },

    _normOverlapRegion(data) {
        const chart = this._get('chart-norm-overlap-region');
        if (!chart || !data) return;
        const hmData = [];
        let maxVal = 0;
        (data.matrix || []).forEach((row, i) => {
            row.forEach((val, j) => {
                hmData.push([j, i, val || '-']);
                if (val > maxVal) maxVal = val;
            });
        });
        chart.setOption({
            ...this._theme,
            grid: { left: 90, right: 60, top: 10, bottom: 80 },
            xAxis: { type: 'category', data: data.regionLabels || [], axisLabel: { color: '#7d7b76', fontSize: 10, rotate: 30 } },
            yAxis: { type: 'category', data: data.comboLabels || [], axisLabel: { color: '#7d7b76', fontSize: 10 } },
            tooltip: { ...this._theme.tooltip },
            visualMap: { min: 0, max: Math.max(maxVal, 1), orient: 'vertical', right: 10, inRange: { color: ['#0e1019', '#9c8adb'] }, textStyle: { color: '#7d7b76' } },
            series: [{
                type: 'heatmap', data: hmData,
                label: { show: true, color: '#d4d2cd', fontSize: 10, formatter: p => p.value[2] === '-' ? '' : p.value[2] },
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
            xAxis: { type: 'value', max: 100, axisLabel: { color: '#7d7b76', formatter: '{value}%' }, splitLine: { lineStyle: { color: '#0e1019' } } },
            yAxis: { type: 'category', data: bars.map(b => b.name).reverse(), axisLabel: { color: '#7d7b76' } },
            tooltip: { ...this._theme.tooltip, trigger: 'axis', formatter: params => {
                const p = params[0];
                const b = bars.find(x => x.name === p.name);
                return b ? `${b.name}: ${b.count}/${b.total} (${b.pct}%)` : '';
            }},
            series: [{
                type: 'bar',
                data: bars.map(b => ({
                    value: b.pct,
                    itemStyle: { color: b.name === 'Single FW' ? '#4a4844' : '#4fa89e', borderRadius: [0, 4, 4, 0] },
                })).reverse(),
                label: {
                    show: true, position: 'right', color: '#7d7b76', fontSize: 10,
                    formatter: p => { const b = bars[bars.length - 1 - p.dataIndex]; return `${b.count}/${b.total}`; },
                },
            }],
        }, true);
    },

    // ═════════════════════════════════════════════════════════════════════
    // TAB 7: MORAL PSYCHOLOGY
    // ═════════════════════════════════════════════════════════════════════

    _initMoralPsych() {
        const M = DATA.moralPsych;

        // Theory bar
        this._mpTheoryBar(M.theoryDist);
        // Timeline
        this._mpTimeline(M.timeline);
        // Cooccurrence
        this._mpCooccurrence(M.cooccurrence, M.coLabels);
        // MFT sub-section
        this._mpMFT(M.mft);
        // Schwartz sub-section
        this._mpSubSection('schwartz', M.schwartz);
        // Developmental sub-section
        this._mpSubSection('dev', M.developmental);
    },

    _mpTheoryBar(dist) {
        const chart = this._get('chart-mp-theory-bar');
        if (!chart) return;
        chart.setOption({
            ...this._theme,
            grid: { left: 200, right: 30, top: 10, bottom: 20 },
            xAxis: { type: 'value', axisLabel: { color: '#7d7b76' }, splitLine: { lineStyle: { color: '#0e1019' } } },
            yAxis: { type: 'category', data: dist.map(d => d.n).reverse(), axisLabel: { color: '#7d7b76', fontSize: 11 } },
            tooltip: { ...this._theme.tooltip, trigger: 'axis' },
            series: [{ type: 'bar', data: dist.map(d => ({ value: d.c, itemStyle: { color: d.col } })).reverse() }],
        }, true);
    },

    _mpTimeline(tl) {
        const chart = this._get('chart-mp-timeline');
        if (!chart) return;
        const series = [
            { name: 'MFT', data: tl.mft, color: '#e8a44a' },
            { name: 'Schwartz', data: tl.schwartz, color: '#5cb4c9' },
            { name: 'Developmental', data: tl.dev, color: '#e8a44a' },
        ].map(s => ({
            name: s.name, type: 'line', data: s.data || [], smooth: true,
            lineStyle: { color: s.color, width: 2 }, itemStyle: { color: s.color },
        }));
        chart.setOption({
            ...this._theme,
            grid: { left: 50, right: 20, top: 40, bottom: 40 },
            legend: { ...this._theme.legend, top: 0 },
            xAxis: { type: 'category', data: (tl.years||[]).map(String), axisLabel: { color: '#7d7b76' } },
            yAxis: { type: 'value', axisLabel: { color: '#7d7b76' }, splitLine: { lineStyle: { color: '#0e1019' } } },
            tooltip: { ...this._theme.tooltip, trigger: 'axis' },
            series,
        }, true);
    },

    _mpCooccurrence(matrix, labels) {
        const chart = this._get('chart-mp-cooccurrence');
        if (!chart) return;
        const hmData = [];
        let maxVal = 0;
        matrix.forEach((row, i) => {
            row.forEach((val, j) => {
                hmData.push([j, i, val || '-']);
                if (val > maxVal) maxVal = val;
            });
        });
        chart.setOption({
            ...this._theme,
            grid: { left: 120, right: 60, top: 40, bottom: 80 },
            xAxis: { type: 'category', data: labels, axisLabel: { color: '#7d7b76', fontSize: 10, rotate: 30 } },
            yAxis: { type: 'category', data: labels, axisLabel: { color: '#7d7b76', fontSize: 10 } },
            tooltip: { ...this._theme.tooltip },
            visualMap: { min: 0, max: Math.max(maxVal, 1), orient: 'vertical', right: 10, inRange: { color: ['#0e1019', '#c47586'] }, textStyle: { color: '#7d7b76' } },
            series: [{
                type: 'heatmap', data: hmData,
                label: { show: true, color: '#d4d2cd', fontSize: 10, formatter: p => p.value[2] === '-' ? '' : p.value[2] },
            }],
        }, true);
    },

    _mpMFT(mft) {
        const countEl = document.getElementById('mp-mft-count');
        if (countEl) countEl.textContent = mft.count;
        const listCountEl = document.getElementById('mp-mft-list-count');
        if (listCountEl) listCountEl.textContent = mft.count;

        // Year distribution bar
        this._yearBar('chart-mp-mft-year', mft.yearDist);

        // MFT radar
        const chart = this._get('chart-mp-mft-radar');
        if (chart) {
            chart.setOption({
                ...this._theme,
                radar: {
                    indicator: mft.foundations.map(f => ({ name: f.n, max: Math.max(...mft.foundations.map(f => f.c), 1) })),
                    axisName: { color: '#7d7b76', fontSize: 11 },
                    splitLine: { lineStyle: { color: '#1d2033' } },
                    splitArea: { areaStyle: { color: ['transparent'] } },
                },
                series: [{
                    type: 'radar',
                    data: [{ value: mft.foundations.map(f => f.c), name: 'MFT Foundations', areaStyle: { color: 'rgba(232,164,74,0.3)' } }],
                    lineStyle: { color: '#e8a44a' }, itemStyle: { color: '#e8a44a' },
                }],
            }, true);
        }

        // Models bar
        this._modelsBar('chart-mp-mft-models', mft.topModels);
        // Research type split
        if (mft.theoryVsEmpirical) this._theoryDonut('chart-mp-mft-split', mft.theoryVsEmpirical);
        // Venue type distribution
        if (mft.venueTypeDist) this._venueTypeDonutSm('chart-mp-mft-venue', mft.venueTypeDist);
        // Geographic focus
        if (mft.regionDist && mft.regionDist.length) this._regionBarSm('chart-mp-mft-regions', mft.regionDist);
        // Paper list
        renderPaperList('mp-mft-papers', mft.papers, 50);
        this._attachSubSectionFilter('mp', 'mft', mft, countEl);
    },

    _mpSubSection(key, data) {
        const countEl = document.getElementById(`mp-${key}-count`);
        if (countEl) countEl.textContent = data.count;
        const listCountEl = document.getElementById(`mp-${key}-list-count`);
        if (listCountEl) listCountEl.textContent = data.count;
        this._yearBar(`chart-mp-${key}-year`, data.yearDist);
        this._modelsBar(`chart-mp-${key}-models`, data.topModels);
        // Paradigm breakdown (Developmental sub-theories)
        if (data.subTheories) this._subTheoryBar(`chart-mp-${key}-paradigm`, data.subTheories);
        // Schwartz value radar
        if (data.valueDims) this._schwartzRadar(`chart-mp-${key}-radar`, data.valueDims);
        // Research type split
        if (data.theoryVsEmpirical) this._theoryDonut(`chart-mp-${key}-split`, data.theoryVsEmpirical);
        // Venue type distribution
        if (data.venueTypeDist) this._venueTypeDonutSm(`chart-mp-${key}-venue`, data.venueTypeDist);
        // Geographic focus
        if (data.regionDist && data.regionDist.length) this._regionBarSm(`chart-mp-${key}-regions`, data.regionDist);
        // Paper list
        renderPaperList(`mp-${key}-papers`, data.papers, 50);
        this._attachSubSectionFilter('mp', key, data, countEl);
    },

    // ═════════════════════════════════════════════════════════════════════
    // TAB 8: RELIGIOUS VALUES
    // ═════════════════════════════════════════════════════════════════════

    _initReligious() {
        const R = DATA.religious;

        // Tradition bar
        this._relTradBar(R.traditionDist);
        // Timeline
        this._relTimeline(R.timeline);
        // Cooccurrence
        this._relCooccurrence(R.cooccurrence, R.coLabels);
        // Sub-sections
        this._relSubSection('islamic', R.islamic);
        this._relIslamicExtended(R.islamic);
        this._relSubSection('christian', R.christianJewish);
        this._relChristianExtended(R.christianJewish);
        this._relSubSection('dharmic', R.dharmic);
        this._relDharmicExtended(R.dharmic);
        this._relSubSection('confucian', R.confucian);
        this._relConfucianExtended(R.confucian);
        this._relSubSection('ubuntu', R.ubuntuIndigenous);
        this._relUbuntuExtended(R.ubuntuIndigenous);
    },

    _relTradBar(dist) {
        const chart = this._get('chart-rel-trad-bar');
        if (!chart) return;
        chart.setOption({
            ...this._theme,
            grid: { left: 120, right: 30, top: 10, bottom: 20 },
            xAxis: { type: 'value', axisLabel: { color: '#7d7b76' }, splitLine: { lineStyle: { color: '#0e1019' } } },
            yAxis: { type: 'category', data: dist.map(d => d.n).reverse(), axisLabel: { color: '#7d7b76', fontSize: 11 } },
            tooltip: { ...this._theme.tooltip, trigger: 'axis' },
            series: [{ type: 'bar', data: dist.map(d => ({ value: d.c, itemStyle: { color: d.col } })).reverse() }],
        }, true);
        chart.off('click');
        chart.on('click', p => { if (p.name) FilterState.toggle('religion', p.name); });
    },

    _relTimeline(tl) {
        const chart = this._get('chart-rel-timeline');
        if (!chart) return;
        const seriesConfig = [
            { key: 'abrahamic', name: 'Abrahamic', color: '#e8a44a' },
            { key: 'dharmic', name: 'Dharmic', color: '#e8a44a' },
            { key: 'eastAsian', name: 'East Asian', color: '#5cb4c9' },
            { key: 'africanIndigenous', name: 'African/Indigenous', color: '#df8844' },
        ];
        chart.setOption({
            ...this._theme,
            grid: { left: 50, right: 20, top: 40, bottom: 40 },
            legend: { ...this._theme.legend, top: 0 },
            xAxis: { type: 'category', data: (tl.years||[]).map(String), axisLabel: { color: '#7d7b76' } },
            yAxis: { type: 'value', axisLabel: { color: '#7d7b76' }, splitLine: { lineStyle: { color: '#0e1019' } } },
            tooltip: { ...this._theme.tooltip, trigger: 'axis' },
            series: seriesConfig.map(s => ({
                name: s.name, type: 'line', data: tl[s.key] || [], smooth: true,
                lineStyle: { color: s.color, width: 2 }, itemStyle: { color: s.color },
            })),
        }, true);
    },

    _relCooccurrence(matrix, labels) {
        const chart = this._get('chart-rel-cooccurrence');
        if (!chart) return;
        const hmData = [];
        let maxVal = 0;
        matrix.forEach((row, i) => {
            row.forEach((val, j) => {
                hmData.push([j, i, val || '-']);
                if (val > maxVal) maxVal = val;
            });
        });
        chart.setOption({
            ...this._theme,
            grid: { left: 110, right: 60, top: 40, bottom: 80 },
            xAxis: { type: 'category', data: labels, axisLabel: { color: '#7d7b76', fontSize: 10, rotate: 30 } },
            yAxis: { type: 'category', data: labels, axisLabel: { color: '#7d7b76', fontSize: 10 } },
            tooltip: { ...this._theme.tooltip },
            visualMap: { min: 0, max: Math.max(maxVal, 1), orient: 'vertical', right: 10, inRange: { color: ['#0e1019', '#df8844'] }, textStyle: { color: '#7d7b76' } },
            series: [{
                type: 'heatmap', data: hmData,
                label: { show: true, color: '#d4d2cd', fontSize: 10, formatter: p => p.value[2] === '-' ? '' : p.value[2] },
            }],
        }, true);
    },

    _relSubSection(key, data) {
        const countEl = document.getElementById(`rel-${key}-count`);
        if (countEl) countEl.textContent = data.count;
        const listCountEl = document.getElementById(`rel-${key}-list-count`);
        if (listCountEl) listCountEl.textContent = data.count;
        this._yearBar(`chart-rel-${key}-year`, data.yearDist);
        this._modelsBar(`chart-rel-${key}-models`, data.topModels);
        renderPaperList(`rel-${key}-papers`, data.papers, 50);
        this._attachSubSectionFilter('rel', key, data, countEl);
    },

    // ─────────────────────────────────────────────────────────────────────
    // RELIGIOUS SUB-SECTION EXTENDED CHARTS
    // ─────────────────────────────────────────────────────────────────────

    // ── Islamic: 5 extended charts ────────────────────────────────────────
    _relIslamicExtended(data) {
        if (!data) return;

        // 1. Domain treemap
        {
            const chart = this._get('chart-rel-islamic-domains');
            if (chart) {
                const items = (data.domainDist || []).map(d => ({ name: d.n, value: d.c }));
                if (items.length) {
                    chart.setOption({
                        ...this._theme,
                        tooltip: { ...this._theme.tooltip, formatter: p => `${p.name}: ${p.value}` },
                        series: [{
                            type: 'treemap',
                            data: items,
                            roam: false,
                            breadcrumb: { show: false },
                            label: { color: '#d4d2cd', fontSize: 11 },
                            itemStyle: { borderColor: '#07080d', borderWidth: 2 },
                            levels: [{ color: ['#2a3520','#15803d','#16a34a','#5ec291','#4ade80','#5ec291'], colorMappingBy: 'index' }],
                        }],
                    }, true);
                }
            }
        }

        // 2. Language / geo bar (horizontal, colored by region)
        {
            const chart = this._get('chart-rel-islamic-langgeo');
            if (chart) {
                const d = (data.langGeo || []).slice(0, 12);
                if (d.length) {
                    const regionColors = {
                        'Middle East': '#5ec291', 'South Asia': '#e8a44a',
                        'Southeast Asia': '#5cb4c9', 'Africa': '#df8844',
                        'Global': '#e8a44a', 'Other': '#4a4844',
                    };
                    chart.setOption({
                        ...this._theme,
                        grid: { left: 110, right: 20, top: 10, bottom: 20 },
                        xAxis: { type: 'value', axisLabel: { color: '#7d7b76' }, splitLine: { lineStyle: { color: '#0e1019' } } },
                        yAxis: { type: 'category', data: d.map(x => x.lang).reverse(), axisLabel: { color: '#7d7b76', fontSize: 11 } },
                        tooltip: { ...this._theme.tooltip, trigger: 'axis', formatter: p => `${p[0].name}: ${p[0].value} (${d.find(x => x.lang === p[0].name)?.region || ''})` },
                        series: [{
                            type: 'bar',
                            data: d.map(x => ({ value: x.c, itemStyle: { color: regionColors[x.region] || '#4a4844', borderRadius: [0,4,4,0] } })).reverse(),
                        }],
                    }, true);
                }
            }
        }

        // 3. Resource vs Bias streams (stacked area / dual-line)
        {
            const chart = this._get('chart-rel-islamic-streams');
            if (chart) {
                const sl = data.streamTimeline || {};
                const years = (sl.years || []).map(String);
                if (years.length) {
                    chart.setOption({
                        ...this._theme,
                        grid: { left: 50, right: 20, top: 40, bottom: 40 },
                        legend: { ...this._theme.legend, top: 0 },
                        xAxis: { type: 'category', data: years, axisLabel: { color: '#7d7b76' } },
                        yAxis: { type: 'value', axisLabel: { color: '#7d7b76' }, splitLine: { lineStyle: { color: '#0e1019' } } },
                        tooltip: { ...this._theme.tooltip, trigger: 'axis' },
                        series: [
                            {
                                name: 'Resource', type: 'line', data: sl.resource || [], smooth: true,
                                lineStyle: { color: '#5ec291', width: 2 }, itemStyle: { color: '#5ec291' },
                                areaStyle: { color: 'rgba(94,194,145,0.2)' },
                            },
                            {
                                name: 'Bias', type: 'line', data: sl.bias || [], smooth: true,
                                lineStyle: { color: '#d4605e', width: 2 }, itemStyle: { color: '#d4605e' },
                                areaStyle: { color: 'rgba(212,96,94,0.2)' },
                            },
                        ],
                    }, true);
                }
            }
        }

        // 4. Source coverage radar
        {
            const chart = this._get('chart-rel-islamic-sources');
            if (chart) {
                const d = data.sourceCoverage || [];
                if (d.length) {
                    const maxVal = Math.max(...d.map(x => x.val), 1);
                    chart.setOption({
                        ...this._theme,
                        radar: {
                            triggerEvent: true,
                            indicator: d.map(x => ({ name: x.axis, max: maxVal })),
                            axisName: { color: '#7d7b76', fontSize: 10 },
                            splitLine: { lineStyle: { color: '#1d2033' } },
                            splitArea: { areaStyle: { color: ['#07080d', '#0e1019'] } },
                            axisLine: { lineStyle: { color: '#1d2033' } },
                        },
                        series: [{
                            type: 'radar',
                            data: [{
                                value: d.map(x => x.val),
                                name: 'Source Coverage',
                                areaStyle: { color: 'rgba(94,194,145,0.3)' },
                            }],
                            lineStyle: { color: '#5ec291' },
                            itemStyle: { color: '#5ec291' },
                        }],
                    }, true);
                }
            }
        }

        // 5. Co-traditions (rendered as horizontal bar showing flow values)
        {
            const chart = this._get('chart-rel-islamic-sankey');
            if (chart) {
                const flows = data.coTraditions || [];
                if (flows.length) {
                    const tradColors = {
                        'Christianity': '#e8a44a', 'Judaism': '#9c8adb',
                        'Buddhism': '#e8a44a', 'Hinduism': '#c47586',
                        'Confucian': '#5cb4c9', 'Ubuntu': '#df8844',
                        'Indigenous': '#4fa89e', 'Shinto': '#c490d8',
                    };
                    const sorted = [...flows].sort((a, b) => b.value - a.value);
                    chart.setOption({
                        ...this._theme,
                        grid: { left: 130, right: 20, top: 10, bottom: 20 },
                        xAxis: { type: 'value', axisLabel: { color: '#7d7b76' }, splitLine: { lineStyle: { color: '#0e1019' } } },
                        yAxis: { type: 'category', data: sorted.map(f => f.target).reverse(), axisLabel: { color: '#7d7b76', fontSize: 11 } },
                        tooltip: { ...this._theme.tooltip, trigger: 'axis' },
                        series: [{
                            type: 'bar',
                            data: sorted.map(f => ({ value: f.value, itemStyle: { color: tradColors[f.target] || '#4a4844', borderRadius: [0,4,4,0] } })).reverse(),
                        }],
                    }, true);
                }
            }
        }

        // ── Click-to-filter wiring for extended charts ──
        const fk = 'rel-islamic';
        this._attachExtFnFilter(fk, 'chart-rel-islamic-domains',
            p => { const d = (data.domainDist||[]).find(x => x.n === p.name); return d ? {label: d.n, fns: d.fns} : null; });
        this._attachExtFnFilter(fk, 'chart-rel-islamic-langgeo',
            p => { const d = (data.langGeo||[]).find(x => x.lang === p.name); return d ? {label: d.lang, fns: d.fns} : null; });
        this._attachExtFnFilter(fk, 'chart-rel-islamic-streams',
            p => { const fns = (data.streamTimelineFns||{})[p.seriesName]; return fns ? {label: p.seriesName, fns} : null; });
        this._attachExtFnFilter(fk, 'chart-rel-islamic-sources',
            p => { const fns = (data.sourceCoverageFns||{})[p.name]; return fns ? {label: p.name, fns} : null; });
        this._attachExtFnFilter(fk, 'chart-rel-islamic-sankey',
            p => { const d = (data.coTraditions||[]).find(x => x.target === p.name); return d ? {label: d.target, fns: d.fns} : null; });
    },

    // ── Christian/Jewish: 5 extended charts ───────────────────────────────
    _relChristianExtended(data) {
        if (!data) return;

        // 1. Tradition breakdown donut
        {
            const chart = this._get('chart-rel-christian-breakdown');
            if (chart) {
                const tradColors = { 'Christianity only': '#e8a44a', 'Judaism only': '#9c8adb', 'Both': '#6db5d6', 'Multi-religion': '#e8a44a' };
                const pieData = (data.traditionBreakdown || []).map(d => ({
                    name: d.n, value: d.c,
                    itemStyle: { color: tradColors[d.n] || '#4a4844' },
                }));
                if (pieData.length) {
                    chart.setOption({
                        ...this._theme,
                        tooltip: { ...this._theme.tooltip, trigger: 'item', formatter: '{b}: {c} ({d}%)' },
                        series: [{
                            type: 'pie', radius: ['40%', '70%'], center: ['50%', '50%'],
                            data: pieData,
                            label: { color: '#7d7b76', fontSize: 12 },
                            emphasis: { label: { show: true, fontSize: 14, fontWeight: 'bold' } },
                        }],
                    }, true);
                }
            }
        }

        // 2. Theological concepts radar
        {
            const chart = this._get('chart-rel-christian-theology');
            if (chart) {
                const d = data.theologicalConcepts || [];
                if (d.length) {
                    const maxVal = Math.max(...d.map(x => x.val), 1);
                    chart.setOption({
                        ...this._theme,
                        radar: {
                            triggerEvent: true,
                            indicator: d.map(x => ({ name: x.axis, max: maxVal })),
                            axisName: { color: '#7d7b76', fontSize: 10 },
                            splitLine: { lineStyle: { color: '#1d2033' } },
                            splitArea: { areaStyle: { color: ['#07080d', '#0e1019'] } },
                            axisLine: { lineStyle: { color: '#1d2033' } },
                        },
                        series: [{
                            type: 'radar',
                            data: [{
                                value: d.map(x => x.val),
                                name: 'Theological Concepts',
                                areaStyle: { color: 'rgba(232,164,74,0.3)' },
                            }],
                            lineStyle: { color: '#e8a44a' },
                            itemStyle: { color: '#e8a44a' },
                        }],
                    }, true);
                }
            }
        }

        // 3. Focus distribution donut
        {
            const chart = this._get('chart-rel-christian-focus');
            if (chart) {
                const pieData = (data.focusDist || []).map((d, i) => ({
                    name: d.n, value: d.c,
                    itemStyle: { color: ['#e8a44a','#9c8adb','#6db5d6','#5ec291','#e8a44a','#4a4844'][i % 6] },
                }));
                if (pieData.length) {
                    chart.setOption({
                        ...this._theme,
                        tooltip: { ...this._theme.tooltip, trigger: 'item', formatter: '{b}: {c} ({d}%)' },
                        series: [{
                            type: 'pie', radius: ['40%', '70%'], center: ['50%', '50%'],
                            data: pieData,
                            label: { color: '#7d7b76', fontSize: 12 },
                            emphasis: { label: { show: true, fontSize: 14, fontWeight: 'bold' } },
                        }],
                    }, true);
                }
            }
        }

        // 4. Normative cross-tradition grouped bar
        {
            const chart = this._get('chart-rel-christian-normative');
            if (chart) {
                const d = data.normativeCross || [];
                if (d.length) {
                    chart.setOption({
                        ...this._theme,
                        grid: { left: 80, right: 20, top: 40, bottom: 40 },
                        legend: { ...this._theme.legend, top: 0 },
                        xAxis: { type: 'category', data: d.map(x => x.framework), axisLabel: { color: '#7d7b76', rotate: 20, fontSize: 10 } },
                        yAxis: { type: 'value', axisLabel: { color: '#7d7b76' }, splitLine: { lineStyle: { color: '#0e1019' } } },
                        tooltip: { ...this._theme.tooltip, trigger: 'axis' },
                        series: [
                            {
                                name: 'Christianity', type: 'bar', data: d.map(x => x.christianity),
                                itemStyle: { color: '#e8a44a', borderRadius: [4,4,0,0] },
                            },
                            {
                                name: 'Judaism', type: 'bar', data: d.map(x => x.judaism),
                                itemStyle: { color: '#9c8adb', borderRadius: [4,4,0,0] },
                            },
                        ],
                    }, true);
                }
            }
        }

        // 5. Tradition comparison HTML table
        {
            const el = document.getElementById('rel-christian-comparison');
            if (el) {
                const tc = data.traditionComparison || {};
                const traditions = Object.keys(tc);
                if (traditions.length) {
                    const fields = [
                        { key: 'paperCount',      label: 'Papers' },
                        { key: 'benchmarkCount',  label: 'Benchmarks' },
                        { key: 'biasStudies',     label: 'Bias Studies' },
                        { key: 'frameworkPapers', label: 'Framework Papers' },
                        { key: 'datasetsCount',   label: 'Datasets' },
                        { key: 'languages',       label: 'Languages', format: v => Array.isArray(v) ? v.join(', ') : String(v) },
                    ];
                    const headerCells = traditions.map(t => `<th style="padding:8px 12px;text-align:right;color:#d4d2cd;border-bottom:1px solid #1d2033">${t}</th>`).join('');
                    const rows = fields.map(f => {
                        const cells = traditions.map(t => {
                            const raw = tc[t]?.[f.key];
                            const display = raw === undefined ? '—' : (f.format ? f.format(raw) : String(raw));
                            return `<td style="padding:6px 12px;text-align:right;color:#7d7b76">${display}</td>`;
                        }).join('');
                        return `<tr><td style="padding:6px 12px;color:#9a9690;font-size:12px">${f.label}</td>${cells}</tr>`;
                    }).join('');
                    el.innerHTML = `
                        <table style="width:100%;border-collapse:collapse;font-size:13px;background:#07080d;border-radius:6px;overflow:hidden">
                            <thead>
                                <tr style="background:#0e1019">
                                    <th style="padding:8px 12px;text-align:left;color:#7d7b76;border-bottom:1px solid #1d2033">Metric</th>
                                    ${headerCells}
                                </tr>
                            </thead>
                            <tbody>${rows}</tbody>
                        </table>`;
                }
            }
        }

        // ── Click-to-filter wiring for extended charts ──
        const fk = 'rel-christian';
        this._attachExtFnFilter(fk, 'chart-rel-christian-breakdown',
            p => { const d = (data.traditionBreakdown||[]).find(x => x.n === p.name); return d ? {label: d.n, fns: d.fns} : null; });
        this._attachExtFnFilter(fk, 'chart-rel-christian-theology',
            p => { const fns = (data.theologicalConceptsFns||{})[p.name]; return fns ? {label: p.name, fns} : null; });
        this._attachExtFnFilter(fk, 'chart-rel-christian-focus',
            p => { const d = (data.focusDist||[]).find(x => x.n === p.name); return d ? {label: d.n, fns: d.fns} : null; });
        this._attachExtFnFilter(fk, 'chart-rel-christian-normative',
            p => { const fns = (data.normativeCrossFns||{})[p.name]; return fns ? {label: p.name, fns} : null; });
    },

    // ── Dharmic: 5 extended charts ────────────────────────────────────────
    _relDharmicExtended(data) {
        if (!data) return;

        // 1. Tradition split grouped bar
        {
            const chart = this._get('chart-rel-dharmic-split');
            if (chart) {
                const d = data.traditionSplit || [];
                if (d.length) {
                    chart.setOption({
                        ...this._theme,
                        grid: { left: 60, right: 20, top: 10, bottom: 40 },
                        xAxis: { type: 'category', data: d.map(x => x.n), axisLabel: { color: '#7d7b76', fontSize: 11 } },
                        yAxis: { type: 'value', axisLabel: { color: '#7d7b76' }, splitLine: { lineStyle: { color: '#0e1019' } } },
                        tooltip: { ...this._theme.tooltip, trigger: 'axis' },
                        series: [{
                            type: 'bar',
                            data: d.map((x, i) => ({
                                value: x.c,
                                itemStyle: { color: i === 0 ? '#e8a44a' : '#c47586', borderRadius: [4,4,0,0] },
                            })),
                        }],
                    }, true);
                }
            }
        }

        // 2. Culture distribution donut
        {
            const chart = this._get('chart-rel-dharmic-cultures');
            if (chart) {
                const pieData = (data.cultureDist || []).map((d, i) => ({
                    name: d.n, value: d.c,
                    itemStyle: { color: ['#e8a44a','#c47586','#6db5d6','#5ec291','#e8a44a','#4a4844'][i % 6] },
                }));
                if (pieData.length) {
                    chart.setOption({
                        ...this._theme,
                        tooltip: { ...this._theme.tooltip, trigger: 'item', formatter: '{b}: {c} ({d}%)' },
                        series: [{
                            type: 'pie', radius: ['40%', '70%'], center: ['50%', '50%'],
                            data: pieData,
                            label: { color: '#7d7b76', fontSize: 12 },
                            emphasis: { label: { show: true, fontSize: 14, fontWeight: 'bold' } },
                        }],
                    }, true);
                }
            }
        }

        // 3. Concept radar — dual polygon (Buddhism + Hinduism)
        {
            const chart = this._get('chart-rel-dharmic-concepts');
            if (chart) {
                const cr = data.conceptRadar || {};
                const labels = cr.labels || [];
                const buddhism = cr.buddhism || [];
                const hinduism = cr.hinduism || [];
                if (labels.length) {
                    const maxVal = Math.max(...buddhism, ...hinduism, 1);
                    chart.setOption({
                        ...this._theme,
                        legend: { ...this._theme.legend, top: 0 },
                        radar: {
                            triggerEvent: true,
                            indicator: labels.map(l => ({ name: l, max: maxVal })),
                            axisName: { color: '#7d7b76', fontSize: 10 },
                            splitLine: { lineStyle: { color: '#1d2033' } },
                            splitArea: { areaStyle: { color: ['#07080d', '#0e1019'] } },
                            axisLine: { lineStyle: { color: '#1d2033' } },
                        },
                        series: [{
                            type: 'radar',
                            data: [
                                {
                                    value: buddhism, name: 'Buddhism',
                                    areaStyle: { color: 'rgba(232,164,74,0.3)' },
                                    lineStyle: { color: '#e8a44a' }, itemStyle: { color: '#e8a44a' },
                                },
                                {
                                    value: hinduism, name: 'Hinduism',
                                    areaStyle: { color: 'rgba(196,117,134,0.3)' },
                                    lineStyle: { color: '#c47586' }, itemStyle: { color: '#c47586' },
                                },
                            ],
                        }],
                    }, true);
                }
            }
        }

        // 4. Research focus stacked bar
        {
            const chart = this._get('chart-rel-dharmic-focus');
            if (chart) {
                const d = data.researchFocus || [];
                if (d.length) {
                    chart.setOption({
                        ...this._theme,
                        grid: { left: 80, right: 20, top: 40, bottom: 40 },
                        legend: { ...this._theme.legend, top: 0 },
                        xAxis: { type: 'category', data: d.map(x => x.category), axisLabel: { color: '#7d7b76', rotate: 20, fontSize: 10 } },
                        yAxis: { type: 'value', axisLabel: { color: '#7d7b76' }, splitLine: { lineStyle: { color: '#0e1019' } } },
                        tooltip: { ...this._theme.tooltip, trigger: 'axis', axisPointer: { type: 'shadow' } },
                        series: [
                            {
                                name: 'Buddhism', type: 'bar', stack: 'total',
                                data: d.map(x => x.buddhism),
                                itemStyle: { color: '#e8a44a' },
                            },
                            {
                                name: 'Hinduism', type: 'bar', stack: 'total',
                                data: d.map(x => x.hinduism),
                                itemStyle: { color: '#c47586' },
                            },
                        ],
                    }, true);
                }
            }
        }

        // 5. Language treemap (colored by tradition)
        {
            const chart = this._get('chart-rel-dharmic-langs');
            if (chart) {
                const tradColors = { 'Buddhism': '#e8a44a', 'Hinduism': '#c47586', 'Both': '#6db5d6', 'Other': '#4a4844' };
                const items = (data.langTreemap || []).map(d => ({
                    name: d.n, value: d.c,
                    itemStyle: { color: tradColors[d.trad] || '#4a4844' },
                }));
                if (items.length) {
                    chart.setOption({
                        ...this._theme,
                        tooltip: { ...this._theme.tooltip, formatter: p => `${p.name}: ${p.value}` },
                        series: [{
                            type: 'treemap',
                            data: items,
                            roam: false,
                            breadcrumb: { show: false },
                            label: { color: '#d4d2cd', fontSize: 11 },
                            itemStyle: { borderColor: '#07080d', borderWidth: 2 },
                        }],
                    }, true);
                }
            }
        }

        // ── Click-to-filter wiring for extended charts ──
        const fk = 'rel-dharmic';
        this._attachExtFnFilter(fk, 'chart-rel-dharmic-split',
            p => { const d = (data.traditionSplit||[]).find(x => x.n === p.name); return d ? {label: d.n, fns: d.fns} : null; });
        this._attachExtFnFilter(fk, 'chart-rel-dharmic-cultures',
            p => { const d = (data.cultureDist||[]).find(x => x.n === p.name); return d ? {label: d.n, fns: d.fns} : null; });
        this._attachExtFnFilter(fk, 'chart-rel-dharmic-concepts',
            p => { const fns = (data.conceptRadarFns||{})[p.name]; return fns ? {label: p.name, fns} : null; });
        this._attachExtFnFilter(fk, 'chart-rel-dharmic-focus',
            p => { const fns = (data.researchFocusFns||{})[p.name]; return fns ? {label: p.name, fns} : null; });
        this._attachExtFnFilter(fk, 'chart-rel-dharmic-langs',
            p => { const d = (data.langTreemap||[]).find(x => x.n === p.name); return d ? {label: d.n, fns: d.fns} : null; });
    },

    // ── Confucian: 6 extended charts ──────────────────────────────────────
    _relConfucianExtended(data) {
        if (!data) return;

        // 1. Cultural footprint treemap
        {
            const chart = this._get('chart-rel-confucian-cultures');
            if (chart) {
                const items = (data.culturalFootprint || []).map(d => ({ name: d.n, value: d.c }));
                if (items.length) {
                    chart.setOption({
                        ...this._theme,
                        tooltip: { ...this._theme.tooltip, formatter: p => `${p.name}: ${p.value}` },
                        series: [{
                            type: 'treemap',
                            data: items,
                            roam: false,
                            breadcrumb: { show: false },
                            label: { color: '#d4d2cd', fontSize: 11 },
                            itemStyle: { borderColor: '#07080d', borderWidth: 2 },
                            levels: [{ color: ['#1a2a30','#155e75','#0e7490','#0891b2','#5cb4c9','#5cb4c9'], colorMappingBy: 'index' }],
                        }],
                    }, true);
                }
            }
        }

        // 2. Framework overlap radar
        {
            const chart = this._get('chart-rel-confucian-frameworks');
            if (chart) {
                const d = data.frameworkOverlap || [];
                if (d.length) {
                    const maxVal = Math.max(...d.map(x => x.val), 1);
                    chart.setOption({
                        ...this._theme,
                        radar: {
                            triggerEvent: true,
                            indicator: d.map(x => ({ name: x.axis, max: maxVal })),
                            axisName: { color: '#7d7b76', fontSize: 10 },
                            splitLine: { lineStyle: { color: '#1d2033' } },
                            splitArea: { areaStyle: { color: ['#07080d', '#0e1019'] } },
                            axisLine: { lineStyle: { color: '#1d2033' } },
                        },
                        series: [{
                            type: 'radar',
                            data: [{
                                value: d.map(x => x.val),
                                name: 'Framework Overlap',
                                areaStyle: { color: 'rgba(92,180,201,0.3)' },
                            }],
                            lineStyle: { color: '#5cb4c9' },
                            itemStyle: { color: '#5cb4c9' },
                        }],
                    }, true);
                }
            }
        }

        // 3. Chinese vs Western LLMs grouped bar
        {
            const chart = this._get('chart-rel-confucian-llms');
            if (chart) {
                const d = data.chineseVsWesternLLMs || [];
                if (d.length) {
                    const chinese = d.filter(x => x.origin === 'Chinese');
                    const western = d.filter(x => x.origin === 'Western');
                    const allNames = [...new Set(d.map(x => x.n))];
                    const lookup = (arr, name) => { const found = arr.find(x => x.n === name); return found ? found.c : 0; };
                    chart.setOption({
                        ...this._theme,
                        grid: { left: 80, right: 20, top: 40, bottom: 40 },
                        legend: { ...this._theme.legend, top: 0 },
                        xAxis: { type: 'category', data: allNames, axisLabel: { color: '#7d7b76', rotate: 20, fontSize: 10 } },
                        yAxis: { type: 'value', axisLabel: { color: '#7d7b76' }, splitLine: { lineStyle: { color: '#0e1019' } } },
                        tooltip: { ...this._theme.tooltip, trigger: 'axis' },
                        series: [
                            {
                                name: 'Chinese', type: 'bar', data: allNames.map(n => lookup(chinese, n)),
                                itemStyle: { color: '#d4605e', borderRadius: [4,4,0,0] },
                            },
                            {
                                name: 'Western', type: 'bar', data: allNames.map(n => lookup(western, n)),
                                itemStyle: { color: '#6db5d6', borderRadius: [4,4,0,0] },
                            },
                        ],
                    }, true);
                }
            }
        }

        // 4. Language distribution donut
        {
            const chart = this._get('chart-rel-confucian-langs');
            if (chart) {
                const pieData = (data.languageDist || []).map((d, i) => ({
                    name: d.n, value: d.c,
                    itemStyle: { color: ['#5cb4c9','#e8a44a','#e8a44a','#5ec291','#c47586','#4a4844'][i % 6] },
                }));
                if (pieData.length) {
                    chart.setOption({
                        ...this._theme,
                        tooltip: { ...this._theme.tooltip, trigger: 'item', formatter: '{b}: {c} ({d}%)' },
                        series: [{
                            type: 'pie', radius: ['40%', '70%'], center: ['50%', '50%'],
                            data: pieData,
                            label: { color: '#7d7b76', fontSize: 12 },
                            emphasis: { label: { show: true, fontSize: 14, fontWeight: 'bold' } },
                        }],
                    }, true);
                }
            }
        }

        // 5. Research trajectory stacked bar (empirical + theoretical over years)
        {
            const chart = this._get('chart-rel-confucian-trajectory');
            if (chart) {
                const rp = data.researchProfile || {};
                const years = (rp.years || []).map(String);
                if (years.length) {
                    chart.setOption({
                        ...this._theme,
                        grid: { left: 50, right: 20, top: 40, bottom: 40 },
                        legend: { ...this._theme.legend, top: 0 },
                        xAxis: { type: 'category', data: years, axisLabel: { color: '#7d7b76' } },
                        yAxis: { type: 'value', axisLabel: { color: '#7d7b76' }, splitLine: { lineStyle: { color: '#0e1019' } } },
                        tooltip: { ...this._theme.tooltip, trigger: 'axis', axisPointer: { type: 'shadow' } },
                        series: [
                            {
                                name: 'Empirical', type: 'bar', stack: 'total',
                                data: rp.empirical || [],
                                itemStyle: { color: '#5cb4c9' },
                            },
                            {
                                name: 'Theoretical', type: 'bar', stack: 'total',
                                data: rp.theoretical || [],
                                itemStyle: { color: '#e8a44a' },
                            },
                        ],
                    }, true);
                }
            }
        }

        // 6. Concept frequency horizontal bar
        {
            const chart = this._get('chart-rel-confucian-concepts');
            if (chart) {
                const d = (data.conceptFreq || []).slice(0, 15);
                if (d.length) {
                    chart.setOption({
                        ...this._theme,
                        grid: { left: 140, right: 20, top: 10, bottom: 20 },
                        xAxis: { type: 'value', axisLabel: { color: '#7d7b76' }, splitLine: { lineStyle: { color: '#0e1019' } } },
                        yAxis: { type: 'category', data: d.map(x => x.n).reverse(), axisLabel: { color: '#7d7b76', fontSize: 11 } },
                        tooltip: { ...this._theme.tooltip, trigger: 'axis' },
                        series: [{
                            type: 'bar',
                            data: d.map(x => x.c).reverse(),
                            itemStyle: { color: '#5cb4c9', borderRadius: [0,4,4,0] },
                        }],
                    }, true);
                }
            }
        }

        // ── Click-to-filter wiring for extended charts ──
        const fk = 'rel-confucian';
        this._attachExtFnFilter(fk, 'chart-rel-confucian-cultures',
            p => { const d = (data.culturalFootprint||[]).find(x => x.n === p.name); return d ? {label: d.n, fns: d.fns} : null; });
        this._attachExtFnFilter(fk, 'chart-rel-confucian-frameworks',
            p => { const fns = (data.frameworkOverlapFns||{})[p.name]; return fns ? {label: p.name, fns} : null; });
        this._attachExtFnFilter(fk, 'chart-rel-confucian-llms',
            p => { const d = (data.chineseVsWesternLLMs||[]).find(x => x.n === p.name); return d ? {label: d.n, fns: d.fns} : null; });
        this._attachExtFnFilter(fk, 'chart-rel-confucian-langs',
            p => { const d = (data.languageDist||[]).find(x => x.n === p.name); return d ? {label: d.n, fns: d.fns} : null; });
        this._attachExtFnFilter(fk, 'chart-rel-confucian-trajectory',
            p => { const fns = (data.researchProfileFns||{})[p.seriesName]; return fns ? {label: p.seriesName, fns} : null; });
        this._attachExtFnFilter(fk, 'chart-rel-confucian-concepts',
            p => { const d = (data.conceptFreq||[]).find(x => x.n === p.name); return d ? {label: d.n, fns: d.fns} : null; });
    },

    // ── Ubuntu/Indigenous: 6 extended charts ──────────────────────────────
    _relUbuntuExtended(data) {
        if (!data) return;

        const UBUNTU_COLORS = { 'Ubuntu': '#df8844', 'Indigenous': '#4fa89e', 'Shinto': '#c490d8' };

        // 1. Sub-tradition donut (custom colors from col field)
        {
            const chart = this._get('chart-rel-ubuntu-subtrad');
            if (chart) {
                const pieData = (data.subTradDist || []).map(d => ({
                    name: d.n, value: d.c,
                    itemStyle: { color: d.col || UBUNTU_COLORS[d.n] || '#4a4844' },
                }));
                if (pieData.length) {
                    chart.setOption({
                        ...this._theme,
                        tooltip: { ...this._theme.tooltip, trigger: 'item', formatter: '{b}: {c} ({d}%)' },
                        series: [{
                            type: 'pie', radius: ['40%', '70%'], center: ['50%', '50%'],
                            data: pieData,
                            label: { color: '#7d7b76', fontSize: 12 },
                            emphasis: { label: { show: true, fontSize: 14, fontWeight: 'bold' } },
                        }],
                    }, true);
                }
            }
        }

        // 2. Culture distribution horizontal bar (colored by trad)
        {
            const chart = this._get('chart-rel-ubuntu-cultures');
            if (chart) {
                const d = (data.cultureDist || []).slice(0, 12);
                if (d.length) {
                    chart.setOption({
                        ...this._theme,
                        grid: { left: 120, right: 20, top: 10, bottom: 20 },
                        xAxis: { type: 'value', axisLabel: { color: '#7d7b76' }, splitLine: { lineStyle: { color: '#0e1019' } } },
                        yAxis: { type: 'category', data: d.map(x => x.n).reverse(), axisLabel: { color: '#7d7b76', fontSize: 11 } },
                        tooltip: { ...this._theme.tooltip, trigger: 'axis' },
                        series: [{
                            type: 'bar',
                            data: d.map(x => ({
                                value: x.c,
                                itemStyle: { color: UBUNTU_COLORS[x.trad] || '#4a4844', borderRadius: [0,4,4,0] },
                            })).reverse(),
                        }],
                    }, true);
                }
            }
        }

        // 3. Eval readiness stacked bar (benchmark + evaluation + ethicsOnly per tradition)
        {
            const chart = this._get('chart-rel-ubuntu-eval');
            if (chart) {
                const d = data.evalReadiness || [];
                if (d.length) {
                    chart.setOption({
                        ...this._theme,
                        grid: { left: 80, right: 20, top: 40, bottom: 40 },
                        legend: { ...this._theme.legend, top: 0 },
                        xAxis: { type: 'category', data: d.map(x => x.tradition), axisLabel: { color: '#7d7b76', fontSize: 11 } },
                        yAxis: { type: 'value', axisLabel: { color: '#7d7b76' }, splitLine: { lineStyle: { color: '#0e1019' } } },
                        tooltip: { ...this._theme.tooltip, trigger: 'axis', axisPointer: { type: 'shadow' } },
                        series: [
                            {
                                name: 'Benchmarks', type: 'bar', stack: 'total',
                                data: d.map(x => x.benchmark),
                                itemStyle: { color: '#e8a44a' },
                            },
                            {
                                name: 'Evaluation', type: 'bar', stack: 'total',
                                data: d.map(x => x.evaluation),
                                itemStyle: { color: '#5ec291' },
                            },
                            {
                                name: 'Ethics Only', type: 'bar', stack: 'total',
                                data: d.map(x => x.ethicsOnly),
                                itemStyle: { color: '#e8a44a' },
                            },
                        ],
                    }, true);
                }
            }
        }

        // 4. Theme radar — 3 traces (Ubuntu, Indigenous, Shinto)
        {
            const chart = this._get('chart-rel-ubuntu-themes');
            if (chart) {
                const tr = data.themeRadar || {};
                const labels = tr.labels || [];
                const ubuntuVals = tr.ubuntu || [];
                const indVals = tr.indigenous || [];
                const shintoVals = tr.shinto || [];
                if (labels.length) {
                    const maxVal = Math.max(...ubuntuVals, ...indVals, ...shintoVals, 1);
                    chart.setOption({
                        ...this._theme,
                        legend: { ...this._theme.legend, top: 0 },
                        radar: {
                            triggerEvent: true,
                            indicator: labels.map(l => ({ name: l, max: maxVal })),
                            axisName: { color: '#7d7b76', fontSize: 10 },
                            splitLine: { lineStyle: { color: '#1d2033' } },
                            splitArea: { areaStyle: { color: ['#07080d', '#0e1019'] } },
                            axisLine: { lineStyle: { color: '#1d2033' } },
                        },
                        series: [{
                            type: 'radar',
                            data: [
                                {
                                    value: ubuntuVals, name: 'Ubuntu',
                                    areaStyle: { color: 'rgba(223,136,68,0.3)' },
                                    lineStyle: { color: '#df8844' }, itemStyle: { color: '#df8844' },
                                },
                                {
                                    value: indVals, name: 'Indigenous',
                                    areaStyle: { color: 'rgba(79,168,158,0.3)' },
                                    lineStyle: { color: '#4fa89e' }, itemStyle: { color: '#4fa89e' },
                                },
                                {
                                    value: shintoVals, name: 'Shinto',
                                    areaStyle: { color: 'rgba(196,144,216,0.3)' },
                                    lineStyle: { color: '#c490d8' }, itemStyle: { color: '#c490d8' },
                                },
                            ],
                        }],
                    }, true);
                }
            }
        }

        // 5. Gap comparison grouped bar (subset vs vault per metric)
        {
            const chart = this._get('chart-rel-ubuntu-gap');
            if (chart) {
                const d = data.gapComparison || [];
                if (d.length) {
                    chart.setOption({
                        ...this._theme,
                        grid: { left: 100, right: 20, top: 40, bottom: 40 },
                        legend: { ...this._theme.legend, top: 0 },
                        xAxis: { type: 'category', data: d.map(x => x.metric), axisLabel: { color: '#7d7b76', rotate: 20, fontSize: 10 } },
                        yAxis: { type: 'value', axisLabel: { color: '#7d7b76' }, splitLine: { lineStyle: { color: '#0e1019' } } },
                        tooltip: { ...this._theme.tooltip, trigger: 'axis' },
                        series: [
                            {
                                name: 'Subset', type: 'bar', data: d.map(x => x.subset),
                                itemStyle: { color: '#df8844', borderRadius: [4,4,0,0] },
                            },
                            {
                                name: 'Vault', type: 'bar', data: d.map(x => x.vault),
                                itemStyle: { color: '#4a4844', borderRadius: [4,4,0,0] },
                            },
                        ],
                    }, true);
                }
            }
        }

        // 6. Language distribution horizontal bar
        {
            const chart = this._get('chart-rel-ubuntu-langs');
            if (chart) {
                const d = (data.languageDist || []).slice(0, 12);
                if (d.length) {
                    chart.setOption({
                        ...this._theme,
                        grid: { left: 110, right: 20, top: 10, bottom: 20 },
                        xAxis: { type: 'value', axisLabel: { color: '#7d7b76' }, splitLine: { lineStyle: { color: '#0e1019' } } },
                        yAxis: { type: 'category', data: d.map(x => x.n).reverse(), axisLabel: { color: '#7d7b76', fontSize: 11 } },
                        tooltip: { ...this._theme.tooltip, trigger: 'axis' },
                        series: [{
                            type: 'bar',
                            data: d.map(x => x.c).reverse(),
                            itemStyle: { color: '#4fa89e', borderRadius: [0,4,4,0] },
                        }],
                    }, true);
                }
            }
        }

        // ── Click-to-filter wiring for extended charts ──
        const fk = 'rel-ubuntu';
        this._attachExtFnFilter(fk, 'chart-rel-ubuntu-subtrad',
            p => { const d = (data.subTradDist||[]).find(x => x.n === p.name); return d ? {label: d.n, fns: d.fns} : null; });
        this._attachExtFnFilter(fk, 'chart-rel-ubuntu-cultures',
            p => { const d = (data.cultureDist||[]).find(x => x.n === p.name); return d ? {label: d.n, fns: d.fns} : null; });
        this._attachExtFnFilter(fk, 'chart-rel-ubuntu-eval',
            p => { const fns = (data.evalReadinessFns||{})[p.name]; return fns ? {label: p.name, fns} : null; });
        this._attachExtFnFilter(fk, 'chart-rel-ubuntu-themes',
            p => { const fns = (data.themeRadarFns||{})[p.name]; return fns ? {label: p.name, fns} : null; });
        this._attachExtFnFilter(fk, 'chart-rel-ubuntu-langs',
            p => { const d = (data.languageDist||[]).find(x => x.n === p.name); return d ? {label: d.n, fns: d.fns} : null; });
    },

    // ═════════════════════════════════════════════════════════════════════
    // TAB 9: MODELS & LLMs
    // ═════════════════════════════════════════════════════════════════════

    _initModels() {
        const L = DATA.llm;

        // LLM models bar
        this._llmModelsBar(L.llmModels);
        // Model families bar
        this._llmFamiliesBar(L.modelFamilies);
        // LLM timeline
        this._llmTimeline(L.llmByYear);
        // Repo distribution
        this._llmRepos(L.repoDist);
    },

    _llmModelsBar(models) {
        const chart = this._get('chart-llm-models');
        if (!chart) return;
        const m = models.slice(0, 20);
        chart.setOption({
            ...this._theme,
            grid: { left: 130, right: 30, top: 10, bottom: 20 },
            xAxis: { type: 'value', axisLabel: { color: '#7d7b76' }, splitLine: { lineStyle: { color: '#0e1019' } } },
            yAxis: { type: 'category', data: m.map(x => x.n).reverse(), axisLabel: { color: '#7d7b76', fontSize: 10 } },
            tooltip: { ...this._theme.tooltip, trigger: 'axis' },
            series: [{ type: 'bar', data: m.map(x => x.c).reverse(), itemStyle: { color: '#9c8adb', borderRadius: [0,4,4,0] } }],
        }, true);
        chart.off('click');
        chart.on('click', p => { if (p.name) FilterState.toggle('llmModel', p.name); });
    },

    _llmFamiliesBar(families) {
        const chart = this._get('chart-llm-families');
        if (!chart) return;
        const f = families.slice(0, 20);
        chart.setOption({
            ...this._theme,
            grid: { left: 130, right: 30, top: 10, bottom: 20 },
            xAxis: { type: 'value', axisLabel: { color: '#7d7b76' }, splitLine: { lineStyle: { color: '#0e1019' } } },
            yAxis: { type: 'category', data: f.map(x => x.n).reverse(), axisLabel: { color: '#7d7b76', fontSize: 10 } },
            tooltip: { ...this._theme.tooltip, trigger: 'axis' },
            series: [{ type: 'bar', data: f.map(x => x.c).reverse(), itemStyle: { color: '#e8a44a', borderRadius: [0,4,4,0] } }],
        }, true);
    },

    _llmTimeline(byYear) {
        const chart = this._get('chart-llm-timeline');
        if (!chart) return;
        const years = Object.keys(byYear).sort();
        chart.setOption({
            ...this._theme,
            grid: { left: 50, right: 20, top: 40, bottom: 40 },
            legend: { ...this._theme.legend, top: 0, data: ['Assessed', 'Not Assessed'] },
            xAxis: { type: 'category', data: years, axisLabel: { color: '#7d7b76' } },
            yAxis: { type: 'value', axisLabel: { color: '#7d7b76' }, splitLine: { lineStyle: { color: '#0e1019' } } },
            tooltip: { ...this._theme.tooltip, trigger: 'axis' },
            series: [
                { name: 'Assessed', type: 'bar', stack: 'total', data: years.map(y => byYear[y].a), itemStyle: { color: '#5ec291' } },
                { name: 'Not Assessed', type: 'bar', stack: 'total', data: years.map(y => byYear[y].na), itemStyle: { color: '#3d3b37' } },
            ],
        }, true);
    },

    _llmRepos(dist) {
        const chart = this._get('chart-llm-repos');
        if (!chart) return;
        const repoColors = { GitHub: '#d4d2cd', HuggingFace: '#e8a44a', Zenodo: '#5ec291', OSF: '#e8a44a', Kaggle: '#5cb4c9', Other: '#4a4844' };
        chart.setOption({
            ...this._theme,
            tooltip: { ...this._theme.tooltip, trigger: 'item', formatter: '{b}: {c} ({d}%)' },
            series: [{
                type: 'pie', radius: ['35%','65%'],
                data: dist.map(d => ({ name: d.n, value: d.c, itemStyle: { color: repoColors[d.n] || '#4a4844' } })),
                label: { color: '#7d7b76' },
            }],
        }, true);
    },

    // ═════════════════════════════════════════════════════════════════════
    // SHARED CHART HELPERS
    // ═════════════════════════════════════════════════════════════════════

    _yearBar(chartId, yearDist) {
        const chart = this._get(chartId);
        if (!chart) return;
        const years = Object.keys(yearDist || {}).sort();
        const counts = years.map(y => yearDist[y]);
        chart.setOption({
            ...this._theme,
            grid: { left: 40, right: 20, top: 10, bottom: 30 },
            xAxis: { type: 'category', data: years, axisLabel: { color: '#7d7b76', fontSize: 10 } },
            yAxis: { type: 'value', axisLabel: { color: '#7d7b76' }, splitLine: { lineStyle: { color: '#0e1019' } } },
            tooltip: { ...this._theme.tooltip, trigger: 'axis' },
            series: [{ type: 'bar', data: counts, itemStyle: { color: '#e8a44a', borderRadius: [4,4,0,0] } }],
        }, true);
    },

    _modelsBar(chartId, models) {
        const chart = this._get(chartId);
        if (!chart) return;
        const m = (models || []).slice(0, 10);
        if (!m.length) {
            chart.setOption({ ...this._theme, graphic: { type: 'text', left: 'center', top: 'center', style: { text: 'No model data', fill: '#4a4844' } } }, true);
            return;
        }
        chart.setOption({
            ...this._theme,
            grid: { left: 120, right: 20, top: 10, bottom: 20 },
            xAxis: { type: 'value', axisLabel: { color: '#7d7b76' }, splitLine: { lineStyle: { color: '#0e1019' } } },
            yAxis: { type: 'category', data: m.map(x => x.n).reverse(), axisLabel: { color: '#7d7b76', fontSize: 10 } },
            tooltip: { ...this._theme.tooltip, trigger: 'axis' },
            series: [{ type: 'bar', data: m.map(x => x.c).reverse(), itemStyle: { color: '#e8a44a', borderRadius: [0,4,4,0] } }],
        }, true);
    },

    // ═════════════════════════════════════════════════════════════════════
    // FRAMEWORK-SPECIFIC CHART METHODS
    // ═════════════════════════════════════════════════════════════════════

    _theoryDonut(chartId, data) {
        const chart = this._get(chartId);
        if (!chart) return;
        const sliceColors = { 'Benchmark / Evaluation': '#5ec291', 'Theoretical / Framework': '#4a4844' };
        const pieData = data.map(d => ({
            name: d.n, value: d.c,
            itemStyle: { color: sliceColors[d.n] || '#7d7b76' },
        }));
        chart.setOption({
            ...this._theme,
            tooltip: { ...this._theme.tooltip, trigger: 'item', formatter: '{b}: {c} ({d}%)' },
            series: [{
                type: 'pie', radius: ['40%', '70%'], center: ['50%', '50%'],
                data: pieData, label: { color: '#7d7b76', fontSize: 12 },
                emphasis: { label: { show: true, fontSize: 14, fontWeight: 'bold' } },
            }],
        }, true);
    },

    _venueTypeDonutSm(chartId, data) {
        const chart = this._get(chartId);
        if (!chart) return;
        const pieData = data.map(d => ({
            name: d.n, value: d.c,
            itemStyle: { color: this._vtColors[d.n] || '#4a4844' },
        }));
        chart.setOption({
            ...this._theme,
            tooltip: { ...this._theme.tooltip, trigger: 'item', formatter: '{b}: {c} ({d}%)' },
            series: [{
                type: 'pie', radius: ['40%', '70%'], center: ['50%', '50%'],
                data: pieData, label: { color: '#7d7b76', fontSize: 12 },
                emphasis: { label: { show: true, fontSize: 14, fontWeight: 'bold' } },
            }],
        }, true);
    },

    _regionBarSm(chartId, data) {
        const chart = this._get(chartId);
        if (!chart) return;
        const d = data.slice(0, 8);
        if (!d.length) return;
        chart.setOption({
            ...this._theme,
            grid: { left: 120, right: 20, top: 10, bottom: 20 },
            xAxis: { type: 'value', axisLabel: { color: '#7d7b76' }, splitLine: { lineStyle: { color: '#0e1019' } } },
            yAxis: { type: 'category', data: d.map(x => x.n).reverse(), axisLabel: { color: '#7d7b76', fontSize: 11 } },
            tooltip: { ...this._theme.tooltip, trigger: 'axis' },
            series: [{ type: 'bar', data: d.map(x => x.c).reverse(), itemStyle: { color: '#c47586', borderRadius: [0,4,4,0] } }],
        }, true);
    },

    _virtueBar(chartId, data) {
        const chart = this._get(chartId);
        if (!chart) return;
        const d = (data || []).slice(0, 15);
        if (!d.length) {
            chart.setOption({ ...this._theme, graphic: { type: 'text', left: 'center', top: 'center', style: { text: 'No virtue data', fill: '#4a4844' } } }, true);
            return;
        }
        chart.setOption({
            ...this._theme,
            grid: { left: 120, right: 20, top: 10, bottom: 20 },
            xAxis: { type: 'value', axisLabel: { color: '#7d7b76' }, splitLine: { lineStyle: { color: '#0e1019' } } },
            yAxis: { type: 'category', data: d.map(x => x.n).reverse(), axisLabel: { color: '#7d7b76', fontSize: 11 } },
            tooltip: { ...this._theme.tooltip, trigger: 'axis' },
            series: [{ type: 'bar', data: d.map(x => x.c).reverse(), itemStyle: { color: '#5ec291', borderRadius: [0,4,4,0] } }],
        }, true);
    },

    _conceptBar(chartId, data, color) {
        const chart = this._get(chartId);
        if (!chart) return;
        const d = (data || []).slice(0, 13);
        if (!d.length) {
            chart.setOption({ ...this._theme, graphic: { type: 'text', left: 'center', top: 'center', style: { text: 'No concept data', fill: '#4a4844' } } }, true);
            return;
        }
        chart.setOption({
            ...this._theme,
            grid: { left: 160, right: 20, top: 10, bottom: 20 },
            xAxis: { type: 'value', axisLabel: { color: '#7d7b76' }, splitLine: { lineStyle: { color: '#0e1019' } } },
            yAxis: { type: 'category', data: d.map(x => x.n).reverse(), axisLabel: { color: '#7d7b76', fontSize: 11 } },
            tooltip: { ...this._theme.tooltip, trigger: 'axis' },
            series: [{ type: 'bar', data: d.map(x => x.c).reverse(), itemStyle: { color: color, borderRadius: [0,4,4,0] } }],
        }, true);
    },

    _subTheoryBar(chartId, data) {
        const chart = this._get(chartId);
        if (!chart) return;
        const d = (data || []).filter(x => x.c > 0);
        if (!d.length) {
            chart.setOption({ ...this._theme, graphic: { type: 'text', left: 'center', top: 'center', style: { text: 'No paradigm data', fill: '#4a4844' } } }, true);
            return;
        }
        const paradigmColors = { 'Kohlberg': '#e8a44a', 'Trolley': '#c47586' };
        chart.setOption({
            ...this._theme,
            grid: { left: 100, right: 20, top: 10, bottom: 20 },
            xAxis: { type: 'value', axisLabel: { color: '#7d7b76' }, splitLine: { lineStyle: { color: '#0e1019' } } },
            yAxis: { type: 'category', data: d.map(x => x.n).reverse(), axisLabel: { color: '#7d7b76', fontSize: 11 } },
            tooltip: { ...this._theme.tooltip, trigger: 'axis' },
            series: [{ type: 'bar', data: d.map(x => ({ value: x.c, itemStyle: { color: paradigmColors[x.n] || '#e8a44a' } })).reverse(), barMaxWidth: 30 }],
        }, true);
    },

    _schwartzRadar(chartId, data) {
        const chart = this._get(chartId);
        if (!chart || !data) return;
        const maxVal = Math.max(...data.map(v => v.c), 1);
        chart.setOption({
            ...this._theme,
            radar: {
                indicator: data.map(v => ({ name: v.n, max: maxVal })),
                axisName: { color: '#7d7b76', fontSize: 10 },
                splitLine: { lineStyle: { color: '#1d2033' } },
                splitArea: { areaStyle: { color: ['transparent'] } },
            },
            series: [{
                type: 'radar',
                data: [{
                    value: data.map(v => v.c),
                    name: 'Schwartz Values',
                    areaStyle: { color: 'rgba(92,180,201,0.3)' },
                }],
                lineStyle: { color: '#5cb4c9' },
                itemStyle: { color: '#5cb4c9' },
            }],
        }, true);
    },
};

// Global resize handler
window.addEventListener('resize', () => Charts.resizeAll());
