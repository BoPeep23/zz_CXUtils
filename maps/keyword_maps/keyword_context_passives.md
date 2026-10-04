# Context: Building keyword_to_passives.json

Read this first. It is the full brief for a fresh chat that builds the passive keyword map. It assumes no prior conversation.

**Status:** Draft. Revisit after the norbyte scraper findings. The scraper is term-driven and capped at 30 hits per query, so the inventory approach below may need small changes. Check [keyword_map_plan.md](keyword_map_plan.md) for the latest.

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
