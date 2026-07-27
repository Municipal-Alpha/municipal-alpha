Title: How well it ran without me
Slug: essays/vacation-mode
Sortorder: 99
Status: published
Author: Matt MacDonald
Date: 2026-07-27
Summary: I went to Sicily for two weeks to find out how much of my company runs without me. The crawlers held. The verification layer certified its own fabrications at a rate of 26 percent, and rated three of the worst ones the strongest in their batch. Five automations failed without making a sound. This is the accounting.

*I went to Sicily for two weeks with family and friends to find out how much of my company runs without me. This is the accounting.*

*One disclosure first, because it's on-topic rather than incidental. This article was drafted by the AI co-author it describes, working from an outline I set and the writing conventions already in my corpus, and I edited it and kept what landed. An article about how well the system runs without me that I hand-wrote from scratch would be a strange artifact.*

I'm writing this on day thirteen. The trip isn't over, so what follows is an interim reading rather than a post-mortem.

The company is one person. Everything else is code, rules, gates and loops I've spent months encoding, which is a polite way of saying I've been trying to write myself down. Crawlers that collect municipal records. Classifiers that read them. A rule layer the AI co-author loads at the start of every session. Pre-commit hooks that refuse work violating those rules. Content gates that refuse to send an email containing a claim they can't trace back to a source document. The design goal for all of it is that the system keeps operating at the standard I set on days when I'm not there to enforce it.

Two weeks away was the first real test.

## What held

The operational half held. Crawling, classification and document collection ran unattended for the whole window. Nothing needed a restart from a phone in a rental car. That was the part I'd been most worried about going in, and it turned out to be the part I should have worried about least.

That's most of the good news. The rest of this is the other kind.

## The verification layer certified its own fabrications

Before I left I ran a test of the thing I actually wanted to know. Could the system find prospects, match them to real signals in the municipal record, and draft outreach that was true, without me reading every one?

It produced 19 signal-anchored emails. The AI layer verified its own work and reported 19 of 19 verified, zero fabrication. A separate deterministic content gate, the one that mechanically refuses em dashes and untraceable numbers and unsupported bio claims, passed all of them clean.

Then four independent judges read the same 19 against the live corpus, each of them told to refute rather than confirm. They found five fabrications. Twenty-six percent.

Three of the five had been rated the strongest email in their batch.

That's the number worth sitting with. Confidence ran highest on the worst output. The checking process scored its best marks on exactly the emails a buyer would have caught.

The root cause was the verification surface rather than the model. The search I built returns a snippet, a window of roughly sixteen tokens around a keyword match, and the verifier was reading that window as though it were the document. The governing word, the one that reverses a claim's meaning, sits outside a sixteen-token window most of the time.

Two examples of the shape. One town's public record said that contrary to talk on social media, nobody had approached the town about a data center. The draft quoted the second half of that sentence and dropped the negation, turning a rumor being knocked down into an active local debate. Elsewhere a zoning district named after a street, the Forest Street Residential Overlay District, got compressed into "a new forest district," which inverts a housing upzoning into conservation zoning. In both cases every proper noun was real, the town was right, the date was right, the document was right, and the meaning was wrong. That is my reading error, not a town's.

Nothing reached a buyer. The call I made from the trip was no-go on autonomous sending, and the deliverable got reframed from a send into a queue. Discovery and matching still run on their own, and instead of drafting an email the system now writes down the prospect, the candidate signal, the source URL and the full source passage for me to judge when I'm back. Every outbound touch during the window was approved by a human.

The finding generalizes past this one test. The agent that makes a claim can't be the agent that certifies it. The drafting agent here reproduced its own elision word for word in its own annotation and then marked it passed. The check didn't just fail to catch the error, it laundered it.

## Five things broke without making a sound

A query behind one of the digests returned nothing at all for eleven days. Nightly bulk classification was killed 26 nights running. A deploy key had been dead for 24 days, which quietly froze every published metric on the website. An off-site backup had never run, not once, leaving several gigabytes of extracted document text one disk failure from gone. A deploy pull aborted and left the production server 54 commits behind.

Every one of those was found by a person noticing that something downstream looked wrong. None of them fired an alert.

My favorite, if that's the word, is the classifier. It was failing every night and the monitoring did report it. The chronic-failure counter capped at eight days, so night ten and night twenty-six both displayed as "CHRONIC 8d." A number that stops moving stops being read, and the outage wallpapered itself.

## The half that didn't run without me

The gap that matters most isn't in the infrastructure.

Before the trip, the customer-facing event log was running at about 22 prospect events a day, measured across the thirty days ending July 14. Since July 15 it's averaged about 1.5 a day. Go-to-market decayed almost immediately and hasn't recovered.

The interesting part is that I did work during the trip. Not many days, but some, and those days produced almost no pipeline activity either. My own note from one of those days reads, "Today went into product and infrastructure because we were going to ship bad data to a customer."

So the chain is short. Output that isn't trustworthy enough to ship unattended pulls me into quality assurance, quality assurance consumes the working hours, and go-to-market gets nothing.

The pipeline runs without me. Go-to-market doesn't, yet. The binding constraint is the trust layer, and every hour it stays unfinished is an hour I spend being the trust layer myself.

## What changed

Four things shipped this month as a direct consequence.

A span-grounding judge, so every claim phrase in a draft has to map to a contiguous span of the full document text with its governing context attached, judged by a model that reads the whole passage instead of the keyhole. Against the five known fabrications it catches five of five, at roughly two hundredths of a cent per claim. Those five are frozen into its test suite alongside five claims that were genuinely clean, and any change to the prompt or the model that drops it below catching all five fails the build. Five is a small set, and catching five of five is a floor rather than proof that it generalizes.

A rule, written down and loaded every session, that verification reads full document text and never a truncated window or a cached excerpt, carrying the measurements that make the case so a future session can't talk itself out of it.

A sentinel for the silent-deploy class. Both repositories get checked nightly for whether they're behind, whether a push failed, whether local changes are blocking a pull, with an email alert that repeats every 24 hours until somebody deals with it.

A reserved budget, so bulk document processing can't eat the daily spending ceiling and starve a customer deliverable of the analysis it needs.

The pattern in all four is one fix per class rather than one patch per incident. Five automations failed quietly and the response was a single sentinel for the shape they shared.

## The honest reading

The question I brought to Sicily was how well the business runs without me. The answer is that the machinery runs and the judgment doesn't. I knew that abstractly before I left. What I didn't know was which judgment, or how expensive it was, and now I have a list. Verification that reads the whole document instead of a window. Alerts that escalate instead of flatlining. A queue I can clear in an evening in place of drafts I'd have to disbelieve one at a time.

None of that makes the company autonomous. It moves the boundary of what I have to be present for, by an amount I can measure, and that boundary is the thing worth tracking over the next year. Two weeks was enough to surface five silent failures and a 26 percent fabrication rate that a clean-looking check had signed off on. I'd rather find that now, with nothing sent, than a year from now with a customer relationship attached.

The trip has a few days left. The crawlers are still running.
