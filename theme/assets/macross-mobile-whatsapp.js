(function () {
  function showWidgetRoot(root) {
    root.classList.add('wa__mobile-menu-open');
    root.style.display = 'block';
    root.style.visibility = 'visible';
    root.style.opacity = '1';
    root.style.pointerEvents = 'auto';
  }

  function hideWidgetRoot(root) {
    var box = root.querySelector('.wa__popup_chat_box');
    if (box && box.classList.contains('wa__active')) return;
    root.classList.remove('wa__mobile-menu-open');
    root.style.display = '';
    root.style.opacity = '';
    root.style.visibility = '';
    root.style.pointerEvents = '';
  }

  document.addEventListener(
    'click',
    function (e) {
      var trigger =
        e.target && e.target.closest && e.target.closest('[data-mobile-whatsapp-launcher]');
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
      hideWidgetRoot(root);
    });
    obs.observe(box, { attributes: true, attributeFilter: ['class'] });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', attachCloseObserver);
  } else {
    attachCloseObserver();
  }
})();
