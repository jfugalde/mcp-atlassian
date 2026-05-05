/**
 * Opens the Seedgrow WhatsApp widget when the in-page PDP trigger is used
 * (floating launcher is hidden via CSS until the chat panel is active).
 */
(function () {
  function showWidgetRoot(root) {
    root.style.visibility = 'visible';
    root.style.opacity = '1';
    root.style.pointerEvents = 'auto';
  }

  function maybeHideWidgetRoot(root) {
    var box = root.querySelector('.wa__popup_chat_box');
    if (box && box.classList.contains('wa__active')) return;
    root.style.opacity = '0';
    root.style.visibility = 'hidden';
    root.style.pointerEvents = 'none';
  }

  document.addEventListener(
    'click',
    function (e) {
      var trigger = e.target && e.target.closest && e.target.closest('[data-pdp-whatsapp-launcher]');
      if (!trigger) return;
      e.preventDefault();
      var root = document.querySelector('.wa__widget_container');
      var btn = document.querySelector('.wa__btn_popup');
      if (!root || !btn) return;
      showWidgetRoot(root);
      window.setTimeout(function () {
        btn.click();
      }, 0);
    },
    true
  );

  function attachCloseObserver() {
    var root = document.querySelector('.wa__widget_container');
    var box = root && root.querySelector('.wa__popup_chat_box');
    if (!root || !box || typeof MutationObserver === 'undefined') return;
    var obs = new MutationObserver(function () {
      maybeHideWidgetRoot(root);
    });
    obs.observe(box, { attributes: true, attributeFilter: ['class'] });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', attachCloseObserver);
  } else {
    attachCloseObserver();
  }
})();
