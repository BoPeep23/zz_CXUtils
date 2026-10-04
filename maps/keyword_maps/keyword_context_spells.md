# Context: Building keyword_to_spells.json

Read this first. It is the full brief for a fresh chat that builds the spell keyword map. It assumes no prior conversation.

**Status (2026-10-03):** First build done. [keyword_to_spells.json](keyword_to_spells.json) is populated (478 unique entries) and the audit log is written. Open decisions are listed under "Open decisions" below. The norbyte scraper was not used. Check [keyword_map_plan.md](keyword_map_plan.md) for the passives side.

## Build state (read this before rebuilding)

**Files in this folder**
- [keyword_to_spells.json](keyword_to_spells.json): the output. Valid JSON, 4-space indent, existing keys in original order, then Subclass, Races, MagicItemType appended.
- [keyword_spells_log.md](keyword_spells_log.md): judgment calls, exclusions with counts, collision resolution, coverage gaps, spot-check results, per-bucket counts.
- [build_keyword_spells.py](build_keyword_spells.py): the full builder. Rerun with `SCR=<scratch dir>` set. The scratch dir must contain `shared_pak/`, produced by the extract command below. Output is written to this folder. The script also writes `diag.json` to `SCR`.

**Rebuild needs Shared.pak extracted**
- Divine: `xport-tool/Packed/Tools/Divine.exe` in bg3-mod-extraction-utils.
- Command: `Divine.exe -g bg3 -a extract-package -s "<BG3 Data>/Shared.pak" -d "<SCR>/shared_pak"`. Use `-d` with a directory. `list-package` prints to stdout, not to `-d`.
- Gustav.pak is 13 GB and was NOT extracted. Its spell stats are the same 22 files already in `allstats_hunt`.

**Corrections to the assumptions above**
- `SpellSet.txt` does not exist in the vanilla extract. Vanilla class membership comes from `Public/Shared/Lists/SpellLists.lsx` inside Shared.pak (126 SpellList nodes), plus the GustavX copy in `scratch_vanilla_extract/gustavx_check`.
- `allstats_hunt` alone is incomplete. Shared.pak also has Spell_* stats in `Public/Shared` and `Public/SharedDev`. Without them, 271 list-referenced IDs were undefined. With them, 37 remain undefined.
- StormWardensTomeOfSpells contributes 0 entries. Its 347 SpellData entries are all pins for IDs that MystraSpells or 5eSpells already define.
- InvocationsExpanded does define spells (147 SpellData entries). 44 are kept after the UNUSED and variant filters.
- All spell-source mods are in the modsettings load order, so no load-order drops were needed.

**Decisions made in the build** (all are in the log)
- Entry format is the internal ID, e.g. `Target_Fireball [BASE]`. This deviates from the brief's `Fireball [BASE]` example, because vanilla localization is not local and internal IDs match the passive map.
- Collisions: 59 IDs. 7 go to 5ESP (Use5e patched set). The other 52 go to MYST, including `Target_TrueSeeing`, which is also vanilla.
- Non-collision duplicates: last in load order wins. Load order used: 5ESP < MYST < U5E < SWTS < INVX < RAN < DTHM.
- Use5e list-dedup losers (22 IDs) are excluded.
- Scope rule 4 is implemented as "no class, subclass, or race list membership". INVX is exempt. This dropped about 7,400 raw definitions.
- Upcast, ritual, default, sneak-attack, and interrupt variants are merged into their base entry.
- Races come from list names (Drow, Tiefling, Forest Gnome, Githyanki) plus ID tokens. EnemyType comes from summon keywords in the ID. MagicItemType is empty by design.
- DamageType counts only when a `DealDamage` term exists.

**Known weaknesses**
- Defense_* buckets are under-counted, because status files are not parsed. SavingThrows has 0 entries, and ConditionImmunity has 0.
- Type and Control buckets come from name patterns and radius heuristics.
- College of Lore is 201 entries, because the TCoE Lore Bard lists are broad.
- Some inherited damage types are wrong (e.g. Target_Goodberry shows Cold).
- Unparsed lists: 5eSpellsLists, SecretScrolls5eSpells, Book of Druids and Sorcerers, SpellListSorter, SpellListCombiner. These could add class memberships.
- 37 list-referenced IDs are undefined in the extracts (e.g. `Projectile_ArcaneShot_*`, `Target_DirtyTrick_*`, `Shout_Wildshape_Star_*`).

## Open decisions (ask Tyler before changing)
1. **StormWardensTomeOfSpells pins.** The Tome's header pins `Target_GreenFlameBlade`, `Target_Frostbite`, and `Projectile_VitriolicSphere` to 5eSpells. The brief's rule puts them under MYST. The Tome loads last, so its pins are what is live in game. Which should win?
2. **Scope rule 4.** Is "no list membership means drop" the rule Tyler wants? Passive-granted spells on no list are lost.
3. **Gustav.pak extraction.** Should the 37 undefined IDs be recovered by extracting Gustav.pak in full (13 GB)?

## Next steps for a future chat
- Get answers to the three decisions above, apply any changes, and rebuild.
- Parse the unparsed list files listed above.
- If Tyler wants Defense_* accurate, parse the status files so Boosts and status effects can be classified.
- Trim the large buckets when Tyler asks. The log lists the candidates.
- Do not change `keyword_to_passives.json`, `guid_mapper_master.json`, or `cx_passive_manager.json` from this chat.

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

## Resolved since the first draft

- `modsettings` was checked. All spell-source mods are in the load order, so no load-order drops were needed.
- The scraper was not used. Inventory came from the local Stats files, and norbyte was not needed.
- InvocationsExpanded does define spells (147 SpellData entries, 44 kept).
