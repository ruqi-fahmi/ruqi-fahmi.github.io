/* Interaksi kecil untuk halaman profil.
   Tanpa pustaka luar. Semuanya opsional: kalau JavaScript mati,
   halaman tetap terbaca utuh karena isinya HTML statis. */

(function () {
  "use strict";

  var root = document.documentElement;
  var adaObserver = "IntersectionObserver" in window;

  /* ---------- tema terang / gelap ---------- */

  var KUNCI = "tema";
  var tombol = document.getElementById("theme");

  function pasangTema(nilai) {
    if (nilai) root.setAttribute("data-theme", nilai);
    else root.removeAttribute("data-theme");

    if (!tombol) return;
    var gelap = nilai === "dark" ||
      (!nilai && window.matchMedia("(prefers-color-scheme: dark)").matches);
    tombol.textContent = gelap ? "☀" : "☽";
    tombol.setAttribute("aria-label", gelap ? "Ganti ke tema terang" : "Ganti ke tema gelap");
  }

  try { pasangTema(localStorage.getItem(KUNCI)); } catch (e) { pasangTema(null); }

  if (tombol) {
    tombol.addEventListener("click", function () {
      var sekarang = root.getAttribute("data-theme");
      var sistemGelap = window.matchMedia("(prefers-color-scheme: dark)").matches;
      var berikut = sekarang
        ? (sekarang === "dark" ? "light" : "dark")
        : (sistemGelap ? "light" : "dark");
      pasangTema(berikut);
      try { localStorage.setItem(KUNCI, berikut); } catch (e) { /* mode privat */ }
    });
  }

  /* ---------- bilah atas menempel ---------- */

  var bar = document.querySelector(".topbar");
  if (bar && adaObserver) {
    var sentinel = document.createElement("div");
    sentinel.setAttribute("aria-hidden", "true");
    sentinel.style.cssText = "position:absolute;top:0;left:0;height:1px;width:1px";
    document.body.prepend(sentinel);

    new IntersectionObserver(function (entri) {
      bar.classList.toggle("stuck", !entri[0].isIntersecting);
    }).observe(sentinel);
  }

  /* ---------- tautan nav mengikuti seksi yang sedang dibaca ---------- */

  var tautan = Array.prototype.slice.call(document.querySelectorAll(".navlinks a"));
  var seksi = tautan
    .map(function (a) { return document.querySelector(a.getAttribute("href")); })
    .filter(Boolean);

  if (seksi.length && adaObserver) {
    var terlihat = Object.create(null);

    function perbarui() {
      var aktif = null;
      for (var i = 0; i < seksi.length; i++) {
        if (terlihat[seksi[i].id]) { aktif = seksi[i]; break; }
      }
      tautan.forEach(function (a) {
        var cocok = aktif && a.getAttribute("href") === "#" + aktif.id;
        a.setAttribute("aria-current", cocok ? "true" : "false");
      });
    }

    var pengamatNav = new IntersectionObserver(function (entri) {
      entri.forEach(function (e) { terlihat[e.target.id] = e.isIntersecting; });
      perbarui();
    }, { rootMargin: "-76px 0px -70% 0px" });

    seksi.forEach(function (s) { pengamatNav.observe(s); });
  }

  /* ---------- munculkan seksi saat digulir ---------- */

  var kurangiGerak = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  if (!kurangiGerak && adaObserver) {
    var pengamatMuncul = new IntersectionObserver(function (entri, diri) {
      entri.forEach(function (e) {
        if (!e.isIntersecting) return;
        e.target.classList.add("shown");
        diri.unobserve(e.target);
      });
    }, { rootMargin: "0px 0px -8% 0px" });

    document.querySelectorAll("section").forEach(function (s) {
      s.classList.add("reveal");
      pengamatMuncul.observe(s);
    });
  }
})();
