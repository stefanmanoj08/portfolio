/**
 * Soft password gate for project pages.
 * Note: client-side only — keeps casual visitors out, not cryptographic security.
 */
(function () {
  var PASS = "stefan08";
  var KEY = "stefan_projects_unlocked";

  function isUnlocked() {
    try {
      return sessionStorage.getItem(KEY) === "1";
    } catch (e) {
      return false;
    }
  }

  function setUnlocked() {
    try {
      sessionStorage.setItem(KEY, "1");
    } catch (e) {}
  }

  // Only individual case pages (projects/*.html) — not the projects list
  function pathLooksProtected(pathname) {
    var p = (pathname || "").replace(/\\/g, "/");
    return /\/projects\/[^/]+\.html$/i.test(p);
  }

  function hrefIsProtected(href) {
    if (!href || href.charAt(0) === "#") return false;
    try {
      var u = new URL(href, window.location.href);
      return pathLooksProtected(u.pathname);
    } catch (e) {
      return /\/projects\/[^/?#]+\.html/i.test(href);
    }
  }

  function isProtectedPage() {
    return pathLooksProtected(window.location.pathname) ||
      /\/projects\/[^/?#]+\.html/i.test(window.location.href);
  }

  function ensureStyles() {
    if (document.getElementById("project-lock-styles")) return;
    var s = document.createElement("style");
    s.id = "project-lock-styles";
    s.textContent = [
      "html.projects-gate-pending body > *:not(#project-lock-root){visibility:hidden !important;}",
      "#project-lock-root{position:fixed;inset:0;z-index:99999;display:flex;align-items:center;justify-content:center;",
      "padding:24px;background:rgba(250,249,252,0.72);backdrop-filter:blur(10px);-webkit-backdrop-filter:blur(10px);",
      "font-family:Manrope,system-ui,sans-serif;}",
      "#project-lock-root[hidden]{display:none !important;}",
      ".pl-card{width:min(400px,100%);background:#faf9fc;border:1px solid rgba(26,26,26,0.08);",
      "border-radius:24px;padding:32px 28px 28px;box-shadow:0 24px 50px rgba(26,26,26,0.12);",
      "background-image:radial-gradient(ellipse 80% 60% at 10% 0%,rgba(167,139,250,0.28),transparent 55%),",
      "radial-gradient(ellipse 70% 50% at 100% 100%,rgba(66,98,255,0.14),transparent 50%);}",
      ".pl-kicker{font-size:11px;font-weight:700;letter-spacing:0.14em;text-transform:uppercase;color:#4262ff;margin:0 0 10px;}",
      ".pl-title{font-family:Syne,Manrope,sans-serif;font-size:26px;font-weight:800;letter-spacing:-0.03em;",
      "color:#1a1a1a;margin:0 0 8px;line-height:1.15;}",
      ".pl-copy{font-size:14px;color:#5c5c5c;line-height:1.5;margin:0 0 22px;}",
      ".pl-form{display:flex;flex-direction:column;gap:12px;}",
      ".pl-input{appearance:none;width:100%;border:1px solid rgba(26,26,26,0.12);border-radius:999px;",
      "padding:14px 18px;font:inherit;font-size:15px;background:#fff;color:#1a1a1a;outline:none;}",
      ".pl-input:focus{border-color:#4262ff;box-shadow:0 0 0 3px rgba(66,98,255,0.18);}",
      ".pl-actions{display:flex;gap:10px;flex-wrap:wrap;}",
      ".pl-btn{appearance:none;border:0;border-radius:999px;padding:14px 22px;font:inherit;font-size:13px;",
      "font-weight:700;letter-spacing:0.06em;text-transform:uppercase;cursor:pointer;}",
      ".pl-btn-primary{background:#1a1a1a;color:#fff;}",
      ".pl-btn-primary:hover{background:#2a2a2a;}",
      ".pl-btn-ghost{background:transparent;color:#5c5c5c;}",
      ".pl-btn-ghost:hover{color:#1a1a1a;}",
      ".pl-error{min-height:18px;font-size:13px;font-weight:600;color:#c0265e;margin:0;}"
    ].join("");
    document.head.appendChild(s);
  }

  var pendingHref = null;
  var root = null;
  var input = null;
  var errorEl = null;

  function closeModal() {
    if (!root) return;
    root.hidden = true;
    pendingHref = null;
    document.documentElement.classList.remove("projects-gate-pending");
    if (input) input.value = "";
    if (errorEl) errorEl.textContent = "";
  }

  function openModal(href) {
    ensureStyles();
    ensureModal();
    pendingHref = href || null;
    root.hidden = false;
    if (errorEl) errorEl.textContent = "";
    if (input) {
      input.value = "";
      setTimeout(function () { input.focus(); }, 30);
    }
  }

  function succeed() {
    setUnlocked();
    var go = pendingHref;
    closeModal();
    if (go) {
      window.location.href = go;
      return;
    }
    document.documentElement.classList.remove("projects-gate-pending");
  }

  function submit() {
    var value = (input && input.value ? input.value : "").trim();
    if (value === PASS) {
      succeed();
      return;
    }
    if (errorEl) errorEl.textContent = "Wrong password — try again.";
    if (input) {
      input.select();
      input.focus();
    }
  }

  function ensureModal() {
    if (root) return;
    root = document.createElement("div");
    root.id = "project-lock-root";
    root.hidden = true;
    root.setAttribute("role", "dialog");
    root.setAttribute("aria-modal", "true");
    root.setAttribute("aria-labelledby", "pl-title");
    root.innerHTML =
      '<div class="pl-card">' +
        '<p class="pl-kicker">Projects</p>' +
        '<h2 class="pl-title" id="pl-title">Password required</h2>' +
        '<p class="pl-copy">These case studies are locked. Enter the password to continue.</p>' +
        '<form class="pl-form" id="pl-form">' +
          '<input class="pl-input" id="pl-input" type="password" name="password" autocomplete="current-password" placeholder="Password" aria-label="Password" />' +
          '<p class="pl-error" id="pl-error" aria-live="polite"></p>' +
          '<div class="pl-actions">' +
            '<button type="submit" class="pl-btn pl-btn-primary">Unlock</button>' +
            '<button type="button" class="pl-btn pl-btn-ghost" id="pl-cancel">Cancel</button>' +
          "</div>" +
        "</form>" +
      "</div>";
    document.body.appendChild(root);
    input = root.querySelector("#pl-input");
    errorEl = root.querySelector("#pl-error");
    root.querySelector("#pl-form").addEventListener("submit", function (e) {
      e.preventDefault();
      submit();
    });
    root.querySelector("#pl-cancel").addEventListener("click", function () {
      if (isProtectedPage() && !isUnlocked()) {
        window.location.href = root.dataset.home || "../index.html";
        return;
      }
      closeModal();
    });
    root.addEventListener("click", function (e) {
      if (e.target === root && !(isProtectedPage() && !isUnlocked())) closeModal();
    });
  }

  function homeHref() {
    if (/\/projects\//i.test(window.location.pathname) || /\/projects\//i.test(window.location.href)) {
      return "../index.html";
    }
    return "index.html";
  }

  function interceptClicks() {
    document.addEventListener(
      "click",
      function (e) {
        if (isUnlocked()) return;
        var a = e.target.closest && e.target.closest("a[href]");
        if (!a) return;
        if (!hrefIsProtected(a.getAttribute("href"))) return;
        e.preventDefault();
        openModal(a.href);
      },
      true
    );
  }

  function gateThisPage() {
    if (!isProtectedPage()) return;
    if (isUnlocked()) return;
    ensureStyles();
    document.documentElement.classList.add("projects-gate-pending");
    function show() {
      ensureModal();
      root.dataset.home = homeHref();
      openModal(null);
    }
    if (document.body) show();
    else document.addEventListener("DOMContentLoaded", show);
  }

  interceptClicks();
  gateThisPage();
})();
