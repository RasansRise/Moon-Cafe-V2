/* ==========================================================================
   Moon Café — navigation.js
   Sticky/compact header, desktop Mega Menu, mobile drawer + accordions.
   Works without GSAP; every link is a real <a href> so navigation never
   depends on this script (design.md §5, seo-strategy.md §4.4).
   ========================================================================== */
(function () {
  'use strict';

  var header = document.querySelector('[data-header]');

  /* ---- Sticky compact header ------------------------------------------- */
  if (header) {
    var ticking = false;
    var setCompact = function () {
      header.classList.toggle('is-compact', window.scrollY > 24);
      ticking = false;
    };
    window.addEventListener('scroll', function () {
      if (!ticking) { window.requestAnimationFrame(setCompact); ticking = true; }
    }, { passive: true });
    setCompact();
  }

  /* ---- Mega Menu --------------------------------------------------------- */
  var megaItem = document.querySelector('[data-mega]');
  if (megaItem) {
    var toggle = megaItem.querySelector('[data-mega-toggle]');
    var panel = megaItem.querySelector('[data-mega-panel]');
    var hoverTimer = null;
    var canHover = window.matchMedia('(hover: hover) and (pointer: fine)');

    var setOpen = function (open) {
      panel.classList.toggle('is-open', open);
      toggle.setAttribute('aria-expanded', String(open));
    };
    var isOpen = function () { return toggle.getAttribute('aria-expanded') === 'true'; };

    toggle.addEventListener('click', function () { setOpen(!isOpen()); });

    // Optional hover enhancement (design.md §5.1) — never the only way in.
    megaItem.addEventListener('mouseenter', function () {
      if (!canHover.matches) return;
      clearTimeout(hoverTimer);
      hoverTimer = setTimeout(function () { setOpen(true); }, 80);
    });
    megaItem.addEventListener('mouseleave', function () {
      if (!canHover.matches) return;
      clearTimeout(hoverTimer);
      hoverTimer = setTimeout(function () { setOpen(false); }, 180);
    });

    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && isOpen()) {
        setOpen(false);
        toggle.focus();
      }
    });
    document.addEventListener('click', function (e) {
      if (isOpen() && !megaItem.contains(e.target)) setOpen(false);
    });
    megaItem.addEventListener('focusout', function (e) {
      if (e.relatedTarget && !megaItem.contains(e.relatedTarget)) setOpen(false);
    });
  }

  /* ---- Side drawer (tablet + mobile) ------------------------------------ */
  var navToggle = document.querySelector('[data-nav-toggle]');
  var drawer = document.querySelector('[data-mobile-nav]');
  if (navToggle && drawer) {
    var panel = drawer.querySelector('.drawer__panel');
    var closeBtn = drawer.querySelector('.drawer__close');

    var focusables = function () {
      return Array.prototype.filter.call(
        panel.querySelectorAll('a[href], button:not([disabled])'),
        function (el) { return el.offsetParent !== null; }
      );
    };

    var setDrawer = function (open, returnFocus) {
      drawer.classList.toggle('is-open', open);
      if (open) drawer.removeAttribute('inert'); else drawer.setAttribute('inert', '');
      navToggle.setAttribute('aria-expanded', String(open));
      document.body.classList.toggle('no-scroll', open);
      if (open) {
        setTimeout(function () { if (closeBtn) closeBtn.focus(); }, 60);
      } else if (returnFocus) {
        navToggle.focus();
      }
    };
    var isOpen = function () { return drawer.classList.contains('is-open'); };

    navToggle.addEventListener('click', function () { setDrawer(!isOpen()); });
    drawer.querySelectorAll('[data-nav-close]').forEach(function (el) {
      el.addEventListener('click', function () { setDrawer(false, true); });
    });

    document.addEventListener('keydown', function (e) {
      if (!isOpen()) return;
      if (e.key === 'Escape') { setDrawer(false, true); return; }
      if (e.key === 'Tab') { // keep focus inside the dialog
        var items = focusables();
        if (!items.length) return;
        var first = items[0];
        var last = items[items.length - 1];
        if (e.shiftKey && document.activeElement === first) { last.focus(); e.preventDefault(); }
        else if (!e.shiftKey && document.activeElement === last) { first.focus(); e.preventDefault(); }
      }
    });

    // Same-page anchors (e.g. #rewards) close the drawer.
    panel.addEventListener('click', function (e) {
      if (e.target.closest('a[href]')) setDrawer(false);
    });
    window.matchMedia('(min-width: 1000px)').addEventListener('change', function (mq) {
      if (mq.matches && isOpen()) setDrawer(false);
    });
  }
})();
