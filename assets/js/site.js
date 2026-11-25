/* ============================================================
   Farma Popular Ouro Preto — configuração e comportamento compartilhado
   ============================================================

   WhatsApp VALIDADO em 23/11/2026: o próprio perfil do Instagram da
   farmácia (farmapopular.ouropreto) aponta para https://wa.me/553135515271.
   O número é, portanto, o canal oficial de atendimento.

   Se a loja trocar de número, altere SOMENTE whatsappNumber abaixo.
   Todos os botões são reconstruídos por este arquivo.
================================================================ */
var SITE_CONFIG = {
  whatsappNumber: '553135515271', // confirmado via Instagram oficial da loja
  whatsappVerified: true,
  defaultMessage: 'Olá! Gostaria de informações sobre os produtos da Farma Popular Ouro Preto.'
};

/* Web Analytics da Vercel: fila de eventos exigida pelo script opcional.
   O script externo só é injetado depois do aceite de cookies (ver abaixo). */
window.va = window.va || function () {
  (window.vaq = window.vaq || []).push(arguments);
};

(function () {
  'use strict';

  function waLink(message) {
    var n = String(SITE_CONFIG.whatsappNumber || '').replace(/\D/g, '');
    var text = message || SITE_CONFIG.defaultMessage;
    return 'https://wa.me/' + n + '?text=' + encodeURIComponent(text);
  }

  function applyWhatsApp() {
    var links = document.querySelectorAll('a[data-wa]');
    for (var i = 0; i < links.length; i++) {
      var a = links[i];
      if (SITE_CONFIG.whatsappVerified) {
        a.href = waLink(a.getAttribute('data-wa-message'));
        a.setAttribute('target', '_blank');
        a.removeAttribute('data-wa-status');
        a.removeAttribute('title');
      } else {
        /* Número não validado: NÃO publicamos link wa.me.
           O botão leva ao aviso em contato.html até a confirmação pela loja. */
        a.href = '/pages/institucionais/contato.html#whatsapp';
        a.removeAttribute('target');
        a.setAttribute('data-wa-status', 'nao-validado');
        a.setAttribute('title', 'Número de WhatsApp em validação — confirme antes de publicar');
      }
    }
    if (!SITE_CONFIG.whatsappVerified && links.length && window.console) {
      console.warn('[Farma Popular] Número de WhatsApp ainda não validado. ' +
        'Nenhum link wa.me foi publicado. Confirme SITE_CONFIG.whatsappNumber e ' +
        'mude whatsappVerified para true em assets/js/site.js antes de publicar.');
    }
  }

  function initMenu() {
    var nav = document.getElementById('nav');
    var btn = document.getElementById('menuToggle');
    var menu = document.getElementById('menu');
    if (!nav || !btn || !menu) return;

    function close() {
      nav.classList.remove('open');
      btn.setAttribute('aria-expanded', 'false');
      btn.setAttribute('aria-label', 'Abrir menu');
    }
    btn.addEventListener('click', function (e) {
      e.stopPropagation();
      var open = nav.classList.toggle('open');
      btn.setAttribute('aria-expanded', String(open));
      btn.setAttribute('aria-label', open ? 'Fechar menu' : 'Abrir menu');
    });
    menu.addEventListener('click', function (e) { if (e.target.closest('a')) close(); });
    document.addEventListener('click', function (e) {
      if (nav.classList.contains('open') && !nav.contains(e.target)) close();
    });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') close(); });
    if (window.matchMedia) {
      var mq = window.matchMedia('(min-width: 821px)');
      if (mq.addEventListener) mq.addEventListener('change', close);
      else if (mq.addListener) mq.addListener(close);
    }
  }

  /* Busca: filtra os produtos ilustrativos da página de medicamentos. */
  function initSearch() {
    var form = document.getElementById('formBusca');
    if (!form) return;
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var input = document.getElementById('q');
      var q = input ? input.value.trim() : '';
      window.location.href = '/pages/medicamentos/medicamentos-e-genericos.html' + (q ? '?q=' + encodeURIComponent(q) : '');
    });
  }

  /* Mostra o termo pesquisado e filtra os cards [data-search] da página. */
  function normText(s) {
    return String(s).toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g, '');
  }

  function initProductFilter() {
    var params = new URLSearchParams(window.location.search);
    var q = (params.get('q') || '').trim();
    var term = document.getElementById('searchTerm');
    if (term && q) {
      term.textContent = 'Resultados para “' + q + '”';
      term.hidden = false;
    }
    if (!q) return;
    var norm = normText(q);
    var cards = document.querySelectorAll('[data-search]');
    var visible = 0;
    for (var i = 0; i < cards.length; i++) {
      var hit = normText(cards[i].getAttribute('data-search')).indexOf(norm) !== -1;
      cards[i].hidden = !hit;
      if (hit) visible++;
    }
    var empty = document.getElementById('emptySearch');
    if (empty) empty.hidden = visible !== 0;
  }

  /* ══ Consentimento de cookies ══
     O Web Analytics da Vercel é opcional: o script só é injetado depois que
     o visitante aceita. A escolha fica em localStorage (fp_cookie_consent).
     O caminho abaixo é o identificador do projeto na Vercel; não alterar
     sem antes atualizar também a Política de Cookies. */
  var COOKIE_KEY = 'fp_cookie_consent';
  var OPTIONAL_SCRIPTS = [
    { src: '/zVf1u7xaTaWT5wfefSPvghK2q/script.js', id: 'vercel-analytics' }
  ];

  function getConsent() {
    try { return window.localStorage.getItem(COOKIE_KEY); }
    catch (e) { return null; }
  }

  function setConsent(value) {
    try { window.localStorage.setItem(COOKIE_KEY, value); }
    catch (e) { /* armazenamento indisponível: apenas não persiste */ }
  }

  function loadOptionalScripts() {
    for (var i = 0; i < OPTIONAL_SCRIPTS.length; i++) {
      if (document.querySelector('script[data-optional="' + i + '"]')) continue;
      var s = document.createElement('script');
      s.src = OPTIONAL_SCRIPTS[i].src;
      s.async = true;
      s.setAttribute('data-optional', String(i));
      if (OPTIONAL_SCRIPTS[i].id) s.id = OPTIONAL_SCRIPTS[i].id;
      document.head.appendChild(s);
    }
  }

  function initCookies() {
    var banner = document.getElementById('cookieBanner');
    if (!banner) return;

    function hide() { banner.hidden = true; }
    function show() {
      banner.hidden = false;
      var first = banner.querySelector('[data-cookie-accept]');
      if (first) first.focus();
    }

    var accept = banner.querySelector('[data-cookie-accept]');
    var reject = banner.querySelector('[data-cookie-reject]');
    if (accept) accept.addEventListener('click', function () {
      setConsent('accepted');
      loadOptionalScripts();
      hide();
    });
    if (reject) reject.addEventListener('click', function () {
      setConsent('rejected');
      hide();
    });

    var openers = document.querySelectorAll('[data-cookie-open]');
    for (var i = 0; i < openers.length; i++) {
      openers[i].addEventListener('click', show);
    }

    var saved = getConsent();
    if (saved === 'accepted') loadOptionalScripts();
    if (!saved) show();

    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && !banner.hidden) hide();
    });
  }

  document.addEventListener('DOMContentLoaded', function () {
    applyWhatsApp();
    initMenu();
    initSearch();
    initProductFilter();
    initCookies();
  });
})();
