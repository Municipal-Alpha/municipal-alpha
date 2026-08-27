# Contributing to municipalalpha.com

## The one thing to know before you push

**In this repository, pushing to `main` is publishing to production.**

There is no staging step and no separate deploy command. A push to `main`
triggers `.github/workflows/deploy.yml`, which builds the site and publishes it
to GitHub Pages at **https://municipalalpha.com**. Your commit is live to the
public within a few minutes.

This is a different bargain from `muni-scraper`, where `main` reaches the VPS on
a nightly pull and there is a night of slack between merging and running. Here
there is none. That difference is deliberate — the marketing site is the surface
where speed matters most and blast radius is smallest — but it should be known
rather than discovered.

## What actually protects the site

Not branch protection. **The deploy job depends on the build job** (`deploy:
needs: build`), so if the build fails, the deploy never runs and Pages keeps
serving the last good version. A broken push cannot take the site down; it just
fails to change it.

The build runs these gates, in order, and any one of them failing stops the
publish:

| gate | what it refuses |
|---|---|
| `tools/redteam_content.py` | competitive-intelligence leaks in markdown |
| `tools/check_metrics_drift.py` | a page claiming a corpus figure that disagrees with `data/metrics.json` |
| `tools/inject_noindex.py` | (not a refusal) stamps `noindex` on every `content/extra/` page |
| `tools/check_no_diffview.py` | a review-scaffolding page reaching the build output |

After the deploy, `tools/check_live_surface.py` fetches the published site and
checks that what a reader actually receives is what we think we shipped. It runs
*after* the publish, so it reports rather than gates: a red `verify` job means
the live site is wrong and needs a fix forward, not a rollback.

## Reverting

Reverting is cheap and is usually the right first move if something published
wrong:

```bash
git revert <sha>
git push origin main        # this republishes; the revert IS the fix
```

Do not force-push to `main`. If the wrong thing is public, get the right thing
public — do not try to make the wrong thing never have happened.

## Before you write copy

Buyer-facing and marketing copy is governed by rules that live in the
`muni-scraper` repo, not this one, because they are shared with every other
outbound surface:

- `.claude/rules/external-data-accuracy.md` — every claim verified, labelled, or
  omitted
- `.claude/rules/bio-accuracy.md` — employment history is checked against
  `business/bio.md`; Matt did not work at Spotify, The Echo Nest, Google or
  Metaweb, they are business-model analogies
- `.claude/rules/business-outreach.md` — voice, pricing, social proof, NDA
  constraints
- `.claude/rules/external-artifact-hygiene.md` — no internal identifiers on a
  published page: no database filenames, table or column names, repo paths,
  message ids or recipient addresses

Run the accuracy scan against anything you are about to publish:

```bash
python3 ../muni-scraper/tools/check_external_content.py --include-html content/extra/<page>/index.html
```

**Known gap, stated rather than hidden:** that scan is *not* wired into this
repo's CI yet. It runs from a pre-push hook in `muni-scraper`, so a change
pushed straight from here never meets it. Treat running it as your
responsibility until the CI step lands.

Any buyer-facing artifact over ~300 words also gets a blind read by the operator
who did not write it, and `python3 ../muni-scraper/tools/llm_review.py
--proposal <file> --mode reader --force --intent "<the one action you want>"`.
Four real readers have told us our prose is hard to parse; one of them walked
over it.

## Reading a change before you publish it

To read a page with its changes highlighted in place rather than as a diff:

```bash
python3 ../muni-scraper/tools/diffview/annotate_html_diff.py \
    --repo ~/Projects/municipal-alpha \
    --file content/extra/<page>/index.html \
    --rev origin/main --open
```

Yellow is added, blue is rewritten (hover for the old text), and ▲/▼ or `j`/`k`
walk the changes. It writes a throwaway copy and refuses to write anywhere
inside a git working tree, so the annotated page can never be committed.

## Local gates

Install the pre-commit hooks so you find problems before CI does:

```bash
brew install pre-commit
pre-commit install
```

## Paths worth knowing

| path | what it is |
|---|---|
| `content/pages/` | Pelican pages — the public, linked site |
| `content/extra/` | standalone HTML, unlinked, `noindex` injected at build |
| `output/` | build output; never edited by hand, never committed |
| `data/metrics.json` | the corpus figures the drift gate checks pages against |

**The site repo is at a different path on each machine.** Laptop:
`~/Projects/municipal-alpha`. VPS: `~/municipal-alpha`. Both are correct;
state which one you mean.
