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

  // Touch devices synthesize a mouseenter/mouseover immediately before the
  // click on a tap (the classic "hover element needs two taps" problem):
  // tap 1 fires mouseenter (opens it), then click fires in the same gesture
  // and sees isOpen() already true, so it immediately closes what it just
  // opened. Binding hover-to-open only where a real hover-capable pointer
  // (a mouse) is present avoids the race entirely; a single tap on a
  // touch/coarse pointer then hits only the click handler below, which
  // opens cleanly from a closed state.
  var canHover = window.matchMedia &&
    window.matchMedia("(hover: hover) and (pointer: fine)").matches;

  document.querySelectorAll("[data-rd-dropdown]").forEach(function (wrap) {
    var trigger = wrap.querySelector("[data-rd-trigger]");
    if (!trigger) return;

    if (canHover) {
      wrap.addEventListener("mouseenter", function () { open(wrap); });
      wrap.addEventListener("mouseleave", function () { close(wrap); });
    }

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
