# norbyte_harvest

Scrapes <https://bg3.norbyte.dev> for candidate `ExtraPassives` / `Spells` to
feed into `cx_passive_manager.json`, and writes `../cx_passive_options.md`
(one section per `CX_*_Boost` passive).

## Why it works this way

The search page renders the first **30 hits server-side** (alphabetical, no
pagination) and everything past that is client-only. So the scraper never asks a
broad question - it fires many *narrow* queries (`type:passive & DreadAmbusher`,
`type:spell & Fireball`, ...) and merges the results. Each hit carries the full
stat entry in a `<code>` block, including the `//`-comment lines Norbyte injects
with the localized DisplayName / Description - that's what the summaries use.

## Files

| file | role |
|---|---|
| `scrape.py` | fetch + on-disk cache (`cache/`) + HTML parse + `summarize()` for one stat entry |
| `terms.py` | the term map: per `CX_*_Boost` passive, a list of `passive` and `spell` search terms (+ a `role` tag) |
| `build_report.py` | runs every term, ranks + de-noises candidates, cross-checks the live manager, writes the Markdown |

## Run

```sh
python build_report.py
```

First run does ~600 HTTP GETs (~8 min, 0.35s politeness delay). Every response
is cached under `cache/`, so re-runs after editing `terms.py` are seconds.
Delete `cache/` to force a refresh against current game data.

## Tuning

- A thin candidate list => the terms missed. Edit that passive's `passive` /
  `spell` list in `terms.py` and re-run. camelCase and `_` both tokenize, so
  `DreadAmbusher` and `Dread_Ambusher` both hit; multi-word terms become AND
  clauses.
- Junk getting through => add a substring to `NOISE_SUBSTR` or the
  `_SPELL_NOISE_RE` pattern in `build_report.py`. Numbered tiers
  (`_1_Passive`, `_2` ...) and spell upcasts (`_2`..`_6`) are already collapsed.
- `MAX_PASSIVE` / `MAX_SPELL` cap how many show per section.

## Reading the report

Per passive: what's already in the manager, then **Passive candidates** and
**Spell candidates**. Within each list, entries you don't already have come
first, and names that literally contain the search term rank above
thematic-only matches. The tail of a long list is the loosest match - skim and
cherry-pick into the Act buckets.
