/* ==========================================================================
   Moon Café — main.js
   Shared page behaviour: featured-products carousel (looping, swipe, RTL),
   footer year.
   ========================================================================== */
(function () {
  'use strict';

  /* ---- Footer year -------------------------------------------------------- */
  document.querySelectorAll('[data-year]').forEach(function (el) {
    el.textContent = String(new Date().getFullYear());
  });

  /* ---- Featured carousel -------------------------------------------------- */
  document.querySelectorAll('[data-carousel]').forEach(initCarousel);

  function initCarousel(root) {
    var viewport = root.querySelector('[data-carousel-viewport]');
    var track = root.querySelector('[data-carousel-track]');
    var prevBtn = root.querySelector('[data-carousel-prev]');
    var nextBtn = root.querySelector('[data-carousel-next]');
    var dotsWrap = root.querySelector('[data-carousel-dots]');
    var status = root.querySelector('[data-carousel-status]');
    var slides = Array.prototype.slice.call(track.children);
    var total = slides.length;
    if (total < 2) return;

    var isRTL = document.documentElement.dir === 'rtl';
    var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
    var DURATION = 520;
    var current = 0;   // data-index of the first visible slide
    var busy = false;
    var gotoLabel = root.getAttribute('data-i18n-goto') || 'Show product {n}';
    var statusLabel = root.getAttribute('data-i18n-status') || 'Product {n} of {t}';

    prevBtn.hidden = false;
    nextBtn.hidden = false;

    // Dots — one per product (matches approved mockup)
    var dots = slides.map(function (_, i) {
      var b = document.createElement('button');
      b.type = 'button';
      b.className = 'carousel__dot';
      b.setAttribute('aria-label', gotoLabel.replace('{n}', i + 1));
      b.addEventListener('click', function () { goTo(i); });
      dotsWrap.appendChild(b);
      return b;
    });

    function update(announce) {
      dots.forEach(function (d, i) {
        if (i === current) d.setAttribute('aria-current', 'true');
        else d.removeAttribute('aria-current');
      });
      if (announce && status) {
        status.textContent = statusLabel.replace('{n}', current + 1).replace('{t}', total);
      }
    }

    function slideWidth() { return track.firstElementChild.getBoundingClientRect().width; }
    function dirSign() { return isRTL ? 1 : -1; }

    function animate(toX, duration) {
      return new Promise(function (resolve) {
        if (!duration) {
          track.style.transition = 'none';
          track.style.transform = toX ? 'translateX(' + toX + 'px)' : '';
          resolve();
          return;
        }
        var done = false;
        var finish = function () {
          if (done) return;
          done = true;
          track.removeEventListener('transitionend', finish);
          resolve();
        };
        track.addEventListener('transitionend', finish);
        setTimeout(finish, duration + 80); // safety net
        track.style.transition = 'transform ' + duration + 'ms cubic-bezier(0.22, 1, 0.36, 1)';
        track.style.transform = 'translateX(' + toX + 'px)';
      });
    }

    function stepNext(duration) {
      var w = slideWidth();
      return animate(dirSign() * w, duration).then(function () {
        track.style.transition = 'none';
        track.appendChild(track.firstElementChild);
        track.style.transform = '';
        current = (current + 1) % total;
      });
    }

    function stepPrev(duration) {
      var w = slideWidth();
      track.style.transition = 'none';
      track.insertBefore(track.lastElementChild, track.firstElementChild);
      track.style.transform = 'translateX(' + (dirSign() * w) + 'px)';
      void track.offsetWidth; // reflow before animating back to 0
      return animate(0, duration).then(function () {
        track.style.transform = '';
        current = (current - 1 + total) % total;
      });
    }

    function run(fn, steps) {
      if (busy) return;
      busy = true;
      var d = reduceMotion.matches ? 0 : (steps > 1 ? Math.round(DURATION / 1.8) : DURATION);
      var chain = Promise.resolve();
      for (var i = 0; i < steps; i++) chain = chain.then(function () { return fn(d); });
      chain.then(function () { busy = false; update(true); });
    }

    function next() { run(stepNext, 1); }
    function prev() { run(stepPrev, 1); }
    function goTo(i) {
      if (i === current) return;
      var fwd = (i - current + total) % total;
      var back = total - fwd;
      if (fwd <= back) run(stepNext, fwd); else run(stepPrev, back);
    }

    nextBtn.addEventListener('click', next);
    prevBtn.addEventListener('click', prev);

    root.addEventListener('keydown', function (e) {
      if (e.target.closest('.carousel__dot, .carousel__arrow') === null) return;
      if (e.key === 'ArrowRight') { (isRTL ? prev : next)(); e.preventDefault(); }
      if (e.key === 'ArrowLeft') { (isRTL ? next : prev)(); e.preventDefault(); }
    });

    // Swipe (touch/pen and mouse drag)
    var startX = null;
    var startY = null;
    viewport.addEventListener('pointerdown', function (e) {
      startX = e.clientX;
      startY = e.clientY;
    });
    viewport.addEventListener('pointerup', function (e) {
      if (startX === null) return;
      var dx = e.clientX - startX;
      var dy = e.clientY - startY;
      startX = null;
      if (Math.abs(dx) < 40 || Math.abs(dx) < Math.abs(dy)) return;
      var towardsNext = isRTL ? dx > 0 : dx < 0;
      if (towardsNext) next(); else prev();
    });
    viewport.addEventListener('pointercancel', function () { startX = null; });

    update(false);
  }
})();
