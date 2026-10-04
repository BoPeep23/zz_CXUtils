# Context: Building keyword_to_spells.json

Read this first. It is the full brief for a fresh chat that builds the spell keyword map. It assumes no prior conversation.

**Status:** Draft. Revisit after the norbyte scraper findings. The scraper is term-driven and capped at 30 hits per query, so the inventory approach below may need small changes. Check [keyword_map_plan.md](keyword_map_plan.md) for the latest.

## Goal

Fill [keyword_to_spells.json](keyword_to_spells.json) so Tyler can search by keyword when editing [guid_mapper_master.json](../../guid_mapper_master.json) or [cx_passive_manager.json](../../cx_passive_manager.json). Example: for an Oathbreaker, search Paladin, Necrotic, or Humanoid.

The file is a map of keyword bucket to a list of spell entries. Record every keyword hit. A later process trims the big buckets, such as Humanoid, so do not cap them now.

The passive map (`keyword_to_passives.json`) has the same structure and is a separate chat. It is out of scope here.

## Decisions already made

- **Entry format:** `Name [CODE]`, for example `Fireball [BASE]`.
- **Source codes:**
  - Vanilla = `BASE`
  - 5eSpells = `5ESP`
  - MystraSpells = `MYST`
  - DeathMarch = `DTHM`
  - InvocationsExpanded = `INVX`
  - RangerSubclasses5eCombined = `RAN`
  - StormWardensTomeOfSpells = `SWTS`
- **Collisions:** 59 spell IDs exist in both 5eSpells and MystraSpells. Index only the winner, using the Use5eSpellsWithMystraSpells rules. 5eSpells wins for its 7 patched IDs, and MystraSpells wins for the rest. Do not index the loser. Source: `bg3-mod-extraction-utils/mods/Use5eSpellsWithMystraSpells/` and [mystra-5espells-compat](../../research/mystra_5espells_compat_report.md).
- **Homebrew is included:** StormWardensTomeOfSpells entries are indexed.
- **Groups:** keep the existing keys. Add these groups:
  - **Subclass**: Paladin, Oathbreaker, and other subclass or archetype keywords, alongside the existing base Class list.
  - **Races**: Halfling, Gnome, Dwarf, etc.
  - **MagicItemType**: Headwear, Cloak, Armor/Clothing, Gloves, Boots, Necklace, Ring, Martial Weapon, Ranged Weapon, Shield. Spells rarely fit these, so expect few or no entries. Keep the keys anyway, so the two maps match.
- **Classification:** structured fields first (DamageType, SpellSchool, Type, Statuses, and Boosts). Use description text only for tie-breaks or gaps. An entry can appear in several buckets.

## Scope rules

1. Drop visual-FX-only spells, such as projectile or impact effect entries that do nothing mechanically.
2. Drop legendary actions. Legendary spells are not a thing, but if any legendary-only entries appear, drop them.
3. Drop spells that reference a resource from a mod that is not in the load order. Check `modsettings` before deciding.
4. Drop single-monster-specific spells that don't generalize. A spell used by one creature, with no broader keyword meaning, is excluded.
5. Upcast variants (`_2` through `_6`) are one spell. Index the base entry.

Use best judgment. When the case is unclear, include the entry and note it in the sidecar log.

## Sources

**Vanilla inventory:** the local Stats text files in `bg3-mod-extraction-utils/scratch_vanilla_extract/allstats_hunt/` (Gustav, GustavDev, Shared, Honour, and others). Start with `Public/*/Stats/Generated/Data/Spell_*.txt` and `SpellSet.txt`. The extract is partial, so confirm coverage before trusting counts. Norbyte is not a full list.

**Mods** (bg3-mod-extraction-utils/mods/):
- 5eSpells, DeathMarch, InvocationsExpanded, MystraSpells (5eSpells wins where the exceptions list applies), RangerSubclasses5eCombined
- Spell stats: `Public/*/Stats/Generated/Data/Spell*.txt`. Spell lists: `Lists/SpellLists.lsx`.
- 5eSpells and MystraSpells keep their stats under `Mods/` as well as `Public/`. Check both.
- Use5eSpellsWithMystraSpells holds the exceptions list. Read it before resolving collisions.
- InvocationsExpanded has no spell stats folder with spells in the same format. Check whether it defines spells at all, and note it in the log if not.
- Keep in mind that the existing `mods/` folder also has StormWardensTomeOfSpells, which is the homebrew source.

**Descriptions (lookup only):** norbyte entry pages through `bg3-mod-extraction-utils/research/norbyte_harvest/scrape.py` (cached fetch). Do not use it for listing. It returns at most 30 hits per query, and WebFetch returns summaries that lack raw fields.

## Method

1. Verify that allstats_hunt covers the vanilla spells you need. Note any gaps.
2. Parse each source's spell stat blocks. Record the name, source code, and structured fields.
3. Resolve the 59 collisions with the Use5eSpells rules. Index only the winners.
4. Apply the scope rules. Collapse upcast variants to their base spell.
5. Classify each spell into every bucket it fits, structured fields first.
6. Write `keyword_to_spells.json`. Keep the existing key structure and key order. Add the new groups.
7. Validate the JSON. Spot-check about 30 random entries against their Stats text. Report per-bucket counts, and flag the largest buckets for later trimming.

## Output rules

- Keep the file as valid JSON with the existing indentation style (4 spaces).
- Write a sidecar log `keyword_spells_log.md` next to the JSON. Record each judgment call, each exclusion with its reason, each collision resolution, and each coverage gap. Keep it short.
- Do not change `keyword_to_passives.json`.
- Do not edit `guid_mapper_master.json` or `cx_passive_manager.json`.

## Open items

- Whether `modsettings` is needed for the load-order check (currently assumed yes).
- Whether the scraper findings change the inventory method.
- Whether InvocationsExpanded defines any spells at all.
