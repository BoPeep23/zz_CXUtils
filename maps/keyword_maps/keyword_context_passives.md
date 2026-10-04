# Context: Building keyword_to_passives.json

Read this first. It is the full brief for a fresh chat that builds the passive keyword map. It assumes no prior conversation.

**Status:** First pass done. `keyword_to_passives.json` is written and validated. Caveats and open work are in the Handoff section at the end. Check [keyword_map_plan.md](keyword_map_plan.md) for the spells side, which is still separate.

## Goal

Fill [keyword_to_passives.json](keyword_to_passives.json) so Tyler can search by keyword when editing [guid_mapper_master.json](../../guid_mapper_master.json) or [cx_passive_manager.json](../../cx_passive_manager.json). Example: for an Oathbreaker, search Paladin, Necrotic, or Humanoid.

The file is a map of keyword bucket to a list of passive entries. Record every keyword hit. A later process trims the big buckets, such as Humanoid, so do not cap them now.

Spells use the same structure in [keyword_to_spells.json](keyword_to_spells.json). That is a separate chat and is out of scope here.

## Decisions already made

- **Entry format:** `Name [CODE]`, for example `CX_Paladin_Boost [CXCX]`.
- **Source codes:**
  - Vanilla = `BASE`
  - DeathMarch = `DTHM`
  - InvocationsExpanded = `INVX`
  - RangerSubclasses5eCombined = `RAN`
  - DeGreaser = `DEGR`
  - EncountersOverhaul = `ENCO`
  - Extra_encounters_plus = `EXEP`
  - featsextra = `FEAT`
  - StormWardensTomeOfEncounters = `SWTE`
  - UtutsCoreLibrary = `UTUT`
  - CombatExtender (CX_* passives) = `CXCX`
  - FADE (Fade's Equipment Distribution, 7 per-class packs; Ranger/Bard/Warlock excluded) = `FADE`
- **Homebrew is included:** CX_* passives and StormWardensTomeOfEncounters entries are indexed.
- **Groups:** keep the existing keys. Add these groups:
  - **Subclass**: Paladin, Oathbreaker, and other subclass or archetype keywords, alongside the existing base Class list.
  - **Races**: Halfling, Gnome, Dwarf, etc.
  - **MagicItemType**: Headwear, Cloak, Armor/Clothing, Gloves, Boots, Necklace, Ring, Martial Weapon, Ranged Weapon, Shield.
- **Classification:** structured fields first (DamageType, Boosts, Requirements, Statuses). Use description text only for tie-breaks or gaps. An entry can appear in several buckets.

## Scope rules

1. Drop visual-FX-only passives.
2. Drop legendary actions and legendary passives.
3. Drop passives that reference a resource from a mod that is not in the load order. Check `modsettings` before deciding. Mods are in `bg3-mod-extraction-utils/mods/`.
4. Drop single-monster-specific passives that don't generalize. Example: halfling/gnome gloves go under Races, not Humanoid. An immunity that applies to Fey as a type does belong under Fey.

Use best judgment. When the case is unclear, include the entry and note it in the sidecar log.

## Sources

**Vanilla inventory:** the local Stats text files in `bg3-mod-extraction-utils/scratch_vanilla_extract/allstats_hunt/` (Gustav, GustavDev, Shared, Honour, and others). Start with `Public/*/Stats/Generated/Data/Passive.txt`. The extract is partial, so confirm coverage before trusting counts. Norbyte is not a full list.

**Mods** (bg3-mod-extraction-utils/mods/):
- DeathMarch, InvocationsExpanded, RangerSubclasses5eCombined, DeGreaser, EncountersOverhaul, Extra_encounters_plus, featsextra, StormWardensTomeOfEncounters, UtutsCoreLibrary (tied to EncountersOverhaul)
- Passive stats: `Public/*/Stats/Generated/Data/Passive*.txt` and `PassiveTag.txt`. Passive lists: `Lists/PassiveLists.lsx`.
- The folder is `featsextra`, not `feats_extra`.
- InvocationsExpanded is in the brief twice. Treat it as one source.

**Homebrew:** CX_* passives come from `CXPassiveEnforcer` and `cx_passive_manager.json`. Tome entries come from `StormWardensTomeOfEncounters`. Check the live manager and `zz_CXUtils/research/cx_passive_options.md` before classifying.

**Descriptions (lookup only):** norbyte entry pages through `bg3-mod-extraction-utils/research/norbyte_harvest/scrape.py` (cached fetch). Do not use it for listing. It returns at most 30 hits per query, and WebFetch returns summaries that lack raw fields.

## Method

1. Verify that allstats_hunt covers the vanilla passives you need. Note any gaps.
2. Parse each source's Passive stat blocks. Record the name, source code, and structured fields.
3. Dedupe. A name that appears in more than one source is one entry per source code.
4. Apply the scope rules.
5. Classify each passive into every bucket it fits, structured fields first.
6. Write `keyword_to_passives.json`. Keep the existing key structure and key order. Add the new groups.
7. Validate the JSON. Spot-check about 30 random entries against their Stats text. Report per-bucket counts, and flag the largest buckets for later trimming.

## Output rules

- Keep the file as valid JSON with the existing indentation style (4 spaces).
- Write a sidecar log `keyword_passives_log.md` next to the JSON. Record each judgment call, each exclusion with its reason, and each coverage gap. Keep it short.
- Do not change `keyword_to_spells.json`.
- Do not edit `guid_mapper_master.json` or `cx_passive_manager.json`.

## Open items

- Whether `modsettings` is needed for the load-order check (currently assumed yes).
- Whether the 5eSpells/MystraSpells collision rule affects any passives. Assumed no, since it is a spell rule.
- Whether the scraper findings change the inventory method.

## Handoff (state as of 2026-10-03)

### What exists
- [keyword_to_passives.json](keyword_to_passives.json): built. Groups in order: DamageTypes, SpellSchools, Class, Subclass, Races, EnemyType, MagicItemType, Type. 1,624 memberships across 1,056 unique passive names. Per-code: BASE 780, UTUT 214, FEAT 111, DTHM 78, RAN 31, DEGR 25, EXEP 23, ENCO 20, SWTE 15, INVX 10, CXCX 133, FADE 184. FADE added 2026-10-03; see the FADE section of the log.
- [keyword_passives_log.md](keyword_passives_log.md): the judgment calls, exclusions, and gaps. Read it before changing anything.
- `keyword_to_spells.json`: untouched. Separate chat.

### How it was built (rules that must hold on any rebuild)
- Parser: scan every `Stats/**/*.txt` under each source's folder and keep only `type "PassiveData"` blocks. Passives are not confined to `Passive*.txt`. InvocationsExpanded and others put them in many files. Dedupe by (name, source code).
- Sources, in load order: vanilla extract `scratch_vanilla_extract/allstats_hunt/`, and `mods/` for DeathMarch, InvocationsExpanded, RangerSubclasses5eCombined, DeGreaser, EncountersOverhaul, Extra_encounters_plus, featsextra, StormWardensTomeOfEncounters, UtutsCoreLibrary. CX_* comes from `cx_passive_manager.json` (62 entries).
- Load order: all sources are in `modsettings.lsx`, checked against 64 entries. The load-order rule has not dropped anything yet.
- Classification uses name tokens and mechanics only.
  - DamageTypes: capitalised arguments (`DealDamage(..., Fire)`, `Resistance(Fire)`, `DamageType.Fire`).
  - Class, Subclass, SpellSchools, Races: name tokens. Races also accept `Tagged('X')`.
  - EnemyType: name tokens or `Tagged('X')`.
  - MagicItemType: item name tokens. Ranged Weapon also accepts `IsRangedWeaponAttack`.
  - Type: rough mechanic heuristics.
  - Do NOT match on status or ID names, or on Conditions. Doing so caused false hits: SHADOWHEART → Shadow, GITHYANKI status names → Races:Githyanki.
- CX_* entries: classified from the passives in their `ExtraPassives` (across all Acts), plus the name. A CX entry with no hits is not indexed (CX_Magic_Boost, CX_Martial_Boost).
- Scope rules applied: legendary actions and LegendaryResistance / Legendary_hook dropped (85). Entries with no mechanics and no name hit dropped (241 FX-only). Same-source duplicates dropped (18).
- Output: 4-space indent, `Name [CODE]` entry format.

### Known gaps and open tasks (in priority order)
1. **Vanilla coverage is partial.** `allstats_hunt` has only Gustav, GustavDev, and Honour. There is no Shared folder. It yields 868 unique vanilla PassiveData names. 161 passives referenced by CX manager entries are not in any scanned source. Examples: Evasion, FastHands, DivineHealth, FightingStyle_Archery, SteelWill, MagicResistance, DarkDevotion, DeflectMissiles. Fix by completing the extract or by pulling entries via `research/norbyte_harvest/scrape.py`. Norbyte is for lookup, not listing. Then rebuild. This is the biggest gap.
2. **Decide the MAG_Legendary_* question.** Currently kept, since they are item-rarity passives, not monster legendary passives. Ask Tyler, then apply.
3. **Add StormWardensTomeOfSpells.** Its `PassiveFixes.txt` has one PassiveData entry. It is not in the source list yet. Add it under code SWTS, per the plan.
4. **Clean up name-token noise.** Subclass/Shadow (21), Light (11), and Life (18) are mostly from names such as UNI_HealInShadow, Shadowheart, and ShadowTouched_Wisdom (a feat). Consider a stoplist or a requirement for a class-prefixed name.
5. **Tighten Type buckets.** Buff_Single (185) is over-broad: it tags any ActionResource or DamageBonus. Control_Single includes Prone-status items that are not control effects (MAG_HaHaHat_Passive). Defense_SavingThrows (52) needs a check.
6. **Review the 538 unindexed entries.** They have mechanics but match no bucket. Most look like one-off monster or item logic. Decide whether any belong in a bucket.
7. **Scope rule 4 (single-monster passives) is not applied.** No reliable marker. Needs a judgment pass, or a manual stoplist.
8. **Re-run spot-check after any rebuild.** The last 30-sample check was about 25/30 correct.

### Scripts (now in the repo)
- Copied into `maps/keyword_maps/`: `parse_passives.py` (parses PassiveData from every `Stats/**/*.txt` into `passives_raw.json`), `classify.py` (vocab and rules), `run.py` (dedupe, scope rules, CX lookup, writes `keyword_to_passives.json` and the log stats), and `passives_raw.json` (the parsed snapshot).
- Rebuild order: `python parse_passives.py` (only if sources changed), then `python run.py`. `run.py` also writes `run_stats.json` into the same folder. It is a generated file and can be deleted.
- `parse_passives.py` hardcodes the bg3-mod-extraction-utils root, so the sources must be at that path.
- Re-run the classifier from a fresh chat. Compare counts with the numbers above. A change in the 953 unique count means something changed.

### Do not
- Do not edit `keyword_to_spells.json`, `guid_mapper_master.json`, or `cx_passive_manager.json` from this work.
