/**
 * CEI Dashboard v4 — Application Logic
 * FilterState singleton, tab switching, Paper Explorer, filter bar rendering
 */

// ═══════════════════════════════════════════════════════════════════════════
// FILTER STATE
// ═══════════════════════════════════════════════════════════════════════════

const FilterState = {
    _filters: {
        year: new Set(),
        venueType: new Set(),
        venue: new Set(),
        confFamily: new Set(),
        ethics: new Set(),
        isBenchmark: new Set(),
        culture: new Set(),
        language: new Set(),
        religion: new Set(),
        llmModel: new Set(),
        category: new Set(),
        flag: new Set(),
    },
    searchQuery: '',
    _listeners: [],
    _papers: null,        // cached reference to DATA.papers
    _searchIndex: null,   // pre-built search text

    init(papers) {
        this._papers = papers;
        // Pre-build lowercase search text for each paper
        this._searchIndex = papers.map(p =>
            [p.t, p.fa, p.la, p.cc, p.ab, p.bn, p.wm,
             (p.cu||[]).join(' '), (p.ln||[]).join(' '),
             (p.rv||[]).join(' '), (p.lm||[]).join(' '),
             (p.cs||[]).join(' ')
            ].join(' ').toLowerCase()
        );
    },

    subscribe(fn) { this._listeners.push(fn); },

    notify() {
        const filtered = this.getFilteredPapers();
        this._listeners.forEach(fn => fn(filtered));
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

    getFilteredPapers(excludeDim) {
        if (!this._papers) return [];
        let result = this._papers;

        // Apply set filters (AND across dimensions, OR within)
        // When excludeDim is set, skip that dimension (for cross-filter counting)
        const f = this._filters;
        if (excludeDim !== 'year' && f.year.size) result = result.filter(p => f.year.has(p.y));
        if (excludeDim !== 'venueType' && f.venueType.size) result = result.filter(p => f.venueType.has(p.vt));
        if (excludeDim !== 'venue' && f.venue.size) result = result.filter(p => f.venue.has(p.cc));
        if (excludeDim !== 'confFamily' && f.confFamily.size) result = result.filter(p => f.confFamily.has(p.cf));
        if (excludeDim !== 'ethics' && f.ethics.size) {
            result = result.filter(p => {
                if (f.ethics.has('Yes') && p.eo) return true;
                if (f.ethics.has('No') && !p.eo) return true;
                if (f.ethics.has('VE') && p.ve) return true;
                if (f.ethics.has('DE') && p.de) return true;
                if (f.ethics.has('CU') && p.ue) return true;
                return false;
            });
        }
        if (excludeDim !== 'isBenchmark' && f.isBenchmark.size) {
            result = result.filter(p => {
                if (f.isBenchmark.has('Yes') && p.ib) return true;
                if (f.isBenchmark.has('No') && !p.ib) return true;
                return false;
            });
        }
        if (excludeDim !== 'culture' && f.culture.size) result = result.filter(p => p.cu && p.cu.some(c => f.culture.has(c)));
        if (excludeDim !== 'language' && f.language.size) result = result.filter(p => p.ln && p.ln.some(l => f.language.has(l)));
        if (excludeDim !== 'religion' && f.religion.size) result = result.filter(p => p.rv && p.rv.some(r => f.religion.has(r)));
        if (excludeDim !== 'llmModel' && f.llmModel.size) {
            result = result.filter(p => {
                if (f.llmModel.has('Yes') && p.lm && p.lm.length) return true;
                if (f.llmModel.has('No') && (!p.lm || !p.lm.length)) return true;
                return p.lm && p.lm.some(m => f.llmModel.has(m));
            });
        }
        if (excludeDim !== 'category' && f.category.size) result = result.filter(p => p.cs && p.cs.some(c => f.category.has(c)));
        if (excludeDim !== 'flag' && f.flag.size) {
            result = result.filter(p => {
                if (f.flag.has('B') && p.ib) return true;
                if (f.flag.has('E') && p.ie) return true;
                if (f.flag.has('D') && p.id) return true;
                if (f.flag.has('C') && p.cu && p.cu.length) return true;
                if (f.flag.has('R') && p.rv && p.rv.length) return true;
                return false;
            });
        }

        // Apply text search
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
            // MultiSelects auto-update via FilterState subscription
        });
        FilterState.subscribe(() => this.render());
    },

    render() {
        const bar = document.getElementById('filter-bar');
        const chips = document.getElementById('filter-chips');
        const count = document.getElementById('filter-count');

        if (!FilterState.isActive()) {
            bar.style.display = 'none';
            return;
        }
        bar.style.display = 'flex';

        const active = FilterState.getActiveFilters();
        const filtered = FilterState.getFilteredPapers();

        // Render chips
        const dimLabels = {
            year: 'Year', venueType: 'Type', venue: 'Venue', confFamily: 'Family',
            ethics: 'Ethics', isBenchmark: 'Benchmark', culture: 'Culture',
            language: 'Language', religion: 'Religion', llmModel: 'Model',
            category: 'Category', flag: 'Flag',
        };
        let html = '';
        if (FilterState.searchQuery) {
            html += `<span class="filter-chip" data-dim="search">Search: "${FilterState.searchQuery}"
                <span class="chip-remove" data-action="clear-search">&times;</span></span>`;
        }
        for (const {dim, val} of active) {
            html += `<span class="filter-chip" data-dim="${dim}">${dimLabels[dim] || dim}: ${val}
                <span class="chip-remove" data-dim="${dim}" data-val="${val}">&times;</span></span>`;
        }
        chips.innerHTML = html;

        // Chip remove handlers
        chips.querySelectorAll('.chip-remove').forEach(el => {
            el.addEventListener('click', () => {
                if (el.dataset.action === 'clear-search') {
                    FilterState.searchQuery = '';
                    document.getElementById('explorer-search').value = '';
                    FilterState.notify();
                } else {
                    FilterState.toggle(el.dataset.dim, isNaN(el.dataset.val) ? el.dataset.val : +el.dataset.val);
                }
            });
        });

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
        if (activeHeader) activeHeader.textContent = this._sortDir > 0 ? ' ▲' : ' ▼';

        // Render table body
        const tbody = document.getElementById('explorer-tbody');
        let html = '';
        for (const p of pageItems) {
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

            // Detail row (hidden by default, toggled on click)
            if (this._expandedIdx === p.i) {
                html += this._renderDetail(p);
            }
        }
        tbody.innerHTML = html;

        // Click handlers for rows
        tbody.querySelectorAll('.paper-row').forEach(row => {
            row.addEventListener('click', () => {
                const idx = +row.dataset.idx;
                this._expandedIdx = this._expandedIdx === idx ? null : idx;
                this.render(this._papers);
            });
        });

        // Pagination
        this._renderPagination(totalPages);
    },

    _renderDetail(p) {
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

const _ptState = {};  // containerId → { papers, maxItems, expandedFn }

function renderPaperList(containerId, papers, maxItems) {
    const el = document.getElementById(containerId);
    if (!el) return;

    // Store args for re-render on expand/collapse
    if (!_ptState[containerId]) _ptState[containerId] = { expandedFn: null };
    const state = _ptState[containerId];
    state.papers = papers;
    state.maxItems = maxItems;

    const items = papers.slice(0, maxItems || 100);

    if (!items.length) {
        el.innerHTML = '<div style="color:var(--text-muted);padding:12px;">No papers in this section.</div>';
        return;
    }

    let html = `<div class="explorer-table-wrap"><table class="explorer-table">
        <thead><tr>
            <th class="col-year">Year</th>
            <th class="col-paper">Paper</th>
            <th class="col-venue">Venue</th>
            <th class="col-ethics">Ethics</th>
            <th class="col-flags">Flags</th>
        </tr></thead><tbody>`;

    for (const sp of items) {
        // Cross-reference slim paper → full paper via filename lookup
        const p = DATA._paperByFn[sp.fn] || sp;
        const vtClass = `vt-${(p.vt || 'N/A') === 'N/A' ? 'NA' : p.vt}`;
        const ethBadges = _ethicsBadges(p);
        const flags = [];
        if (p.ib) flags.push('<span class="flag-badge fb-B" title="Benchmark">B</span>');
        if (p.ie) flags.push('<span class="flag-badge fb-E" title="Eval">E</span>');
        if (p.id) flags.push('<span class="flag-badge fb-D" title="Dataset">D</span>');
        if (p.cu && p.cu.length) flags.push('<span class="flag-badge fb-C" title="Cultural">C</span>');
        if (p.rv && p.rv.length) flags.push('<span class="flag-badge fb-R" title="Religious">R</span>');

        const title = p.t || (sp.fn ? sp.fn.replace('.md', '') : '—');
        const authors = p.fa ? `${esc(p.fa)}${p.la ? ', ' + esc(p.la) : ''}` : '';

        html += `<tr class="paper-row" data-fn="${esc(sp.fn)}">
            <td class="col-year">${p.y || '—'}</td>
            <td class="col-paper">
                <div class="paper-title">${esc(title)}</div>
                ${authors ? `<div class="paper-authors">${authors}</div>` : ''}
            </td>
            <td class="col-venue"><span class="venue-badge ${vtClass}" title="${esc(p.cc || '')}">${esc(p.cc || '—')}</span></td>
            <td class="col-ethics"><div class="eth-badges">${ethBadges}</div></td>
            <td class="col-flags"><div class="flag-badges">${flags.join('')}</div></td>
        </tr>`;

        if (state.expandedFn === sp.fn) {
            html += _renderPLDetail(p);
        }
    }

    html += '</tbody></table></div>';
    el.innerHTML = html;

    // Click-to-expand handlers
    el.querySelectorAll('.paper-row').forEach(row => {
        row.addEventListener('click', () => {
            const fn = row.dataset.fn;
            state.expandedFn = state.expandedFn === fn ? null : fn;
            renderPaperList(containerId, state.papers, state.maxItems);
        });
    });
}

function _renderPLDetail(p) {
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
                <div class="detail-field"><span class="detail-label">Venue</span><span class="detail-value">${esc(p.cc || '')} ${p.vt ? '(' + p.vt + ')' : ''}</span></div>
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
}


// ═══════════════════════════════════════════════════════════════════════════
// UTILITIES
// ═══════════════════════════════════════════════════════════════════════════

function esc(str) {
    if (!str) return '';
    return String(str).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');
}

function getPaginationRange(current, total) {
    if (total <= 7) return Array.from({length: total}, (_, i) => i + 1);
    const pages = [];
    pages.push(1);
    if (current > 3) pages.push('...');
    for (let i = Math.max(2, current - 1); i <= Math.min(total - 1, current + 1); i++) {
        pages.push(i);
    }
    if (current < total - 2) pages.push('...');
    pages.push(total);
    return pages;
}

function fmt(n) {
    return n >= 1000 ? n.toLocaleString() : String(n);
}

function _ethicsBadges(p) {
    if (!p.eo) return '<span class="eth-badge eth-no">No</span>';
    const tags = [];
    if (p.ve) tags.push('<span class="eth-badge eth-ve" title="Virtue Ethics">VE</span>');
    if (p.de) tags.push('<span class="eth-badge eth-de" title="Deontological">DE</span>');
    if (p.ue) tags.push('<span class="eth-badge eth-cu" title="Consequentialism">CU</span>');
    if (!tags.length) return '<span class="eth-badge eth-yes">Yes</span>';
    return tags.join('');
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
     */
    constructor(containerId, config) {
        this.el = document.getElementById(containerId);
        if (!this.el) return;
        this.dim = config.dimension;
        this.label = config.label;
        this.allOptions = config.options;
        this.matchFn = config.matchFn;
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

    _parseValue(str) {
        if (this.dim === 'year') { const n = +str; if (!isNaN(n)) return n; }
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
        const activeSet = FilterState._filters[this.dim];
        const crossFiltered = FilterState.getFilteredPapers(this.dim);

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

document.addEventListener('DOMContentLoaded', () => {
    if (typeof DATA === 'undefined') {
        document.body.innerHTML = '<div style="padding:40px;color:#ef4444;">Error: data.js not found. Run generate_vault_dashboard_4.py first.</div>';
        return;
    }

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

    // ── Multi-Select Dropdowns ──
    // Category
    new MultiSelect('msel-category', {
        dimension: 'category',
        label: 'Category',
        options: (DATA.agg.categories || []).map(c => ({ value: c, label: c })),
        matchFn: (p, v) => p.cs && p.cs.includes(v),
    });

    // Year (distinct years, descending)
    const years = [...new Set(DATA.papers.map(p => p.y).filter(Boolean))].sort((a, b) => b - a);
    new MultiSelect('msel-year', {
        dimension: 'year',
        label: 'Year',
        options: years.map(y => ({ value: y, label: String(y) })),
        matchFn: (p, v) => p.y === v,
    });

    // Venue Type
    new MultiSelect('msel-venue-type', {
        dimension: 'venueType',
        label: 'Venue Type',
        options: Object.keys(DATA.agg.vtDist || {}).map(name => ({ value: name, label: name })),
        matchFn: (p, v) => p.vt === v,
    });

    // Ethics
    new MultiSelect('msel-ethics', {
        dimension: 'ethics',
        label: 'Ethics',
        options: [
            { value: 'Yes', label: 'Ethics: Yes' },
            { value: 'No', label: 'Ethics: No' },
            { value: 'VE', label: 'Virtue Ethics (VE)' },
            { value: 'DE', label: 'Deontological (DE)' },
            { value: 'CU', label: 'Consequentialist (CU)' },
        ],
        matchFn: (p, v) => {
            switch (v) {
                case 'Yes': return !!p.eo;
                case 'No': return !p.eo;
                case 'VE': return !!p.ve;
                case 'DE': return !!p.de;
                case 'CU': return !!p.ue;
                default: return false;
            }
        },
    });

    // LLM Model
    const models = [...new Set(DATA.papers.flatMap(p => p.lm || []))].sort();
    new MultiSelect('msel-model', {
        dimension: 'llmModel',
        label: 'Model',
        options: [
            { value: 'Yes', label: 'Has Models' },
            { value: 'No', label: 'No Models' },
            ...models.map(m => ({ value: m, label: m })),
        ],
        matchFn: (p, v) => {
            if (v === 'Yes') return !!(p.lm && p.lm.length);
            if (v === 'No') return !p.lm || !p.lm.length;
            return p.lm && p.lm.includes(v);
        },
    });

    // Flags
    new MultiSelect('msel-flag', {
        dimension: 'flag',
        label: 'Flags',
        options: [
            { value: 'B', label: 'Benchmark (B)' },
            { value: 'E', label: 'Eval (E)' },
            { value: 'D', label: 'Dataset (D)' },
            { value: 'C', label: 'Cultural (C)' },
            { value: 'R', label: 'Religious (R)' },
        ],
        matchFn: (p, v) => {
            switch (v) {
                case 'B': return !!p.ib;
                case 'E': return !!p.ie;
                case 'D': return !!p.id;
                case 'C': return !!(p.cu && p.cu.length);
                case 'R': return !!(p.rv && p.rv.length);
                default: return false;
            }
        },
    });

    // Initial render of explorer
    Explorer.render(DATA.papers);
});
