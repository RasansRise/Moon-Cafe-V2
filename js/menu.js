/* ==========================================================================
   Moon Café — menu.js
   Menu page: category filters + pagination over products that are already
   in the HTML (so everything stays crawlable and visible without JS).
   State lives in the URL (?category=hot-coffee&page=2) so filters are
   shareable and the Back button works.
   ========================================================================== */
(function () {
  'use strict';

  var root = document.querySelector('[data-menu]');
  if (!root) return;

  var PER_PAGE = 12;
  var i18n = {};
  try { i18n = JSON.parse(root.getAttribute('data-i18n') || '{}'); } catch (e) { /* defaults below */ }
  var t = function (key, vars) {
    var s = i18n[key] || key;
    Object.keys(vars || {}).forEach(function (k) { s = s.replace('{' + k + '}', vars[k]); });
    return s;
  };

  var grid = root.querySelector('[data-menu-grid]');
  var items = Array.prototype.slice.call(grid.children);
  var options = Array.prototype.slice.call(root.querySelectorAll('[data-filter]'));
  var selectBtn = root.querySelector('[data-select-btn]');
  var selectList = root.querySelector('[data-select-list]');
  var selectValue = root.querySelector('[data-select-value]');
  var selectCount = root.querySelector('[data-select-count]');
  var pager = root.querySelector('[data-menu-pagination]');
  var status = root.querySelector('[data-menu-status]');
  var isRTL = document.documentElement.dir === 'rtl';
  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
  var validCats = options.map(function (o) { return o.getAttribute('data-filter'); });

  var state = readURL();

  function readURL() {
    var params = new URLSearchParams(window.location.search);
    var cat = params.get('category') || 'all';
    if (validCats.indexOf(cat) === -1) cat = 'all';
    var page = parseInt(params.get('page'), 10) || 1;
    return { category: cat, page: page };
  }

  function writeURL(push) {
    var params = new URLSearchParams();
    if (state.category !== 'all') params.set('category', state.category);
    if (state.page > 1) params.set('page', String(state.page));
    var qs = params.toString();
    var url = window.location.pathname + (qs ? '?' + qs : '');
    if (push) window.history.pushState(state, '', url);
    else window.history.replaceState(state, '', url);
  }

  function matching() {
    return items.filter(function (li) {
      return state.category === 'all' || li.getAttribute('data-category') === state.category;
    });
  }

  function render(animate) {
    var list = matching();
    var pages = Math.max(1, Math.ceil(list.length / PER_PAGE));
    state.page = Math.min(Math.max(state.page, 1), pages);
    var start = (state.page - 1) * PER_PAGE;
    var visible = list.slice(start, start + PER_PAGE);

    items.forEach(function (li) { li.hidden = true; li.classList.remove('is-entering'); li.style.removeProperty('--i'); });
    visible.forEach(function (li, i) {
      li.hidden = false;
      if (animate && !reduceMotion.matches) {
        li.style.setProperty('--i', i);
        void li.offsetWidth; // restart the entrance animation
        li.classList.add('is-entering');
      }
    });

    options.forEach(function (o) {
      var on = o.getAttribute('data-filter') === state.category;
      o.setAttribute('aria-selected', String(on));
      if (on) {
        selectValue.textContent = o.querySelector('.menu-select__text').textContent;
        selectCount.textContent = o.querySelector('.menu-filter__count').textContent;
      }
    });

    if (status) {
      status.textContent = list.length
        ? t('status', { from: start + 1, to: start + visible.length, total: list.length })
        : '';
    }
    renderPager(pages);
  }

  function pageButton(label, page, opts) {
    var b = document.createElement('button');
    b.type = 'button';
    b.className = 'pagination__btn' + (opts.cls ? ' ' + opts.cls : '');
    b.innerHTML = label;
    if (opts.aria) b.setAttribute('aria-label', opts.aria);
    if (opts.current) b.setAttribute('aria-current', 'page');
    if (opts.disabled) b.disabled = true;
    b.addEventListener('click', function () { goTo(page); });
    return b;
  }

  // 1 … 4 5 6 … 10 — compact list of page numbers around the current page
  function pageList(total, current) {
    if (total <= 7) return Array.from({ length: total }, function (_, i) { return i + 1; });
    var out = [1];
    var from = Math.max(2, current - 1);
    var to = Math.min(total - 1, current + 1);
    if (from > 2) out.push('…');
    for (var i = from; i <= to; i++) out.push(i);
    if (to < total - 1) out.push('…');
    out.push(total);
    return out;
  }

  function renderPager(total) {
    pager.innerHTML = '';
    pager.hidden = total <= 1;
    if (total <= 1) return;
    var arrow = function (dir) {
      // "prev" points back in reading direction (left in LTR, right in RTL)
      var d = (dir === 'prev') !== isRTL ? 'M15 5l-7 7 7 7' : 'M9 5l7 7-7 7';
      return '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="' + d + '" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>';
    };
    pager.appendChild(pageButton(arrow('prev'), state.page - 1, { cls: 'pagination__arrow', aria: t('prev'), disabled: state.page === 1 }));
    pageList(total, state.page).forEach(function (n) {
      if (n === '…') {
        var gap = document.createElement('span');
        gap.className = 'pagination__gap';
        gap.textContent = '…';
        gap.setAttribute('aria-hidden', 'true');
        pager.appendChild(gap);
      } else {
        pager.appendChild(pageButton(String(n), n, { aria: t('page', { n: n }), current: n === state.page }));
      }
    });
    pager.appendChild(pageButton(arrow('next'), state.page + 1, { cls: 'pagination__arrow', aria: t('next'), disabled: state.page === total }));
  }

  function scrollToCatalog() {
    var top = root.getBoundingClientRect().top + window.scrollY - 90;
    if (window.scrollY > top) {
      window.scrollTo({ top: top, behavior: reduceMotion.matches ? 'auto' : 'smooth' });
    }
  }

  function goTo(page) {
    state.page = page;
    writeURL(true);
    render(true);
    scrollToCatalog();
  }

  function setCategory(cat, push) {
    state.category = validCats.indexOf(cat) === -1 ? 'all' : cat;
    state.page = 1;
    writeURL(push);
    render(true);
  }

  /* ---- Category dropdown (accessible listbox) -------------------------- */
  var activeIndex = 0;
  var isOpen = function () { return selectBtn.getAttribute('aria-expanded') === 'true'; };

  function highlight(i) {
    activeIndex = (i + options.length) % options.length;
    options.forEach(function (o, k) { o.classList.toggle('is-active', k === activeIndex); });
    selectList.setAttribute('aria-activedescendant', options[activeIndex].id);
    options[activeIndex].scrollIntoView({ block: 'nearest' });
  }
  function openList() {
    selectBtn.setAttribute('aria-expanded', 'true');
    root.querySelector('[data-menu-select]').classList.add('is-open');
    var sel = options.findIndex(function (o) { return o.getAttribute('aria-selected') === 'true'; });
    highlight(sel < 0 ? 0 : sel);
    selectList.focus({ preventScroll: true });
  }
  function closeList(focusBtn) {
    selectBtn.setAttribute('aria-expanded', 'false');
    root.querySelector('[data-menu-select]').classList.remove('is-open');
    if (focusBtn) selectBtn.focus({ preventScroll: true });
  }
  function choose(i) {
    var cat = options[i].getAttribute('data-filter');
    closeList(true);
    if (cat !== state.category) { setCategory(cat, true); scrollToCatalog(); }
  }

  selectBtn.addEventListener('click', function () { if (isOpen()) closeList(true); else openList(); });
  selectBtn.addEventListener('keydown', function (e) {
    if (e.key === 'ArrowDown' || e.key === 'ArrowUp') { e.preventDefault(); openList(); }
  });
  selectList.addEventListener('keydown', function (e) {
    if (e.key === 'ArrowDown') { e.preventDefault(); highlight(activeIndex + 1); }
    else if (e.key === 'ArrowUp') { e.preventDefault(); highlight(activeIndex - 1); }
    else if (e.key === 'Home') { e.preventDefault(); highlight(0); }
    else if (e.key === 'End') { e.preventDefault(); highlight(options.length - 1); }
    else if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); choose(activeIndex); }
    else if (e.key === 'Escape') { e.preventDefault(); closeList(true); }
    else if (e.key === 'Tab') { closeList(false); }
  });
  options.forEach(function (o, i) {
    o.addEventListener('click', function () { choose(i); });
    o.addEventListener('mousemove', function () { if (activeIndex !== i) highlight(i); });
  });
  document.addEventListener('click', function (e) {
    if (isOpen() && !root.querySelector('[data-menu-select]').contains(e.target)) closeList(false);
  });

  // Mega-menu category links point to this page (?category=…): filter in place
  document.addEventListener('click', function (e) {
    var a = e.target.closest('a[href*="?category="]');
    if (!a || e.metaKey || e.ctrlKey || e.shiftKey || e.button !== 0) return;
    var url = new URL(a.href, window.location.href);
    if (url.pathname !== window.location.pathname) return;
    e.preventDefault();
    setCategory(url.searchParams.get('category'), true);
    var panel = document.querySelector('[data-mega-panel].is-open');
    if (panel) document.querySelector('[data-mega-toggle]').click();
    scrollToCatalog();
  });

  window.addEventListener('popstate', function () {
    state = readURL();
    render(true);
  });

  root.classList.add('is-ready');
  writeURL(false);
  render(false);
})();
