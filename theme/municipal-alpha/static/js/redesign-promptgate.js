/* Build-vs-buy prompt gate. Posts to the same Google Form as the free-lead
   intake, tagged with a marker the Apps Script trigger (tools/apps-script/
   prompt-gate.gs) looks for, so one form serves both flows and an ordinary
   lead submission is untouched.

   Same tradeoff redesign-intake.js documents: the POST is no-cors, so the
   response is opaque and this page cannot confirm Google accepted it. A real
   end-to-end test submission is the only proof, not a runtime check. */
(function () {
  "use strict";

  var FORM_ACTION = "https://docs.google.com/forms/d/e/1FAIpQLSePu9lLZss_MnjySIns25FhIv6VAxaf-cgo1VopfYm-BoecOg/formResponse";
  var ENTRY = { name: "entry.834810311", email: "entry.742667339", notes: "entry.227212710" };
  var MARKER = "BUILD-VS-BUY PROMPT REQUEST";

  var form = document.getElementById("rd-gate-form");
  if (!form) return;
  var emailEl = document.getElementById("rd-gate-email");
  var nameEl = document.getElementById("rd-gate-name");
  var errorEl = document.getElementById("rd-gate-error");
  var successEl = document.getElementById("rd-gate-success");

  function looksLikeEmail(v) {
    return /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(v);
  }

  form.addEventListener("submit", function (e) {
    e.preventDefault();
    errorEl.hidden = true;
    var email = (emailEl.value || "").trim();
    if (!looksLikeEmail(email)) {
      emailEl.classList.add("rd-invalid");
      errorEl.textContent = "That does not look like an email address, so we would have nowhere to send it.";
      errorEl.hidden = false;
      emailEl.focus();
      return;
    }
    emailEl.classList.remove("rd-invalid");

    var params = new URLSearchParams();
    params.append(ENTRY.name, (nameEl && nameEl.value ? nameEl.value.trim() : ""));
    params.append(ENTRY.email, email);
    params.append(ENTRY.notes, MARKER);

    fetch(FORM_ACTION, { method: "POST", mode: "no-cors", body: params })
      .then(function () {
        form.style.display = "none";
        successEl.hidden = false;
      })
      .catch(function () {
        errorEl.textContent = "Something went wrong sending that. Email matt@municipalalpha.com and we will send the prompt straight over.";
        errorEl.hidden = false;
      });
  });
})();
