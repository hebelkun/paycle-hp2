/* PAYCLE — shared interactions */
(function () {
  "use strict";

  /* ---- Mobile nav toggle ---- */
  var toggle = document.querySelector(".nav-toggle");
  var menu = document.querySelector(".nav-menu");
  if (toggle && menu) {
    toggle.addEventListener("click", function () {
      var open = menu.classList.toggle("open");
      toggle.classList.toggle("open", open);
      toggle.setAttribute("aria-expanded", String(open));
    });
    menu.querySelectorAll("a").forEach(function (a) {
      a.addEventListener("click", function () {
        menu.classList.remove("open");
        toggle.classList.remove("open");
        toggle.setAttribute("aria-expanded", "false");
      });
    });
  }

  /* ---- Reveal on scroll ---- */
  var reveals = document.querySelectorAll(".reveal");
  if (reveals.length && "IntersectionObserver" in window) {
    var io = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (e) {
          if (e.isIntersecting) {
            e.target.classList.add("in");
            io.unobserve(e.target);
          }
        });
      },
      { threshold: 0.12, rootMargin: "0px 0px -40px 0px" }
    );
    reveals.forEach(function (el) { io.observe(el); });
  } else {
    reveals.forEach(function (el) { el.classList.add("in"); });
  }

  /* ---- Card video: play on hover / focus, pause + reset on leave ---- */
  var mobileCards = window.matchMedia("(max-width: 980px), (pointer: coarse)");
  document.querySelectorAll(".feature-card .card-video").forEach(function (video) {
    var card = video.closest(".feature-card");
    if (!card) return;

    function play() {
      var p = video.play();
      if (p && p.catch) { p.catch(function () {}); } // ignore autoplay rejections
    }
    function stop() {
      video.pause();
      try { video.currentTime = 0; } catch (e) {}
    }

    card.addEventListener("mouseenter", play);
    card.addEventListener("mouseleave", stop);
    card.addEventListener("focus", play);
    card.addEventListener("blur", stop);
  });

  /* ---- Service videos: play when scrolled into view on mobile ---- */
  var serviceVideos = document.querySelectorAll(".cards-deal .card-video");
  if (serviceVideos.length && "IntersectionObserver" in window && mobileCards.matches) {
    var videoObserver = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          var video = entry.target.querySelector(".card-video");
          if (!video) return;

          if (entry.isIntersecting) {
            var p = video.play();
            if (p && p.catch) { p.catch(function () {}); }
          } else {
            video.pause();
            try { video.currentTime = 0; } catch (e) {}
          }
        });
      },
      { threshold: 0.45, rootMargin: "0px 0px -10% 0px" }
    );

    document.querySelectorAll(".cards-deal .feature-card").forEach(function (card) {
      videoObserver.observe(card);
    });
  }

  /* ---- Contact form (front-end demo) ---- */
  var form = document.querySelector("#contact-form");
  if (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var done = form.querySelector(".form-done");
      if (done) { done.hidden = false; }
      form.reset();
    });
  }
})();
