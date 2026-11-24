/* ==========================================================================
   Moon Café — animations.js
   Performance-conscious motion: brief preloader, interactive hero (ribbon
   marquee + pointer parallax cups), scroll reveals. Transform/opacity only.
   Everything is progressive enhancement and respects prefers-reduced-motion
   (design.md §7). Written in vanilla JS; GSAP can replace the rAF loops later
   if a timeline genuinely needs it.
   ========================================================================== */
(function () {
  'use strict';

  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)');

  /* ---- Preloader: short and never blocking ------------------------------ */
  var preloader = document.querySelector('.preloader');
  var hidePreloader = function () {
    if (!preloader || preloader.classList.contains('is-done')) return;
    preloader.classList.add('is-done');
    document.documentElement.classList.add('is-loaded');
    setTimeout(function () { if (preloader) preloader.remove(); }, 600);
  };
  if (preloader) {
    if (reduceMotion.matches) {
      hidePreloader();
    } else {
      window.addEventListener('load', hidePreloader, { once: true });
      setTimeout(hidePreloader, 900); // hard cap — content is never held back
    }
  }

  /* ---- Scroll reveal ------------------------------------------------------ */
  var revealEls = document.querySelectorAll('[data-reveal]');
  if (revealEls.length) {
    if (reduceMotion.matches || !('IntersectionObserver' in window)) {
      revealEls.forEach(function (el) { el.classList.add('is-visible'); });
    } else {
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add('is-visible');
            io.unobserve(entry.target);
          }
        });
      }, { rootMargin: '0px 0px -8% 0px', threshold: 0.12 });
      revealEls.forEach(function (el) { io.observe(el); });
    }
  }

  /* ---- Rewards: full-screen scroll sequence ----------------------------- */
  var rewards = document.querySelector('[data-rewards]');
  if (rewards) {
    var steps = Array.prototype.slice.call(rewards.querySelectorAll('[data-step]'))
      .sort(function (a, b) { return a.getAttribute('data-step') - b.getAttribute('data-step'); });
    var stepValues = steps.map(function (el) { return el.getAttribute('data-step'); })
      .filter(function (v, i, arr) { return arr.indexOf(v) === i; });
    var cup = rewards.querySelector('[data-rewards-cup]');
    var tallEnough = window.matchMedia('(min-height: 620px)');
    var rTicking = false;
    var cupShift = 0;
    var pin = rewards.querySelector('.rewards__pin');

    var updateRewards = function () {
      rTicking = false;
      if (!rewards.classList.contains('is-pinned')) return;
      var total = rewards.offsetHeight - window.innerHeight;
      var p = Math.min(Math.max(-rewards.getBoundingClientRect().top / total, 0), 1);
      // First slice shows the cup alone; each following slice reveals the next box.
      // Elements sharing a data-step value appear together.
      var active = Math.floor(p * (stepValues.length + 1.2));
      steps.forEach(function (el) {
        el.classList.toggle('is-on', stepValues.indexOf(el.getAttribute('data-step')) < active);
      });
      if (cup) {
        // Starts alone in the middle of the screen, then settles into its slot.
        var settle = Math.min(p * 5, 1); // settled before the heading appears
        var r = cup.getBoundingClientRect();
        var baseCenter = r.top + r.height / 2 - cupShift;
        var pinRect = pin.getBoundingClientRect();
        cupShift = (pinRect.top + pinRect.height / 2 - baseCenter) * (1 - settle);
        cup.style.transform = 'translateY(' + cupShift.toFixed(1) + 'px) scale(' + (1.22 - 0.22 * settle).toFixed(3) + ') rotate(' + (-6 + 6 * settle).toFixed(2) + 'deg)';
      }
    };
    var inner = rewards.querySelector('.rewards__inner');
    // Pin only if the whole scene fits the viewport; otherwise show it as a normal section.
    var fits = function () {
      var pinEl = rewards.querySelector('.rewards__pin');
      var cs = getComputedStyle(pinEl);
      var room = window.innerHeight - parseFloat(cs.paddingTop) - parseFloat(cs.paddingBottom);
      return inner.scrollHeight <= room;
    };
    var setMode = function () {
      var pinned = tallEnough.matches && !reduceMotion.matches && fits();
      rewards.classList.toggle('is-pinned', pinned);
      if (!pinned) {
        steps.forEach(function (el) { el.classList.remove('is-on'); });
        if (cup) cup.style.transform = '';
        cupShift = 0;
      }
      updateRewards();
    };
    window.addEventListener('scroll', function () {
      if (!rTicking) { rTicking = true; window.requestAnimationFrame(updateRewards); }
    }, { passive: true });
    window.addEventListener('resize', function () { setMode(); });
    tallEnough.addEventListener('change', setMode);
    reduceMotion.addEventListener('change', setMode);
    setMode();
  }

  /* ---- Interactive hero --------------------------------------------------- */
  var hero = document.querySelector('[data-hero]');
  if (!hero) return;

  var stage = hero.querySelector('[data-hero-stage]');
  var textPath = hero.querySelector('[data-ribbon-path]');
  var textEl = hero.querySelector('[data-ribbon-text]');
  var cups = Array.prototype.slice.call(hero.querySelectorAll('.hero__cup')).map(function (el, i) {
    return { el: el, depth: parseFloat(el.getAttribute('data-depth')) || 1, phase: i * 1.7, x: 0, y: 0, r: 0 };
  });

  var isRTL = document.documentElement.dir === 'rtl';
  var baseOffset = 60;
  var repLength = 0;
  var shift = 0;
  var speed = 26;        // viewBox units per second
  var boost = 0;
  var pointer = { x: 0, y: 0, active: false };
  var running = false;
  var visible = true;
  var last = 0;
  var start = performance.now();

  var measure = function () {
    if (!textEl) return;
    try { repLength = textEl.getComputedTextLength() / 4; } catch (e) { repLength = 0; }
  };

  var finePointer = window.matchMedia('(pointer: fine)');
  hero.addEventListener('pointermove', function (e) {
    if (!finePointer.matches) return;
    var rect = stage.getBoundingClientRect();
    pointer.x = ((e.clientX - rect.left) / rect.width) * 2 - 1;
    pointer.y = ((e.clientY - rect.top) / rect.height) * 2 - 1;
    pointer.active = true;
  });
  hero.addEventListener('pointerleave', function () { pointer.active = false; });

  var lastScroll = window.scrollY;
  window.addEventListener('scroll', function () {
    var y = window.scrollY;
    boost = Math.min(boost + Math.abs(y - lastScroll) * 2.2, 420);
    lastScroll = y;
  }, { passive: true });

  var frame = function (now) {
    if (!running) return;
    var dt = Math.min((now - last) / 1000, 0.05);
    last = now;
    var t = (now - start) / 1000;

    // Ribbon marquee
    if (textPath && repLength > 0) {
      shift = (shift + (speed + boost) * dt) % repLength;
      boost *= 0.92;
      var offset = isRTL ? baseOffset - repLength + shift : baseOffset - shift;
      textPath.setAttribute('startOffset', offset.toFixed(2));
    }

    // Cups: idle float + pointer parallax (eased)
    var px = pointer.active ? pointer.x : 0;
    var py = pointer.active ? pointer.y : 0;
    cups.forEach(function (c) {
      var tx = px * 14 * c.depth;
      var ty = py * 8 * c.depth + Math.sin(t * 1.1 + c.phase) * 4 * c.depth;
      var tr = px * 2.2 * c.depth;
      c.x += (tx - c.x) * 0.08;
      c.y += (ty - c.y) * 0.08;
      c.r += (tr - c.r) * 0.08;
      c.el.style.transform = 'translate3d(' + c.x.toFixed(2) + 'px,' + c.y.toFixed(2) + 'px,0) rotate(' + c.r.toFixed(2) + 'deg)';
    });

    window.requestAnimationFrame(frame);
  };

  var startLoop = function () {
    if (running || reduceMotion.matches || !visible) return;
    running = true;
    last = performance.now();
    window.requestAnimationFrame(frame);
  };
  var stopLoop = function () { running = false; };

  if ('IntersectionObserver' in window) {
    new IntersectionObserver(function (entries) {
      visible = entries[0].isIntersecting;
      if (visible) startLoop(); else stopLoop();
    }).observe(hero);
  }

  reduceMotion.addEventListener('change', function () {
    if (reduceMotion.matches) {
      stopLoop();
      cups.forEach(function (c) { c.el.style.transform = ''; });
    } else {
      startLoop();
    }
  });

  var init = function () { measure(); startLoop(); };
  if (document.fonts && document.fonts.ready) {
    document.fonts.ready.then(init);
  } else {
    init();
  }
  window.addEventListener('resize', measure);
})();
