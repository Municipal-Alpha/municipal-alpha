Title: Build vs Buy: Evaluate Us Yourself
Slug: build-vs-buy
Sortorder: 90

## Before you pay us a dollar, try to build this yourself.

We mean it. The question every serious buyer asks, out loud or quietly in a budget meeting, is "can't we just do this with AI?" It deserves a real answer, not a sales answer.

So here is the evaluation prompt we hand prospective buyers. Paste it into Claude, Gemini, ChatGPT, whatever your team uses. Run it against your whole exposed footprint, not a sample of two towns. Refine it however you want. Then put what you get next to what we deliver every week, and decide. We would rather you buy this knowing exactly what it is worth.

One honest note on scope before you start. The answer depends on your footprint. If your exposure is a few dozen towns you already know by name, a scripted watch of your own is a reasonable build and we will tell you so. The economics flip when the footprint is broad, hundreds or thousands of jurisdictions, refreshed weekly, with misses that cost you money.

## The prompt

Replace the bracketed line with your own exposure, then run it.

```
I am evaluating a vendor, Municipal Alpha, that reads precursor signals out of
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
cost of doing it ourselves.
```

## How to read what comes back

**Whatever the model flags as hard is the real product.** In our own runs of this prompt (July 2026), two frontier models independently recommended buy and converged on the same hard parts, the registry of where each of thousands of towns actually publishes, OCR on scanned documents at volume, continuous maintenance as portals change, and the historical corpus. We agree with what they call cheap, too. The AI classification step is a commodity, and we use the same models you do.

**The history is the part no budget recovers.** A build you start today gets you a snapshot, it can't produce last year's crawl. Tracing a decision back through the working-group discussion and the first agenda mention, months earlier, requires having been there. You can build the photograph, you can't build the movie backward.

**Watch for a lazy run.** The verifiable-hands-on and self-audit rules are in the prompt because a model that fabricates its hands-on step will tell you the build is easy. Keep the rules in. Honesty favors whichever answer is actually true for your footprint. The same goes for invented specifics: in our own test runs, models made up statute names and town examples. If a run names a tool, a law, or a company as evidence, make it show the fetched source.

**Make the model audit us, too.** Step 5 asks the model how we tilted this prompt in our own favor, and to rewrite it neutrally. Keep that step in, take whatever rewrite it produces, and run that version instead if you like it better. We did not write a prompt that makes us look good. We wrote one you can take apart.

**Take the pilot demands seriously.** A good run of this prompt will hand you a list of things to make us prove, recall not curated hits, showing the misses, audited lead time, and a clean export with no lock-in. Bring that list to the call. It is the pilot we already run.

## Decide with the comparison in hand

Run the prompt, then [tell us your footprint](/contact/) and we'll show you what the record says about it, next to what your build would cost.
