/**
 * CEI Dashboard v4 — Application Logic (v6.1 Extensibility Refactor)
 * FilterState singleton, tab switching, Paper Explorer, filter bar rendering
 * Phase 1: FILTER_DIMS registry — single source of truth for all filterable dimensions.
 * Adding a new filter = 1 registry entry (~8 lines) + 1 HTML <div>.
 */

// ═══════════════════════════════════════════════════════════════════════════
// FILTER DIMENSION REGISTRY
// ═══════════════════════════════════════════════════════════════════════════

/**
 * Each entry declares: key, label, mselId (null if no dropdown),
 * options() (lazy, called after DATA loads), match(paper, value),
 * and optional parseValue(str).
 */
const FILTER_DIMS = [
    { key: 'year', label: 'Year', mselId: 'msel-year',
      options: () => [...new Set(DATA.papers.map(p => p.y).filter(Boolean))].sort((a,b) => b-a).map(y => ({value:y, label:String(y)})),
      match: (p, v) => p.y === v,
      parseValue: str => +str },
    { key: 'venueType', label: 'Venue Type', mselId: 'msel-venue-type',
      options: () => Object.keys(DATA.agg.vtDist || {}).map(n => ({value:n, label:n})),
      match: (p, v) => p.vt === v },
    { key: 'venue', label: 'Venue', mselId: null,
      match: (p, v) => p.cc === v },
    { key: 'confFamily', label: 'Family', mselId: null,
      match: (p, v) => p.cf === v },
    { key: 'ethics', label: 'Ethics', mselId: 'msel-ethics',
      options: () => [
          { value: 'Yes', label: 'Ethics: Yes' },
          { value: 'No', label: 'Ethics: No' },
          { value: 'VE', label: 'Virtue Ethics (VE)' },
          { value: 'DE', label: 'Deontological (DE)' },
          { value: 'CU', label: 'Consequentialist (CU)' },
      ],
      match: (p, v) => {
          switch (v) {
              case 'Yes': return !!p.eo;
              case 'No': return !p.eo;
              case 'VE': return !!p.ve;
              case 'DE': return !!p.de;
              case 'CU': return !!p.ue;
              default: return false;
          }
      }},
    { key: 'isBenchmark', label: 'Benchmark', mselId: null,
      match: (p, v) => {
          if (v === 'Yes') return !!p.ib;
          if (v === 'No') return !p.ib;
          return false;
      }},
    { key: 'culture', label: 'Culture', mselId: null,
      match: (p, v) => p.cu && p.cu.includes(v) },
    { key: 'language', label: 'Language', mselId: null,
      match: (p, v) => p.ln && p.ln.includes(v) },
    { key: 'religion', label: 'Religion', mselId: 'msel-religion',
      options: () => {
          const religions = [...new Set(DATA.papers.flatMap(p => p.rv || []))].sort();
          return [
              { value: 'Yes', label: 'Has Religion' },
              { value: 'No', label: 'No Religion' },
              ...religions.map(r => ({ value: r, label: r })),
          ];
      },
      match: (p, v) => {
          if (v === 'Yes') return !!(p.rv && p.rv.length);
          if (v === 'No') return !p.rv || !p.rv.length;
          return p.rv && p.rv.includes(v);
      }},
    { key: 'moralPsych', label: 'Moral Psych', mselId: 'msel-moral-psych',
      options: () => [
          { value: 'Yes', label: 'Has Framework' },
          { value: 'No', label: 'No Framework' },
          { value: 'MFT', label: 'MFT (Moral Foundations)' },
          { value: 'Schwartz', label: 'Schwartz Values' },
          { value: 'Developmental', label: 'Developmental (Kohlberg)' },
      ],
      match: (p, v) => {
          switch (v) {
              case 'Yes': return !!p.mp;
              case 'No': return !p.mp;
              case 'MFT': return p.mp && p.mp.includes('Moral Foundations');
              case 'Schwartz': return p.mp && p.mp.includes('Schwartz');
              case 'Developmental': return p.mp && p.mp.includes('Developmental');
              default: return false;
          }
      }},
    { key: 'llmModel', label: 'Model', mselId: 'msel-model',
      options: () => {
          const models = [...new Set(DATA.papers.flatMap(p => p.lm || []))].sort();
          return [
              { value: 'Yes', label: 'Has Models' },
              { value: 'No', label: 'No Models' },
              ...models.map(m => ({ value: m, label: m })),
          ];
      },
      match: (p, v) => {
          if (v === 'Yes') return !!(p.lm && p.lm.length);
          if (v === 'No') return !p.lm || !p.lm.length;
          return p.lm && p.lm.includes(v);
      }},
    { key: 'category', label: 'Category', mselId: 'msel-category',
      options: () => (DATA.agg.categories || []).map(c => ({ value: c, label: c })),
      match: (p, v) => p.cs && p.cs.includes(v) },
    { key: 'flag', label: 'Flag', mselId: 'msel-flag',
      options: () => [
          { value: 'B', label: 'Benchmark (B)' },
          { value: 'E', label: 'Eval (E)' },
          { value: 'D', label: 'Dataset (D)' },
          { value: 'C', label: 'Cultural (C)' },
          { value: 'R', label: 'Religious (R)' },
      ],
      match: (p, v) => {
          switch (v) {
              case 'B': return !!p.ib;
              case 'E': return !!p.ie;
              case 'D': return !!p.id;
              case 'C': return !!(p.cu && p.cu.length);
              case 'R': return !!(p.rv && p.rv.length);
              default: return false;
          }
      }},
];


// ═══════════════════════════════════════════════════════════════════════════
// FILTER STATE
// ═══════════════════════════════════════════════════════════════════════════

const FilterState = {
    _filters: Object.fromEntries(FILTER_DIMS.map(d => [d.key, new Set()])),
    searchQuery: '',
    _listeners: [],
    _papers: null,        // cached reference to DATA.papers
    _searchIndex: null,   // pre-built search text

    init(papers) {
        this._papers = papers;
        this._buildSearchIndex();
    },

    /** Build/rebuild search index. Includes detail fields if available. */
    _buildSearchIndex() {
        this._searchIndex = this._papers.map(p => {
            const d = (DATA._detail && DATA._detail[p.i]) || {};
            return [p.t, p.fa, p.la, p.cc, d.ab || p.ab || '', d.bn || p.bn || '', d.wm || p.wm || '',
                (p.cu||[]).join(' '), (p.ln||[]).join(' '),
                (p.rv||[]).join(' '), (p.lm||[]).join(' '),
                (p.cs||[]).join(' '), p.mp || ''
            ].join(' ').toLowerCase();
        });
    },

    _notifyPending: false,
    _crossCache: null,

    subscribe(fn) { this._listeners.push(fn); },

    notify() {
        if (this._notifyPending) return;
        this._notifyPending = true;
        this._crossCache = null; // invalidate cross-filter cache
        queueMicrotask(() => {
            this._notifyPending = false;
            const filtered = this.getFilteredPapers();
            this._listeners.forEach(fn => fn(filtered));
        });
    },

    /** Pre-computed cross-filtered results for all dimensions (used by MultiSelect) */
    getCrossFiltered(dim) {
        if (!this._crossCache) this._crossCache = {};
        if (!this._crossCache[dim]) this._crossCache[dim] = this.getFilteredPapers(dim);
        return this._crossCache[dim];
    },

    /** Accessor for filter Sets — use instead of direct _filters access */
    getFilters(dim) {
        return this._filters[dim];
    },

    toggle(dimension, value) {
        const set = this._filters[dimension];
        if (!set) return;
        if (set.has(value)) set.delete(value);
        else set.add(value);
        this.notify();
    },

    setSearch(query) {
        this.searchQuery = query.toLowerCase().trim();
        this.notify();
    },

    clear() {
        Object.values(this._filters).forEach(s => s.clear());
        this.searchQuery = '';
        this.notify();
    },

    clearDimension(dimension) {
        const set = this._filters[dimension];
        if (set) set.clear();
        this.notify();
    },

    isActive() {
        return this.searchQuery !== '' ||
            Object.values(this._filters).some(s => s.size > 0);
    },

    getActiveFilters() {
        const active = [];
        for (const [dim, set] of Object.entries(this._filters)) {
            for (const val of set) {
                active.push({ dim, val });
            }
        }
        return active;
    },

    /** Registry-driven filter: AND across dimensions, OR within each dimension */
    getFilteredPapers(excludeDim) {
        if (!this._papers) return [];
        let result = this._papers;
        for (const dim of FILTER_DIMS) {
            if (dim.key === excludeDim || !this._filters[dim.key].size) continue;
            const active = this._filters[dim.key];
            result = result.filter(p => {
                for (const v of active) { if (dim.match(p, v)) return true; }
                return false;
            });
        }
        if (this.searchQuery) {
            const q = this.searchQuery;
            result = result.filter(p => this._searchIndex[p.i].includes(q));
        }
        return result;
    }
};


// ═══════════════════════════════════════════════════════════════════════════
// TAB SWITCHING
// ═══════════════════════════════════════════════════════════════════════════

const TabManager = {
    _initialized: new Set(),

    init() {
        document.querySelectorAll('.tab-btn').forEach(btn => {
            btn.addEventListener('click', () => this.switchTab(btn.dataset.tab));
        });
        // Sub-nav pills
        document.querySelectorAll('.sub-nav').forEach(nav => {
            nav.querySelectorAll('.sub-btn').forEach(btn => {
                btn.addEventListener('click', () => this.switchSub(nav, btn));
            });
        });
    },

    switchTab(tabId) {
        document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
        document.querySelectorAll('.tab-pane').forEach(p => p.classList.remove('active'));
        const btn = document.querySelector(`.tab-btn[data-tab="${tabId}"]`);
        const pane = document.getElementById(`pane-${tabId}`);
        if (btn) btn.classList.add('active');
        if (pane) pane.classList.add('active');

        // Lazy init charts for this tab
        if (!this._initialized.has(tabId) && typeof Charts !== 'undefined') {
            Charts.initTab(tabId);
            this._initialized.add(tabId);
        }
        // Resize charts in tab
        if (typeof Charts !== 'undefined') Charts.resizeAll();
    },

    switchSub(nav, btn) {
        const parent = nav.parentElement;
        nav.querySelectorAll('.sub-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        parent.querySelectorAll('.sub-pane').forEach(p => p.classList.remove('active'));
        const target = document.getElementById(`sub-${btn.dataset.sub}`);
        if (target) target.classList.add('active');
        if (typeof Charts !== 'undefined') Charts.resizeAll();
    },

    markInitialized(tabId) { this._initialized.add(tabId); }
};


// ═══════════════════════════════════════════════════════════════════════════
// FILTER BAR
// ═══════════════════════════════════════════════════════════════════════════

const FilterBar = {
    init() {
        document.getElementById('btn-clear-filters').addEventListener('click', () => {
            FilterState.clear();
            document.getElementById('explorer-search').value = '';
        });
        // Delegated click handler for chip remove buttons (set up once, never re-bound)
        document.getElementById('filter-chips').addEventListener('click', (e) => {
            const el = e.target.closest('.chip-remove');
            if (!el) return;
            if (el.dataset.action === 'clear-search') {
                FilterState.searchQuery = '';
                document.getElementById('explorer-search').value = '';
                FilterState.notify();
            } else {
                FilterState.toggle(el.dataset.dim, isNaN(el.dataset.val) ? el.dataset.val : +el.dataset.val);
            }
        });
        FilterState.subscribe(() => this.render());
    },

    /** Derived from FILTER_DIMS registry — no manual sync needed */
    _dimLabels: Object.fromEntries(FILTER_DIMS.map(d => [d.key, d.label])),

    render() {
        const bar = document.getElementById('filter-bar');
        const chips = document.getElementById('filter-chips');
        const count = document.getElementById('filter-count');
        if (!FilterState.isActive()) { bar.style.display = 'none'; return; }
        bar.style.display = 'flex';
        const active = FilterState.getActiveFilters();
        const filtered = FilterState.getFilteredPapers();
        let html = '';
        if (FilterState.searchQuery) {
            html += `<span class="filter-chip" data-dim="search">Search: "${FilterState.searchQuery}" <span class="chip-remove" data-action="clear-search">&times;</span></span>`;
        }
        for (const {dim, val} of active) {
            html += `<span class="filter-chip" data-dim="${dim}">${this._dimLabels[dim] || dim}: ${val} <span class="chip-remove" data-dim="${dim}" data-val="${val}">&times;</span></span>`;
        }
        chips.innerHTML = html;
        count.textContent = `${filtered.length} of ${DATA.agg.total} papers`;
    }
};


// ═══════════════════════════════════════════════════════════════════════════
// PAPER EXPLORER
// ═══════════════════════════════════════════════════════════════════════════

const Explorer = {
    _page: 1,
    _pageSize: 50,
    _sortKey: 'y',
    _sortDir: -1,  // -1 = desc
    _papers: [],
    _expandedIdx: null,

    init() {
        // Search
        const searchEl = document.getElementById('explorer-search');
        let debounce = null;
        searchEl.addEventListener('input', () => {
            clearTimeout(debounce);
            debounce = setTimeout(() => FilterState.setSearch(searchEl.value), 200);
        });

        // Page size
        document.getElementById('explorer-page-size').addEventListener('change', (e) => {
            this._pageSize = +e.target.value;
            this._page = 1;
            this.render(FilterState.getFilteredPapers());
        });

        // Sort headers
        document.querySelectorAll('.sortable').forEach(th => {
            th.addEventListener('click', () => {
                const key = th.dataset.sort;
                if (this._sortKey === key) this._sortDir *= -1;
                else { this._sortKey = key; this._sortDir = -1; }
                this.render(this._papers);
            });
        });

        // Delegated click handler for paper rows (set up once, never re-bound)
        document.getElementById('explorer-tbody').addEventListener('click', (e) => {
            const row = e.target.closest('.paper-row');
            if (!row) return;
            const idx = +row.dataset.idx;
            this._expandedIdx = this._expandedIdx === idx ? null : idx;
            this.render(this._papers);
        });

        // Subscribe to filter changes
        FilterState.subscribe(papers => {
            this._page = 1;
            this._expandedIdx = null;
            this.render(papers);
        });
    },

    render(papers) {
        this._papers = papers || [];
        const sorted = [...this._papers].sort((a, b) => {
            const va = a[this._sortKey], vb = b[this._sortKey];
            if (typeof va === 'string') return va.localeCompare(vb) * this._sortDir;
            return (va - vb) * this._sortDir;
        });

        const total = sorted.length;
        const totalPages = Math.max(1, Math.ceil(total / this._pageSize));
        if (this._page > totalPages) this._page = totalPages;
        const start = (this._page - 1) * this._pageSize;
        const pageItems = sorted.slice(start, start + this._pageSize);

        const countEl = document.getElementById('explorer-count');
        if (FilterState.isActive()) {
            countEl.textContent = `${fmt(total)} of ${fmt(DATA.agg.total)} papers`;
            countEl.classList.add('count-filtered');
        } else {
            countEl.textContent = `${fmt(total)} papers`;
            countEl.classList.remove('count-filtered');
        }

        // Update sort arrows
        document.querySelectorAll('.sortable .sort-arrow').forEach(el => el.textContent = '');
        const activeHeader = document.querySelector(`.sortable[data-sort="${this._sortKey}"] .sort-arrow`);
        if (activeHeader) activeHeader.textContent = this._sortDir > 0 ? ' \u25B2' : ' \u25BC';

        // Render table body using shared renderPaperRow / renderPaperDetail
        const tbody = document.getElementById('explorer-tbody');
        let html = '';
        for (const p of pageItems) {
            html += renderPaperRow(p);
            if (this._expandedIdx === p.i) html += renderPaperDetail(p);
        }
        tbody.innerHTML = html;

        // Pagination
        this._renderPagination(totalPages);
    },

    _renderPagination(totalPages) {
        const container = document.getElementById('explorer-pagination');
        if (totalPages <= 1) { container.innerHTML = ''; return; }

        let html = '';
        html += `<button class="page-btn" data-page="${this._page - 1}" ${this._page <= 1 ? 'disabled' : ''}>Prev</button>`;

        const pages = getPaginationRange(this._page, totalPages);
        for (const pg of pages) {
            if (pg === '...') {
                html += `<span class="page-btn" style="border:none;cursor:default;">...</span>`;
            } else {
                html += `<button class="page-btn ${pg === this._page ? 'active' : ''}" data-page="${pg}">${pg}</button>`;
            }
        }
        html += `<button class="page-btn" data-page="${this._page + 1}" ${this._page >= totalPages ? 'disabled' : ''}>Next</button>`;

        container.innerHTML = html;
        container.querySelectorAll('.page-btn[data-page]').forEach(btn => {
            btn.addEventListener('click', () => {
                const pg = +btn.dataset.page;
                if (pg >= 1 && pg <= totalPages) {
                    this._page = pg;
                    this._expandedIdx = null;
                    this.render(this._papers);
                    document.getElementById('pane-explorer').scrollIntoView({ behavior: 'smooth' });
                }
            });
        });
    }
};


// ═══════════════════════════════════════════════════════════════════════════
// PAPER LIST RENDERER (Explorer-style tables for deep-dive sub-tabs)
// ═══════════════════════════════════════════════════════════════════════════

const _ptState = {};      // containerId → { papers, maxItems, expandedFn }
const _ptDelegated = new Set(); // track which containers have delegated click handlers

function renderPaperList(containerId, papers, maxItems) {
    const el = document.getElementById(containerId);
    if (!el) return;
    if (!_ptState[containerId]) _ptState[containerId] = { expandedFn: null };
    const state = _ptState[containerId];
    state.papers = papers;
    state.maxItems = maxItems;

    // Set up delegated click handler once per container
    if (!_ptDelegated.has(containerId)) {
        _ptDelegated.add(containerId);
        el.addEventListener('click', (e) => {
            const row = e.target.closest('.paper-row');
            if (!row) return;
            const fn = row.dataset.fn;
            const st = _ptState[containerId];
            if (!st) return;
            st.expandedFn = st.expandedFn === fn ? null : fn;
            renderPaperList(containerId, st.papers, st.maxItems);
        });
    }

    const items = papers.slice(0, maxItems || 100);
    if (!items.length) {
        el.innerHTML = '<div style="color:var(--text-muted);padding:12px;">No papers in this section.</div>';
        return;
    }
    let html = `<div class="explorer-table-wrap"><table class="explorer-table">
        <thead><tr><th class="col-year">Year</th><th class="col-paper">Paper</th><th class="col-venue">Venue</th><th class="col-ethics">Ethics</th><th class="col-flags">Flags</th></tr></thead><tbody>`;
    for (const sp of items) {
        const p = DATA._paperByFn[sp.fn] || sp;
        html += renderPaperRow(p, sp.fn);
        if (state.expandedFn === sp.fn) html += renderPaperDetail(p);
    }
    html += '</tbody></table></div>';
    el.innerHTML = html;
}


// ═══════════════════════════════════════════════════════════════════════════
// UTILITIES
// ═══════════════════════════════════════════════════════════════════════════

const _escMap = { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' };
const _escRe = /[&<>"]/g;
function esc(str) {
    if (!str) return '';
    return String(str).replace(_escRe, c => _escMap[c]);
}

function getPaginationRange(current, total) {
    if (total <= 7) return Array.from({length: total}, (_, i) => i + 1);
    const pages = [1];
    if (current > 3) pages.push('...');
    for (let i = Math.max(2, current - 1); i <= Math.min(total - 1, current + 1); i++) pages.push(i);
    if (current < total - 2) pages.push('...');
    pages.push(total);
    return pages;
}

function fmt(n) { return n >= 1000 ? n.toLocaleString() : String(n); }

function _ethicsBadges(p) {
    if (!p.eo) return '<span class="eth-badge eth-no">No</span>';
    const tags = [];
    if (p.ve) tags.push('<span class="eth-badge eth-ve" title="Virtue Ethics">VE</span>');
    if (p.de) tags.push('<span class="eth-badge eth-de" title="Deontological">DE</span>');
    if (p.ue) tags.push('<span class="eth-badge eth-cu" title="Consequentialism">CU</span>');
    return tags.length ? tags.join('') : '<span class="eth-badge eth-yes">Yes</span>';
}

function _flagBadges(p) {
    const flags = [];
    if (p.ib) flags.push('<span class="flag-badge fb-B" title="Benchmark">B</span>');
    if (p.ie) flags.push('<span class="flag-badge fb-E" title="Eval">E</span>');
    if (p.id) flags.push('<span class="flag-badge fb-D" title="Dataset">D</span>');
    if (p.cu && p.cu.length) flags.push('<span class="flag-badge fb-C" title="Cultural">C</span>');
    if (p.rv && p.rv.length) flags.push('<span class="flag-badge fb-R" title="Religious">R</span>');
    return flags.join('');
}

/**
 * Shared paper row renderer. Used by Explorer, renderPaperList, and Charts heatmap drilldown.
 */
function renderPaperRow(p, fn) {
    const vtClass = `vt-${(p.vt || 'N/A') === 'N/A' ? 'NA' : p.vt}`;
    const title = p.t || (fn ? fn.replace('.md', '') : '\u2014');
    const authors = p.fa ? `${esc(p.fa)}${p.la ? ', ' + esc(p.la) : ''}` : '';
    return `<tr class="paper-row"${p.i !== undefined ? ` data-idx="${p.i}"` : ''}${fn ? ` data-fn="${esc(fn)}"` : ''}>
        <td class="col-year">${p.y || '\u2014'}</td>
        <td class="col-paper">
            <div class="paper-title">${esc(title)}</div>
            ${authors ? `<div class="paper-authors">${authors}</div>` : ''}
        </td>
        <td class="col-venue"><span class="venue-badge ${vtClass}" title="${esc(p.cc || '')}">${esc(p.cc || '\u2014')}</span></td>
        <td class="col-ethics"><div class="eth-badges">${_ethicsBadges(p)}</div></td>
        <td class="col-flags"><div class="flag-badges">${_flagBadges(p)}</div></td>
    </tr>`;
}

/**
 * Shared paper detail row renderer.
 * Merges detail fields (ab, bn, wm, url, doi, du) from DATA._detail when available.
 */
function renderPaperDetail(p) {
    const d = (DATA._detail && DATA._detail[p.i]) || {};
    const bn = d.bn || p.bn || '';
    const wm = d.wm || p.wm || '';
    const url = d.url || p.url || '';
    const doi = d.doi || p.doi || '';
    const du = d.du || p.du || '';
    const ab = d.ab || p.ab || '';

    const links = [];
    if (url) links.push(`<a href="${esc(url)}" target="_blank">Paper URL</a>`);
    if (doi) links.push(`<a href="https://doi.org/${esc(doi)}" target="_blank">DOI</a>`);
    if (du) links.push(`<a href="${esc(du)}" target="_blank">Data/Code</a>`);
    const ethDetail = [];
    if (p.eo) ethDetail.push('Ethics: Yes');
    if (p.ve) ethDetail.push('Virtue Ethics');
    if (p.de) ethDetail.push('Deontological');
    if (p.ue) ethDetail.push('Consequentialism/Utilitarianism');
    if (p.mp) ethDetail.push('Moral Psych: ' + p.mp);
    return `<tr class="detail-row"><td colspan="5">
        <div class="paper-detail">
            <div class="detail-grid">
                <div class="detail-field"><span class="detail-label">Venue</span><span class="detail-value">${esc(p.cc || '')} ${p.vt ? '(' + p.vt + ')' : ''}</span></div>
                <div class="detail-field"><span class="detail-label">Year</span><span class="detail-value">${p.y || '\u2014'}</span></div>
                <div class="detail-field"><span class="detail-label">Ethics</span><span class="detail-value">${ethDetail.join(', ') || '\u2014'}</span></div>
                <div class="detail-field"><span class="detail-label">Benchmark</span><span class="detail-value">${esc(bn) || '\u2014'}</span></div>
                <div class="detail-field"><span class="detail-label">Measures</span><span class="detail-value">${esc(wm) || '\u2014'}</span></div>
                <div class="detail-field"><span class="detail-label">Cultures</span><span class="detail-value">${(p.cu||[]).join(', ') || '\u2014'}</span></div>
                <div class="detail-field"><span class="detail-label">Languages</span><span class="detail-value">${(p.ln||[]).join(', ') || '\u2014'}</span></div>
                <div class="detail-field"><span class="detail-label">Religion</span><span class="detail-value">${(p.rv||[]).join(', ') || '\u2014'}</span></div>
                <div class="detail-field"><span class="detail-label">Models</span><span class="detail-value">${(p.lm||[]).join(', ') || '\u2014'}</span></div>
                <div class="detail-field"><span class="detail-label">Links</span><span class="detail-value">${links.join(' | ') || '\u2014'}</span></div>
                <div class="detail-field"><span class="detail-label">File</span><span class="detail-value">${esc(p.fn)}</span></div>
            </div>
            ${ab ? `<div class="abstract-text"><strong>Abstract:</strong> ${esc(ab)}</div>` : ''}
        </div>
    </td></tr>`;
}


// ═══════════════════════════════════════════════════════════════════════════
// MULTI-SELECT DROPDOWN
// ═══════════════════════════════════════════════════════════════════════════

class MultiSelect {
    static _instances = [];

    /**
     * @param {string} containerId - DOM id of the container div
     * @param {object} config
     * @param {string} config.dimension - FilterState dimension key
     * @param {string} config.label - Display label
     * @param {Array<{value:*, label:string}>} config.options - Available options
     * @param {function(paper, value):boolean} config.matchFn - Does paper match this option value?
     * @param {function(string):*} [config.parseValue] - Convert string to typed value (e.g., year → number)
     */
    constructor(containerId, config) {
        this.el = document.getElementById(containerId);
        if (!this.el) return;
        this.dim = config.dimension;
        this.label = config.label;
        this.allOptions = config.options;
        this.matchFn = config.matchFn;
        this._parseFn = config.parseValue || null;
        this.el.setAttribute('data-dim', this.dim);
        this.isOpen = false;

        MultiSelect._instances.push(this);
        this._build();
        this._update(); // initial state

        FilterState.subscribe(() => this._update());

        document.addEventListener('click', (e) => {
            if (!this.el.contains(e.target)) this._close();
        });
    }

    _build() {
        const optsHtml = this.allOptions.map(opt =>
            `<label class="msel-option" data-value="${esc(String(opt.value))}">
                <input type="checkbox" value="${esc(String(opt.value))}">
                <span class="msel-opt-label">${esc(opt.label)}</span>
                <span class="msel-opt-count">0</span>
            </label>`
        ).join('');

        this.el.innerHTML =
            `<button class="msel-trigger" type="button">
                <span class="msel-label">${esc(this.label)}</span>
                <span class="msel-chevron">&#9662;</span>
            </button>
            <div class="msel-panel" style="display:none;">${optsHtml}</div>`;

        this.el.querySelector('.msel-trigger').addEventListener('click', (e) => {
            e.stopPropagation();
            this.isOpen ? this._close() : this._open();
        });

        this.el.querySelectorAll('.msel-option input').forEach(cb => {
            cb.addEventListener('change', (e) => {
                e.stopPropagation();
                FilterState.toggle(this.dim, this._parseValue(cb.value));
            });
        });
    }

    /** Config-driven parseValue — defaults to identity, year uses +str */
    _parseValue(str) {
        if (this._parseFn) return this._parseFn(str);
        return str;
    }

    _open() {
        MultiSelect._instances.forEach(ms => { if (ms !== this) ms._close(); });
        this.isOpen = true;
        this.el.querySelector('.msel-panel').style.display = '';
        this.el.classList.add('msel-open');
    }

    _close() {
        this.isOpen = false;
        const panel = this.el.querySelector('.msel-panel');
        if (panel) panel.style.display = 'none';
        this.el.classList.remove('msel-open');
    }

    _update() {
        const activeSet = FilterState.getFilters(this.dim);
        const crossFiltered = FilterState.getCrossFiltered(this.dim);

        // Update trigger label
        const trigger = this.el.querySelector('.msel-label');
        if (activeSet.size === 0) {
            trigger.textContent = this.label;
            this.el.classList.remove('msel-active');
        } else if (activeSet.size === 1) {
            const val = [...activeSet][0];
            const opt = this.allOptions.find(o => String(o.value) === String(val));
            trigger.textContent = `${this.label}: ${opt ? opt.label : val}`;
            this.el.classList.add('msel-active');
        } else {
            trigger.textContent = `${this.label} (${activeSet.size})`;
            this.el.classList.add('msel-active');
        }

        // Update each option: checked state + count
        this.el.querySelectorAll('.msel-option').forEach(el => {
            const val = this._parseValue(el.dataset.value);
            const cb = el.querySelector('input');
            const countEl = el.querySelector('.msel-opt-count');

            cb.checked = activeSet.has(val);

            const count = crossFiltered.filter(p => this.matchFn(p, val)).length;
            countEl.textContent = count;

            if (count === 0 && !activeSet.has(val)) {
                el.classList.add('msel-opt-zero');
            } else {
                el.classList.remove('msel-opt-zero');
            }
        });
    }

    static resetAll() {
        // No-op: FilterState.clear() handles state, _update() handles UI via subscription
    }
}


// ═══════════════════════════════════════════════════════════════════════════
// INITIALIZATION
// ═══════════════════════════════════════════════════════════════════════════

/**
 * Called when data-detail.js finishes loading (async).
 * Merges detail data into DATA and rebuilds search index.
 * Guards against being called before FilterState.init().
 */
function _onDetailLoaded() {
    if (typeof DATA_DETAIL !== 'undefined' && typeof DATA !== 'undefined') {
        DATA._detail = DATA_DETAIL;
        if (FilterState._papers) FilterState._buildSearchIndex();
    }
}

document.addEventListener('DOMContentLoaded', () => {
    if (typeof DATA === 'undefined') {
        document.body.innerHTML = '<div style="padding:40px;color:#ef4444;">Error: data.js not found. Run generate_vault_dashboard_4.py first.</div>';
        return;
    }

    // Init detail data reference (may already be loaded if cached, or will be set by _onDetailLoaded)
    DATA._detail = (typeof DATA_DETAIL !== 'undefined') ? DATA_DETAIL : null;

    // Init FilterState
    FilterState.init(DATA.papers);

    // Build filename → full paper lookup for sub-tab paper tables
    DATA._paperByFn = {};
    DATA.papers.forEach(p => { DATA._paperByFn[p.fn] = p; });

    // Init managers
    TabManager.init();
    FilterBar.init();
    Explorer.init();

    // Populate header KPIs
    document.getElementById('kpi-total').textContent = fmt(DATA.agg.total);
    document.getElementById('kpi-date').textContent = DATA.generated;

    // Init overview tab (default active)
    if (typeof Charts !== 'undefined') {
        Charts.initTab('overview');
        TabManager.markInitialized('overview');
    }

    // ── Multi-Select Dropdowns (loop-wired from FILTER_DIMS registry) ──
    for (const dim of FILTER_DIMS) {
        if (!dim.mselId) continue;
        new MultiSelect(dim.mselId, {
            dimension: dim.key,
            label: dim.label,
            options: dim.options(),
            matchFn: dim.match,
            parseValue: dim.parseValue,
        });
    }

    // Initial render of explorer
    Explorer.render(DATA.papers);
});
