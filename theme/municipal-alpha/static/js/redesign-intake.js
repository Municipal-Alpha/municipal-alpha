(function () {
  "use strict";

  // Google Form entry IDs, confirmed 2026-08-31 via "Get pre-filled link"
  // against the real form (id 1FAIpQLSePu9lLZss_MnjySIns25FhIv6VAxaf-cgo1VopfYm-BoecOg).
  // This is an unofficial-but-standard technique: POSTing straight to a Google
  // Form's own response endpoint lets this page keep its fully custom design
  // instead of embedding Google's own form UI. Tradeoff, stated plainly: the
  // request is sent with `mode: "no-cors"`, so the response is opaque, this
  // page cannot actually confirm Google accepted the submission, only that
  // the request didn't fail at the network level. A one-time real test
  // submission (confirming a row lands in the linked Sheet) is the mitigation,
  // not a runtime check this code can perform.
  var FORM_ACTION = "https://docs.google.com/forms/d/e/1FAIpQLSePu9lLZss_MnjySIns25FhIv6VAxaf-cgo1VopfYm-BoecOg/formResponse";
  var ENTRY = {
    name: "entry.834810311",
    email: "entry.742667339",
    // The Google Form question behind this id is still titled "Company"; this
    // page now asks for the company website and posts the URL into it. Renaming
    // the question in the form does NOT change its entry id, so that rename is
    // safe to make independently of this file (asked of Christian 2026-09-01).
    website: "entry.652650228",
    buyerType: "entry.645215840",
    offer: "entry.1255949052",
    jurisdictions: "entry.1995577041",
    territory: "entry.482034844",
    signals: "entry.59812795",
    notes: "entry.227212710"
  };

  var form = document.getElementById("rd-intake-form");
  if (!form) return;

  var editingPanel = document.getElementById("rd-intake-editing");
  var successPanel = document.getElementById("rd-intake-success");
  var successLine = document.getElementById("rd-intake-success-line");
  var errorLine = document.getElementById("rd-intake-error");
  var resetBtn = document.getElementById("rd-intake-reset");

  var REQUIRED = [
    { key: "name", label: "name" },
    { key: "email", label: "a valid work email" },
    { key: "website", label: "a company website" },
    { key: "offer", label: "what you sell or are looking for" },
    { key: "territory", label: "territory or geography" }
  ];
  var EMAIL_RE = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  // Deliberately forgiving: no scheme required, no TLD allowlist. It only rules
  // out a plain company name ("Acme Inc"), which is the answer this field used
  // to ask for and the one people will keep typing out of habit.
  var WEBSITE_RE = /^(https?:\/\/)?[^\s\/?#.]+(\.[^\s\/?#.]+)+([\/?#]\S*)?$/i;

  function fieldEl(key) { return form.querySelector('[name="' + key + '"]'); }

  function clearInvalid() {
    form.querySelectorAll(".rd-invalid").forEach(function (el) { el.classList.remove("rd-invalid"); });
  }

  function validate() {
    var missing = [];
    REQUIRED.forEach(function (r) {
      var el = fieldEl(r.key);
      var val = (el.value || "").trim();
      if (r.key === "email") {
        if (!EMAIL_RE.test(val)) missing.push({ key: r.key, label: r.label, el: el });
      } else if (r.key === "website") {
        if (!WEBSITE_RE.test(val)) missing.push({ key: r.key, label: r.label, el: el });
      } else if (!val) {
        missing.push({ key: r.key, label: r.label, el: el });
      }
    });
    return missing;
  }

  form.querySelectorAll("input, textarea, select").forEach(function (el) {
    el.addEventListener("input", function () {
      el.classList.remove("rd-invalid");
      errorLine.textContent = "";
      errorLine.hidden = true;
    });
  });

  form.querySelectorAll(".rd-chip").forEach(function (chip) {
    chip.addEventListener("click", function () {
      var pressed = chip.getAttribute("aria-pressed") === "true";
      chip.setAttribute("aria-pressed", pressed ? "false" : "true");
    });
  });

  function checkedChipValues(group) {
    return Array.prototype.slice
      .call(form.querySelectorAll('.rd-chip[data-group="' + group + '"][aria-pressed="true"]'))
      .map(function (el) { return el.dataset.value; });
  }

  function buildPayload() {
    var params = new URLSearchParams();
    params.append(ENTRY.name, fieldEl("name").value.trim());
    params.append(ENTRY.email, fieldEl("email").value.trim());
    params.append(ENTRY.website, fieldEl("website").value.trim());
    params.append(ENTRY.buyerType, fieldEl("buyerType").value);
    params.append(ENTRY.offer, fieldEl("offer").value.trim());
    checkedChipValues("jurisdictions").forEach(function (v) { params.append(ENTRY.jurisdictions, v); });
    params.append(ENTRY.territory, fieldEl("territory").value.trim());
    checkedChipValues("signals").forEach(function (v) { params.append(ENTRY.signals, v); });
    params.append(ENTRY.notes, fieldEl("notes").value.trim());
    return params;
  }

  form.addEventListener("submit", function (e) {
    e.preventDefault();
    clearInvalid();
    var missing = validate();
    if (missing.length) {
      missing.forEach(function (m) { m.el.classList.add("rd-invalid"); });
      errorLine.textContent = "Still needed: " + missing.map(function (m) { return m.label; }).join(", ") + ".";
      errorLine.hidden = false;
      return;
    }

    var payload = buildPayload();
    fetch(FORM_ACTION, { method: "POST", mode: "no-cors", body: payload })
      .then(function () { showSuccess(); })
      .catch(function () {
        errorLine.textContent = "Something went wrong sending this, please try again, or email matt@municipalalpha.com directly.";
        errorLine.hidden = false;
      });
  });

  // Panels use inline `display` (not the `hidden` attribute/property) because
  // an inline `style="display:flex"` in the markup always outranks the
  // browser's `[hidden]{display:none}` UA rule, toggling `.hidden` alone
  // left both panels visible at once. See PR #11 notes.
  function showSuccess() {
    var first = fieldEl("name").value.trim().split(" ")[0];
    successLine.textContent = first ? "Thanks, " + first + ", we are on it." : "Thanks, we are on it.";
    editingPanel.style.display = "none";
    successPanel.style.display = "flex";
  }

  resetBtn.addEventListener("click", function () {
    form.reset();
    form.querySelectorAll('.rd-chip[aria-pressed="true"]').forEach(function (el) { el.setAttribute("aria-pressed", "false"); });
    errorLine.textContent = "";
    errorLine.hidden = true;
    successPanel.style.display = "none";
    editingPanel.style.display = "flex";
  });
})();
