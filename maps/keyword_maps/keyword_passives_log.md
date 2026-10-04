# keyword_to_passives.json: build log

First pass, rule-based. Classification uses name tokens and mechanics (Boosts, StatsFunctors, ToggleOnFunctors). Descriptions were not used. Spot-check and trim before relying on it.

## Coverage gaps

- **Vanilla (BASE) is partial.** The local extract (`scratch_vanilla_extract/allstats_hunt/`) has only Gustav, GustavDev, and Honour. There is no Shared folder. It yields 868 unique PassiveData names. Core passives are missing, including Evasion, FastHands, DivineHealth, FightingStyle_Archery, and SteelWill. 161 passives referenced by CX_* manager entries were not found in any scanned source. Vanilla entries are under-indexed until the extract is completed or norbyte fills the gap.
- **Passive definitions are not only in Passive.txt.** InvocationsExpanded and others put PassiveData in many Stats files. The parser scans every `Stats/**/*.txt` and keeps `type "PassiveData"`.
- **CX_* passives have no stat block of their own.** Their buckets come from the passives they grant (`ExtraPassives` in cx_passive_manager.json), plus name tokens. Where a referenced passive is missing from the scan, the CX entry is tagged from what was found. CX_Magic_Boost and CX_Martial_Boost have no bucket hits and are not indexed.
- **StormWardensTomeOfSpells** is not in this run. Its PassiveFixes.txt holds one PassiveData entry. Add it to the source list if it should be indexed.
- **Load order.** All scanned sources are in modsettings.lsx (checked against the 64-entry load order). The "not in load order" rule dropped nothing.
- **Single-monster passives (scope rule 4).** Not applied. There is no reliable structural marker, so they were kept. The Races bucket covers the halfling/gnome-glove example.

## Scope decisions

- **Legendary (rule 2).** Dropped 85 entries: DeathMarch_LegendaryActions* and LegendaryResistance / Legendary_hook. **Judgment call:** MAG_Legendary_* magic-item passives were kept. They are item rarity, not monster legendary passives. Say if you want them dropped.
- **Visual/FX-only (rule 1).** Dropped 241 entries with no Boosts, StatsFunctors, or ToggleOnFunctors, and no name-token hit. Some are script-driven (UCL metamagic NPC variants, featsextra), so a few may be functional but invisible to this rule.
- **Duplicates.** 18 same-source duplicates removed (mostly UTUT).
- **Mechanics with no keyword hit.** 538 entries have mechanics but match none of the buckets. They are not indexed. Most are one-off monster or item logic.
- **UCL_IsXLevel_N progression helpers** get a Class or Subclass tag from the name only. They have no mechanics. Kept for the name hit.

## Classification rules

- **DamageTypes:** capitalised damage arguments only (`DealDamage(..., Fire)`, `Resistance(Fire)`, `DamageType.Fire`). Status IDs such as `CHARGED_LIGHTNING` are ignored.
- **Class / Subclass / SpellSchools / Races:** name tokens only. Races also match `Tagged('X')`. Status and ID names are not matched, because they caused heavy false hits (SHADOWHEART, GITHYANKI status names).
- **EnemyType:** name tokens or `Tagged('X')`.
- **MagicItemType:** item name tokens. Ranged Weapon also matches `IsRangedWeaponAttack`.
- **Type:** rough heuristics on mechanics (Boosts/StatsFunctors). This is the weakest group. See the trim notes.

## Largest buckets (trim targets)

- Type / Buff_Single: 185
- MagicItemType / Armor/Clothing: 65
- Type / Defense_SavingThrows: 52
- Type / Control_Single: 43 (includes Prone-status items; some false positives)
- Type / Defense_DamageResistance: 36
- MagicItemType / Gloves: 36
- Class / Druid: 36
- Type / Defense_ConditionImmunity: 35

Subclass / Shadow (21) and Light (11) are mostly name-token hits (UNI_HealInShadow, Shadowheart status names). They are noise.

## Spot-check (30 random entries against raw Stats)

About 25 of 30 were correct. Misses:
- ShadowTouched_Wisdom gets Subclass:Shadow from its name. It is a feat, not a subclass.
- MAG_HaHaHat_Passive gets Control_Single from the Prone condition, not from the item.
- Buff_Single over-tags any ActionResource or DamageBonus entry.

## Counts

- Kept after scope rules: 1,491 entries. 538 of them have no bucket hit and are not indexed.
- Indexed: 953 unique entries, 1,441 bucket memberships. Per-code memberships: BASE 780, UTUT 214, FEAT 111, DTHM 79, RAN 31, DEGR 25, EXEP 23, ENCO 20, SWTE 15, INVX 10, CXCX 133. 61 of 62 CX_* entries are indexed.

## Not changed

- keyword_to_spells.json
- guid_mapper_master.json
- cx_passive_manager.json

## FADE pass (2026-10-03)

- **Source:** 7 of 10 FADE_ equipment packs, all coded `FADE`: Sorcerer (CC), Cleric (FF), Druid (GG), Paladin (OO), Monk (UU), Rogue (VV), Wizard (WW). Ranger (BB), Bard (SS), and Warlock (PP) are excluded by Tyler's choice. Source path: `bg3-mod-extraction-utils/mods/FADE_*/`.
- **Result:** 249 raw PassiveData blocks, 108 unique indexed passives, 184 new memberships. Existing entries are unchanged, except for the one manual removal below.
- **Drops:** visual/FX-only went 241 to 261 (+20 FADE). Legendary (85) and same-source duplicates (18) are unchanged.
- **Load order:** six packs (CC, FF, GG, OO, UU, VV) are in the live `modsettings.lsx`. **WW (Wizard) is not enabled in the live load order.** Its pak sits in `Mods/`. Kept per Tyler's instruction. Its passives are not active in-game until the pack is enabled.
- **Classification:** name tokens and mechanics, as for the other sources. The packs' class prefixes (CC_, WW_, etc.) make Sorcerer, Wizard, and similar tags land correctly. Paladin lands under Subclass.
- **Manual edit preserved:** `DefaultStatus_BediTheBarbarian_AspectOfTheStallion [DTHM]` was removed from `Class:Barbarian` in the saved file, but the scripts still produce it. The rebuild reapplies that removal, so the map keeps it removed. Decide whether the script should carry the same exclusion.
