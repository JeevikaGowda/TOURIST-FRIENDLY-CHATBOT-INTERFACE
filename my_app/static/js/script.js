// script.js

document.addEventListener("DOMContentLoaded", function () {
  "use strict";

  const header = document.querySelector("[data-header]");
  const navbar = document.querySelector("[data-navbar]");
  const goTopBtn = document.querySelector("[data-go-top]");
  const overlay = document.querySelector("[data-overlay]");
  const navOpenBtn = document.querySelector("[data-nav-open-btn]");
  const navCloseBtn = document.querySelector("[data-nav-close-btn]");
  const navLinks = document.querySelectorAll("[data-nav-link]");

  const navElemArr = [navOpenBtn, navCloseBtn, overlay];

  const navToggleEvent = function (elem) {
    for (let i = 0; i < elem.length; i++) {
      elem[i].addEventListener("click", function () {
        navbar.classList.toggle("active");
        overlay.classList.toggle("active");
      });
    }
  };

  navToggleEvent(navElemArr);
  navToggleEvent(navLinks);

  window.addEventListener("scroll", function () {
    if (window.scrollY >= 200) {
      header.classList.add("active");
      goTopBtn.classList.add("active");
      navbar.classList.add("active");
    } else {
      header.classList.remove("active");
      goTopBtn.classList.remove("active");
      navbar.classList.remove("active");
    }
  });
});
