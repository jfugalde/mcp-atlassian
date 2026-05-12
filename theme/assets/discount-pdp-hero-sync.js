/**
 * Keeps discount PDP masthead (.mp-offer) prices/tier in sync with variant changes.
 * Relies on MinimogEvents VARIANT_CHANGE (same as sticky ATC) and Shopify.formatMoney.
 */
(function () {
  if (!window.MinimogEvents || !window.MinimogSettings) return;

  var root = document.querySelector('.discount-pdp[data-product-id][data-section-type="product-page"]');
  if (!root) return;

  var hero = root.querySelector('[data-discount-pdp-hero]');
  if (!hero) return;

  var productId = root.getAttribute('data-product-id');
  if (!productId) return;

  function formatCents(cents) {
    if (typeof Shopify !== 'undefined' && typeof Shopify.formatMoney === 'function') {
      return Shopify.formatMoney(cents, window.MinimogSettings.money_format);
    }
    return String(cents);
  }

  function formatUnitBase(variant) {
    var m = variant.unit_price_measurement;
    if (!m) return '';
    var refVal = m.reference_value;
    var ref = refVal == null || Number(refVal) === 1 ? '' : String(refVal);
    return ref + (m.reference_unit || '');
  }

  function refreshHeroAria() {
    var titleEl = hero.querySelector('.mp-offer__title');
    var nowEl = hero.querySelector('[data-mp-offer-now]');
    var cmpEl = hero.querySelector('[data-mp-offer-compare]');
    var tierLabel = hero.querySelector('[data-mp-offer-tier-label]');
    if (!titleEl || !nowEl) return;
    var title = titleEl.textContent.trim();
    var onSale = !hero.classList.contains('mp-offer--regular');
    var parts = [title];
    if (onSale && cmpEl && cmpEl.textContent.trim()) {
      parts.push(cmpEl.textContent.trim(), nowEl.textContent.trim());
      if (tierLabel && tierLabel.textContent.trim()) parts.push(tierLabel.textContent.trim());
    } else {
      parts.push(nowEl.textContent.trim());
    }
    hero.setAttribute('aria-label', parts.join('. '));
  }

  window.MinimogEvents.subscribe(productId + '__VARIANT_CHANGE', function (variant) {
    if (!variant) return;

    var price = variant.price;
    var cap = variant.compare_at_price;
    var onSale = cap != null && cap > price;

    var nowEl = hero.querySelector('[data-mp-offer-now]');
    if (nowEl) nowEl.innerHTML = formatCents(price);
    if (nowEl) {
      if (onSale) nowEl.classList.remove('mp-offer__now--regular');
      else nowEl.classList.add('mp-offer__now--regular');
    }

    var pricesWrap = hero.querySelector('.mp-offer__prices');
    if (pricesWrap) {
      if (onSale) pricesWrap.classList.remove('mp-offer__prices--solo');
      else pricesWrap.classList.add('mp-offer__prices--solo');
    }

    var wasWrap = hero.querySelector('[data-mp-offer-was-wrap]');
    var cmpEl = hero.querySelector('[data-mp-offer-compare]');
    if (wasWrap && cmpEl) {
      if (onSale) {
        wasWrap.classList.remove('hidden');
        cmpEl.innerHTML = formatCents(cap);
      } else {
        wasWrap.classList.add('hidden');
        cmpEl.innerHTML = '';
      }
    }

    var badge = hero.querySelector('[data-mp-offer-badge]');
    if (badge) {
      if (onSale) {
        badge.classList.remove('hidden');
        var pctEl = badge.querySelector('[data-mp-offer-pct]');
        if (pctEl) {
          var p = Math.round(((cap - price) * 100) / cap);
          pctEl.textContent = '-' + p + '%';
        }
      } else {
        badge.classList.add('hidden');
      }
    }

    hero.classList.toggle('mp-offer--regular', !onSale);

    var tierRow = hero.querySelector('[data-mp-offer-tier]');
    if (tierRow) {
      if (onSale) {
        tierRow.classList.remove('hidden');
        var saving = cap - price;
        var savedEl = tierRow.querySelector('[data-mp-offer-saved-amount]');
        if (savedEl) savedEl.innerHTML = formatCents(saving);

        var discountPct = Math.round((saving * 100) / cap);
        var tierNum = 1;
        if (discountPct >= 30) tierNum = 3;
        else if (discountPct >= 15) tierNum = 2;

        hero.classList.remove('mp-offer--tier-1', 'mp-offer--tier-2', 'mp-offer--tier-3');
        hero.classList.add('mp-offer--tier-' + tierNum);

        var tierLabel = tierRow.querySelector('[data-mp-offer-tier-label]');
        if (tierLabel) {
          var t1 = hero.getAttribute('data-tier-label-1') || '';
          var t2 = hero.getAttribute('data-tier-label-2') || '';
          var t3 = hero.getAttribute('data-tier-label-3') || '';
          tierLabel.textContent = tierNum === 3 ? t3 : tierNum === 2 ? t2 : t1;
        }
      } else {
        tierRow.classList.add('hidden');
      }
    }

    var unitRow = hero.querySelector('[data-mp-offer-unit-row]');
    var unitInner = hero.querySelector('[data-mp-offer-unit-inner]');
    if (unitRow && unitInner) {
      var um = variant.unit_price_measurement;
      if (um && variant.unit_price != null) {
        unitRow.classList.remove('hidden');
        unitInner.innerHTML =
          formatCents(variant.unit_price) + '<span aria-hidden="true"> / </span>' + formatUnitBase(variant);
      } else {
        unitRow.classList.add('hidden');
        unitInner.innerHTML = '';
      }
    }

    refreshHeroAria();
  });
})();
