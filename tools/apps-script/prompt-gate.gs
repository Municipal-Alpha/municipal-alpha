/**
 * Municipal Alpha — build-vs-buy prompt gate.
 *
 * Installed as an on-form-submit trigger on the lead Google Form
 * (1FAIpQLSePu9lLZss_MnjySIns25FhIv6VAxaf-cgo1VopfYm-BoecOg).
 *
 * Only fires for submissions carrying the marker below, which the gate form on
 * /build-vs-buy/ puts in the notes field. Ordinary free-lead submissions from
 * /free-lead-intake/ do not carry it and are left completely alone, so one form
 * serves both flows and no existing behaviour changes.
 *
 * INSTALL: CHRISTIAN, not Matt. He owns the Form, so he owns this bound
 * script project, and a trigger runs as whoever creates it. Installed by
 * anyone else it either will not save or will send from the wrong mailbox.
 * One time, ~2 minutes:
 *   1. Open the Form, three-dot menu, Apps Script.
 *   2. Paste this file in, save.
 *   3. Triggers (clock icon), Add Trigger:
 *        function: onPromptRequest
 *        event source: From form
 *        event type: On form submit
 *   4. Authorise when prompted (it needs permission to send mail as you).
 *      If the trigger does not appear afterwards, the consent window was
 *      dismissed or popup-blocked: run onPromptRequest once from the editor
 *      to force the prompt, then add the trigger. It fails on the missing
 *      event object, which is expected and harmless.
 *   5. Test: submit the gate form on the page with your own address and confirm
 *      the prompt arrives. Per redesign-intake.js's own note, our POST is
 *      no-cors and opaque, so a real end-to-end test is the only proof it works.
 *
 * NOTE ON REQUIRED QUESTIONS: the gate posts only name, email and notes. If any
 * other question on the Form is marked Required, Google will reject the
 * submission and nothing will arrive. Set the others optional, or this flow
 * silently does nothing, which is exactly the failure shape worth avoiding.
 */

var MARKER = 'BUILD-VS-BUY PROMPT REQUEST';

var PROMPT_TEXT = `I am evaluating a vendor, Municipal Alpha, that reads precursor signals out of
municipalities' own meeting minutes, agendas, and spending records: the zoning change,
the draft moratorium, the budget line, the vendor payment, months before the decision
is on record. Before I pay for it, I want to decide honestly whether I can produce
this myself. An example of their published output:
https://municipalalpha.com/research/amherst-tower/

Act as my analyst and evaluate BUILD vs BUY for my WHOLE exposed footprint, not a
sample. [Describe your business and where municipal decisions touch it, e.g. "I
develop solar projects across six states" or "my revenue depends on local government
activity in 900 towns."] Evaluate the real thing: continuous, low-miss coverage across
my whole footprint, refreshed weekly, early enough to catch a change while it is still
an agenda item, not a one-time look at a few towns.

Rules, so this is honest and not a demo:
- You do NOT have the vendor's method, town list, or sources. Use only public web
  tools and your own knowledge, which is exactly the position I'd be in building it.
- VERIFIABLE HANDS-ON ONLY. If you try specific towns, paste the exact source URL you
  fetched and one verbatim quoted sentence with its location. If you cannot actually
  open a document, write "UNVERIFIED, could not fetch" and do not describe its
  contents from memory. Facts you know from training do not count as "found it."
- LABEL EVERY NUMBER inline: [FETCHED] (from a source you opened), [DERIVED]
  (computed from numbers you fetched), or [PRIOR] (training knowledge or assumption).
  For the three numbers your recommendation depends on most, state what would prove
  each one wrong and how I could check it myself in 15 minutes.

Do this:
1. Reverse-engineer their pipeline end to end.
2. Try it hands-on on 3-4 towns (verifiable, per the rule above). Report what you
   found, what you couldn't, and how long each took.
3. Scope the REAL build: continuous, low-miss coverage across thousands of
   heterogeneous town sites, weekly, with OCR on scanned PDFs and ongoing breakage
   maintenance. Derive the cost and timeline FROM your hands-on attempt (how many site
   platforms you hit, what fraction were scanned image PDFs, how many towns you failed
   on), as a range, not a point estimate.
4. Separate what is cheap to DIY from what is hard or infeasible (the historical
   corpus, the registry of where each town publishes, recall-at-scale, continuous ops).
5. PROMPT AUDIT: the vendor wrote this prompt. Assume it is engineered to make BUY
   look good. Identify every way the framing, rules, or scope tilt the conclusion in
   the vendor's favor, rewrite the prompt to remove that tilt, and say whether your
   recommendation changes under your neutral version.
6. SELF-AUDIT: list every claim you verified from a fetched source vs. inferred from
   prior knowledge, and the three assumptions most likely to make your recommendation
   wrong.
7. STEELMAN the case for building it ourselves, then give a clear BUILD vs BUY
   recommendation with a rough cost/time comparison and what I should make the vendor
   prove on a pilot before committing.

Output as a build-vs-buy memo. Be skeptical of the vendor AND honest about the real
cost of doing it ourselves.`;

function onPromptRequest(e) {
  try {
    var answers = {};
    var items = e.response.getItemResponses();
    for (var i = 0; i < items.length; i++) {
      answers[items[i].getItem().getTitle()] = items[i].getResponse();
    }

    var blob = JSON.stringify(answers);
    if (blob.indexOf(MARKER) === -1) return;  // an ordinary lead, not a prompt request

    var email = e.response.getRespondentEmail();
    if (!email) {
      for (var key in answers) {
        var v = answers[key];
        if (typeof v === 'string' && v.indexOf('@') > -1 && v.indexOf(' ') === -1) { email = v; break; }
      }
    }
    if (!email) {
      MailApp.sendEmail('matt@municipalalpha.com',
        'Prompt request with no usable address',
        'A build-vs-buy prompt request came in but no email address could be read from it.\n\n' + blob);
      return;
    }

    var name = '';
    for (var k in answers) {
      if (k.toLowerCase().indexOf('name') > -1 && answers[k]) { name = String(answers[k]).trim(); break; }
    }
    var greeting = name ? ('Hi ' + name.split(' ')[0] + ',') : 'Hi,';

    var body = greeting + '\n\n'
      + 'Here is the build-vs-buy evaluation prompt, as promised.\n\n'
      + 'Replace the bracketed line with your own exposure, then paste the whole thing into\n'
      + 'whatever your team uses. Run it across your whole footprint rather than a couple of\n'
      + 'towns, because the answer genuinely depends on scale: if your exposure is a few dozen\n'
      + 'towns you already know by name, a scripted watch of your own is a reasonable build and\n'
      + 'the prompt should tell you so.\n\n'
      + 'Keep the audit steps in. Step 5 asks your AI to find how we tilted the prompt in our\n'
      + 'own favour and rewrite it neutrally. Run that version instead if you prefer it.\n\n'
      + '--- THE PROMPT ---\n\n'
      + PROMPT_TEXT + '\n\n'
      + '--- END ---\n\n'
      + 'When you have a result, send it over and we will return a per-jurisdiction coverage\n'
      + 'manifest next to what your build would cost, including the towns the model tested.\n\n'
      + 'Christian Milz\n'
      + 'Municipal Alpha\n'
      + 'christian@municipalalpha.com\n';

    MailApp.sendEmail({
      to: email,
      subject: 'The build-vs-buy evaluation prompt',
      body: body,
      name: 'Christian Milz'
    });

    MailApp.sendEmail('matt@municipalalpha.com,christian@municipalalpha.com',
      'Prompt sent: ' + email,
      'The build-vs-buy prompt was sent to ' + email + '.\n\nSubmission:\n' + blob);

  } catch (err) {
    MailApp.sendEmail('matt@municipalalpha.com,christian@municipalalpha.com',
      'Prompt gate FAILED',
      'onPromptRequest threw: ' + err + '\n\nNobody received the prompt. Check the trigger.');
  }
}
