/* ==========================================================================
   Moon Café — popup.js
   Product details popup on the Menu page, built on the native <dialog>:
   - showModal() makes the rest of the page inert and traps focus
   - Escape closes it (native), as do the close button and a click on the
     dark backdrop; focus returns to the card that opened it
   - page scrolling is locked while it is open
   Only verified data is shown: product name, category and image.
   ========================================================================== */
(function () {
  'use strict';

  var dialog = document.querySelector('[data-product-dialog]');
  if (!dialog || typeof dialog.showModal !== 'function') return;

  var img = dialog.querySelector('[data-pd-image]');
  var nameEl = dialog.querySelector('[data-pd-name]');
  var catEl = dialog.querySelector('[data-pd-category]');
  var closeBtn = dialog.querySelector('[data-product-close]');
  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
  var trigger = null;
  var closing = false;

  function open(btn) {
    trigger = btn;
    nameEl.textContent = btn.getAttribute('data-name');
    catEl.textContent = btn.getAttribute('data-category');
    img.src = btn.getAttribute('data-image');
    img.alt = btn.getAttribute('data-name');
    dialog.querySelector('.product-dialog__inner').scrollTop = 0;
    document.body.classList.add('no-scroll');
    dialog.showModal();
    closeBtn.focus();
  }

  function finishClose() {
    dialog.classList.remove('is-closing');
    closing = false;
    if (dialog.open) dialog.close();
  }

  function requestClose() {
    if (!dialog.open || closing) return;
    if (reduceMotion.matches) { finishClose(); return; }
    closing = true;
    dialog.classList.add('is-closing');
    setTimeout(finishClose, 220);
  }

  // Escape: animate out instead of the instant native close
  dialog.addEventListener('cancel', function (e) {
    e.preventDefault();
    requestClose();
  });

  dialog.addEventListener('close', function () {
    document.body.classList.remove('no-scroll');
    if (trigger) trigger.focus({ preventScroll: true });
  });

  closeBtn.addEventListener('click', requestClose);

  // A click on the backdrop lands on the <dialog> element itself
  dialog.addEventListener('click', function (e) {
    if (e.target === dialog) requestClose();
  });

  document.addEventListener('click', function (e) {
    var btn = e.target.closest('[data-product-open]');
    if (btn) open(btn);
  });
})();
