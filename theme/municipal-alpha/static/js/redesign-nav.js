(function () {
  "use strict";

  function closeAll(except) {
    document.querySelectorAll("[data-rd-dropdown]").forEach(function (wrap) {
      if (wrap === except) return;
      var panel = wrap.querySelector("[data-rd-panel]");
      var trigger = wrap.querySelector("[data-rd-trigger]");
      if (panel) panel.classList.remove("rd-open");
      if (trigger) trigger.setAttribute("aria-expanded", "false");
    });
  }

  function open(wrap) {
    closeAll(wrap);
    var panel = wrap.querySelector("[data-rd-panel]");
    var trigger = wrap.querySelector("[data-rd-trigger]");
    if (panel) panel.classList.add("rd-open");
    if (trigger) trigger.setAttribute("aria-expanded", "true");
  }

  function close(wrap) {
    var panel = wrap.querySelector("[data-rd-panel]");
    var trigger = wrap.querySelector("[data-rd-trigger]");
    if (panel) panel.classList.remove("rd-open");
    if (trigger) trigger.setAttribute("aria-expanded", "false");
  }

  function isOpen(wrap) {
    var panel = wrap.querySelector("[data-rd-panel]");
    return !!(panel && panel.classList.contains("rd-open"));
  }

  document.querySelectorAll("[data-rd-dropdown]").forEach(function (wrap) {
    var trigger = wrap.querySelector("[data-rd-trigger]");
    if (!trigger) return;

    wrap.addEventListener("mouseenter", function () { open(wrap); });
    wrap.addEventListener("mouseleave", function () { close(wrap); });

    trigger.addEventListener("click", function (e) {
      e.stopPropagation();
      if (isOpen(wrap)) {
        close(wrap);
      } else {
        open(wrap);
      }
    });
  });

  document.addEventListener("click", function () { closeAll(); });

  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape") closeAll();
  });
})();
