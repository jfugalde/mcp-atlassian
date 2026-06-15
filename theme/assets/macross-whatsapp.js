/**
 * Macross native WhatsApp: hostname routing, cookie-gated geo, wa.me prefill, branch picker.
 */
(function () {
  var STORAGE_CONSENT = 'macross_tracking_consent';
  var STORAGE_BRANCH = 'macross_wa_branch';
  var CACHE_MS = 30 * 60 * 1000;
  var GEO_TIMEOUT_MS = 8000;
  var HOST_BRANCH_KEYS = ['cdmx', 'puebla', 'guadalajara'];
  var MENU_CLOSE_MS = 300;

  var JALISCO_CITY_HINTS = [
    'guadalajara',
    'zapopan',
    'tlaquepaque',
    'tonala',
    'tlajomulco',
    'santa rita',
  ];

  var config = null;
  var branches = [];
  var modalEl = null;
  var resolveInFlight = null;
  var activeMessage = '';

  function readConfig() {
    if (config) return config;
    var el = document.getElementById('macross-whatsapp-config');
    if (!el) return null;
    try {
      config = JSON.parse(el.textContent);
      branches = (config && config.branches) || [];
      return config;
    } catch (e) {
      return null;
    }
  }

  function normalizeText(value) {
    return String(value || '')
      .toLowerCase()
      .normalize('NFD')
      .replace(/[\u0300-\u036f]/g, '');
  }

  function branchByKey(key) {
    for (var i = 0; i < branches.length; i++) {
      if (branches[i].key === key) return branches[i];
    }
    return null;
  }

  function branchKeyFromDevQuery() {
    try {
      var params = new URLSearchParams(window.location.search);
      var q = normalizeText(params.get('macross_branch'));
      if (q && branchByKey(q)) return q;
    } catch (e) {}
    return null;
  }

  function branchKeyFromHostname() {
    var host = normalizeText(window.location.hostname);
    for (var i = 0; i < HOST_BRANCH_KEYS.length; i++) {
      var key = HOST_BRANCH_KEYS[i];
      if (host === key + '.farmaciasmacross.com.mx' || host.indexOf(key + '.') === 0) {
        return key;
      }
    }
    return null;
  }

  function getActiveBranchKey() {
    var cached = readCachedBranch();
    if (cached && cached.branchKey) return cached.branchKey;
    return branchKeyFromDevQuery() || branchKeyFromHostname();
  }

  function resolveBranchFromHostname() {
    var key = branchKeyFromDevQuery() || branchKeyFromHostname();
    if (!key) return null;
    var branch = branchByKey(key);
    if (!branch) return null;
    return { branch: branch, confidence: 'high', source: 'hostname' };
  }

  function isHostnameRouted() {
    return resolveBranchFromHostname() !== null;
  }

  function hasTrackingConsent() {
    try {
      if (localStorage.getItem(STORAGE_CONSENT) === '1') return true;
      if (
        window.Shopify &&
        window.Shopify.customerPrivacy &&
        typeof window.Shopify.customerPrivacy.analyticsProcessingAllowed === 'function'
      ) {
        return window.Shopify.customerPrivacy.analyticsProcessingAllowed();
      }
    } catch (e) {}
    return false;
  }

  function readCachedBranch() {
    try {
      var raw = sessionStorage.getItem(STORAGE_BRANCH);
      if (!raw) return null;
      var parsed = JSON.parse(raw);
      if (!parsed || !parsed.branchKey || !parsed.number || !parsed.ts) return null;
      if (parsed.source !== 'hostname' && Date.now() - parsed.ts > CACHE_MS) return null;
      return parsed;
    } catch (e) {
      return null;
    }
  }

  function writeCachedBranch(payload) {
    try {
      payload.ts = Date.now();
      sessionStorage.setItem(STORAGE_BRANCH, JSON.stringify(payload));
    } catch (e) {}
  }

  function haversineKm(lat1, lng1, lat2, lng2) {
    var toRad = function (deg) {
      return (deg * Math.PI) / 180;
    };
    var dLat = toRad(lat2 - lat1);
    var dLng = toRad(lng2 - lng1);
    var a =
      Math.sin(dLat / 2) * Math.sin(dLat / 2) +
      Math.cos(toRad(lat1)) * Math.cos(toRad(lat2)) * Math.sin(dLng / 2) * Math.sin(dLng / 2);
    return 6371 * (2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a)));
  }

  function nearestBranchByCoords(lat, lng) {
    var nearest = branches[0];
    var minKm = Infinity;
    branches.forEach(function (branch) {
      var km = haversineKm(lat, lng, branch.lat, branch.lng);
      if (km < minKm) {
        minKm = km;
        nearest = branch;
      }
    });
    return { branch: nearest, distanceKm: minKm };
  }

  function resolveBranchFromIp(data) {
    var country = normalizeText(data.country_code);
    var region = normalizeText(data.region);
    var city = normalizeText(data.city);

    if (country && country !== 'mx') {
      return { branch: branchByKey('cdmx'), confidence: 'low', source: 'ip' };
    }

    if (region.indexOf('puebla') !== -1 || city.indexOf('puebla') !== -1) {
      return { branch: branchByKey('puebla'), confidence: 'high', source: 'ip' };
    }

    if (
      region.indexOf('jalisco') !== -1 ||
      data.region_code === 'JAL'
    ) {
      for (var j = 0; j < JALISCO_CITY_HINTS.length; j++) {
        if (city.indexOf(normalizeText(JALISCO_CITY_HINTS[j])) !== -1) {
          return { branch: branchByKey('guadalajara'), confidence: 'high', source: 'ip' };
        }
      }
      return { branch: branchByKey('guadalajara'), confidence: 'medium', source: 'ip' };
    }

    if (
      region.indexOf('mexico city') !== -1 ||
      region.indexOf('ciudad de mexico') !== -1 ||
      city.indexOf('mexico city') !== -1 ||
      city.indexOf('ciudad de mexico') !== -1 ||
      data.region_code === 'DF'
    ) {
      return { branch: branchByKey('cdmx'), confidence: 'high', source: 'ip' };
    }

    var isEdomex =
      region.indexOf('mexico') !== -1 ||
      region.indexOf('estado de mexico') !== -1 ||
      data.region_code === 'MEX';

    if (isEdomex) {
      return { branch: branchByKey('cdmx'), confidence: 'medium', source: 'ip' };
    }

    return { branch: branchByKey('cdmx'), confidence: 'low', source: 'ip' };
  }

  function fetchIpGeo() {
    return fetch('https://ipapi.co/json/', { credentials: 'omit' })
      .then(function (res) {
        if (!res.ok) throw new Error('ip geo failed');
        return res.json();
      })
      .then(function (data) {
        return resolveBranchFromIp(data);
      });
  }

  function fetchBrowserGeo() {
    return new Promise(function (resolve, reject) {
      if (!navigator.geolocation) {
        reject(new Error('geolocation unavailable'));
        return;
      }
      navigator.geolocation.getCurrentPosition(
        function (pos) {
          resolve(pos.coords);
        },
        function (err) {
          reject(err);
        },
        { enableHighAccuracy: false, timeout: GEO_TIMEOUT_MS, maximumAge: CACHE_MS }
      );
    });
  }

  function buildPayload(result) {
    return {
      branchKey: result.branch.key,
      number: result.branch.number,
      confidence: result.confidence,
      source: result.source,
    };
  }

  function resolveBranch(options) {
    var skipBrowserGeo = options && options.skipBrowserGeo;
    var hostResult = resolveBranchFromHostname();
    if (hostResult) {
      var hostPayload = buildPayload(hostResult);
      writeCachedBranch(hostPayload);
      return Promise.resolve(hostPayload);
    }

    if (!hasTrackingConsent()) return Promise.resolve(null);
    if (resolveInFlight) return resolveInFlight;

    resolveInFlight = fetchIpGeo()
      .then(function (ipResult) {
        if (skipBrowserGeo) return ipResult;
        return fetchBrowserGeo()
          .then(function (coords) {
            var nearest = nearestBranchByCoords(coords.latitude, coords.longitude);
            if (nearest.distanceKm <= 120) {
              return {
                branch: nearest.branch,
                confidence: 'high',
                source: 'geolocation',
              };
            }
            return ipResult;
          })
          .catch(function () {
            return ipResult;
          });
      })
      .then(function (result) {
        if (!result || !result.branch) return null;
        var payload = buildPayload(result);
        writeCachedBranch(payload);
        return payload;
      })
      .catch(function () {
        return null;
      })
      .finally(function () {
        resolveInFlight = null;
      });

    return resolveInFlight;
  }

  function waDigits(number) {
    return String(number || '').replace(/\D/g, '');
  }

  function buildMessage(context) {
    var cfg = readConfig();
    if (!cfg || !cfg.messages) return '';
    var isProduct =
      context === 'product' && cfg.product && cfg.product.title && cfg.product.url;
    var template = isProduct ? cfg.messages.product : cfg.messages.general;
    if (isProduct) {
      return template
        .replace(/\{\{\s*product\s*\}\}/g, cfg.product.title)
        .replace(/\{\{\s*url\s*\}\}/g, cfg.product.url);
    }
    return template;
  }

  function launcherContext(trigger) {
    if (!trigger) return 'general';
    var explicit = trigger.getAttribute('data-macross-whatsapp-context');
    if (explicit) return explicit;
    if (trigger.closest('.sticky-atc__whatsapp, [data-macross-whatsapp-context="product"]')) {
      return 'product';
    }
    return 'general';
  }

  function openDirectWhatsApp(number, message) {
    var url = 'https://wa.me/' + waDigits(number);
    if (message) url += '?text=' + encodeURIComponent(message);
    window.open(url, '_blank', 'noopener,noreferrer');
  }

  function getModal() {
    if (modalEl) return modalEl;
    modalEl = document.getElementById('macross-wa-modal');
    return modalEl;
  }

  function closeBranchPicker() {
    var modal = getModal();
    if (!modal) return;
    modal.hidden = true;
    document.documentElement.classList.remove('macross-wa-modal-open');
  }

  function openBranchPicker(recommendedKey, showBadge) {
    var modal = getModal();
    if (!modal) return;

    var cfg = readConfig();
    var badgeText = (cfg && cfg.messages && cfg.messages.recommendedBadge) || 'Sucursal recomendada';
    var list = modal.querySelector('[data-macross-wa-branch-list]');
    if (!list) return;

    var buttons = list.querySelectorAll('[data-macross-wa-branch]');
    buttons.forEach(function (btn) {
      btn.classList.remove('macross-wa--recommended');
      var existing = btn.querySelector('.macross-wa__recommended-badge');
      if (existing) existing.remove();
    });

    if (recommendedKey) {
      var recommendedBtn = list.querySelector('[data-macross-wa-branch="' + recommendedKey + '"]');
      if (recommendedBtn && recommendedBtn.parentElement) {
        list.insertBefore(recommendedBtn.parentElement, list.firstChild);
      }
      if (showBadge && recommendedBtn) {
        recommendedBtn.classList.add('macross-wa--recommended');
        var nameEl = recommendedBtn.querySelector('.macross-wa-modal__branch-name');
        if (nameEl) {
          var badge = document.createElement('span');
          badge.className = 'macross-wa__recommended-badge';
          badge.textContent = badgeText;
          nameEl.appendChild(badge);
        }
      }
    }

    modal.hidden = false;
    document.documentElement.classList.add('macross-wa-modal-open');
    var firstBtn = modal.querySelector('[data-macross-wa-branch]');
    if (firstBtn) firstBtn.focus();
  }

  function openBranchByKey(key) {
    var branch = branchByKey(key);
    if (!branch) return;
    closeBranchPicker();
    openDirectWhatsApp(branch.number, activeMessage);
  }

  function closeMobileMenu() {
    var menuWrapper = document.querySelector('.sf-menu-wrapper-mobile');
    if (!menuWrapper || menuWrapper.classList.contains('hidden')) return;

    var menu = menuWrapper.querySelector('.sf-menu-content');
    menuWrapper.style.setProperty('--tw-bg-opacity', '0');
    if (menuWrapper.firstElementChild) {
      menuWrapper.firstElementChild.classList.add('-translate-x-full');
    }

    window.setTimeout(function () {
      menuWrapper.classList.add('hidden');
      document.documentElement.classList.remove('prevent-scroll');
      if (menu) {
        menu.classList.remove('sf-sub-menu-open', 'open-level-1', 'open-level-2');
      }
    }, MENU_CLOSE_MS);
  }

  function openFromLauncher(trigger) {
    readConfig();
    var context = launcherContext(trigger);
    activeMessage = buildMessage(context);

    if (trigger && trigger.closest('.sf-menu-mobile-whatsapp')) {
      closeMobileMenu();
    }

    var cached = readCachedBranch();

    if (cached && cached.source === 'hostname') {
      openDirectWhatsApp(cached.number, activeMessage);
      return;
    }

    if (!hasTrackingConsent()) {
      openBranchPicker(null, false);
      return;
    }

    if (!cached) {
      resolveBranch({ skipBrowserGeo: false }).then(function (resolved) {
        if (resolved && resolved.confidence === 'high') {
          openDirectWhatsApp(resolved.number, activeMessage);
          return;
        }
        openBranchPicker(
          resolved ? resolved.branchKey : null,
          resolved && resolved.confidence === 'medium'
        );
      });
      return;
    }

    if (cached.confidence === 'high') {
      openDirectWhatsApp(cached.number, activeMessage);
      return;
    }

    openBranchPicker(cached.branchKey, cached.confidence === 'medium');
  }

  function applyHostnameBranch() {
    var hostResult = resolveBranchFromHostname();
    if (!hostResult) return;
    writeCachedBranch(buildPayload(hostResult));
  }

  function scheduleBackgroundResolve() {
    var run = function () {
      resolveBranch({ skipBrowserGeo: true });
    };
    if ('requestIdleCallback' in window) {
      requestIdleCallback(run, { timeout: 8000 });
    } else {
      window.setTimeout(run, 3000);
    }
  }

  function onConsentGranted() {
    if (isHostnameRouted()) return;
    scheduleBackgroundResolve();
  }

  function attachModalListeners() {
    var modal = getModal();
    if (!modal) return;

    modal.addEventListener('click', function (e) {
      var closeBtn = e.target.closest('[data-macross-wa-close]');
      if (closeBtn) {
        e.preventDefault();
        closeBranchPicker();
        return;
      }

      var branchBtn = e.target.closest('[data-macross-wa-branch]');
      if (branchBtn) {
        e.preventDefault();
        openBranchByKey(branchBtn.getAttribute('data-macross-wa-branch'));
      }
    });

    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && modal && !modal.hidden) {
        closeBranchPicker();
      }
    });
  }

  function attachLauncherListener() {
    document.addEventListener(
      'click',
      function (e) {
        var trigger =
          e.target && e.target.closest && e.target.closest('[data-macross-whatsapp-launcher]');
        if (!trigger) return;
        e.preventDefault();
        openFromLauncher(trigger);
      },
      true
    );
  }

  function init() {
    readConfig();
    applyHostnameBranch();
    attachModalListeners();
    attachLauncherListener();

    if (hasTrackingConsent() && !isHostnameRouted() && !readCachedBranch()) {
      scheduleBackgroundResolve();
    }

    window.addEventListener('macross:cookie-accept', onConsentGranted);
  }

  var api = {
    hasTrackingConsent: hasTrackingConsent,
    getActiveBranchKey: getActiveBranchKey,
    resolveBranch: resolveBranch,
    openFromLauncher: openFromLauncher,
    openBranchPicker: openBranchPicker,
    openDirectWhatsApp: openDirectWhatsApp,
  };

  window.MacrossWhatsApp = api;
  window.MacrossWhatsAppGeo = api;

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
