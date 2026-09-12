# MystraSpells + 5eSpells + Use5eSpellsWithMystrasSpells compatibility report

_Compiled from local extraction of the three active .pak mods (`MystrasSpells.pak`, `5eSpells.pak`, `Use5eSpellsWithMystrasSpells.pak`) in `bg3-mod-extraction-utils`, extracted to `mods/MystraSpells`, `mods/5eSpells`, `mods/Use5eSpellsWithMystraSpells`._

**Method.** Parsed every `type "SpellData"` block in each mod's `Stats/Generated/Data/*.txt`, and every `SpellList` in each mod's `Lists/SpellLists.lsx` (the list is what's actually offered on a class/level spellbook — it filters out internal helper variants like `_Default`, `_SneakAttack`, per-level upcast clones, and reaction/interrupt copies). A **"new spell"** = an entry with its own `SpellData` block that also appears on some class spell list (not just a vanilla spell the mod adds to one more class's list unchanged).

**Overlap has two distinct causes, and I checked for both:**
1. **Identical entry-ID collisions** — both mods independently define a `SpellData` block under the *exact same internal name* (e.g. both ship `"Shout_SwordBurst"`). BG3's stat loader does not merge these: whichever mod loads **later** in the load order silently wins, and the other mod's version of that spell is discarded entirely, game-wide. Detected by intersecting both mods' raw entry-ID sets.
2. **Different-ID, same real-world spell** — each mod ships its own separate implementation under a different internal name (e.g. Mystra's `Shout_FarStep` vs. 5eSpells' `Target_FarStep`, both "Far Step"). This doesn't silently break either spell, but without a fix both would appear twice in the Character Creation / level-up list. Detected via `Use5eSpellsWithMystrasSpells`'s own hard-coded `duplicatedSpellsLists` table in `ScriptExtender/Lua/U5EWM.lua`, which it subtracts from the merged vanilla `SpellList`s on load.

## 1. Spells in both mods, and how Use5eSpellsWithMystrasSpells remedies them

**Bottom line: 59 spells collide by identical ID, and the compatibility patch only addresses 7 of them.** The other 52 are a real, unaddressed conflict in your load order right now — for each one, whichever of MystraSpells / 5eSpells loads **later** silently wins and the earlier mod's version of that spell never functions, even though both mods think they granted it.

### 1a. Identical-ID collisions (the real conflict list)

| Spell | Entry ID (shared by both mods) | Level | School | Damage Type | Patch remedy |
|---|---|---|---|---|---|
| Create Bonfire | `Target_CreateBonfire` | Cantrip | Conjuration | Fire | NOT remedied (silent overwrite, load-order dependent) |
| Frostbite | `Target_Frostbite` | Cantrip | Evocation | Cold | NOT remedied (silent overwrite, load-order dependent) |
| Green-Flame Blade | `Target_GreenFlameBlade` | Cantrip | Evocation | Fire | NOT remedied (silent overwrite, load-order dependent) |
| Gust | `Target_Gust` | Cantrip | Transmutation | Force | NOT remedied (silent overwrite, load-order dependent) |
| Lightning Lure | `Target_LightningLure` | Cantrip | Evocation | Lightning | NOT remedied (silent overwrite, load-order dependent) |
| Prestidigitation | `Target_Prestidigitation` | Cantrip | Transmutation | - | NOT remedied (silent overwrite, load-order dependent) |
| Primal Savagery | `Target_PrimalSavagery` | Cantrip | Transmutation | Poison | NOT remedied (silent overwrite, load-order dependent) |
| Sword Burst | `Shout_SwordBurst` | Cantrip | Conjuration | Force | NOT remedied (silent overwrite, load-order dependent) |
| Thunderclap | `Shout_Thunderclap` | Cantrip | Evocation | Thunder | NOT remedied (silent overwrite, load-order dependent) |
| Word of Radiance | `Shout_WordOfRadiance` | Cantrip | Evocation | Radiant | NOT remedied (silent overwrite, load-order dependent) |
| Beast Bond | `Target_BeastBond` | 1st Level | Divination | - | NOT remedied (silent overwrite, load-order dependent) |
| Catapult | `Throw_Catapult` | 1st Level | Transmutation | Bludgeoning | NOT remedied (silent overwrite, load-order dependent) |
| Cause Fear | `Target_CauseFear` | 1st Level | Necromancy | - | NOT remedied (silent overwrite, load-order dependent) |
| Ceremony | `Target_Ceremony` | 1st Level | Evocation | - | NOT remedied (silent overwrite, load-order dependent) |
| Earth Tremor | `Shout_EarthTremor` | 1st Level | Evocation | Bludgeoning | NOT remedied (silent overwrite, load-order dependent) |
| Frost Fingers | `Zone_FrostFingers` | 1st Level | Evocation | Cold | NOT remedied (silent overwrite, load-order dependent) |
| Snare | `Target_Snare` | 1st Level | Abjuration | - | NOT remedied (silent overwrite, load-order dependent) |
| Tasha's Caustic Brew | `Zone_CausticBrew` | 1st Level | Evocation | Acid | NOT remedied (silent overwrite, load-order dependent) |
| Zephyr Strike | `Shout_ZephyrStrike` | 1st Level | Transmutation | - | NOT remedied (silent overwrite, load-order dependent) |
| Borrowed Knowledge | `Shout_BorrowedKnowledge` | 2nd Level | Divination | - | Compat stat replacement |
| Dragon's Breath | `Target_DragonsBreath` | 2nd Level | Transmutation | - | Compat stat replacement |
| Flock of Familiars | `Target_FlockOfFamiliars` | 2nd Level | Conjuration | Psychic | Compat stat replacement |
| Healing Spirit | `Target_HealingSpirit` | 2nd Level | Conjuration | - | NOT remedied (silent overwrite, load-order dependent) |
| Kinetic Jaunt | `Shout_KineticJaunt` | 2nd Level | Transmutation | - | NOT remedied (silent overwrite, load-order dependent) |
| Mind Spike | `Target_MindSpike` | 2nd Level | Divination | Psychic | NOT remedied (silent overwrite, load-order dependent) |
| Nathair's Mischief | `Target_NathairsMischief` | 2nd Level | Illusion | - | NOT remedied (silent overwrite, load-order dependent) |
| Pyrotechnics | `Target_Pyrotechnics` | 2nd Level | Transmutation | - | NOT remedied (silent overwrite, load-order dependent) |
| Summon Beast | `Target_SummonBeast` | 2nd Level | Conjuration | Acid | Compat stat replacement |
| Tasha's Mind Whip | `Target_MindWhip` | 2nd Level | Enchantment | Psychic | NOT remedied (silent overwrite, load-order dependent) |
| Vortex Warp | `Target_VortexWarp` | 2nd Level | Conjuration | - | NOT remedied (silent overwrite, load-order dependent) |
| Wither and Bloom | `Target_WitherAndBloom` | 2nd Level | Necromancy | Necrotic | NOT remedied (silent overwrite, load-order dependent) |
| Antagonize | `Target_Antagonize` | 3rd Level | Enchantment | Psychic | NOT remedied (silent overwrite, load-order dependent) |
| Ashardalon's Stride | `Shout_AshardalonsStride` | 3rd Level | Transmutation | Fire | NOT remedied (silent overwrite, load-order dependent) |
| Catnap | `Target_Catnap` | 3rd Level | Enchantment | - | NOT remedied (silent overwrite, load-order dependent) |
| Enemies Abound | `Target_EnemiesAbound` | 3rd Level | Enchantment | - | NOT remedied (silent overwrite, load-order dependent) |
| Erupting Earth | `Target_EruptingEarth` | 3rd Level | Transmutation | - | NOT remedied (silent overwrite, load-order dependent) |
| Flame Arrows | `Target_FlameArrows` | 3rd Level | Transmutation | Fire | NOT remedied (silent overwrite, load-order dependent) |
| Intellect Fortress | `Target_IntellectFortress` | 3rd Level | Enchantment | - | NOT remedied (silent overwrite, load-order dependent) |
| Life Transference | `Target_LifeTransference` | 3rd Level | Necromancy | - | NOT remedied (silent overwrite, load-order dependent) |
| Motivational Speech | `Target_MotivationalSpeech` | 3rd Level | Enchantment | - | NOT remedied (silent overwrite, load-order dependent) |
| Spirit Shroud | `Shout_SpiritShroud` | 3rd Level | Necromancy | - | Compat stat replacement |
| Summon Shadowspawn | `Target_SummonShadowspawn` | 3rd Level | Conjuration | Necrotic | Compat stat replacement |
| Thunder Step | `Teleportation_ThunderStep` | 3rd Level | Conjuration | - | NOT remedied (silent overwrite, load-order dependent) |
| Aura of Life | `Shout_AuraOfLife` | 4th Level | Abjuration | - | NOT remedied (silent overwrite, load-order dependent) |
| Charm Monster | `Target_CharmMonster` | 4th Level | Enchantment | - | NOT remedied (silent overwrite, load-order dependent) |
| Guardian of Nature | `Shout_GuardianOfNature` | 4th Level | Transmutation | - | NOT remedied (silent overwrite, load-order dependent) |
| Shadow of Moil | `Shout_ShadowOfMoil` | 4th Level | Necromancy | - | NOT remedied (silent overwrite, load-order dependent) |
| Storm Sphere | `Target_StormSphere` | 4th Level | Evocation | Bludgeoning | NOT remedied (silent overwrite, load-order dependent) |
| Summon Construct | `Target_SummonConstruct` | 4th Level | Conjuration | Necrotic | NOT remedied (silent overwrite, load-order dependent) |
| Summon Elemental | `Target_SummonElemental` | 4th Level | Conjuration | - | NOT remedied (silent overwrite, load-order dependent) |
| Vitriolic Sphere | `Projectile_VitriolicSphere` | 4th Level | Evocation | Acid | NOT remedied (silent overwrite, load-order dependent) |
| Holy Weapon | `Target_HolyWeapon` | 5th Level | Evocation | - | NOT remedied (silent overwrite, load-order dependent) |
| Maelstrom | `Target_Maelstrom` | 5th Level | Evocation | Bludgeoning | NOT remedied (silent overwrite, load-order dependent) |
| Negative Energy Flood | `Projectile_NegativeEnergyFlood` | 5th Level | Necromancy | Necrotic | NOT remedied (silent overwrite, load-order dependent) |
| Steel Wind Strike | `Target_SteelWindStrike` | 5th Level | Conjuration | Force | Lua list-dedup |
| Swift Quiver | `Shout_SwiftQuiver` | 5th Level | Transmutation | - | NOT remedied (silent overwrite, load-order dependent) |
| Synaptic Static | `Target_SynapticStatic` | 5th Level | Enchantment | Psychic | NOT remedied (silent overwrite, load-order dependent) |
| Tenser's Transformation | `Shout_TensersTransformation` | 6th Level | Transmutation | - | NOT remedied (silent overwrite, load-order dependent) |
| True Seeing | `Target_TrueSeeing` | 6th Level | Transmutation | - | NOT remedied (silent overwrite, load-order dependent) |

### 1b. Different-ID duplicates removed from spell lists by `U5EWM.lua`

| Spell | Level bucket | Removed entry | Removed from | Surviving entry | Surviving mod |
|---|---|---|---|---|---|
| Mystra's Booming Blade | Cantrip | `Target_BoomingBladeMove` | MystraSpells | _no counterpart found in current build — rule appears stale/vestigial_ | - |
| Infestation | Cantrip | `Projectile_Infestation` | MystraSpells | `Target_Infestation` | 5eSpells |
| Mind Sliver | Cantrip | `Projectile_MindSilver` | MystraSpells | `Target_MindSliver` | 5eSpells |
| Mold Earth | Cantrip | `Target_CreateDestroyMoldEarth` | MystraSpells | `Target_MoldEarth` | 5eSpells |
| Shape Water | Cantrip | `Target_ShapeWater_Container` | MystraSpells | `Target_ShapeWater` | 5eSpells |
| Magic Stone | Cantrip | `Shout_MagicStone` | MystraSpells | `Target_MagicStone` | 5eSpells |
| Absorb Elements | 1st | `Shout_AbsorbElementsSpell` | MystraSpells | `Shout_AbsorbElements` | 5eSpells |
| Chaos Bolt | 1st | `Projectile_ChaosBoltNew` | MystraSpells | `Target_ChaosBolt` | 5eSpells |
| Aganazzar's Scorcher | 2nd | `Zone_AganazzarScorcher` | MystraSpells | `Zone_AganazzarsScorcher` | 5eSpells |
| Dust Devil | 2nd | `Shout_DustDevil` | MystraSpells | `Target_DustDevil` | 5eSpells |
| Maximillian's Earthen Grasp | 2nd | `Target_EarthenGrasp` | MystraSpells | `Target_MaximiliansEarthenGrasp` | 5eSpells |
| Snilloc's Snowball Storm | 2nd | `Target_SnowballStorm` | MystraSpells | `Target_SnillocsSnowballStorm` | 5eSpells |
| Mystra's Shadow Blade | 2nd | `Shout_ShadowBlade_Spell` | MystraSpells | _no counterpart found in current build — rule appears stale/vestigial_ | - |
| Create Food and Water | 3rd | `Shout_CreateFoodAndWater` | MystraSpells | `Target_CreateFoodAndWater` | 5eSpells |
| Melf's Minute Meteors | 3rd | `Shout_MelfsMinuteMeteors` | MystraSpells | `Projectile_MinuteMeteors` | 5eSpells |
| Summon Fey | 3rd | `Target_SummonFey` | 5eSpells | `Target_SummonFey_Container` | MystraSpells |
| Water Walk | 3rd | `Shout_WaterWalk` | 5eSpells | `Target_WaterWalk` | MystraSpells |
| Arcane Eye | 4th | `Target_ArcaneEyeNew` | MystraSpells | `Target_ArcaneEye` | 5eSpells |
| Raulothim's Psychic Lance | 4th | `Target_PsychicLance` | MystraSpells | `Projectile_RaulothimsPsychicLance` | 5eSpells |
| Summon Aberration: Beholderkin | 4th | `Target_SummonBeholderkin` | 5eSpells | _no counterpart found in current build — rule appears stale/vestigial_ | - |
| Far Step | 5th | `Shout_FarStep` | MystraSpells | `Target_FarStep` | 5eSpells |
| None | 5th | `Target_SummonDraconicSpirit` | UNKNOWN | _no counterpart found in current build — rule appears stale/vestigial_ | - |

Notes: **Mystra's Booming Blade**'s removal is a no-op (5eSpells' Booming Blade isn't wired to any class list in the current build). **Summon Aberration: Beholderkin** and **Summon Draconic Spirit** removals are also no-ops (no current Mystra counterpart). **Mystra's Shadow Blade**'s survivor is base-game vanilla Shadow Blade (5eSpells just adds the existing vanilla spell to more class lists rather than reimplementing it).

### 1c. Mechanical/stat compatibility fixes (patch ships its own merged data)

Beyond list membership, these Summon-type (and Dust Devil/Magic Stone/Shape Water) families needed dedicated replacement stat blocks because the *mechanics* — not just the CC menu — conflicted between mods:

| Family | Root entry | Also an identical-ID collision? |
|---|---|---|
| Borrowed Knowledge | `Shout_BorrowedKnowledge` | Yes |
| Dragon's Breath | `Target_DragonsBreath` | Yes |
| Dust Devil | `Shout_DustDevil` | No (list-dedup only, see 1b) |
| Flock of Familiars | `Target_FlockOfFamiliars` | Yes |
| Magic Stone | `Shout_MagicStone` | No (list-dedup only, see 1b) |
| Shape Water | `Target_ShapeWater` | No (list-dedup only, see 1b) |
| Spirit Shroud | `Shout_SpiritShroud` | Yes |
| Summon Beast | `Target_SummonBeast` | Yes |
| Summon Fey | `Target_SummonFey_Container` | No (list-dedup only, see 1b) |
| Summon Shadowspawn | `Target_SummonShadowspawn` | Yes |

**Total unique real-world spells confirmed in both mods: 81** (59 identical-ID collisions + 22 different-ID duplicates).

## 2. Spells unique to each mod (no overlap)

After removing every spell involved in section 1: MystraSpells has **56** truly unique new spells, 5eSpells has **37**.

### MystraSpells — unique (56)

| Spell | Entry ID | Level | School | Damage/Utility | Uses spell slot | Classes granted to |
|---|---|---|---|---|---|---|
| Hand of Radiance | `Shout_HandOfRadiance` | Cantrip | Evocation | Radiant | No (cantrip/ritual) | Bard, Cleric |
| Larloch's Minor Drain | `Projectile_LarlochsMinorDrain` | Cantrip | Necromancy | Necrotic | No (cantrip/ritual) | Bard, Cleric, Fighter (Eldritch Knight), Sorcerer, Wizard |
| Sapping Sting | `Projectile_SappingSting` | Cantrip | Necromancy | Necrotic | No (cantrip/ritual) | Bard, Cleric, Fighter (Eldritch Knight), Wizard |
| Gift of Alacrity | `Target_GiftOfAlacrity` | 1st Level | Divination | Buff/Utility | Yes | Bard, Cleric, Ritual Caster Feat NEW, Wizard |
| Sudden Awakening | `Target_SuddenAwakening` | 1st Level | Enchantment | Buff/Utility | Yes | Bard, Ranger, Rogue (Arcane Trickster), Sorcerer, Warlock (Archfey), Warlock (Great Old One), Wizard |
| Id Insinuation | `Target_IdInsinuation` | 1st Level | Enchantment | Psychic | Yes | Bard, Rogue (Arcane Trickster), Sorcerer, Warlock (Archfey), Warlock (Fiend), Warlock (Great Old One), Warlock (Hexblade), Wizard |
| Acid Stream | `Zone_AcidStream` | 1st Level | Evocation | Acid | Yes | Bard, Fighter (Eldritch Knight), Sorcerer, Wizard |
| Jim's Magic Missile | `Shout_MagicMissile_Jim` | 1st Level | Evocation | Buff/Utility | Yes | Bard, Fighter (Eldritch Knight), Wizard |
| Magnify Gravity | `Target_MagnifyGravity` | 1st Level | Transmutation | Force | Yes | Bard, Warlock (Great Old One), Wizard |
| Mental Barrier | `Shout_MentalBarrier` | 2nd Level | Abjuration | Buff/Utility | Yes | Bard, Fighter (Eldritch Knight), Sorcerer, Warlock (Archfey), Warlock (Fiend), Warlock (Great Old One), Warlock (Hexblade), Wizard |
| Healing Elixir | `Target_HealingElixir` | 2nd Level | Conjuration | Buff/Utility | Yes | Bard, Warlock (Archfey), Warlock (Fiend), Warlock (Great Old One), Warlock (Hexblade), Wizard |
| Spray of Cards | `Zone_SprayOfCards` | 2nd Level | Conjuration | Debuff/Control | Yes | Bard, Sorcerer, Warlock (Archfey), Warlock (Fiend), Warlock (Great Old One), Warlock (Hexblade), Wizard |
| Summon Moonblade | `Shout_SummonMoonblade_Container` | 2nd Level | Conjuration | Summon | Yes | Bard, Sorcerer, Warlock (Great Old One), Wizard |
| Silvery Barbs | `Target_SilveryBarbs` | 2nd Level | Enchantment | Buff/Utility | Yes | Bard, Rogue (Arcane Trickster), Sorcerer, Wizard |
| Jim's Glowing Coin | `Projectile_GlowingCoin_Jim` | 2nd Level | Enchantment | Debuff/Control | Yes | Bard, Rogue (Arcane Trickster), Wizard |
| Bestial Growth | `Shout_BeastAspect` | 2nd Level | Transmutation | Buff/Utility | Yes | Bard, Druid, Sorcerer, Wizard |
| Force Weapon | `Target_ForceWeapon` | 2nd Level | Transmutation | Buff/Utility | Yes | Bard, Cleric, Paladin, Ranger, Sorcerer, Warlock (Hexblade), Wizard |
| Earthbind | `Target_Earthbind` | 2nd Level | Transmutation | Debuff/Control | Yes | Bard, Cleric, Druid, Sorcerer, Warlock (Archfey), Warlock (Fiend), Warlock (Great Old One), Warlock (Hexblade), Wizard |
| Volley of Arrows | `Projectile_VolleyOfArrows` | 2nd Level | Transmutation | Piercing | Yes | Bard, Ranger |
| Freedom of the Waves | `Target_FreedomOfTheWaves` | 3rd Level | Conjuration | Debuff/Control | Yes | Bard, Druid, Sorcerer |
| Tidal Wave | `Target_TidalWave` | 3rd Level | Conjuration | Debuff/Control | Yes | Bard, Druid, Sorcerer, Wizard |
| Summon Lesser Demons | `Target_SummonLesserDemons` | 3rd Level | Conjuration | Psychic | Yes | Bard, Warlock (Archfey), Warlock (Fiend), Warlock (Great Old One), Warlock (Hexblade), Wizard |
| Sense Vitals | `Shout_SenseVitals` | 3rd Level | Divination | Buff/Utility | Yes | Bard, Ranger |
| Incite Greed | `Shout_InciteGreed` | 3rd Level | Enchantment | Debuff/Control | Yes | Bard, Cleric, Sorcerer, Warlock (Archfey), Warlock (Fiend), Warlock (Great Old One), Warlock (Hexblade), Wizard |
| Blind Faith | `Shout_BlindFaith` | 3rd Level | Evocation | Buff/Utility | Yes | Cleric, Paladin |
| Psionic Blast | `Zone_PsionicBlast` | 3rd Level | Evocation | Force | Yes | Bard, Sorcerer, Warlock (Archfey), Warlock (Fiend), Warlock (Great Old One), Warlock (Hexblade), Wizard |
| Pulse Wave | `Zone_PulseWave` | 3rd Level | Evocation | Force | Yes | Bard, Wizard |
| Discordant Melody | `Shout_DiscordantMelody` | 3rd Level | Evocation | Thunder | Yes | Bard |
| Venomous Barbs | `Target_VenomousBarbs` | 3rd Level | Transmutation | Buff/Utility | Yes | Bard, Druid, Ranger |
| Aura of Purity | `Shout_AuraOfPurity` | 4th Level | Abjuration | Buff/Utility | Yes | Bard, Cleric |
| Summon Aberration | `Target_SummonAberration` | 4th Level | Conjuration | Acid | Yes | Bard, Warlock (Archfey), Warlock (Fiend), Warlock (Great Old One), Warlock (Hexblade), Wizard |
| Summon Greater Demon | `Target_SummonGreaterDemon` | 4th Level | Conjuration | Fire | Yes | Bard, Warlock (Archfey), Warlock (Fiend), Warlock (Great Old One), Warlock (Hexblade), Wizard |
| Ego Whip | `Target_EgoWhip` | 4th Level | Enchantment | Debuff/Control | Yes | Bard, Druid, Warlock (Archfey), Warlock (Fiend), Warlock (Great Old One), Warlock (Hexblade), Wizard |
| Mesmer's Lullaby | `Shout_MesmersLullaby` | 4th Level | Enchantment | Debuff/Control | Yes | Bard, Warlock (Archfey) |
| Dream | `Target_DreamSleep` | 4th Level | Enchantment | Psychic | Yes | Bard, Sorcerer, Warlock (Archfey), Warlock (Fiend), Warlock (Great Old One), Warlock (Hexblade), Wizard |
| Web of Fire | `Projectile_WebOfFire` | 4th Level | Evocation | Fire | Yes | Bard, Cleric, Warlock (Fiend), Wizard |
| Gravity Sinkhole | `Target_GravitySinkhole` | 4th Level | Evocation | Force | Yes | Bard, Warlock (Great Old One), Wizard |
| Illusory Weapon | `Target_IllusoryWeapon` | 4th Level | Illusion | Buff/Utility | Yes | Bard, Cleric, Sorcerer, Warlock (Hexblade), Wizard |
| Control Water | `Target_ControlWater_Container` | 4th Level | Transmutation | Buff/Utility | Yes | Bard, Cleric, Druid, Sorcerer, Wizard |
| Stone Shape | `Target_StoneShape_Container` | 4th Level | Transmutation | Buff/Utility | Yes | Bard, Cleric, Druid, Wizard |
| Elemental Bane | `Target_ElementalBane` | 4th Level | Transmutation | Debuff/Control | Yes | Bard, Druid, Warlock (Archfey), Warlock (Fiend), Warlock (Great Old One), Warlock (Hexblade), Wizard |
| Astral Disjunction | `Target_AstralDisjunction` | 5th Level | Abjuration | Buff/Utility | Yes | Bard, Warlock (Great Old One), Wizard |
| Bigby's Hand | `Target_BigbyHand` | 5th Level | Conjuration | Buff/Utility | Yes | Bard, Sorcerer, Wizard |
| Infernal Calling | `Target_InfernalCalling` | 5th Level | Conjuration | Fire | Yes | Bard, Warlock (Archfey), Warlock (Fiend), Warlock (Great Old One), Warlock (Hexblade), Wizard |
| Summon Draconic Spirit | `Target_SummonDragon` | 5th Level | Conjuration | Fire | Yes | Bard, Druid, Sorcerer, Wizard |
| Immolation | `Target_Immolation` | 5th Level | Evocation | Fire | Yes | Bard, Cleric, Sorcerer, Warlock (Fiend), Wizard |
| Danse Macabre | `Target_DanseMacabre_Container` | 5th Level | Necromancy | Necrotic | Yes | Bard, Warlock (Archfey), Warlock (Fiend), Warlock (Great Old One), Warlock (Hexblade), Wizard |
| Enervation | `Projectile_Enervation` | 5th Level | Necromancy | Necrotic | Yes | Bard, Sorcerer, Warlock (Archfey), Warlock (Fiend), Warlock (Great Old One), Warlock (Hexblade), Wizard |
| Macabre Explosion | `Target_MacabreExplosion` | 5th Level | Necromancy | Necrotic | Yes | Bard, Sorcerer, Warlock (Archfey), Warlock (Fiend), Warlock (Great Old One), Warlock (Hexblade), Wizard |
| Primordial Ward | `Shout_PrimordialWard` | 6th Level | Abjuration | Buff/Utility | Yes | Bard, Druid |
| Conjure Fey | `Target_ConjureFey` | 6th Level | Conjuration | Acid | Yes | Druid, Warlock |
| Psychic Crush | `Target_PsychicCrush` | 6th Level | Enchantment | Psychic | Yes | Bard, Sorcerer, Warlock, Wizard |
| Fissure | `Zone_Fissure` | 6th Level | Evocation | Force | Yes | Druid, Wizard |
| Elemental Investiture | `Shout_ElementalInvestiture` | 6th Level | Transmutation | Buff/Utility | Yes | Druid, Warlock, Wizard |
| Lesser Regeneration | `Target_LesserRegenerate` | 6th Level | Transmutation | Healing | Yes | Cleric, Druid |
| Moonflare | `Projectile_Moonflare` | None | Evocation | Radiant | No (cantrip/ritual) | Bard, Cleric, Druid, SpellSniperAttackSpells NEW |

### 5eSpells — unique (37)

| Spell | Entry ID | Level | School | Damage/Utility | Uses spell slot | Classes granted to |
|---|---|---|---|---|---|---|
| Control Flames | `Target_ControlFlames` | Cantrip | Transmutation | Buff/Utility | No (cantrip/ritual) | Bard, Druid, Sorcerer, Wizard |
| Druidcraft | `Shout_Druidcraft` | Cantrip | Transmutation | Buff/Utility | No (cantrip/ritual) | Bard, Druid |
| Unseen Servant | `Target_UnseenServant` | 1st Level | Conjuration | Buff/Utility | Yes | Bard, Warlock (Archfey), Warlock (Fiend), Warlock (Great Old One), Warlock (Hexblade), Wizard |
| Unseen Servant: Ritual | `Target_UnseenServant_Ritual` | 1st Level | Conjuration | Buff/Utility | No (cantrip/ritual) | Ritual Caster Feat |
| Detect Evil and Good | `Shout_DetectEvilAndGood` | 1st Level | Divination | Buff/Utility | Yes | Bard, Cleric, Paladin |
| Detect Magic | `Shout_DetectMagic` | 1st Level | Divination | Buff/Utility | Yes | Bard, Cleric, Druid, Paladin, Ranger, Sorcerer, Wizard |
| Detect Magic: Ritual | `Shout_DetectMagic_Ritual` | 1st Level | Divination | Buff/Utility | No (cantrip/ritual) | Ritual Caster Feat |
| Ceremony: Ritual | `Target_Ceremony_Ritual` | 1st Level | Evocation | Buff/Utility | No (cantrip/ritual) | Ritual Caster Feat |
| Find Traps | `Shout_FindTraps` | 2nd Level | Divination | Buff/Utility | Yes | Bard, Cleric, Druid, Ranger |
| Zone of Truth | `Target_ZoneofTruth` | 2nd Level | Enchantment | Buff/Utility | Yes | Bard, Cleric, Paladin |
| Continual Flame | `Target_ContinualFlame` | 2nd Level | Evocation | Buff/Utility | Yes | Bard, Cleric, Druid, Fighter (Eldritch Knight), Wizard |
| Warding Wind | `Shout_WardingWind` | 2nd Level | Evocation | Buff/Utility | Yes | Bard, Druid, Fighter (Eldritch Knight), Sorcerer, Wizard |
| Rime's Binding Ice | `Zone_RimesBindingIce` | 2nd Level | Evocation | Cold | Yes | Bard, Fighter (Eldritch Knight), Sorcerer, Wizard |
| Gentle Repose | `Target_GentleRepose` | 2nd Level | Necromancy | Buff/Utility | Yes | Bard, Cleric, Paladin, Wizard |
| Alter Self | `Shout_AlterSelf` | 2nd Level | Transmutation | Buff/Utility | Yes | Bard, Sorcerer, Wizard |
| Magic Circle | `Target_MagicCircle` | 3rd Level | Abjuration | Buff/Utility | Yes | Bard, Cleric, Fighter (Eldritch Knight), Paladin, Warlock (Archfey), Warlock (Fiend), Warlock (Great Old One), Warlock (Hexblade), Wizard |
| Nondetection | `Target_Nondetection` | 3rd Level | Abjuration | Buff/Utility | Yes | Bard, Fighter (Eldritch Knight), Ranger, Wizard |
| Conjure Animals | `Target_ConjureAnimals_Container` | 3rd Level | Conjuration | Buff/Utility | Yes | Bard, Druid, Ranger |
| Antilife Shell | `Shout_AntilifeShell` | 5th Level | Abjuration | Buff/Utility | Yes | Bard, Druid |
| Circle of Power | `Shout_CircleOfPower` | 5th Level | Abjuration | Buff/Utility | Yes | Bard, Paladin |
| Teleportation Circle | `Teleportation_TeleportationCircle` | 5th Level | Conjuration | Buff/Utility | Yes | Bard, Sorcerer, Warlock (Archfey), Warlock (Fiend), Warlock (Great Old One), Warlock (Hexblade), Wizard |
| Conjure Volley | `ProjectileStrike_ConjureVolley` | 5th Level | Conjuration | Debuff/Control | Yes | Bard, Ranger |
| Commune with Nature | `Shout_CommuneWithNature` | 5th Level | Divination | Buff/Utility | Yes | Bard, Druid, Ranger |
| Dawn | `Target_Dawn` | 5th Level | Evocation | Radiant | Yes | Bard, Cleric, Wizard |
| Mislead | `Target_Mislead` | 5th Level | Illusion | Buff/Utility | Yes | Bard, Warlock (Archfey), Warlock (Fiend), Warlock (Great Old One), Warlock (Hexblade), Wizard |
| Raise Dead | `Target_RaiseDead` | 5th Level | Necromancy | Buff/Utility | Yes | Bard, Cleric, Paladin |
| Skill Empowerment | `Target_SkillEmpowerment` | 5th Level | Transmutation | Buff/Utility | Yes | Bard, Sorcerer, Wizard |
| Finger of Death | `Target_FingerOfDeath` | 7th Level | Necromancy | Necrotic | Yes | Bard, Sorcerer, Warlock, Wizard |
| Regenerate | `Target_Regenerate` | 7th Level | Transmutation | Healing | Yes | Bard, Cleric, Druid |
| Holy Aura | `Shout_HolyAura` | 8th Level | Abjuration | Buff/Utility | Yes | Bard, Cleric |
| Mind Blank | `Target_MindBlank` | 8th Level | Abjuration | Buff/Utility | Yes | Bard, Wizard |
| Feeblemind | `Target_Feeblemind` | 8th Level | Enchantment | Buff/Utility | Yes | Bard, Druid, Warlock, Wizard |
| Dominate Monster | `Target_DominateMonster` | 8th Level | Enchantment | Debuff/Control | Yes | Bard, Sorcerer, Warlock, Wizard |
| Foresight | `Target_Foresight` | 9th Level | Divination | Buff/Utility | Yes | Bard, Druid, Warlock, Wizard |
| Power Word: Kill | `Target_PowerWordKill` | 9th Level | Enchantment | Buff/Utility | Yes | Bard, Sorcerer, Warlock, Wizard |
| Power Word: Heal | `Target_PowerWordHeal` | 9th Level | Evocation | Healing | Yes | Bard, Cleric |
| Spare the Dying | `Target_SpareTheDying` | None | - | Buff/Utility | No (cantrip/ritual) | Bard, Cleric |

## 3. Slot-castability

From each spell's resolved `UseCosts` (same underlying data bg3.norbyte.dev's `type:spell` search reflects). A `SpellSlotsGroup:` cost means it needs a real spell-slot resource and can be granted via CX's normal spell-slot pipeline. Without it — every cantrip and ritual below — the spell is action-point-only; granting it to a creature via a slot-based mechanism will silently do nothing, it must be granted as an at-will/innate cast.

### MystraSpells: 115 slot-cost / 20 no-slot (cantrip or ritual)

- `Target_CreateBonfire` — **Create Bonfire** (Conjuration)
- `Target_Frostbite` — **Frostbite** (Evocation)
- `Target_GreenFlameBlade` — **Green-Flame Blade** (Evocation)
- `Target_Gust` — **Gust** (Transmutation)
- `Shout_HandOfRadiance` — **Hand of Radiance** (Evocation)
- `Projectile_Infestation` — **Infestation** (Conjuration)
- `Projectile_LarlochsMinorDrain` — **Larloch's Minor Drain** (Necromancy)
- `Target_LightningLure` — **Lightning Lure** (Evocation)
- `Shout_MagicStone` — **Magic Stone** (Transmutation)
- `Projectile_MindSilver` — **Mind Sliver** (Enchantment)
- `Target_CreateDestroyMoldEarth` — **Mold Earth** (Transmutation)
- `Projectile_Moonflare` — **Moonflare** (Evocation)
- `Target_BoomingBladeMove` — **Mystra's Booming Blade** (Evocation)
- `Target_Prestidigitation` — **Prestidigitation** (Transmutation)
- `Target_PrimalSavagery` — **Primal Savagery** (Transmutation)
- `Projectile_SappingSting` — **Sapping Sting** (Necromancy)
- `Target_ShapeWater_Container` — **Shape Water** (Transmutation)
- `Shout_SwordBurst` — **Sword Burst** (Conjuration)
- `Shout_Thunderclap` — **Thunderclap** (Evocation)
- `Shout_WordOfRadiance` — **Word of Radiance** (Evocation)

### 5eSpells: 94 slot-cost / 21 no-slot (cantrip or ritual)

- `Target_Ceremony_Ritual` — **Ceremony: Ritual** (Evocation)
- `Target_ControlFlames` — **Control Flames** (Transmutation)
- `Target_CreateBonfire` — **Create Bonfire** (Conjuration)
- `Shout_DetectMagic_Ritual` — **Detect Magic: Ritual** (Divination)
- `Shout_Druidcraft` — **Druidcraft** (Transmutation)
- `Target_Frostbite` — **Frostbite** (Evocation)
- `Target_GreenFlameBlade` — **Green-Flame Blade** (Evocation)
- `Target_Gust` — **Gust** (Transmutation)
- `Target_Infestation` — **Infestation** (Conjuration)
- `Target_LightningLure` — **Lightning Lure** (Evocation)
- `Target_MagicStone` — **Magic Stone** (Transmutation)
- `Target_MindSliver` — **Mind Sliver** (Enchantment)
- `Target_MoldEarth` — **Mold Earth** (Transmutation)
- `Target_Prestidigitation` — **Prestidigitation** (Transmutation)
- `Target_PrimalSavagery` — **Primal Savagery** (Transmutation)
- `Target_ShapeWater` — **Shape Water** (Transmutation)
- `Target_SpareTheDying` — **Spare the Dying** (?)
- `Shout_SwordBurst` — **Sword Burst** (Conjuration)
- `Shout_Thunderclap` — **Thunderclap** (Evocation)
- `Target_UnseenServant_Ritual` — **Unseen Servant: Ritual** (Conjuration)
- `Shout_WordOfRadiance` — **Word of Radiance** (Evocation)

## 5. All spells (both mods, deduplicated), sorted by Level -> School -> Damage/Utility Type

Total deduplicated catalog: **173** spells.

| Spell | Entry ID | Mod | Level | School | Damage/Utility | Slot? |
|---|---|---|---|---|---|---|
| Sword Burst | `Shout_SwordBurst` | Both (ID collision) | Cantrip | Conjuration | Force | No |
| Infestation | `Target_Infestation` | 5eSpells [shared] | Cantrip | Conjuration | Poison | No |
| Mind Sliver | `Target_MindSliver` | 5eSpells [shared] | Cantrip | Enchantment | Debuff/Control | No |
| Frostbite | `Target_Frostbite` | Both (ID collision) | Cantrip | Evocation | Cold | No |
| Green-Flame Blade | `Target_GreenFlameBlade` | Both (ID collision) | Cantrip | Evocation | Fire | No |
| Lightning Lure | `Target_LightningLure` | Both (ID collision) | Cantrip | Evocation | Lightning | No |
| Hand of Radiance | `Shout_HandOfRadiance` | MystraSpells | Cantrip | Evocation | Radiant | No |
| Word of Radiance | `Shout_WordOfRadiance` | Both (ID collision) | Cantrip | Evocation | Radiant | No |
| Mystra's Booming Blade | `Target_BoomingBladeMove` | MystraSpells [shared] | Cantrip | Evocation | Thunder | No |
| Thunderclap | `Shout_Thunderclap` | Both (ID collision) | Cantrip | Evocation | Thunder | No |
| Larloch's Minor Drain | `Projectile_LarlochsMinorDrain` | MystraSpells | Cantrip | Necromancy | Necrotic | No |
| Sapping Sting | `Projectile_SappingSting` | MystraSpells | Cantrip | Necromancy | Necrotic | No |
| Control Flames | `Target_ControlFlames` | 5eSpells | Cantrip | Transmutation | Buff/Utility | No |
| Druidcraft | `Shout_Druidcraft` | 5eSpells | Cantrip | Transmutation | Buff/Utility | No |
| Magic Stone | `Target_MagicStone` | 5eSpells [shared] | Cantrip | Transmutation | Buff/Utility | No |
| Mold Earth | `Target_MoldEarth` | 5eSpells [shared] | Cantrip | Transmutation | Buff/Utility | No |
| Prestidigitation | `Target_Prestidigitation` | Both (ID collision) | Cantrip | Transmutation | Buff/Utility | No |
| Shape Water | `Target_ShapeWater` | 5eSpells [shared] | Cantrip | Transmutation | Buff/Utility | No |
| Gust | `Target_Gust` | Both (ID collision) | Cantrip | Transmutation | Force | No |
| Primal Savagery | `Target_PrimalSavagery` | Both (ID collision) | Cantrip | Transmutation | Poison | No |
| Absorb Elements | `Shout_AbsorbElements` | 5eSpells [shared] | 1st Level | Abjuration | Buff/Utility | Yes |
| Snare | `Target_Snare` | Both (ID collision) | 1st Level | Abjuration | Debuff/Control | Yes |
| Unseen Servant | `Target_UnseenServant` | 5eSpells | 1st Level | Conjuration | Buff/Utility | Yes |
| Unseen Servant: Ritual | `Target_UnseenServant_Ritual` | 5eSpells | 1st Level | Conjuration | Buff/Utility | No |
| Beast Bond | `Target_BeastBond` | Both (ID collision) | 1st Level | Divination | Buff/Utility | Yes |
| Detect Evil and Good | `Shout_DetectEvilAndGood` | 5eSpells | 1st Level | Divination | Buff/Utility | Yes |
| Detect Magic | `Shout_DetectMagic` | 5eSpells | 1st Level | Divination | Buff/Utility | Yes |
| Detect Magic: Ritual | `Shout_DetectMagic_Ritual` | 5eSpells | 1st Level | Divination | Buff/Utility | No |
| Gift of Alacrity | `Target_GiftOfAlacrity` | MystraSpells | 1st Level | Divination | Buff/Utility | Yes |
| Sudden Awakening | `Target_SuddenAwakening` | MystraSpells | 1st Level | Enchantment | Buff/Utility | Yes |
| Id Insinuation | `Target_IdInsinuation` | MystraSpells | 1st Level | Enchantment | Psychic | Yes |
| Acid Stream | `Zone_AcidStream` | MystraSpells | 1st Level | Evocation | Acid | Yes |
| Tasha's Caustic Brew | `Zone_CausticBrew` | Both (ID collision) | 1st Level | Evocation | Acid | Yes |
| Earth Tremor | `Shout_EarthTremor` | Both (ID collision) | 1st Level | Evocation | Bludgeoning | Yes |
| Ceremony: Ritual | `Target_Ceremony_Ritual` | 5eSpells | 1st Level | Evocation | Buff/Utility | No |
| Chaos Bolt | `Target_ChaosBolt` | 5eSpells [shared] | 1st Level | Evocation | Buff/Utility | Yes |
| Jim's Magic Missile | `Shout_MagicMissile_Jim` | MystraSpells | 1st Level | Evocation | Buff/Utility | Yes |
| Frost Fingers | `Zone_FrostFingers` | Both (ID collision) | 1st Level | Evocation | Cold | Yes |
| Ceremony | `Target_Ceremony` | Both (ID collision) | 1st Level | Evocation | Debuff/Control | Yes |
| Cause Fear | `Target_CauseFear` | Both (ID collision) | 1st Level | Necromancy | Debuff/Control | Yes |
| Zephyr Strike | `Shout_ZephyrStrike` | Both (ID collision) | 1st Level | Transmutation | Buff/Utility | Yes |
| Catapult | `Throw_Catapult` | Both (ID collision) | 1st Level | Transmutation | Debuff/Control | Yes |
| Magnify Gravity | `Target_MagnifyGravity` | MystraSpells | 1st Level | Transmutation | Force | Yes |
| Mental Barrier | `Shout_MentalBarrier` | MystraSpells | 2nd Level | Abjuration | Buff/Utility | Yes |
| Summon Beast | `Target_SummonBeast` | Both (ID collision) | 2nd Level | Conjuration | Acid | Yes |
| Dust Devil | `Target_DustDevil` | 5eSpells [shared] | 2nd Level | Conjuration | Buff/Utility | Yes |
| Healing Elixir | `Target_HealingElixir` | MystraSpells | 2nd Level | Conjuration | Buff/Utility | Yes |
| Healing Spirit | `Target_HealingSpirit` | Both (ID collision) | 2nd Level | Conjuration | Buff/Utility | Yes |
| Spray of Cards | `Zone_SprayOfCards` | MystraSpells | 2nd Level | Conjuration | Debuff/Control | Yes |
| Vortex Warp | `Target_VortexWarp` | Both (ID collision) | 2nd Level | Conjuration | Debuff/Control | Yes |
| Flock of Familiars | `Target_FlockOfFamiliars` | Both (ID collision) | 2nd Level | Conjuration | Psychic | Yes |
| Summon Moonblade | `Shout_SummonMoonblade_Container` | MystraSpells | 2nd Level | Conjuration | Summon | Yes |
| Borrowed Knowledge | `Shout_BorrowedKnowledge` | Both (ID collision) | 2nd Level | Divination | Buff/Utility | Yes |
| Find Traps | `Shout_FindTraps` | 5eSpells | 2nd Level | Divination | Buff/Utility | Yes |
| Mind Spike | `Target_MindSpike` | Both (ID collision) | 2nd Level | Divination | Psychic | Yes |
| Silvery Barbs | `Target_SilveryBarbs` | MystraSpells | 2nd Level | Enchantment | Buff/Utility | Yes |
| Zone of Truth | `Target_ZoneofTruth` | 5eSpells | 2nd Level | Enchantment | Buff/Utility | Yes |
| Jim's Glowing Coin | `Projectile_GlowingCoin_Jim` | MystraSpells | 2nd Level | Enchantment | Debuff/Control | Yes |
| Tasha's Mind Whip | `Target_MindWhip` | Both (ID collision) | 2nd Level | Enchantment | Psychic | Yes |
| Continual Flame | `Target_ContinualFlame` | 5eSpells | 2nd Level | Evocation | Buff/Utility | Yes |
| Warding Wind | `Shout_WardingWind` | 5eSpells | 2nd Level | Evocation | Buff/Utility | Yes |
| Rime's Binding Ice | `Zone_RimesBindingIce` | 5eSpells | 2nd Level | Evocation | Cold | Yes |
| Snilloc's Snowball Storm | `Target_SnillocsSnowballStorm` | 5eSpells [shared] | 2nd Level | Evocation | Debuff/Control | Yes |
| Aganazzar's Scorcher | `Zone_AganazzarsScorcher` | 5eSpells [shared] | 2nd Level | Evocation | Fire | Yes |
| Mystra's Shadow Blade | `Shout_ShadowBlade_Spell` | MystraSpells [shared] | 2nd Level | Illusion | Buff/Utility | Yes |
| Nathair's Mischief | `Target_NathairsMischief` | Both (ID collision) | 2nd Level | Illusion | Debuff/Control | Yes |
| Gentle Repose | `Target_GentleRepose` | 5eSpells | 2nd Level | Necromancy | Buff/Utility | Yes |
| Wither and Bloom | `Target_WitherAndBloom` | Both (ID collision) | 2nd Level | Necromancy | Necrotic | Yes |
| Maximilian's Earthen Grasp | `Target_MaximiliansEarthenGrasp` | 5eSpells [shared] | 2nd Level | Transmutation | Bludgeoning | Yes |
| Alter Self | `Shout_AlterSelf` | 5eSpells | 2nd Level | Transmutation | Buff/Utility | Yes |
| Bestial Growth | `Shout_BeastAspect` | MystraSpells | 2nd Level | Transmutation | Buff/Utility | Yes |
| Dragon's Breath | `Target_DragonsBreath` | Both (ID collision) | 2nd Level | Transmutation | Buff/Utility | Yes |
| Force Weapon | `Target_ForceWeapon` | MystraSpells | 2nd Level | Transmutation | Buff/Utility | Yes |
| Kinetic Jaunt | `Shout_KineticJaunt` | Both (ID collision) | 2nd Level | Transmutation | Buff/Utility | Yes |
| Earthbind | `Target_Earthbind` | MystraSpells | 2nd Level | Transmutation | Debuff/Control | Yes |
| Pyrotechnics | `Target_Pyrotechnics` | Both (ID collision) | 2nd Level | Transmutation | Debuff/Control | Yes |
| Volley of Arrows | `Projectile_VolleyOfArrows` | MystraSpells | 2nd Level | Transmutation | Piercing | Yes |
| Magic Circle | `Target_MagicCircle` | 5eSpells | 3rd Level | Abjuration | Buff/Utility | Yes |
| Nondetection | `Target_Nondetection` | 5eSpells | 3rd Level | Abjuration | Buff/Utility | Yes |
| Conjure Animals | `Target_ConjureAnimals_Container` | 5eSpells | 3rd Level | Conjuration | Buff/Utility | Yes |
| Create Food and Water | `Target_CreateFoodAndWater` | 5eSpells [shared] | 3rd Level | Conjuration | Buff/Utility | Yes |
| Thunder Step | `Teleportation_ThunderStep` | Both (ID collision) | 3rd Level | Conjuration | Buff/Utility | Yes |
| Freedom of the Waves | `Target_FreedomOfTheWaves` | MystraSpells | 3rd Level | Conjuration | Debuff/Control | Yes |
| Tidal Wave | `Target_TidalWave` | MystraSpells | 3rd Level | Conjuration | Debuff/Control | Yes |
| Summon Shadowspawn | `Target_SummonShadowspawn` | Both (ID collision) | 3rd Level | Conjuration | Necrotic | Yes |
| Summon Lesser Demons | `Target_SummonLesserDemons` | MystraSpells | 3rd Level | Conjuration | Psychic | Yes |
| Summon Fey | `Target_SummonFey_Container` | MystraSpells [shared] | 3rd Level | Conjuration | Summon | Yes |
| Sense Vitals | `Shout_SenseVitals` | MystraSpells | 3rd Level | Divination | Buff/Utility | Yes |
| Catnap | `Target_Catnap` | Both (ID collision) | 3rd Level | Enchantment | Buff/Utility | Yes |
| Enemies Abound | `Target_EnemiesAbound` | Both (ID collision) | 3rd Level | Enchantment | Buff/Utility | Yes |
| Intellect Fortress | `Target_IntellectFortress` | Both (ID collision) | 3rd Level | Enchantment | Buff/Utility | Yes |
| Motivational Speech | `Target_MotivationalSpeech` | Both (ID collision) | 3rd Level | Enchantment | Buff/Utility | Yes |
| Incite Greed | `Shout_InciteGreed` | MystraSpells | 3rd Level | Enchantment | Debuff/Control | Yes |
| Antagonize | `Target_Antagonize` | Both (ID collision) | 3rd Level | Enchantment | Psychic | Yes |
| Blind Faith | `Shout_BlindFaith` | MystraSpells | 3rd Level | Evocation | Buff/Utility | Yes |
| Minute Meteors | `Projectile_MinuteMeteors` | 5eSpells [shared] | 3rd Level | Evocation | Buff/Utility | Yes |
| Psionic Blast | `Zone_PsionicBlast` | MystraSpells | 3rd Level | Evocation | Force | Yes |
| Pulse Wave | `Zone_PulseWave` | MystraSpells | 3rd Level | Evocation | Force | Yes |
| Discordant Melody | `Shout_DiscordantMelody` | MystraSpells | 3rd Level | Evocation | Thunder | Yes |
| Spirit Shroud | `Shout_SpiritShroud` | Both (ID collision) | 3rd Level | Necromancy | Debuff/Control | Yes |
| Life Transference | `Target_LifeTransference` | Both (ID collision) | 3rd Level | Necromancy | Healing | Yes |
| Flame Arrows | `Target_FlameArrows` | Both (ID collision) | 3rd Level | Transmutation | Buff/Utility | Yes |
| Venomous Barbs | `Target_VenomousBarbs` | MystraSpells | 3rd Level | Transmutation | Buff/Utility | Yes |
| Water Walk | `Target_WaterWalk` | MystraSpells [shared] | 3rd Level | Transmutation | Buff/Utility | Yes |
| Ashardalon's Stride | `Shout_AshardalonsStride` | Both (ID collision) | 3rd Level | Transmutation | Debuff/Control | Yes |
| Erupting Earth | `Target_EruptingEarth` | Both (ID collision) | 3rd Level | Transmutation | Debuff/Control | Yes |
| Aura of Life | `Shout_AuraOfLife` | Both (ID collision) | 4th Level | Abjuration | Buff/Utility | Yes |
| Aura of Purity | `Shout_AuraOfPurity` | MystraSpells | 4th Level | Abjuration | Buff/Utility | Yes |
| Summon Aberration | `Target_SummonAberration` | MystraSpells | 4th Level | Conjuration | Acid | Yes |
| Summon Greater Demon | `Target_SummonGreaterDemon` | MystraSpells | 4th Level | Conjuration | Fire | Yes |
| Summon Construct | `Target_SummonConstruct` | Both (ID collision) | 4th Level | Conjuration | Necrotic | Yes |
| Summon Aberration: Beholderkin | `Target_SummonBeholderkin` | 5eSpells [shared] | 4th Level | Conjuration | Psychic | Yes |
| Summon Elemental | `Target_SummonElemental` | Both (ID collision) | 4th Level | Conjuration | Summon | Yes |
| Arcane Eye | `Target_ArcaneEye` | 5eSpells [shared] | 4th Level | Divination | Psychic | Yes |
| Charm Monster | `Target_CharmMonster` | Both (ID collision) | 4th Level | Enchantment | Buff/Utility | Yes |
| Ego Whip | `Target_EgoWhip` | MystraSpells | 4th Level | Enchantment | Debuff/Control | Yes |
| Mesmer's Lullaby | `Shout_MesmersLullaby` | MystraSpells | 4th Level | Enchantment | Debuff/Control | Yes |
| Dream | `Target_DreamSleep` | MystraSpells | 4th Level | Enchantment | Psychic | Yes |
| Raulothim's Psychic Lance | `Projectile_RaulothimsPsychicLance` | 5eSpells [shared] | 4th Level | Enchantment | Psychic | Yes |
| Vitriolic Sphere | `Projectile_VitriolicSphere` | Both (ID collision) | 4th Level | Evocation | Acid | Yes |
| Storm Sphere | `Target_StormSphere` | Both (ID collision) | 4th Level | Evocation | Bludgeoning | Yes |
| Web of Fire | `Projectile_WebOfFire` | MystraSpells | 4th Level | Evocation | Fire | Yes |
| Gravity Sinkhole | `Target_GravitySinkhole` | MystraSpells | 4th Level | Evocation | Force | Yes |
| Illusory Weapon | `Target_IllusoryWeapon` | MystraSpells | 4th Level | Illusion | Buff/Utility | Yes |
| Shadow of Moil | `Shout_ShadowOfMoil` | Both (ID collision) | 4th Level | Necromancy | Buff/Utility | Yes |
| Control Water | `Target_ControlWater_Container` | MystraSpells | 4th Level | Transmutation | Buff/Utility | Yes |
| Guardian of Nature | `Shout_GuardianOfNature` | Both (ID collision) | 4th Level | Transmutation | Buff/Utility | Yes |
| Stone Shape | `Target_StoneShape_Container` | MystraSpells | 4th Level | Transmutation | Buff/Utility | Yes |
| Elemental Bane | `Target_ElementalBane` | MystraSpells | 4th Level | Transmutation | Debuff/Control | Yes |
| Antilife Shell | `Shout_AntilifeShell` | 5eSpells | 5th Level | Abjuration | Buff/Utility | Yes |
| Astral Disjunction | `Target_AstralDisjunction` | MystraSpells | 5th Level | Abjuration | Buff/Utility | Yes |
| Circle of Power | `Shout_CircleOfPower` | 5eSpells | 5th Level | Abjuration | Buff/Utility | Yes |
| Bigby's Hand | `Target_BigbyHand` | MystraSpells | 5th Level | Conjuration | Buff/Utility | Yes |
| Far Step | `Target_FarStep` | 5eSpells [shared] | 5th Level | Conjuration | Buff/Utility | Yes |
| Teleportation Circle | `Teleportation_TeleportationCircle` | 5eSpells | 5th Level | Conjuration | Buff/Utility | Yes |
| Conjure Volley | `ProjectileStrike_ConjureVolley` | 5eSpells | 5th Level | Conjuration | Debuff/Control | Yes |
| Infernal Calling | `Target_InfernalCalling` | MystraSpells | 5th Level | Conjuration | Fire | Yes |
| Summon Draconic Spirit | `Target_SummonDragon` | MystraSpells | 5th Level | Conjuration | Fire | Yes |
| Steel Wind Strike | `Target_SteelWindStrike` | Both (ID collision) | 5th Level | Conjuration | Force | Yes |
| Commune with Nature | `Shout_CommuneWithNature` | 5eSpells | 5th Level | Divination | Buff/Utility | Yes |
| Synaptic Static | `Target_SynapticStatic` | Both (ID collision) | 5th Level | Enchantment | Psychic | Yes |
| Maelstrom | `Target_Maelstrom` | Both (ID collision) | 5th Level | Evocation | Bludgeoning | Yes |
| Holy Weapon | `Target_HolyWeapon` | Both (ID collision) | 5th Level | Evocation | Buff/Utility | Yes |
| Immolation | `Target_Immolation` | MystraSpells | 5th Level | Evocation | Fire | Yes |
| Dawn | `Target_Dawn` | 5eSpells | 5th Level | Evocation | Radiant | Yes |
| Mislead | `Target_Mislead` | 5eSpells | 5th Level | Illusion | Buff/Utility | Yes |
| Raise Dead | `Target_RaiseDead` | 5eSpells | 5th Level | Necromancy | Buff/Utility | Yes |
| Danse Macabre | `Target_DanseMacabre_Container` | MystraSpells | 5th Level | Necromancy | Necrotic | Yes |
| Enervation | `Projectile_Enervation` | MystraSpells | 5th Level | Necromancy | Necrotic | Yes |
| Macabre Explosion | `Target_MacabreExplosion` | MystraSpells | 5th Level | Necromancy | Necrotic | Yes |
| Negative Energy Flood | `Projectile_NegativeEnergyFlood` | Both (ID collision) | 5th Level | Necromancy | Necrotic | Yes |
| Skill Empowerment | `Target_SkillEmpowerment` | 5eSpells | 5th Level | Transmutation | Buff/Utility | Yes |
| Swift Quiver | `Shout_SwiftQuiver` | Both (ID collision) | 5th Level | Transmutation | Buff/Utility | Yes |
| Primordial Ward | `Shout_PrimordialWard` | MystraSpells | 6th Level | Abjuration | Buff/Utility | Yes |
| Conjure Fey | `Target_ConjureFey` | MystraSpells | 6th Level | Conjuration | Acid | Yes |
| Psychic Crush | `Target_PsychicCrush` | MystraSpells | 6th Level | Enchantment | Psychic | Yes |
| Fissure | `Zone_Fissure` | MystraSpells | 6th Level | Evocation | Force | Yes |
| Elemental Investiture | `Shout_ElementalInvestiture` | MystraSpells | 6th Level | Transmutation | Buff/Utility | Yes |
| Tenser's Transformation | `Shout_TensersTransformation` | Both (ID collision) | 6th Level | Transmutation | Buff/Utility | Yes |
| True Seeing | `Target_TrueSeeing` | Both (ID collision) | 6th Level | Transmutation | Buff/Utility | Yes |
| Lesser Regeneration | `Target_LesserRegenerate` | MystraSpells | 6th Level | Transmutation | Healing | Yes |
| Finger of Death | `Target_FingerOfDeath` | 5eSpells | 7th Level | Necromancy | Necrotic | Yes |
| Regenerate | `Target_Regenerate` | 5eSpells | 7th Level | Transmutation | Healing | Yes |
| Holy Aura | `Shout_HolyAura` | 5eSpells | 8th Level | Abjuration | Buff/Utility | Yes |
| Mind Blank | `Target_MindBlank` | 5eSpells | 8th Level | Abjuration | Buff/Utility | Yes |
| Feeblemind | `Target_Feeblemind` | 5eSpells | 8th Level | Enchantment | Buff/Utility | Yes |
| Dominate Monster | `Target_DominateMonster` | 5eSpells | 8th Level | Enchantment | Debuff/Control | Yes |
| Foresight | `Target_Foresight` | 5eSpells | 9th Level | Divination | Buff/Utility | Yes |
| Power Word: Kill | `Target_PowerWordKill` | 5eSpells | 9th Level | Enchantment | Buff/Utility | Yes |
| Power Word: Heal | `Target_PowerWordHeal` | 5eSpells | 9th Level | Evocation | Healing | Yes |
| Create Bonfire | `Target_CreateBonfire` | Both (ID collision) | None | Conjuration | Fire | No |
| Moonflare | `Projectile_Moonflare` | MystraSpells | None | Evocation | Radiant | No |
| Spare the Dying | `Target_SpareTheDying` | 5eSpells | None | - | Buff/Utility | No |