# Keyword Map Plan: keyword_to_passives.json / keyword_to_spells.json

Status: plan approved in part; execution not started. Sources and rules below reflect your answers so far.

## Decisions (from your answers)

- **Entry format:** `Name [CODE]`, e.g. `CX_Paladin_Boost [CXCX]`.
- **Source codes:**
  - Vanilla = `BASE`
  - DeathMarch = `DTHM`
  - InvocationsExpanded = `INVX`
  - RangerSubclasses5eCombined = `RAN` (note: three letters, not four; used as written, say if you want `RANG`)
  - DeGreaser = `DEGR`
  - EncountersOverhaul = `ENCO`
  - Extra_encounters_plus = `EXEP`
  - featsextra = `FEAT`
  - StormWardensTomeOfEncounters = `SWTE`
  - UtutsCoreLibrary = `UTUT`
  - 5eSpells = `5ESP`
  - MystraSpells = `MYST`
  - StormWardensTomeOfSpells = `SWTS`
  - CombatExtender (CX_* passives) = `CXCX`
- **Spell collisions:** the 59 IDs shared by 5eSpells and MystraSpells are indexed by the winner under the Use5eSpellsWithMystraSpells rules (5eSpells for its 7 patched IDs, MystraSpells for the rest). The loser is not indexed.
- **Homebrew:** CX_* passives, StormWardensTomeOfSpells, and StormWardensTomeOfEncounters are indexed.
- **New groups:**
  - Subclass (Paladin, Oathbreaker, and other subclass/archetype keywords), alongside the existing base Class list.
  - Races (Halfling, Gnome, Dwarf, etc.).
  - MagicItemType: Headwear, Cloak, Armor/Clothing, Gloves, Boots, Necklace, Ring, Martial Weapon, Ranged Weapon, Shield.
- **Classification signal:** structured fields first (DamageType, SpellSchool, Boosts, Requirements, Statuses). Description text is used only for tie-breaks or gaps. An entry can appear in several buckets.

## Scope rules

1. Drop visual-FX-only entries.
2. Drop legendary actions and legendary passives.
3. Drop entries that reference a resource from a mod that is not in the load order.
4. Drop single-monster-specific entries that don't generalize. Example: halfling/gnome gloves go under Races, not Humanoid.

## Sources

**Passives**
- Vanilla: norbyte `type:passive` (about 1,879 results, 30 per page)
- DeathMarch, InvocationsExpanded, RangerSubclasses5eCombined, DeGreaser, EncountersOverhaul, Extra_encounters_plus, featsextra, StormWardensTomeOfEncounters, UtutsCoreLibrary (tied to EncountersOverhaul)
- Plus CX_* and the homebrew passives above

**Spells**
- Vanilla: norbyte `type:spell`
- 5eSpells, DeathMarch, InvocationsExpanded, MystraSpells (5eSpells wins where the exceptions list applies), RangerSubclasses5eCombined
- Plus StormWardensTomeOfSpells

## Steps

1. **Inventory.** Vanilla entries come from the local Stats text files in `bg3-mod-extraction-utils/scratch_vanilla_extract/allstats_hunt/` (Gustav, GustavDev, Shared, Honour, etc.), not norbyte. Verify coverage first, because the extract is partial. Parse each mod's Stats text files and PassiveLists/SpellLists. Save raw output to the scratchpad. Norbyte is used only for per-entry DisplayName/Description lookups, through `research/norbyte_harvest/scrape.py`.
2. **Dedupe and resolve collisions.** Apply the 5eSpells/MystraSpells winner rule.
3. **Filter.** Apply the scope rules above.
4. **Classify.** Structured fields first, then description text for tie-breaks. Multi-bucket allowed.
5. **Write.** Fill both JSON files with the same key structure, adding Subclass, Races, and MagicItemType.
6. **Verify.** Validate the JSON. Spot-check about 30 random entries. Report per-keyword counts so heavy buckets (e.g. Humanoid) are visible for the later trim.

## Known risk

Norbyte search does not support bulk listing. `research/norbyte_harvest/` runs narrow term queries and gets at most 30 hits per query, with no pagination. Its `terms.py` is a CX-candidate term map, not a full inventory. WebFetch returns summaries, not raw fields. So full inventory must come from local Stats files, and norbyte is only for descriptions. Any Boosts/DamageType/School values come from the raw Stats text.
