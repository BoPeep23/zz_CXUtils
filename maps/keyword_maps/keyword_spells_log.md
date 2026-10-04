# keyword_to_spells: build log

Written for: Tyler, to audit judgment calls before trimming.

Result: 478 unique entries across 7 populated groups. Sources: BASE 274, MYST 111, 5ESP 51, INVX 42, SWTS 0.
Rebuild: `build_keyword_spells.py` (this folder). Needs `SCR` set to a scratch folder holding `shared_pak/` (Shared.pak extracted with Divine).

## Sources
- **BASE (vanilla):** `allstats_hunt/Public/{GustavDev,Gustav,Honour}` plus `Shared.pak` Stats (`Shared`, `SharedDev`). The allstats_hunt extract alone left 271 list-referenced IDs undefined; adding Shared.pak leaves 37. Gustav.pak's spell files are the same 22 as allstats_hunt, so it was not extracted (13 GB).
- **Class lists (vanilla):** `Shared.pak` `Public/Shared/Lists/SpellLists.lsx` (126 nodes) plus the GustavX copy.
- **Mods:** 5eSpells, MystraSpells, Use5eSpellsWithMystraSpells (replacement stats only), StormWardensTomeOfSpells, InvocationsExpanded, DeathMarch, RangerSubclasses5eCombined. All are in the modsettings load order, so no load-order drops were needed.
- **Non-collision duplicates:** last in load order wins (5ESP < MYST < U5E < SWTS < INVX < RAN < DTHM).

## Judgment calls
1. **Entry name is the internal ID** (`Target_Fireball [BASE]`), not a display name. Vanilla localization is not local, and internal IDs match the passive map and CX data.
2. **59 collisions** (5eSpells and MystraSpells both define the ID): 7 go to 5ESP (the Use5e patched set), 52 go to MYST. `Target_TrueSeeing` is also a vanilla ID; it goes to MYST under the same rule.
3. **Storm Warden's Tome conflict.** The Tome is last in load order, and its header pins `Target_GreenFlameBlade`, `Target_Frostbite`, and `Projectile_VitriolicSphere` to 5eSpells. The brief's rule attributes them to MYST, so the index follows the brief. The Tome's pins are the copies that are live in game.
4. **SWTS contributes zero entries.** All 347 SpellData entries are pins for IDs that MystraSpells or 5eSpells already define. Pins yield to the origin mod.
5. **Scope rule 4 (single-monster spells)** is applied as "no class, subclass, or race list membership". This dropped 7,373 raw definitions. INVX is exempt, because its spells are granted by invocations rather than lists. The main risk is a passive-granted spell in any other mod that is on no list.
6. **Variants collapsed** into their base: `_2`–`_6` upcasts, `_Ritual`, `_Default`, `_SneakAttack`, `_Interrupt` (52).
7. **Dropped as Use5e list-dedup losers** (22 IDs): not reachable from any class list.
8. **Other drops:** visual or no-effect and unlisted (440); legendary, matched on "Legendary" in the ID or flags (41, heuristic); `UNUSED` flag, INVX only (30).
9. **DamageType** counts only when the spell has a `DealDamage` term. An inherited `DamageType` field alone does not count.
10. **Type buckets** are heuristic. Radius above 6 is Large; Zone, Shout, and Wall are AOE. Control comes from status-name patterns. Status files are not parsed, so **Defense_* is under-counted**: ArmorClass, DamageResistance, and HitPoints have 1–2 entries each, SavingThrows has 0, and ConditionImmunity has 0.
11. **Description text was not used** (no norbyte lookups).
12. **EnemyType** applies only to summon-type spells, from keywords in the ID. Humanoid, Giant, and most others stay empty.
13. **Races** come from list names (Drow, Tiefling, Forest Gnome, Githyanki) plus ID tokens.
14. **Subclass keys added:** Paladin and Oathbreaker per the brief, plus Eldritch Knight, Archfey, and the rest of the list-derived subclasses. Groups are appended after the existing keys.
15. **MagicItemType** is empty by design. Spell stats carry no item-type fields.
16. **Unmapped list names** (17): feats, companion lists, Wild Shape forms, and a few racial cantrips such as Mage Hand. These are skipped.

## Coverage gaps
- **37 list-referenced IDs have no stat definition** in any loaded pak extract, e.g. `Projectile_ArcaneShot_*`, `Target_DirtyTrick_*`, `Shout_Wildshape_Star_*`, `Target_BoomingBlade_ClassSpell`. Extracting Gustav.pak in full would find them, or they can be read from the game later.
- **Unparsed lists:** 5eSpellsLists, SecretScrolls5eSpells, Book of Druids and Sorcerers, SpellListSorter, and SpellListCombiner. They could add class memberships, so some spells may be under-indexed in Class.
- **Name-to-list mapping** is keyword-based. Lore Bard lists from TCoE are broad, which inflates College of Lore to 201.

## Spot-check
- 60 random entries (two samples of 30) were checked against raw Stats fields.
- Fixed: inherited `DamageType` false positives (Animate Dead, Conjure Fey); a `SAVED_AGAINST_*` save-marker false positive; `UNUSED` entries.
- Known noise: some inherited damage types still appear (e.g. `Target_Goodberry` shows Cold).
- The second sample ran before the race and subclass mapper change. That change only adds Subclass and Races hits from lists.

## Bucket counts (populated only)
### DamageTypes
Fire 26, Force 26, Necrotic 24, Psychic 21, Radiant 18, Bludgeoning 17, Cold 17, Lightning 12, Poison 12, Thunder 12, Acid 11, Piercing 10, Slashing 2
### SpellSchools
Evocation 88, Conjuration 79, Transmutation 69, Enchantment 46, Necromancy 45, Abjuration 44, Divination 18, Illusion 17
### Class
Bard 332, Wizard 243, Sorcerer 184, Cleric 168, Warlock 152, Druid 144, Fighter 100, Rogue 74, Ranger 67, Barbarian 5
### EnemyType
Undead 4, Aberration 1, Beast 1, Construct 1, Dragon 1, Elemental 1, Fey 1, Fiend 1
### Type
SpellDamage_Single 101, Buff_Single 70, SpellDamage_AOE_Small 67, Buff_Multiple 63, Control_Single 30, Debuff_Single 21, Healing_Single 13, Defense_Special 12, Teleportation 12, Debuff_Multiple 11, Control_AOE_Small 8, Healing_AOE 8, SpellDamage_AOE_Large 7, Control_AOE_Large 2, Defense_ArmorClass 2, Defense_DamageResistance 2, Defense_HitPoints 1
### Subclass
College of Lore 201, Archfey 91, Eldritch Knight 88, Great Old One 88, Hexblade 85, Fiend 84, Paladin 69, Arcane Trickster 69, Death Domain 17, Light Domain 17, Trickery Domain 16, War Domain 15, Life Domain 14, Nature Domain 14, Tempest Domain 14, Knowledge Domain 13, Oathbreaker 9, Swarmkeeper 4, Arcane Archer 3, Circle of Stars 2, Hunter 2, Berserker 2, Shadow Sorcerer 1, Totem Warrior 1, Beast Master 1, Storm Sorcery 1
### Races
Tiefling 6, Drow 3, Githyanki 3, Gnome 1
### MagicItemType
_empty by design_

## Largest buckets (candidates for trimming)
Class Bard, Wizard, Sorcerer, Cleric, Warlock. Subclass College of Lore, Archfey, Eldritch Knight, Great Old One, Hexblade, Fiend. Type SpellDamage_Single, Buff_Single, SpellDamage_AOE_Small.

## Not done
- Two kept entries have no bucket hit and are not written: `Shout_CloakOfFlies_Dismiss`, `Target_Maddening_Hex`.
- `keyword_to_passives.json` and the two `guid_mapper`/`cx_passive` files were not touched.
