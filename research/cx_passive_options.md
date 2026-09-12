# CX passive-manager candidate options

Auto-harvested from <https://bg3.norbyte.dev> for every `CX_*_Boost` passive tracked in `cx_passive_manager.json`. Each list is *candidates to consider*, not a recommendation - skim and cherry-pick into the Act buckets.

_Generated 2026-09-10 17:49 - Norbyte search returns the first 30 hits only; very broad terms are truncated._

**Legend** - `already in manager` means the name is already present in some Act bucket for this passive. Candidates you do not own yet are listed first, and names that literally contain the search term rank above thematic-only matches. Spell upcast variants (`_2` .. `_6`) are collapsed to the base name.

---

## Generic

### `CX_Boss_Boost`  -  _boss_
_Currently in manager_ - passives: `MAG_Myrkulites_CircletOfMyrkul_Circlet_Passive`; spells: `AJ_Shout_ActionSurge_Emergency`

**Passive candidates** (24 found, showing 18)
- `DamageReduction_Dragon` - **Great Wyrm's Scales**
- `DamageReduction_Dragon_Tactician` - **Greater Wyrm's Scales**
  <br>`Boosts=DamageReduction(All, Flat, 4)`
- `Indomitable` - **Indomitable** | You have become as durable as an iron golem. Whenever you fail a Saving Throw, you can roll again, using the new result instead.
  <br>`Boosts=UnlockInterrupt(Interrupt_Indomitable);ActionResource(Interrupt_Indomitable,1,0)`
- `LegendaryResistance`
- `MAG_PhysicalDamageReduction_Passive` - **Steel Physiology** | Reduce incoming Bludgeoning, Piercing, and Slashing damage by [1].
  <br>`Boosts=DamageReduction(Piercing, Flat, 1);DamageReduction(Bludgeoning, Flat, 1);DamageReduction(Slashing, Flat, 1)`
- `MagicResistance` - **Magic Resistance** | Has Advantage on Saving Throws against spells and other magical effects.
  <br>`Boosts=IF(HasSpellFlag(SpellFlags.Spell)):Advantage(AllSavingThrows)`
- `RelentlessAvenger` - **Relentless Avenger** | If you hit an enemy with an Opportunity Attack, your movement speed increases by [1] on your next turn.
- `RelentlessEndurance` - **Relentless Endurance** | If you reach 0 hit points, you regain [1] instead of becoming Downed.
- `RelentlessRage` - **Relentless Rage** | Once per Short Rest, if you drop to [1] hit points while Enraged, you regain [2] instead of being Downed.
- `ARM_ExceptionalPlate_1_Passive` _(+2 numbered tiers)_ - **Exceptional Plate** | You take [1] less damage from Slashing, Piercing, and Bludgeoning sources.
  <br>`Boosts=DamageReduction(Slashing, Flat, 1);DamageReduction(Piercing, Flat, 1);DamageReduction(Bludgeoning, Flat, 1)`
- `ARM_MagicalPlate_1_Passive` _(+2 numbered tiers)_ - **Magical Plate** | All incoming damage is reduced by [1].
  <br>`Boosts=DamageReduction(All, Flat, 1)`
- `ARM_SuperiorMaterial_1_Passive` _(+2 numbered tiers)_ - **Superior Material** | You take [1] less Slashing damage.
  <br>`Boosts=DamageReduction(Slashing, Flat, 1)`
- `ARM_SuperiorPadding_1_Passive` _(+2 numbered tiers)_ - **Superior Padding** | You take [1] less Bludgeoning damage.
  <br>`Boosts=DamageReduction(Bludgeoning, Flat, 1)`
- `ARM_SuperiorPlate_1_Passive` _(+2 numbered tiers)_ - **Superior Plate** | You take [1] less Piercing damage.
  <br>`Boosts=DamageReduction(Piercing, Flat, 1)`
- `DungeonDelver_ResistTraps` - **Dungeon Delver: Resist Traps** | You have Advantage on Saving Throws made to avoid traps and Resistance to trap damage.
  <br>`Boosts=IF(IsTrap()):Advantage(SavingThrow, Strength);IF(IsTrap()):Advantage(SavingThrow, Wisdom);IF(IsTrap()):Advantage(SavingThrow, Constitution);IF(IsTrap()):Advantage(SavingThrow, Dext…`
- `EtherealForm_ScryingEye` - **Ethereal Form** | All incoming damage is reduced by [1].
  <br>`Boosts=DamageReduction(All, Flat, 8)`
- `Gith_MartialProdigy` - **Martial Prodigy** | A lifetime of relentless training gave you Armour Proficiency with Light and Medium Armour, as well as Proficiency with the Shortsword, Longsword, and Greatsword.
  <br>`Boosts=Proficiency(LightArmor);Proficiency(MediumArmor);Proficiency(Shortswords);Proficiency(Longswords);Proficiency(Greatswords)`
- `HeavyArmorMaster` - **Heavy Armour Master** | Increase your Strength score by [1] (up to a maximum of [2]), and reduce incoming damage from non-magical attacks by [3].
  <br>`Boosts=Ability(Strength, 1, 20); IF(HasHeavyArmor() and not HasDamageEffectFlag(DamageFlags.Magical)):DamageReduction(Slashing, Flat, 3); IF(HasHeavyArmor() and not HasDamageEffectFlag(Da…`

**Spell candidates** (12 found)
- `Shout_ActionSurge` - **Action Surge** | Immediately gain an extra action to use this turn.
  <br>`SpellType=Shout`  `SpellProperties=ApplyStatus(ACTION_SURGE,100,1)`
- `Shout_FrightfulPresence_Dragon_Skeletal` - **Frightful Presence**
- `Shout_GoadingRoar_Bear_Summon` - **Goading Roar** | Roar at nearby enemies to goad them into attacking you.
- `Shout_Roar_Bear_Polar`
  <br>`SpellType=Shout`
- `Shout_SecondWind` - **Second Wind** | Draw on your stamina to heal yourself.
  <br>`SpellType=Shout`  `SpellProperties=RegainHitPoints(1d10+ClassLevel(Fighter))`
- `Shout_WildMagic_ActionSurge` - **Wild Magic: Action Surge** | You gain an additional action this turn.
  <br>`SpellType=Shout`  `SpellProperties=ApplyStatus(ACTION_SURGE,100,1)`
- `Shout_Poison_TollCollector_Face` - **Unleash a roar that wounds and Poisons nearby foes.**
- `Shout_Reckless_Minotaur` - **Reckless Roar**
- `Shout_Silence_TollCollector_Face` - **Unleash a roar that wounds and Silences nearby foes.**
- `Shout_Slow_TollCollector_Face` - **Unleash a roar that wounds and Slows nearby foes.**
- `Target_FlameStrike` - **Make a pillar of divine fire roar down from the heavens like the wrath of affronted angels.**
- `Target_RangersCompanion_Bear` - **Bear Companion** | Summon a black bear that can endure heavy attacks and draw the enemy's attention with its Goading Roar.
  <br>`SpellType=Target`  `SpellProperties=GROUND:IF(not CharacterLevelGreaterThan(4)):Summon(d642d398-f349-4eab-b98c-a82cbda19918,Permanent,,,'CombatSummonStack',UNSUMMON_ABLE,RANGERS_COMPANION_BEAR,SHADOWCURSE_SUMMON_CHEC…`

### `CX_MiniBoss_Boost`  -  _boss_
_Currently in manager_ - passives: `LOW_SharGrotto_Mirror_ConstitutionBoon_Passive`

**Passive candidates** (9 found)
- `Background_BloodWarVeteran` - **Blood War Veteran** | You have Proficiency in Athletics and Survival checks, essential tools for any who fight the Blood War's most fevered frays.
  <br>`Boosts=ProficiencyBonus(Skill,Athletics);ProficiencyBonus(Skill,Survival)`
- `MagicResistance` - **Magic Resistance** | Has Advantage on Saving Throws against spells and other magical effects.
  <br>`Boosts=IF(HasSpellFlag(SpellFlags.Spell)):Advantage(AllSavingThrows)`
- `Resilient_Charisma` - **Resilient: Charisma** | Increase your Charisma by [1] and gain Proficiency in Charisma Saving Throws.
  <br>`Boosts=Ability(Charisma,1,20);ProficiencyBonus(SavingThrow,Charisma)`
- `Resilient_Constitution` - **Resilient: Constitution** | Increase your Constitution by [1] and gain Proficiency in Constitution Saving Throws.
  <br>`Boosts=Ability(Constitution,1,20);ProficiencyBonus(SavingThrow,Constitution)`
- `Resilient_Dexterity` - **Resilient: Dexterity** | Increase your Dexterity by [1] and gain Proficiency in Dexterity Saving Throws.
  <br>`Boosts=Ability(Dexterity,1,20);ProficiencyBonus(SavingThrow,Dexterity)`
- `Resilient_Intelligence` - **Resilient: Intelligence** | Increase your Intelligence by [1] and gain Proficiency in Intelligence Saving Throws.
  <br>`Boosts=Ability(Intelligence,1,20);ProficiencyBonus(SavingThrow,Intelligence)`
- `Resilient_Strength` - **Resilient: Strength** | Increase your Strength by [1] and gain Proficiency in Strength Saving Throws.
  <br>`Boosts=Ability(Strength,1,20);ProficiencyBonus(SavingThrow,Strength)`
- `Resilient_Wisdom` - **Resilient: Wisdom** | Increase your Wisdom by [1] and gain Proficiency in Wisdom Saving Throws.
  <br>`Boosts=Ability(Wisdom,1,20);ProficiencyBonus(SavingThrow,Wisdom)`
- `UnarmouredDefence_Barbarian` - **Unarmoured Defence** | Your body is as resilient as any armour. While not wearing armour, you add your Constitution Modifier to your Armour Class.
  <br>`Boosts=ACOverrideFormula(10,true,Dexterity,Constitution)`

**Spell candidates** (7 found)
- `Projectile_MenacingAttack` - **Menacing Attack (Ranged)**
- `Shout_ActionSurge` - **Action Surge** | Immediately gain an extra action to use this turn.
  <br>`SpellType=Shout`  `SpellProperties=ApplyStatus(ACTION_SURGE,100,1)`
- `Shout_Owlbear_Wildshape_Enrage` - **Enrage**
- `Shout_SecondWind` - **Second Wind** | Draw on your stamina to heal yourself.
  <br>`SpellType=Shout`  `SpellProperties=RegainHitPoints(1d10+ClassLevel(Fighter))`
- `Shout_WildMagic_ActionSurge` - **Wild Magic: Action Surge** | You gain an additional action this turn.
  <br>`SpellType=Shout`  `SpellProperties=ApplyStatus(ACTION_SURGE,100,1)`
- `Target_MenacingAttack` - **Menacing Attack (Melee)**
- `Shout_Dreadful_Aspect` - **Let your darkest emotions burst forth as a menacing pulse to Frighten nearby enemies.**

### `CX_Magic_Boost`  -  _caster_
_Currently in manager_ - spells: `Projectile_Jump`

**Passive candidates** (8 found)
- `ALCH_Elixir_ArcaneAcuity_Passive` - **Elixir of Battlemage's Power** | You have Arcane Acuity until your next Long Rest. Replaces effects from other elixirs when drunk.
- `EmpoweredEvocation` - **Empowered Evocation** | Your grasp of Evocation magic has tightened, and you can add your Intelligence Modifier to damage rolls with any Evocation spells.
  <br>`Boosts=IF(IsSpell() and IsSpellSchool(SpellSchool.Evocation)):DamageBonus(max(0, IntelligenceModifier))`
- `MAG_ArcaneAcuity_ReduceDurationPerDamage_Passive`
- `MAG_ElementalGish_ArcaneAcuity_Helmet_Passive` - **Battle Acuity** | Whenever you deal damage with a weapon attack, you gain Arcane Acuity for 2 turns.
- `MAG_Gish_ArcaneAcuity_Gloves_Passive` - **Battlemage's Power** | When you hit a target with a spell or cantrip that uses a weapon, you gain Arcane Acuity.
- `PotentCantrip` - **Potent Cantrip** | Your cantrips become harder to evade entirely.When a creature succeeds its Saving Throw against one of your cantrips, it still takes half the cantrip's damage, but suffers no additional effects.
- `WarCaster_Bonuses` - **War Caster: Concentration** | You have Advantage on Saving Throws to maintain Concentration on a spell.
  <br>`Boosts=Advantage(Concentration)`
- `WarCaster_OpportunitySpell` - **War Caster: Opportunity Spell** | You can use a reaction to cast Shocking Grasp at a target moving out of melee range.
  <br>`Boosts=UnlockInterrupt(Interrupt_WarCaster)`

**Spell candidates** (22 found, showing 14)
- `Projectile_MagicMissile` - **Magic Missile** | Shoot [2] magical darts, each dealing [1]. They always hit their target.
  <br>`SpellType=Projectile`  `SpellProperties=DealDamage(1d4+1,Force,Magical)`
- `Projectile_MagicMissile_MindFlayer`
  <br>`SpellType=Projectile`
- `Projectile_ScorchingRay` - **Scorching Ray** | Hurl [2] rays of fire. Each ray deals [1].
  <br>`SpellType=Projectile`  `SpellSuccess=DealDamage(2d6,Fire,Magical)`  `SpellProperties=GROUND:SurfaceChange(Ignite);GROUND:SurfaceChange(Melt)`
- `Projectile_ScorchingRay_CircletOfBlasting`
  <br>`SpellType=Projectile`
- `Shout_MirrorImage` - **Mirror Image** | Create 3 illusory duplicates of yourself that distract attackers. Each duplicate increases your Armour Class by 3.
  <br>`SpellType=Shout`  `SpellProperties=ApplyStatus(MIRROR_IMAGE_3,100,10);ApplyStatus(MIRROR_IMAGE_2,100,10);ApplyStatus(MIRROR_IMAGE_1,100,10)`
- `Shout_Slow_TollCollector_Face`
  <br>`SpellSuccess=ApplyStatus(<em>SLOW</em>, 100, 2);`
- `Shout_WildMagic_Slow` - **Wild Magic: Slow** | You are Slowed.
  <br>`SpellType=Shout`  `SpellProperties=ApplyStatus(SLOW,100,2)`
- `Target_Counterspell` - **Counterspell**
- `Target_Counterspell_Failure` - **Failed Counterspell**
  <br>`SpellType=Target`
- `Target_CounterSpell_Mindflayer`
  <br>`SpellType=Target`
- `Target_Counterspell_Success` - **Nullify another creature's spell as a reaction. The spell must be 3rd Level or lower. If it is higher, you must succeed a Check to nullify it, the difficulty of which is based on the spell's Level.**
  <br>`SpellType=Target`
- `Target_Haste`
  <br>`SpellProperties=ApplyStatus(<em>HASTE</em>,100,10)`
- `Target_Slow`
  <br>`SpellSuccess=ApplyStatus(<em>SLOW</em>,100,10)`
- `Projectile_WhiteSporeCloud` - **Haste Spores**

### `CX_Martial_Boost`  -  _martial_
_Currently in manager_ - passives: `WeaponMaster`; spells: `Projectile_Jump`

**Passive candidates** (27 found, showing 18)
- `ExtraAttack`
- `ExtraAttack_2` - **Improved Extra Attack** | You can make two additional attacks after attacking with your main-hand weapon.
- `ExtraAttack_BonusTechnical`
- `GreatWeaponMaster_BonusAttack` - **Great Weapon Master: Bonus Attack** | When you land a Critical Hit or kill a target with a melee weapon attack, you can make another melee weapon attack as a bonus action that turn.
- `GreatWeaponMaster_BonusDamage` - **Great Weapon Master: All In** | When attacking with a melee weapon you are Proficient with and are wielding in both hands, Attack Rolls take a -5 penalty, but their damage increases by 10.
  <br>`Boosts=IF(GreatWeaponMaster(context.Source)):RollBonus(MeleeWeaponAttack, -5);IF(GreatWeaponMaster(context.Source)):CharacterWeaponDamage(10)`
- `HeavyArmorMaster` - **Heavy Armour Master** | Increase your Strength score by [1] (up to a maximum of [2]), and reduce incoming damage from non-magical attacks by [3].
  <br>`Boosts=Ability(Strength, 1, 20); IF(HasHeavyArmor() and not HasDamageEffectFlag(DamageFlags.Magical)):DamageReduction(Slashing, Flat, 3); IF(HasHeavyArmor() and not HasDamageEffectFlag(Da…`
- `Indomitable` - **Indomitable** | You have become as durable as an iron golem. Whenever you fail a Saving Throw, you can roll again, using the new result instead.
  <br>`Boosts=UnlockInterrupt(Interrupt_Indomitable);ActionResource(Interrupt_Indomitable,1,0)`
- `LOW_Guildhall_ExtraAttack_DaggerSpecialist` - **Dagger Specialist** | This creature can throw up to 3 daggers per round.
- `MAG_PHB_Sentinel_Shield_Passive` - **Heightened Awareness** | Gain a +[1] bonus to Initiative rolls and Advantage on Perception Ability Checks.
  <br>`Boosts=Initiative(3);Advantage(Skill, Perception)`
- `PolearmMaster_AttackOfOpportunity` - **Polearm Master: Opportunity Attack** | When wielding a glaive, halberd, quarterstaff, or spear, you can make an Opportunity Attack when a target comes within range.
  <br>`Boosts=UnlockInterrupt(Interrupt_PolearmMaster)`
- `PolearmMaster_BonusAttack` - **Polearm Master: Bonus Attack** | When attacking with a glaive, halberd, quarterstaff, or spear, you can use a bonus action to attack with the butt of your weapon and deal [1].
- `SavageAttacker` - **Savage Attacker** | When making melee weapon attacks, you roll your damage dice twice and use the highest result.
- `Sentinel_Attack` - **Sentinel: Vengeance** | When an enemy within melee range attacks an ally, you can use a reaction to make a weapon attack against that enemy.
  <br>`Boosts=UnlockInterrupt(Interrupt_Sentinel)`
- `Sentinel_OpportunityAdvantage` - **Sentinel: Opportunity Advantage** | You have Advantage on Opportunity Attacks.
  <br>`Boosts=IF(SpellId('Target_Sentinel_AttackOfOpportunity')):Advantage(AttackRoll)`
- `Sentinel_ZeroSpeed` - **Sentinel: Snare** | When you hit a creature with an Opportunity Attack, it can no longer move for the rest of its turn.
- `Slayer_ExtraAttack`
- `Slayer_ExtraAttack_2`
- `BestialFury` - **Bestial Fury** | Your bond with your companion has deepened, unlocking their inner strength and giving them an Extra Attack.

**Spell candidates** (27 found, showing 14)
- `Rush_Aggressive`
  <br>`SpellType=Rush`
- `Rush_Charge_Minotaur`
  <br>`SpellType=<em>Rush</em>`
- `Rush_Charge_Minotaur_Ally`
  <br>`SpellType=Rush`
- `Rush_Charger_Attack`
  <br>`SpellType=<em>Rush</em>`
- `Rush_Charger_Push`
  <br>`SpellType=<em>Rush</em>`
- `Rush_ForceTunnel`
  <br>`SpellType=<em>Rush</em>`
- `Rush_GoldenLance`
  <br>`SpellType=<em>Rush</em>`
- `Rush_InfernalTrample`
  <br>`SpellType=Rush`  `SpellSuccess=DealDamage(1d4,Fire,Magical)`
- `Rush_Primal_Stampede`
  <br>`SpellType=<em>Rush</em>`
- `Rush_Rush`
  <br>`SpellType=<em>Rush</em>`
- `Rush_Rush_Boar`
  <br>`SpellType=<em>Rush</em>`
- `Rush_Rush_Boar_Summon`
  <br>`SpellType=<em>Rush</em>`
- `Rush_Rush_DeepRothe`
  <br>`SpellType=<em>Rush</em>`
- `Rush_SpringAttack`
  <br>`SpellType=<em>Rush</em>`

---

## Barbarian

### `CX_Barbarian_Boost`  -  _martial_
_Currently in manager_ - passives: `RageUnlock`; spells: `Projectile_Jump`, `Target_RecklessAttack`, `Target_Shove`

**Passive candidates** (7 found)
- `BrutalCritical` - **Brutal Critical** | You've trained to strike swift and true. When you land a Critical Hit, you roll an extra damage die as well as the normal additional critical dice.
  <br>`Boosts=CriticalHitExtraDice(1, MeleeWeaponAttack);CriticalHitExtraDice(1, MeleeUnarmedAttack);`
- `DangerSense` - **Danger Sense** | You sense when things aren't as they should be.You have Advantage on Dexterity Saving Throws against traps, spells, and surfaces. To gain this benefit, you can't be Blinded or Incapacitated.
  <br>`Boosts=Advantage(SavingThrow,Dexterity)`
- `FastMovement` - **Fast Movement** | Movement speed increased by [1] while not wearing Heavy Armour.
  <br>`Boosts=ActionResource(Movement, 3, 0)`
- `FeralInstinct` - **Feral Instinct** | You have honed your instincts to the utmost degree. You gain a +[1] bonus to Initiative and can't be Surprised.
  <br>`Boosts=Initiative(3);StatusImmunity(SURPRISED);`
- `GOB_Boss_RecklessAttack` - **Crude Frenzy** | This goblin can make an additional free attack after making a Main Hand Attack, but the second attack has Disadvantage on its Attack Roll.
- `RecklessAttack` - **Reckless Attack** | Gain Advantage on Attack Rolls until the end of your turn, but enemies also have Advantage against you.
  <br>`Boosts=UnlockInterrupt(Interrupt_RecklessAttack);UnlockSpell(Target_RecklessAttack)`
- `RelentlessRage` - **Relentless Rage** | Once per Short Rest, if you drop to [1] hit points while Enraged, you regain [2] instead of being Downed.

**Spell candidates** (38 found, showing 14)
- `Shout_EndlessRage` - **Endless Rage**
- `Shout_EndRage` - **End Rage**
  <br>`SpellProperties=RemoveStatus(SG_Rage);`
- `Shout_GoadingRoar_Bear_Summon` - **Goading Roar** | Roar at nearby enemies to goad them into attacking you.
- `Shout_Owlbear_Wildshape_Enrage` - **Enrage**
- `Shout_Rage`
- `Shout_Rage_Boar` - **Go into a frenzy, increasing your size and becoming stronger through raw anger.** | While raging, your melee attacks deal an additional [1]. You gain Resistance to physical damage, and Advantage on Strength Checks and Saving Throws.You can use Frenzied Strike.
  <br>`SpellType=Shout`  `SpellProperties=AI_IGNORE:ApplyStatus(RAGE_BOAR,100,10);AI_ONLY:IF(HasActionResource('ActionPoint', 1, 0, false)):ApplyStatus(AI_HELPER_RAGE,100,1);`
- `Shout_Rage_Frenzy` - **Your RAGE">Rage turns into a frenzy! You gain <LSTag**
- `Shout_Rage_Giant` - **Giant's Rage** | Enter a Rage and increase in size. Your Rage damage bonus is doubled on Throw attacks.
  <br>`SpellType=Shout`  `SpellProperties=AI_IGNORE:IF(not ClassLevelHigherOrEqualThan(9,'Barbarian')):ApplyStatus(RAGE_GIANT,100,10);AI_IGNORE:IF(ClassLevelHigherOrEqualThan(9,'Barbarian')):ApplyStatus(RAGE_GIANT_2,100,10…`
- `Shout_Rage_Totem_Bear` - **Rage: Bear Heart**
- `Shout_Rage_Totem_Eagle` - **Rage: Eagle Heart**
- `Shout_Rage_Totem_Elk` - **Rage: Elk Heart**
- `Shout_Rage_Totem_Tiger` - **Rage: Tiger Heart**
- `Shout_Rage_Totem_Wolf` - **Rage: Wolf Heart**
- `Shout_Rage_WildMagic` - **Rage: Wild Magic** | Enter a Rage that releases all the magic roiling inside of you, causing a random magical effect.
  <br>`SpellType=Shout`  `SpellProperties=AI_IGNORE:TriggerRandomCast(1,0,WildMagicBarbarian);IF(ClassLevelHigherOrEqualThan(1,'Barbarian') and not ClassLevelHigherOrEqualThan(9,'Barbarian')):ApplyStatus(RAGE,100,10);IF(Cl…`

### `CX_Barbarian_Berserker_Boost`  -  _martial_
_Currently in manager_ - passives: `MindlessRage`, `RageFrenzyUnlock`; spells: `Shout_Rage_Frenzy`

**Passive candidates** (9 found)
- `MAG_END_PsychicRetaliation_Passive` - **Imperial Retaliation** | When the wielder succeeds a Saving Throw, the foe that caused the throw needs to make an Intelligence Saving Throw or be Stunned for [1] turn.
- `MAG_FlamingFist_BlazingRetaliation_Passive` - **Blazing Retaliation** | Huddle behind your shield to increase your Armour Class by [1] and retaliate against attackers who miss you.
  <br>`Boosts=AC(1)`
- `Rage_Frenzy_NoHeavyArmour_VFX`
- `GOB_Boss_RecklessAttack` - **Crude Frenzy** | This goblin can make an additional free attack after making a Main Hand Attack, but the second attack has Disadvantage on its Attack Roll.
- `GuardianOfFaith_Retaliate` - **Retaliation** | Strike back at the next enemy that attacks you.
  <br>`Boosts=UnlockInterrupt(Interrupt_GuardianOfFaith_Retaliate)`
- `LegendaryAction_SCL_Drider_PsionicVengeance` - **Legendary Action: Fanatic Retaliation** | Once per round when a Spindleweb Fanatic is killed, Kar'niss can use a Legendary Action to possibly deal [1] and Silence the attacker.
- `WildMagicBarbarian_MagicRetribution_Passive` - **Wild Magic: Magic Retribution** | Your magic lashes out whenever you take damage. Until the end of your Rage, enemies that hit you take [1] in retaliation.
- `MindlessRage` _(already in manager)_ - **Mindless Rage** | Your rage becomes all-consuming, repelling outside influence. While Frenzied, you can't be Charmed or Frightened, and Calm Emotions no longer ends your rage.
- `RageFrenzyUnlock` _(already in manager)_ - **Rage Becomes Frenzy** | Your bloodthirst transforms your rage, making it stronger.
  <br>`Boosts=UnlockSpell(Shout_Rage_Frenzy)`

**Spell candidates** (33 found, showing 14)
- `Shout_EndlessRage` - **Endless Rage**
- `Shout_EndRage` - **End Rage**
  <br>`SpellProperties=RemoveStatus(SG_Rage);`
- `Shout_Rage`
- `Shout_Rage_Giant` - **Giant's Rage** | Enter a Rage and increase in size. Your Rage damage bonus is doubled on Throw attacks.
  <br>`SpellType=Shout`  `SpellProperties=AI_IGNORE:IF(not ClassLevelHigherOrEqualThan(9,'Barbarian')):ApplyStatus(RAGE_GIANT,100,10);AI_IGNORE:IF(ClassLevelHigherOrEqualThan(9,'Barbarian')):ApplyStatus(RAGE_GIANT_2,100,10…`
- `Shout_Rage_Totem_Bear` - **Rage: Bear Heart**
- `Shout_Rage_Totem_Eagle` - **Rage: Eagle Heart**
- `Shout_Rage_Totem_Elk` - **Rage: Elk Heart**
- `Shout_Rage_Totem_Tiger` - **Rage: Tiger Heart**
- `Shout_Rage_Totem_Wolf` - **Rage: Wolf Heart**
- `Shout_Rage_WildMagic` - **Rage: Wild Magic** | Enter a Rage that releases all the magic roiling inside of you, causing a random magical effect.
  <br>`SpellType=Shout`  `SpellProperties=AI_IGNORE:TriggerRandomCast(1,0,WildMagicBarbarian);IF(ClassLevelHigherOrEqualThan(1,'Barbarian') and not ClassLevelHigherOrEqualThan(9,'Barbarian')):ApplyStatus(RAGE,100,10);IF(Cl…`
- `Target_FrenziedStrike` - **Frenzied Strike**
- `Target_FrenziedStrike_Boar` - **Frenzied Strike**
- `Target_IntimidatingPresence` - **Intimidating Presence** | Menace an enemy and instil a terrible Fear within them.
  <br>`SpellType=Target`  `SpellSuccess=ApplyStatus(INTIMIDATING_PRESENCE,100,2);ApplyStatus(SELF,INTIMIDATING_PRESENCE_OWNER,100,2)`
- `Target_IntimidatingPresence_Maintain` - **Maintain Intimidating Presence** | Prolong the Fear inflicted on a target by your Intimidating Presence.
  <br>`SpellType=Target`  `SpellProperties=SetStatusDuration(INTIMIDATING_PRESENCE,2);SetStatusDuration(SELF,INTIMIDATING_PRESENCE_OWNER,2)`

### `CX_Barbarian_WildMagic_Boost`  -  _hybrid_
_Currently in manager_ - passives: `RageGiantUnlock`, `WildMagic`, `WildMagicRage`; spells: `Shout_Rage_WildMagic`

**Passive candidates** (2 found)
- `WildMagicBarbarian_FlumphDestruct`
- `WildMagicBarbarian_MagicRetribution_Passive` - **Wild Magic: Magic Retribution** | Your magic lashes out whenever you take damage. Until the end of your Rage, enemies that hit you take [1] in retaliation.

**Spell candidates** (74 found, showing 14)
- `Projectile_ArrowOfTeleportation` - **Teleport wherever you fire this arrow.**
- `Projectile_MagicMissile` - **Magic Missile** | Shoot [2] magical darts, each dealing [1]. They always hit their target.
  <br>`SpellType=Projectile`  `SpellProperties=DealDamage(1d4+1,Force,Magical)`
- `Projectile_MagicMissile_MindFlayer`
  <br>`SpellType=Projectile`
- `Projectile_WildMagic_Heal`
  <br>`SpellType=Projectile`  `SpellProperties=RegainHitPoints(1d4)`
- `Shout__WildMagic` - **Wild Magic Surge** | Your spellcasting can unleash unpredictable surges of untamed magic.
  <br>`SpellType=Shout`
- `Shout__WildMagic_Activate` - **Wild Magic Surge** | Your spellcasting can unleash unpredictable surges of untamed magic.
  <br>`SpellType=Shout`
- `Shout_EndlessRage` - **Endless Rage**
- `Shout_EndRage` - **End Rage**
  <br>`SpellProperties=RemoveStatus(SG_Rage);`
- `Shout_Rage`
- `Shout_Rage_Boar` - **Go into a frenzy, increasing your size and becoming stronger through raw anger.** | While raging, your melee attacks deal an additional [1]. You gain Resistance to physical damage, and Advantage on Strength Checks and Saving Throws.You can use Frenzied Strike.
  <br>`SpellType=Shout`  `SpellProperties=AI_IGNORE:ApplyStatus(RAGE_BOAR,100,10);AI_ONLY:IF(HasActionResource('ActionPoint', 1, 0, false)):ApplyStatus(AI_HELPER_RAGE,100,1);`
- `Shout_Rage_Frenzy` - **Your RAGE">Rage turns into a frenzy! You gain <LSTag**
- `Shout_Rage_Giant` - **Giant's Rage** | Enter a Rage and increase in size. Your Rage damage bonus is doubled on Throw attacks.
  <br>`SpellType=Shout`  `SpellProperties=AI_IGNORE:IF(not ClassLevelHigherOrEqualThan(9,'Barbarian')):ApplyStatus(RAGE_GIANT,100,10);AI_IGNORE:IF(ClassLevelHigherOrEqualThan(9,'Barbarian')):ApplyStatus(RAGE_GIANT_2,100,10…`
- `Shout_Rage_Totem_Bear` - **Rage: Bear Heart**
- `Shout_Rage_Totem_Eagle` - **Rage: Eagle Heart**

### `CX_Barbarian_Wildheart_Boost`  -  _martial_
_Currently in manager_ - passives: `MAG_ChargingTiger_RestoreMovement_Passive`, `TotemSpirit_Bear`; spells: `Shout_Rage_Totem_Bear`

**Passive candidates** (15 found)
- `TotemSpirit_Bear_Rage_Boosts` - **Bestial Heart: Bear Rage Bonuses**
  <br>`Boosts=Advantage(Ability, Strength);Advantage(SavingThrow, Strength);IF(IsAttackType(AttackType.MeleeWeaponAttack)): CharacterWeaponDamage(LevelMapValue(RageDamage));IF(IsAttackType(Attac…`
- `TotemSpirit_Bear_Rage_Boosts_2`
  <br>`Boosts=Advantage(Ability, Strength);Advantage(SavingThrow, Strength);IF(IsAttackType(AttackType.MeleeWeaponAttack)): CharacterWeaponDamage(LevelMapValue(RageDamage));IF(IsAttackType(Attac…`
- `TotemSpirit_Eagle` - **Eagle Heart** | While Raging, you can use Diving Strike.Foes also have Disadvantage on Opportunity Attacks against you, and you can use Dash as a bonus action.
  <br>`Boosts=UnlockSpell(Shout_Rage_Totem_Eagle);UnlockSpell(Projectile_DivingStrike)`
- `TotemSpirit_Eagle_Rage_Boosts` - **Bestial Heart: Eagle Rage Bonuses**
  <br>`Boosts=Advantage(Ability, Strength);Advantage(SavingThrow, Strength);Resistance(Slashing, Resistant);Resistance(Piercing, Resistant);Resistance(Bludgeoning, Resistant);IF(IsAttackType(Att…`
- `TotemSpirit_Eagle_Rage_Boosts_2`
  <br>`Boosts=Advantage(Ability, Strength);Advantage(SavingThrow, Strength);Resistance(Slashing, Resistant);Resistance(Piercing, Resistant);Resistance(Bludgeoning, Resistant);IF(IsAttackType(Att…`
- `TotemSpirit_Elk` - **Elk Heart** | While Raging, you can use Primal Stampede, and your movement speed increases by [1].
  <br>`Boosts=UnlockSpell(Shout_Rage_Totem_Elk);UnlockSpell(Rush_Primal_Stampede)`
- `TotemSpirit_Elk_Rage_Boosts` - **Bestial Heart: Elk Rage Bonuses**
  <br>`Boosts=Advantage(Ability, Strength);Advantage(SavingThrow, Strength);Resistance(Slashing, Resistant);Resistance(Piercing, Resistant);Resistance(Bludgeoning, Resistant);IF(IsAttackType(Att…`
- `TotemSpirit_Elk_Rage_Boosts_2`
  <br>`Boosts=Advantage(Ability, Strength);Advantage(SavingThrow, Strength);Resistance(Slashing, Resistant);Resistance(Piercing, Resistant);Resistance(Bludgeoning, Resistant);IF(IsAttackType(Att…`
- `TotemSpirit_Tiger` - **Tiger Heart** | While Raging, you can use Tiger's Bloodlust, and your jump distance increases by [1].
  <br>`Boosts=UnlockSpell(Shout_Rage_Totem_Tiger);UnlockSpell(Zone_TigersBloodlust)`
- `TotemSpirit_Tiger_Rage_Boosts` - **Bestial Heart: Tiger Rage Bonuses**
  <br>`Boosts=Advantage(Ability, Strength);Advantage(SavingThrow, Strength);Resistance(Slashing, Resistant);Resistance(Piercing, Resistant);Resistance(Bludgeoning, Resistant);IF(IsAttackType(Att…`
- `TotemSpirit_Tiger_Rage_Boosts_2`
  <br>`Boosts=Advantage(Ability, Strength);Advantage(SavingThrow, Strength);Resistance(Slashing, Resistant);Resistance(Piercing, Resistant);Resistance(Bludgeoning, Resistant);IF(IsAttackType(Att…`
- `TotemSpirit_Wolf` - **Wolf Heart** | While Raging, you can use Inciting Howl, and your allies have Advantage on melee Attack Rolls against enemies within [1] of you.
  <br>`Boosts=UnlockSpell(Shout_Rage_Totem_Wolf);UnlockSpell(Shout_PackHowl_Barbarian)`
- `TotemSpirit_Wolf_Rage_Boosts` - **Bestial Heart: Wolf Rage Bonuses**
  <br>`Boosts=Advantage(Ability, Strength);Advantage(SavingThrow, Strength);Resistance(Slashing, Resistant);Resistance(Piercing, Resistant);Resistance(Bludgeoning, Resistant);IF(IsAttackType(Att…`
- `TotemSpirit_Wolf_Rage_Boosts_2`
  <br>`Boosts=Advantage(Ability, Strength);Advantage(SavingThrow, Strength);Resistance(Slashing, Resistant);Resistance(Piercing, Resistant);Resistance(Bludgeoning, Resistant);IF(IsAttackType(Att…`
- `TotemSpirit_Bear` _(already in manager)_ - **Bear Heart** | While Raging, you can use Unrelenting Ferocity, and have Resistance to all damage except Psychic damage.
  <br>`Boosts=UnlockSpell(Shout_Rage_Totem_Bear);UnlockSpell(Shout_FerociousAppetite)`

**Spell candidates** (36 found, showing 14)
- `Shout_EndlessRage` - **Endless Rage**
- `Shout_EndRage` - **End Rage**
  <br>`SpellProperties=RemoveStatus(SG_Rage);`
- `Shout_GoadingRoar_Bear_Summon` - **Goading Roar** | Roar at nearby enemies to goad them into attacking you.
- `Shout_Rage`
- `Shout_Rage_Boar` - **Go into a frenzy, increasing your size and becoming stronger through raw anger.** | While raging, your melee attacks deal an additional [1]. You gain Resistance to physical damage, and Advantage on Strength Checks and Saving Throws.You can use Frenzied Strike.
  <br>`SpellType=Shout`  `SpellProperties=AI_IGNORE:ApplyStatus(RAGE_BOAR,100,10);AI_ONLY:IF(HasActionResource('ActionPoint', 1, 0, false)):ApplyStatus(AI_HELPER_RAGE,100,1);`
- `Shout_Rage_Frenzy` - **Your RAGE">Rage turns into a frenzy! You gain <LSTag**
- `Shout_Rage_Giant` - **Giant's Rage** | Enter a Rage and increase in size. Your Rage damage bonus is doubled on Throw attacks.
  <br>`SpellType=Shout`  `SpellProperties=AI_IGNORE:IF(not ClassLevelHigherOrEqualThan(9,'Barbarian')):ApplyStatus(RAGE_GIANT,100,10);AI_IGNORE:IF(ClassLevelHigherOrEqualThan(9,'Barbarian')):ApplyStatus(RAGE_GIANT_2,100,10…`
- `Shout_Rage_Totem_Eagle` - **Rage: Eagle Heart**
- `Shout_Rage_Totem_Elk` - **Rage: Elk Heart**
- `Shout_Rage_Totem_Tiger` - **Rage: Tiger Heart**
- `Shout_Rage_Totem_Wolf` - **Rage: Wolf Heart**
- `Shout_Rage_WildMagic` - **Rage: Wild Magic** | Enter a Rage that releases all the magic roiling inside of you, causing a random magical effect.
  <br>`SpellType=Shout`  `SpellProperties=AI_IGNORE:TriggerRandomCast(1,0,WildMagicBarbarian);IF(ClassLevelHigherOrEqualThan(1,'Barbarian') and not ClassLevelHigherOrEqualThan(9,'Barbarian')):ApplyStatus(RAGE,100,10);IF(Cl…`
- `Shout_Roar_Bear_Polar`
  <br>`SpellType=Shout`
- `Target_Rage_Sahuagin` - **Blood Frenzy** | The scent of blood sends the sahuagin into a Blood-scent Frenzy!
  <br>`SpellType=Target`  `SpellProperties=AI_IGNORE:ApplyStatus(SELF,RAGE_SAHUAGIN,100,6);AI_ONLY:ApplyStatus(SELF,AI_HELPER_BUFF_LARGE,100,2)`

---

## Bard

### `CX_Bard_Boost`  -  _caster_
_Currently in manager_ - passives: `ARP_BardicInspiration_3`, `BardSpellcasting`, `BardicInspiration`, `Goon_Summon_Potion_Healing_x1`; spells: `Goon_Target_Longstrider_Passive`, `Projectile_Jump`, `Shout_HealingWord_Mass`, `Target_HealingWord`, `Target_Shatter`, `Target_ViciousMockery`

**Passive candidates** (14 found)
- `BardicInspiration_Ability`
- `BardicInspiration_Ability_d10`
  <br>`Boosts=RollBonus(SkillCheck,1d10);RollBonus(RawAbility,1d10)`
- `BardicInspiration_Ability_d8`
- `BardicInspiration_d10`
- `BardicInspiration_d8` - **Improved Bardic Inspiration** | The bonus gained from Bardic Inspiration increases to +[1].
- `JackOfAllTrades` - **Jack of All Trades** | Your vast experiences make you more likely to succeed in any undertaking. Add half of your Proficiency Bonus (rounded down) to Ability Checks that you are not Proficient in.
  <br>`Boosts=IF(not HasProficiencyBonus(context.CheckedAbility,context.CheckedSkill,context.Source)):RollBonus(SkillCheck,ProficiencyBonus/2);IF(not HasProficiencyBonus(context.CheckedAbility,c…`
- `MAG_BardicInspiration_Heal_Hat_Passive` - **Soothing Songs** | When you inspire an ally using Bardic Inspiration, they also regain [1].
- `MAG_BardicInspiration_TempHP_Armor_Passive` - **Remedial Rhymes** | When you inspire an ally using Bardic Inspiration, you gain [1].
- `SCE_TieflingFollowup_BardicInspiration_Attack_Ability` - **Improved Bardic Inspiration: Attack Roll or Ability Check** | Add a +[1] bonus to your next Attack Roll or Ability Check.
  <br>`Boosts=RollBonus(SkillCheck,1d12);RollBonus(RawAbility,1d12);RollBonus(Attack,1d12)`
- `SCE_TieflingFollowup_BardicInspiration_SavingThrow` - **Improved Bardic Inspiration: Saving Throw** | Add a +[1] bonus to your next Saving Throw.
  <br>`Boosts=RollBonus(SavingThrow,1d12)`
- `FontOfInspiration` - **Font of Inspiration** | You regain all your Bardic Inspiration after a Long or Short Rest.
  <br>`Boosts=ActionResourceReplenishTypeOverride(BardicInspiration,ShortRest)`
- `MAG_WondrousGloves_Passive` - **Troubadour's Wonder** | Your Armour Class increases by [1]. In addition, if you have Bardic Inspiration, you gain [2] more use of it.
  <br>`Boosts=AC(1)`
- `TAD_Freecast` - **Freecast** | You have discovered a marvellous adaptability within yourself. Spell slots, charges, and similar resource costs for your next action or spell are removed. Refreshes after a Long Rest.
  <br>`Boosts=UnlockSpellVariant(FreecastCheck(),ModifyIconGlow(),ModifyTooltipDescription(),ModifyUseCosts(Replace,SpellSlot,0,-1,SpellSlot),ModifyUseCosts(Replace,Rage,0,0,Rage),ModifyUseCosts…`
- `BardicInspiration` _(already in manager)_ - **Bardic Inspiration** | Can use Bardic Inspiration.
  <br>`Boosts=UnlockSpell(Target_BardicInspiration)`

**Spell candidates** (17 found, showing 14)
- `Projectile_Potion_Destroy_Sleep` - **Potion of Sleep**
  <br>`SpellType=Projectile`  `SpellProperties=ApplyStatus(SLEEP,100,3,,,,not SavingThrow(Ability.Constitution,11, AdvantageOnPoisoned()))`
- `Projectile_Solution_Oil_Bane_Destroy` - **Oil of Bane**
  <br>`SpellType=Projectile`
- `Shout_Countercharm_Perform_ThePower` - **Countercharm**
- `Target_Bane`
  <br>`SpellSuccess=ApplyStatus(<em>BANE</em>, 100, 10)`
- `Target_Bane_Drider`
  <br>`SpellType=Target`
- `Target_Bane_ThiefOfFiveFates` - **Invocation: Bane**
  <br>`SpellType=Target`
- `Target_BanesWrath` - **Bane's Wrath**
- `Target_Countercharm` - **Countercharm**
- `Target_Eyebite_Asleep` - **Eyebite: Asleep**
- `Target_GlyphOfWarding_Sleep` - **Glyph of Warding: Sleep**
- `Target_Heroism`
  <br>`SpellProperties=ApplyStatus(<em>HEROISM</em>, 100, 10)`
- `Target_HideousLaughter` - **Tasha's Hideous Laughter** | Leave a creature Prone with laughter, without the ability to get up.
  <br>`SpellType=Target`  `SpellSuccess=ApplyStatus(HIDEOUS_LAUGHTER,100,10)`
- `Target_Sleep`
  <br>`SpellProperties=ApplyStatus(<em>SLEEP</em>,100,2)`
- `Target_Sleep_MindFlayer`
  <br>`SpellType=Target`

### `CX_Bard_Lore_Boost`  -  _caster_
_Currently in manager_ - passives: `Background_Entertainer`, `CuttingWords`; spells: `Target_DissonantWhispers`, `Target_MindSliver`, `Target_MindWhip`

**Passive candidates** (3 found)
- `BonusProficiencies` - **Additional Proficiencies** | You have additional proficiencies.
- `CollegeOfLore_Proficiency` - **Additional Proficiencies** | Gain Proficiency in Arcana, Intimidation and Sleight of Hand.
  <br>`Boosts=ProficiencyBonus(Skill,Arcana);ProficiencyBonus(Skill,Intimidation);ProficiencyBonus(Skill,SleightOfHand)`
- `CuttingWords` _(already in manager)_ - **Cutting Words** | Use your wit to distract a creature and sap its confidence.
  <br>`Boosts=UnlockInterrupt(Interrupt_CuttingWords)`

**Spell candidates** (17 found, showing 14)
- `Projectile_Solution_Oil_Bane_Destroy` - **Oil of Bane**
  <br>`SpellType=Projectile`
- `Target_Bane`
  <br>`SpellSuccess=ApplyStatus(<em>BANE</em>, 100, 10)`
- `Target_Bane_Drider`
  <br>`SpellType=Target`
- `Target_Bane_ThiefOfFiveFates` - **Invocation: Bane**
  <br>`SpellType=Target`
- `Target_BanesWrath` - **Bane's Wrath**
- `Target_Command_Approach` - **Command: Approach** | Command a creature to move towards you on its turn and do nothing else.
  <br>`SpellType=Target`  `SpellSuccess=ApplyStatus(COMMAND_APPROACH, 100, 1)`
- `Target_Command_Drop` - **Command: Drop** | Command a creature to drop its weapon.
  <br>`SpellType=Target`  `SpellSuccess=ApplyStatus(DISARM, 100, 1)`
- `Target_Command_Flee` - **Command: Flee** | Command a creature to flee from you on its turn and do nothing else.
  <br>`SpellType=Target`  `SpellSuccess=ApplyStatus(COMMAND_FLEE, 100, 1)`
- `Target_Command_Grovel` - **Command: Grovel** | Command a creature to fall Prone immediately.
  <br>`SpellType=Target`  `SpellSuccess=ApplyStatus(COMMAND_GROVEL, 100, 1)`
- `Target_Command_Halt` - **Command: Halt** | Command a creature to halt, preventing it from moving or taking any type of action.
- `Target_Counterspell` - **Counterspell**
- `Target_Counterspell_Failure` - **Failed Counterspell**
  <br>`SpellType=Target`
- `Target_CounterSpell_Mindflayer`
  <br>`SpellType=Target`
- `Target_Counterspell_Success` - **Nullify another creature's spell as a reaction. The spell must be 3rd Level or lower. If it is higher, you must succeed a Check to nullify it, the difficulty of which is based on the spell's Level.**
  <br>`SpellType=Target`

### `CX_Bard_Swords_Boost`  -  _hybrid_
_Currently in manager_ - passives: `FightingStyle_Dueling`, `FightingStyle_TwoWeaponFighting`, `MAG_ArcaneTrickster_Ring_Passive`; spells: `Projectile_BladeFlourish_Slashing`, `Shout_MirrorImage`, `Target_BladeFlourish_Defensive`, `Target_ViciousMockery`, `Zone_BladeFlourish_Slashing`

**Passive candidates** (3 found)
- `MAG_TwoWeaponFighting`
- `MAG_TheCrimson_TwoWeapon_Passive` - **Crimson Weapon**
  <br>`Boosts=TwoWeaponFighting()`
- `FightingStyle_TwoWeaponFighting` _(already in manager)_ - **Two-Weapon Fighting** | When you make an attack with your off-hand weapon, you can add your Ability Modifier to the damage of the attack.
  <br>`Boosts=TwoWeaponFighting()`

**Spell candidates** (10 found)
- `Projectile_BladeFlourish_Defensive` - **Defensive Flourish (Ranged)**
- `Projectile_BladeFlourish_Mobile` - **Mobile Flourish (Ranged)**
- `Target_BladeFlourish_Mobile` - **Mobile Flourish (Melee)**
- `Target_BladeFlourish_Mobile_FollowUp` - **Mobile Flourish: Teleport**
- `Target_DirtyTrick_Vicious`
  <br>`SpellSuccess=ApplyStatus(<em>VICIOUSMOCKERY</em>,100,1);DealDamage(LevelMapValue(D4Cantrip),Psychic,Magical);ApplyStatus(SELF,SWASHBUCKLER_ADV,100,2);`
- `Target_OpeningAttack` - **Flourish**
- `Projectile_BladeFlourish_Slashing` _(already in manager)_ - **Slashing Flourish (Ranged)**
- `Target_BladeFlourish_Defensive` _(already in manager)_ - **Defensive Flourish (Melee)**
- `Target_ViciousMockery` _(already in manager)_
  <br>`SpellSuccess=ApplyStatus(<em>VICIOUSMOCKERY</em>,100,1);DealDamage(LevelMapValue(D4Cantrip),Psychic,Magical)`
- `Zone_BladeFlourish_Slashing` _(already in manager)_ - **Slashing Flourish (Melee)**

### `CX_Bard_Valor_Boost`  -  _hybrid_
_Currently in manager_ - passives: `DualWielder_BonusAC`, `FightingStyle_Dueling`, `FightingStyle_TwoWeaponFighting`, `ModeratelyArmored`; spells: `Shout_BladeWard`, `Shout_HealingWord_Mass`, `Shout_MirrorImage`, `Target_FaerieFire`

**Passive candidates** (16 found)
- `CombatInspiration` - **Combat Inspiration** | Can use Combat Inspiration.
  <br>`Boosts=UnlockSpell(Target_BardicInspiration_Combat)`
- `CombatInspiration_Ability` - **Valiant Roll** | Add a +[1] bonus to your next Ability Check.
  <br>`Boosts=RollBonus(SkillCheck,1d6);RollBonus(RawAbility,1d6)`
- `CombatInspiration_Ability_d10`
  <br>`Boosts=RollBonus(SkillCheck,1d10);RollBonus(RawAbility,1d10)`
- `CombatInspiration_Ability_d8` - **Valiant Roll** | Add a +[1] bonus to your next Ability Check.
  <br>`Boosts=RollBonus(SkillCheck,1d8);RollBonus(RawAbility,1d8)`
- `ExtraAttack`
- `ExtraAttack_2` - **Improved Extra Attack** | You can make two additional attacks after attacking with your main-hand weapon.
- `ExtraAttack_BonusTechnical`
- `LOW_Guildhall_ExtraAttack_DaggerSpecialist` - **Dagger Specialist** | This creature can throw up to 3 daggers per round.
- `Slayer_ExtraAttack`
- `Slayer_ExtraAttack_2`
- `BestialFury` - **Bestial Fury** | Your bond with your companion has deepened, unlocking their inner strength and giving them an Extra Attack.
- `GOB_Boss_RecklessAttack` - **Crude Frenzy** | This goblin can make an additional free attack after making a Main Hand Attack, but the second attack has Disadvantage on its Attack Roll.
- `ThirstingBlade_Blade`
- `ThirstingBlade_Check` - **The Extra Attack gained by this feature doesn't stack with Extra Attacks gained from other class levels.**
- `WarPriest` - **War Priest** | When you make an unarmed or weapon attack, you can spend a War Priest Charge to make an additional attack as a bonus action.
- `WildStrike` - **Wild Strike** | You can make an additional attack after making an Unarmed Strike while in Wild Shape.

**Spell candidates** (5 found)
- `Target_Bless`
  <br>`SpellProperties=ApplyStatus(<em>BLESS</em>, 100, 10)`
- `Target_Haste`
  <br>`SpellProperties=ApplyStatus(<em>HASTE</em>,100,10)`
- `Target_Heroism`
  <br>`SpellProperties=ApplyStatus(<em>HEROISM</em>, 100, 10)`
- `Projectile_WhiteSporeCloud` - **Haste Spores**
- `Shout_BurningRage_Myrmidon_Fire` - **Ignite with incandescent, primordial flames that HASTE">Hasten you.**

---

## Cleric

### `CX_Cleric_Boost`  -  _caster_
_Currently in manager_ - passives: `ARP_ChannelDivinity_1`; spells: `Projectile_Jump`, `Projectile_Moonflare`, `Shout_HealingWord_Mass`, `Target_HealingWord`, `Target_InflictWounds`, `Target_SacredFlame`

**Passive candidates** (9 found)
- `DestroyUndead` - **Destroy Undead** | When you successfully Turn an undead creature, it also takes [1].
- `DivineIntervention` - **Divine Intervention** | You can cast Divine Intervention to invoke your God's aid. Once used, this can never be used again.
  <br>`Boosts=Tag(DIVINE_INTERVENTION)`
- `DestructiveWrath` - **Destructive Wrath** | When you roll Thunder or Lightning damage, you can use your Channel Divinity to deal maximum damage instead.
  <br>`Boosts=UnlockInterrupt(Interrupt_DestructiveWrath)`
- `Guided_Strike` - **Channel Divinity: Guided Strike** | Channel the guidance of your god to strike with supernatural accuracy. You gain a +[1] bonus to your Attack Roll.
  <br>`Boosts=UnlockSpell(Shout_GuidedStrike)`
- `Guided_Strike_Toggle`
- `MAG_OfTheDevout_Amulet_Passive` - **Godswill** | You gain an additional use of Channel Divinity. Once used, it is restored upon taking a Long Rest.
- `TAD_Freecast` - **Freecast** | You have discovered a marvellous adaptability within yourself. Spell slots, charges, and similar resource costs for your next action or spell are removed. Refreshes after a Long Rest.
  <br>`Boosts=UnlockSpellVariant(FreecastCheck(),ModifyIconGlow(),ModifyTooltipDescription(),ModifyUseCosts(Replace,SpellSlot,0,-1,SpellSlot),ModifyUseCosts(Replace,Rage,0,0,Rage),ModifyUseCosts…`
- `TouchOfDeath` - **Channel Divinity: Touch of Death** | When you hit a creature with a melee attack, you can use your Channel Divinity to deal extra Necrotic damage.
  <br>`Boosts=UnlockInterrupt(Interrupt_ChannelDivinity_TouchOfDeath)`
- `WarGodsBlessing` - **Channel Divinity: War God's Blessing** | Endow a nearby ally with the glory of your god to grant them a +[1] bonus to their Attack Roll.
  <br>`Boosts=UnlockInterrupt(Interrupt_WarGodsBlessing)`

**Spell candidates** (9 found)
- `Shout_SpiritGuardians` - **Spirit Guardians** | Call forth spirits to protect you. Nearby enemies take [1] or [2] per turn, and their movement speed is halved.
  <br>`SpellType=Shout`
- `Shout_SpiritGuardians_Necrotic` - **Call forth spirits to protect the area around you.** | Nearby enemies take [1] per turn, and their movement speed is halved.
  <br>`SpellType=Shout`  `SpellProperties=ApplyStatus(SPIRIT_GUARDIANS_NECROTIC_AURA,100,10)`
- `Shout_SpiritGuardians_Radiant` - **Call forth spirits to protect the area around you.** | Nearby enemies take [1] per turn, and their movement speed is halved.
  <br>`SpellType=Shout`  `SpellProperties=ApplyStatus(SPIRIT_GUARDIANS_RADIANT_AURA,100,10)`
- `Shout_TurnUndead` - **Turn Undead** | Pray to Turn all undead that can see you.
  <br>`SpellType=Shout`  `SpellSuccess=ApplyStatus(TURNED, 100, 3)`
- `Target_Bless`
  <br>`SpellProperties=ApplyStatus(<em>BLESS</em>, 100, 10)`
- `Target_GuardianOfFaith` - **Guardian of Faith** | Call forth a divine guardian that attacks nearby enemies. Every time it deals damage, the guardian loses an equal amount of hit points.
  <br>`SpellType=Target`  `SpellProperties=GROUND:IF(Tagged('ALIGN_GOOD',context.Source)):Summon(4c90b3c1-55dd-4b7e-b08f-8d7cc15f8d41, 10,Projectile_AiHelper_Summon_Strong,,'GuardianOfFaithStack',GUARDIAN_OF_FAITH_AURA,SHAD…`
- `Target_HoldPerson` - **Hold Person** | Hold a humanoid enemy still. They can't move, act or react. Attacks from within [1] are always Critical Hits.
  <br>`SpellType=Target`  `SpellSuccess=ApplyStatus(HOLD_PERSON,100,10)`
- `Target_HoldPerson_Redcap`
  <br>`SpellType=Target`
- `Target_MainHandAttack_GuardianOfFaith` - **Strike of the Guardian** | Channel the power of your deity in your sword strike to protect the cleric that brought you into being.
  <br>`SpellType=Target`  `SpellSuccess=DealDamage(20,Radiant,Magical);AI_IGNORE:DealDamage(SELF,20,Radiant,Magical)`

### `CX_Cleric_Knowledge_Boost`  -  _caster_
_Currently in manager_ - passives: `MAG_SpellSaveDC_Enchantment_Passive`; spells: `Target_CalmEmotions`, `Target_HypnoticPattern`, `Target_MindSpik`, `Target_Sleep`

**Passive candidates** (2 found)
- `BlessingsOfKnowledge` - **Blessings of Knowledge** | Become Proficient in two of the following Skills: Arcana, History, Nature, or Religion. Your Proficiency Bonus is doubled for Ability Checks made using these Skills.
- `Doppelganger_ReadThoughts` - **Mindreader** | Ranged attacks have Disadvantage against this creature.

**Spell candidates** (18 found, showing 14)
- `Projectile_Solution_Oil_Bane_Destroy` - **Oil of Bane**
  <br>`SpellType=Projectile`
- `Shout_DetectThoughts` - **Detect Thoughts** | Focus your mind to read the thoughts of certain creatures while talking to them.
  <br>`SpellType=Shout`  `SpellProperties=ApplyStatus(DETECT_THOUGHTS,100,-1)`
- `Target_Bane`
  <br>`SpellSuccess=ApplyStatus(<em>BANE</em>, 100, 10)`
- `Target_Bane_Drider`
  <br>`SpellType=Target`
- `Target_Bane_ThiefOfFiveFates` - **Invocation: Bane**
  <br>`SpellType=Target`
- `Target_BanesWrath` - **Bane's Wrath**
- `Target_Command_Approach` - **Command: Approach** | Command a creature to move towards you on its turn and do nothing else.
  <br>`SpellType=Target`  `SpellSuccess=ApplyStatus(COMMAND_APPROACH, 100, 1)`
- `Target_Command_Drop` - **Command: Drop** | Command a creature to drop its weapon.
  <br>`SpellType=Target`  `SpellSuccess=ApplyStatus(DISARM, 100, 1)`
- `Target_Command_Flee` - **Command: Flee** | Command a creature to flee from you on its turn and do nothing else.
  <br>`SpellType=Target`  `SpellSuccess=ApplyStatus(COMMAND_FLEE, 100, 1)`
- `Target_Command_Grovel` - **Command: Grovel** | Command a creature to fall Prone immediately.
  <br>`SpellType=Target`  `SpellSuccess=ApplyStatus(COMMAND_GROVEL, 100, 1)`
- `Target_Command_Halt` - **Command: Halt** | Command a creature to halt, preventing it from moving or taking any type of action.
- `Target_Counterspell` - **Counterspell**
- `Target_Counterspell_Failure` - **Failed Counterspell**
  <br>`SpellType=Target`
- `Target_CounterSpell_Mindflayer`
  <br>`SpellType=Target`

### `CX_Cleric_Life_Boost`  -  _caster_
_Currently in manager_ - passives: `BlessedHealer`, `DiscipleOfLife`, `UND_SocietyOfBrilliance_PullingRing_Passive`; spells: `Shout_BladeWard`, `Shout_HealingWord_Mass`, `Shout_PreserveLife`, `Target_CureWounds`, `Target_LesserRestoration`, `Target_Sanctuary`

**Passive candidates** (2 found)
- `BlessedHealer` _(already in manager)_ - **Blessed Healer** | Healing others heals you as well.When you cast a healing spell of Level 1 or higher on another creature, you regain hit points equal to 2 + the spell's level.
- `DiscipleOfLife` _(already in manager)_ - **Disciple of Life** | Your devotion empowers your healing spells. When casting a healing spell, the target regains additional hit points equal to 2 + the spell's level.

**Spell candidates** (23 found, showing 14)
- `Projectile_WildMagic_Heal`
  <br>`SpellType=Projectile`  `SpellProperties=RegainHitPoints(1d4)`
- `Shout_HealingRadiance_Heal` - **Heal yourself and all nearby allies for [1]. Regain another [1] next turn.**
- `Shout_WildMagic_Heal` - **When you hit a target with a spell, heal all creatures within [1] for [2] per spell slot level used.**
- `Shout_WildShape_Combat_Heal` - **Lunar Mend** | Expend spell slots to regain hit points while in Wild Shape.
  <br>`SpellType=Shout`
- `Shout_WildShape_Combat_Heal_1` - **Expend a Level 1 spell slot to heal yourself.**
- `Target_CureWounds_Mass` - **Mass Cure Wounds** | Unleash a soothing hum of energy that heals you and nearby allies.
  <br>`SpellType=Target`  `SpellProperties=RegainHitPoints(3d8+SpellCastingAbilityModifier)`
- `Target_Heal` - **Heal** | Heal a target's wounds and remove Blindness and any diseases.
- `Target_Healer_Heal` - **Seal Wounds** | Seal an ally's wounds shut, as if closing a door upon their pain.
  <br>`SpellType=Target`  `SpellProperties=RegainHitPoints(1d6+4+Level); ApplyStatus(HEALER_HEALED,100,-1)`
- `Target_HealingWord` - **Healing Word** | Heal a creature you can see.
  <br>`SpellType=Target`  `SpellProperties=RegainHitPoints(1d4+SpellCastingAbilityModifier)`
- `Target_StarryForm_Chalice_Heal` - **Heal yourself or another creature within reach.**
- `Teleportation_Revivify` - **Revivify**
- `Teleportation_Revivify_Deva` - **Revivify**
- `Teleportation_Revivify_Scroll`
  <br>`SpellType=Teleportation`
- `Shout_CursedTome_Seelie_Wildshape`

### `CX_Cleric_Light_Boost`  -  _caster_
_Currently in manager_ - passives: `WardingFlare`, `WardingFlare_Improved`; spells: `Projectile_ChromaticOrb_Fire`, `Projectile_FireBolt`, `Projectile_Fireball`, `Projectile_Moonflare`, `Shout_RadianceOfTheDawn`, `Target_FlamingSphere`

**Passive candidates** (2 found)
- `WardingFlare` _(already in manager)_ - **Warding Flare** | Shield yourself with divine light. Use your reaction to impose Disadvantage on an attacker, possibly causing their attack to miss.
  <br>`Boosts=UnlockInterrupt(Interrupt_WardingFlare)`
- `WardingFlare_Improved` _(already in manager)_ - **Improved Warding Flare** | When an enemy attacks an ally, you can use your reaction to impose Disadvantage on the Attack Roll, possibly causing their attack to miss.
  <br>`Boosts=UnlockInterrupt(Interrupt_WardingFlare_Improved)`

**Spell candidates** (11 found)
- `Projectile_Fireball_Dragon` - **Fire Breath**
  <br>`SpellType=Projectile`  `SpellSuccess=DealDamage(14d6,Fire,Magical);ApplyStatus(BURNING,100,2)`
- `Projectile_ScorchingRay` - **Scorching Ray** | Hurl [2] rays of fire. Each ray deals [1].
  <br>`SpellType=Projectile`  `SpellSuccess=DealDamage(2d6,Fire,Magical)`  `SpellProperties=GROUND:SurfaceChange(Ignite);GROUND:SurfaceChange(Melt)`
- `Projectile_ScorchingRay_CircletOfBlasting`
  <br>`SpellType=Projectile`
- `Target_Daylight`
  <br>`SpellProperties=GROUND:Summon(f662449b-057a-477c-a80e-9083aff62b00, -1,,,<em>Daylight</em>,DAYLIGHT_GROUND);GROUND:SurfaceChange(<em>Daylight</em>)`
- `Target_Daylight_Enchantment`
  <br>`SpellProperties=GROUND:SurfaceChange(<em>Daylight</em>,100,0,100,15)`
- `Target_FaerieFire` - **Faerie Fire** | All targets within the light turn visible, and Attack Rolls against them have Advantage.
  <br>`SpellType=Target`  `SpellSuccess=ApplyStatus(FAERIE_FIRE, 100, 10)`
- `Target_FaerieFire_Drider`
  <br>`SpellType=Target`
- `Target_FaerieFire_DrowMagic` - **Drow Magic: Faerie Fire**
  <br>`SpellType=Target`
- `Target_StrengthDrain_Shadow` - **If the target is in bright light or daylight, it makes its Saving Throw with Advantage.**
- `Projectile_Fireball` _(already in manager)_ - **Fireball**
- `Shout_RadianceOfTheDawn` _(already in manager)_ - **Radiance of the Dawn** | The sun's divine power dispels any magical darkness.
  <br>`SpellType=Shout`  `SpellSuccess=DealDamage(2d10+Level,Radiant,Magical)`  `SpellProperties=GROUND:SurfaceChange(Daylight)`

### `CX_Cleric_Nature_Boost`  -  _caster_
_Currently in manager_ - passives: `DampenElements`; spells: `Target_DampenElements_Interrupt`, `Target_Entangle`, `Target_PlantGrowth`, `Target_SpikeGrowth`, `Target_ThornWhip`

**Passive candidates** (8 found)
- `AcolyteOfNature` - **Acolyte of Nature** | You learn a druid cantrip, and become Proficient in Animal Handling, Nature, or Survival.
- `DampenElements_Check`
- `Divine_Strike_Life_Toggle`
  <br>`Boosts=UnlockInterrupt(Interrupt_DivineStrike_Radiant);UnlockInterrupt(Interrupt_DivineStrike_Radiant_Critical);ActionResource(Interrupt_DivineStrike,1,0)`
- `Divine_Strike_Nature_Toggle`
  <br>`Boosts=UnlockInterrupt(Interrupt_DivineStrike_Cold);UnlockInterrupt(Interrupt_DivineStrike_Cold_Critical);UnlockInterrupt(Interrupt_DivineStrike_Fire);UnlockInterrupt(Interrupt_DivineStri…`
- `Divine_Strike_Tempest_Toggle`
  <br>`Boosts=UnlockInterrupt(Interrupt_DivineStrike_Thunder);UnlockInterrupt(Interrupt_DivineStrike_Thunder_Critical);ActionResource(Interrupt_DivineStrike,1,0)`
- `Divine_Strike_Trickery_Toggle`
  <br>`Boosts=UnlockInterrupt(Interrupt_DivineStrike_Poison);UnlockInterrupt(Interrupt_DivineStrike_Poison_Critical);ActionResource(Interrupt_DivineStrike,1,0)`
- `Divine_Strike_War_Toggle`
  <br>`Boosts=UnlockInterrupt(Interrupt_DivineStrike_MeleeWeapon);UnlockInterrupt(Interrupt_DivineStrike_MeleeWeapon_Critical);UnlockInterrupt(Interrupt_DivineStrike_RangedWeapon);UnlockInterrup…`
- `DampenElements` _(already in manager)_ - **Dampen Elements** | When you or an ally gets hit with Acid, Cold, Fire, Lightning, or Thunder damage, you can use your reaction to halve the attack's damage.
  <br>`Boosts=UnlockInterrupt(Interrupt_DampenElements)`

**Spell candidates** (10 found)
- `Shout_WildMagic_SpikeGrowth` - **Wild Magic: Spike Growth** | Shape a piece of ground around yourself into hard spikes. A creature walking on the spikes takes [1] for every [2] it moves.
  <br>`SpellType=Shout`  `SpellProperties=GROUND:CreateSurface(4,3,SpikeGrowth)`
- `Target_Barkskin`
  <br>`SpellProperties=ApplyStatus(<em>BARKSKIN</em>,100,-1)`
- `Target_CallLightning` - **Call Lightning** | Lightning strikes all targets within range. Then for 10 turns, you can call down lightning again without expending a spell slot.
  <br>`SpellType=Target`  `SpellSuccess=DealDamage(3d10,Lightning,Magical)`  `SpellProperties=GROUND:ApplyStatus(SELF,CALL_LIGHTNING_TECHNICAL,100,10);GROUND:SurfaceChange(Electrify)`
- `Target_CallLightning_LightningBolt` - **Activate Call Lightning** | Call down more lightning to hit all targets within range.
  <br>`SpellType=Target`  `SpellProperties=GROUND:SurfaceChange(Electrify);RemoveStatus(SELF,SANCTUARY);RemoveStatus(SELF,SANCTUARY_TRANQUILITY);`
- `Target_CharmPerson` - **Charm Person** | Charm a humanoid to prevent it from attacking you. You gain Advantage on Charisma Checks in dialogue.
  <br>`SpellType=Target`  `SpellSuccess=ApplyStatus(CHARMED,100,10)`
- `Target_CharmPerson_Cultist`
  <br>`SpellType=Target`
- `Target_CharmPerson_Vampire`
  <br>`SpellType=Target`
- `Target_SpikeGrowth_Dryad`
  <br>`SpellType=Target`
- `Zone_Thunderwave` - **Thunderwave**
- `Target_SpikeGrowth` _(already in manager)_
  <br>`SpellProperties=GROUND:CreateSurface(6,100,<em>SpikeGrowth</em>,true)`

### `CX_Cleric_Trickery_Boost`  -  _caster_
_Currently in manager_ - passives: `Goon_Target_ShieldOfFaith_Passive`, `MAG_Poison_PoisonExposure_Gloves_Passive`; spells: `Projectile_RayOfSickness`, `Shout_CloakOfShadows`, `Shout_MirrorImage`, `Target_HoldPerson`, `Target_InvokeDuplicity`, `Target_PoisonSpray`

**Passive candidates** (5 found)
- `Divine_Strike_Life_Toggle`
  <br>`Boosts=UnlockInterrupt(Interrupt_DivineStrike_Radiant);UnlockInterrupt(Interrupt_DivineStrike_Radiant_Critical);ActionResource(Interrupt_DivineStrike,1,0)`
- `Divine_Strike_Nature_Toggle`
  <br>`Boosts=UnlockInterrupt(Interrupt_DivineStrike_Cold);UnlockInterrupt(Interrupt_DivineStrike_Cold_Critical);UnlockInterrupt(Interrupt_DivineStrike_Fire);UnlockInterrupt(Interrupt_DivineStri…`
- `Divine_Strike_Tempest_Toggle`
  <br>`Boosts=UnlockInterrupt(Interrupt_DivineStrike_Thunder);UnlockInterrupt(Interrupt_DivineStrike_Thunder_Critical);ActionResource(Interrupt_DivineStrike,1,0)`
- `Divine_Strike_Trickery_Toggle`
  <br>`Boosts=UnlockInterrupt(Interrupt_DivineStrike_Poison);UnlockInterrupt(Interrupt_DivineStrike_Poison_Critical);ActionResource(Interrupt_DivineStrike,1,0)`
- `Divine_Strike_War_Toggle`
  <br>`Boosts=UnlockInterrupt(Interrupt_DivineStrike_MeleeWeapon);UnlockInterrupt(Interrupt_DivineStrike_MeleeWeapon_Critical);UnlockInterrupt(Interrupt_DivineStrike_RangedWeapon);UnlockInterrup…`

**Spell candidates** (25 found, showing 14)
- `Projectile_Potion_Destroy_Invisibility` - **Potion of Invisibility**
  <br>`SpellType=Projectile`  `SpellProperties=GROUND:CreateSurface(1,,PotionInvisibilityCloud);`
- `Shout_Blur` - **Blur**
  <br>`SpellProperties=ApplyStatus(<em>BLUR</em>,100,10)`
- `Shout_Invisibility_Duergar`
  <br>`SpellType=Shout`
- `Shout_Invisibility_Imp`
  <br>`SpellProperties=AI_IGNORE:ApplyStatus(<em>INVISIBILITY</em>,100,-1);AI_ONLY:ApplyStatus(<em>INVISIBILITY</em>,100,2);`
- `Shout_Invisibility_MistyEscape` - **Cloaking Mist** | Turn Invisible after casting Misty Step.
  <br>`SpellType=Shout`  `SpellProperties=ApplyStatus(MISTY_ESCAPE_INVISIBLE,100,1);`
- `Shout_Invisibility_Myrmidon_Air` - **Invisibility**
- `Shout_Invisibility_Quasit`
  <br>`SpellType=Shout`
- `Shout_Invisibility_ShadarKai_GloomWeaver` - **Invisibility** | Become Invisible. The spell ends if you attack, take an action or take damage.
  <br>`SpellType=Shout`  `SpellProperties=ApplyStatus(INVISIBILITY_SHADARKAI_GLOOMWEAVER,100,1);`
- `Shout_InvisibilityField_Orthon`
  <br>`SpellProperties=ApplyStatus(<em>INVISIBILITY</em>,100,2);`
- `Shout_PassWithoutTrace` - **Pass Without Trace** | Call forth a veil of shadows and silence that gives you and all nearby companions a +10 bonus to Stealth Checks.
  <br>`SpellType=Shout`  `SpellProperties=ApplyStatus(PASS_WITHOUT_TRACE_AURA, 100, -1)`
- `Shout_SeeInvisibility` - **See Invisibility**
- `Shout_SeeInvisibility_ThirdEye` - **Third Eye: See Invisibility**
- `Shout_SeeInvisibility_TrainedEye` - **See Invisibility**
- `Shout_WildMagic_Blur` - **Wild Magic: Blur**
  <br>`SpellProperties=ApplyStatus(<em>BLUR</em>,100,3)`

### `CX_Cleric_Tempest_Boost`  -  _caster_
_Currently in manager_ - passives: `ElementalAdept_Lightning`, `WarCaster_OpportunitySpell`, `WrathOfTheStorm_Thunder_NPC`; spells: `DestructiveWrath`, `Target_CallLightning`, `Zone_RimesBindingIce`, `Zone_Thunderwave`

**Passive candidates** (3 found)
- `DestructiveWrath` - **Destructive Wrath** | When you roll Thunder or Lightning damage, you can use your Channel Divinity to deal maximum damage instead.
  <br>`Boosts=UnlockInterrupt(Interrupt_DestructiveWrath)`
- `ThunderboltStrike` - **Thunderbolt Strike** | When you deal Lightning or Thunder damage to a creature that is Large or smaller, you can also push it up to [1].
- `WrathOfTheStorm` - **Wrath of the Storm** | As a reaction strike back at an attacking creature, dealing [1] or [2]. The target takes half damage on a successful Saving Throw.
  <br>`Boosts=UnlockInterrupt(Interrupt_WrathOfTheStorm_Lightning);UnlockInterrupt(Interrupt_WrathOfTheStorm_Thunder)`

**Spell candidates** (12 found)
- `Target_CallLightning_LightningBolt` - **Activate Call Lightning** | Call down more lightning to hit all targets within range.
  <br>`SpellType=Target`  `SpellProperties=GROUND:SurfaceChange(Electrify);RemoveStatus(SELF,SANCTUARY);RemoveStatus(SELF,SANCTUARY_TRANQUILITY);`
- `Target_Shatter` - **Shatter**
- `Target_ShockingGrasp` - **Shocking Grasp**
- `Target_WrathOfTheStorm_Lightning` - **Wrath of the Storm: Lightning** | Conflagrate a foe with electric bolts.
  <br>`SpellType=Target`  `SpellSuccess=DealDamage(2d8,Lightning,Magical)`
- `Target_WrathOfTheStorm_Thunder` - **Wrath of the Storm: Thunder**
  <br>`SpellType=Target`  `SpellSuccess=DealDamage(2d8,Thunder,Magical)`
- `Zone_LightningBolt` - **Lightning Bolt** | Call forth a blast of lightning that hits all creatures in the line of the eruption.
  <br>`SpellType=Zone`  `SpellSuccess=DealDamage(8d6,Lightning,Magical)`
- `Projectile_SuperNova_Dragon_Skeletal` - **Blast the entire arena with an explosion of lightning, possibly Shocking your foes.**
- `Shout_MixChangeExplosion_Lightning_Brewer` - **Shocking Overflow**
- `Shout_Shapechanger_Doppelganger_Dismiss_Urgent` - **Undergo a shocking transformation to startle your foes. Successf**
- `Shout_Whirlwind_Elemental_Air` - **Gales of crackling stormy wind swirl around you, battering at nearby creatures and Shocking them.**
- `Target_CallLightning` _(already in manager)_ - **Call Lightning** | Lightning strikes all targets within range. Then for 10 turns, you can call down lightning again without expending a spell slot.
  <br>`SpellType=Target`  `SpellSuccess=DealDamage(3d10,Lightning,Magical)`  `SpellProperties=GROUND:ApplyStatus(SELF,CALL_LIGHTNING_TECHNICAL,100,10);GROUND:SurfaceChange(Electrify)`
- `Zone_Thunderwave` _(already in manager)_ - **Thunderwave**

### `CX_Cleric_War_Boost`  -  _hybrid_
_Currently in manager_ - passives: `ExtraAttack`, `WarGodsBlessing`; spells: `Shout_GuidedStrike`, `Target_GreenFlameBlade`, `Target_Smite_Searing`, `Target_SpiritualWeapon`

**Passive candidates** (7 found)
- `WarPriest` - **War Priest** | When you make an unarmed or weapon attack, you can spend a War Priest Charge to make an additional attack as a bonus action.
- `Divine_Strike_Life_Toggle`
  <br>`Boosts=UnlockInterrupt(Interrupt_DivineStrike_Radiant);UnlockInterrupt(Interrupt_DivineStrike_Radiant_Critical);ActionResource(Interrupt_DivineStrike,1,0)`
- `Divine_Strike_Nature_Toggle`
  <br>`Boosts=UnlockInterrupt(Interrupt_DivineStrike_Cold);UnlockInterrupt(Interrupt_DivineStrike_Cold_Critical);UnlockInterrupt(Interrupt_DivineStrike_Fire);UnlockInterrupt(Interrupt_DivineStri…`
- `Divine_Strike_Tempest_Toggle`
  <br>`Boosts=UnlockInterrupt(Interrupt_DivineStrike_Thunder);UnlockInterrupt(Interrupt_DivineStrike_Thunder_Critical);ActionResource(Interrupt_DivineStrike,1,0)`
- `Divine_Strike_Trickery_Toggle`
  <br>`Boosts=UnlockInterrupt(Interrupt_DivineStrike_Poison);UnlockInterrupt(Interrupt_DivineStrike_Poison_Critical);ActionResource(Interrupt_DivineStrike,1,0)`
- `Divine_Strike_War_Toggle`
  <br>`Boosts=UnlockInterrupt(Interrupt_DivineStrike_MeleeWeapon);UnlockInterrupt(Interrupt_DivineStrike_MeleeWeapon_Critical);UnlockInterrupt(Interrupt_DivineStrike_RangedWeapon);UnlockInterrup…`
- `WarGodsBlessing` _(already in manager)_ - **Channel Divinity: War God's Blessing** | Endow a nearby ally with the glory of your god to grant them a +[1] bonus to their Attack Roll.
  <br>`Boosts=UnlockInterrupt(Interrupt_WarGodsBlessing)`

**Spell candidates** (24 found, showing 14)
- `Projectile_Fly_SpiritualWeapon`
  <br>`SpellType=Projectile`
- `Shout_CrusadersMantle` - **Crusader's Mantle** | Radiate a holy power that emboldens you and nearby allies. You and your allies' weapon attacks deal an additional [1].
  <br>`SpellType=Shout`  `SpellProperties=AI_IGNORE:ApplyStatus(CRUSADERS_MANTLE,100,10);AI_ONLY:IF(not HasStatus('CRUSADERS_MANTLE')):ApplyStatus(AI_HELPER_BUFF_LARGE,100,4)`
- `Target_Bless`
  <br>`SpellProperties=ApplyStatus(<em>BLESS</em>, 100, 10)`
- `Target_ConcussiveSmash_SpiritualWeapon_Maul`
  <br>`SpellType=Target`  `SpellSuccess=IF(Character() and not SavingThrow(Ability.Constitution, HybridCasterWeaponActionDC())):ApplyStatus(DAZED,100,2);DealDamage(UnarmedDamage+Owner.SpellCastingAbilityModifier , Force)`
- `Target_MainHandAttack_SpiritualWeapon_Greataxe` - **Greataxe Slash** | Cleave into a target with your mighty head.
  <br>`SpellType=Target`  `SpellSuccess=DealDamage(UnarmedDamage+Owner.SpellCastingAbilityModifier , Force,Magical)`
- `Target_MainHandAttack_SpiritualWeapon_Greatsword` - **Greatsword Slash** | Slice into a target with your holy blade.
  <br>`SpellType=Target`
- `Target_MainHandAttack_SpiritualWeapon_Halberd` - **Halberd Slash** | Cleave into a target with your glorious blade.
  <br>`SpellType=Target`
- `Target_MainHandAttack_SpiritualWeapon_Maul` - **Maul Blow** | Smash into a target with your mighty head.
  <br>`SpellType=Target`
- `Target_MainHandAttack_SpiritualWeapon_Spear` - **Spear Thrust** | Skewer a target upon your holy spike.
  <br>`SpellType=Target`
- `Target_MainHandAttack_SpiritualWeapon_Trident` - **Trident Thrust** | Plunge your glorious spikes into a target.
  <br>`SpellType=Target`
- `Target_PiercingThrust_SpiritualWeapon_Spear`
  <br>`SpellType=Target`
- `Target_PiercingThrust_SpiritualWeapon_Trident`
  <br>`SpellType=Target`  `SpellSuccess=IF(not SavingThrow(Ability.Constitution, ManeuverSaveDC()+2)):ApplyStatus(GAPING_WOUND,100,2);DealDamage(UnarmedDamage+Owner.SpellCastingAbilityModifier , Force,Magical)`
- `Target_ShieldOfFaith` - **Shield of Faith** | Protect a creature from attacks: increase its Armour Class by 2.
  <br>`SpellType=Target`  `SpellProperties=ApplyStatus(SHIELD_OF_FAITH,100,-1)`
- `Target_Slash_SpiritualWeapon_Greataxe`
  <br>`SpellType=Target`  `SpellSuccess=IF(not SavingThrow(Ability.Constitution, ManeuverSaveDC()+2)):ApplyStatus(BLEEDING,100,2);DealDamage(UnarmedDamage+Owner.SpellCastingAbilityModifier , Force)`

---

## Druid

### `CX_Druid_Boost`  -  _caster_
_Currently in manager_ - passives: `DEN_FaithwardenStaff_Passive`, `Goon_Shout_Shillelagh_Passive`, `MAG_Druid_Nature_Regeneration_Passive`; spells: `Projectile_Jump`, `Target_HealingWord`

**Passive candidates** (7 found)
- `ExposingBite_Wildshape`
- `MAG_Druid_ExtraWildShape_Passive` - **Nature's Embrace** | Increase your Wild Shape charge by [1]. This additional charge is restored upon taking a Long Rest.
- `MAG_Druid_Wildshape_SpellResistance_Passive` - **Lunar Bestial Fortitude** | You have a +[1] bonus to Armour Class. You also have Advantage on Saving Throws against spells. This effect persists while using your druidic Wild Shape ability.
  <br>`Boosts=IF(IsSpell()):Advantage(AllSavingThrows);AC(2)`
- `MAG_Druid_Wildshape_TempHP_Passive` - **Lunar Bestial Vitality** | You gain [1] temporary hit points after casting Wild Shape. While those temporary hit points are active reduce all incoming damage by [2].
- `PrimalStrike` - **Primal Strike** | While in beast form, your attacks count as magical for the purpose of overcoming Resistance and Immunity to non-magical damage.
  <br>`Boosts=UnarmedMagicalProperty()`
- `WildShape_Combat` - **Lunar Mend** | As a bonus action in animal form, you can expend spell slots to heal yourself. You regain [1] per spell slot level.
  <br>`Boosts=IF(ConditionResult(false)):UnlockSpell(Shout_WildShape_Combat_Heal,,d136c5d9-0ff0-43da-acce-a74a07f8d6bf);UnlockSpellVariant(SpellId('Shout_AberrantShape'),ModifyUseCosts(Replace,B…`
- `TAD_Freecast` - **Freecast** | You have discovered a marvellous adaptability within yourself. Spell slots, charges, and similar resource costs for your next action or spell are removed. Refreshes after a Long Rest.
  <br>`Boosts=UnlockSpellVariant(FreecastCheck(),ModifyIconGlow(),ModifyTooltipDescription(),ModifyUseCosts(Replace,SpellSlot,0,-1,SpellSlot),ModifyUseCosts(Replace,Rage,0,0,Rage),ModifyUseCosts…`

**Spell candidates** (33 found, showing 14)
- `Projectile_AiHelper_MoonBeam`
  <br>`SpellType=Projectile`  `SpellProperties=ApplyStatus(MOONBEAM,100,1); DealDamage(2d10, Radiant);`
- `Shout_WildMagic_Entangle` - **Wild Magic: Entangle** | Create a vine surface around yourself, slowing down creatures, possibly Entangling them.
  <br>`SpellType=Shout`  `SpellProperties=GROUND:CreateSurface(4,3,Vines)`
- `Shout_WildMagic_SpikeGrowth` - **Wild Magic: Spike Growth** | Shape a piece of ground around yourself into hard spikes. A creature walking on the spikes takes [1] for every [2] it moves.
  <br>`SpellType=Shout`  `SpellProperties=GROUND:CreateSurface(4,3,SpikeGrowth)`
- `Shout_WildShape_Combat`
  <br>`SpellType=Shout`
- `Shout_WildShape_Combat_Badger`
  <br>`SpellType=Shout`
- `Shout_WildShape_Combat_Bear_Polar`
  <br>`SpellType=Shout`
- `Shout_WildShape_Combat_Cat`
  <br>`SpellType=Shout`
- `Shout_WildShape_Combat_DeepRothe`
  <br>`SpellType=Shout`
- `Shout_WildShape_Combat_Dilophosaurus`
  <br>`SpellType=Shout`
- `Shout_WildShape_Combat_Myrmidon_Air`
  <br>`SpellType=Shout`
- `Shout_WildShape_Combat_Myrmidon_Earth`
  <br>`SpellType=Shout`
- `Shout_WildShape_Combat_Myrmidon_Fire`
  <br>`SpellType=Shout`
- `Shout_WildShape_Combat_Myrmidon_Water`
  <br>`SpellType=Shout`
- `Shout_WildShape_Combat_Owlbear`
  <br>`SpellType=Shout`

### `CX_Druid_Land_Boost`  -  _caster_
_Currently in manager_ - passives: `ARP_SpellSlot_2_1`; spells: `Projectile_AcidArrow`, `Projectile_ProduceFlame`, `Target_CallLightning`, `Target_Entangle`, `Target_Frostbite`, `Target_MistyStep`, `Target_ThornWhip`, `Zone_Thunderwave`

**Passive candidates** (4 found)
- `LandsStride_Advantage` - **Land's Stride: Advantage** | You have become an expert at moving through the wilderness.You have Advantage on Saving Throws against plants that are magically created to impede your movement.
  <br>`Boosts=Tag(PLANT_IMPEDE_ADV)`
- `LandsStride_DifficultTerrain` - **Land's Stride: Difficult Terrain** | You have become an expert at moving through the wilderness. Difficult Terrain no longer slows you down.
  <br>`Boosts=StatusImmunity(SG_DifficultTerrain)`
- `LandsStride_Surfaces` - **Land's Stride: Plants** | You have become an expert at moving through the wilderness.Plant-based surfaces with thorns, spines, or similar hazards no longer harm you.
  <br>`Boosts=StatusImmunity(SHADOW_CURSED_VINES);StatusImmunity(SPIKE_GROWTH);StatusImmunity(BLIGHT_ENTANGLE);StatusImmunity(PLANT_GROWTH);StatusImmunity(DIFFICULT_TERRAIN_VINES);StatusImmunity…`
- `NaturesWard` - **Nature's Ward** | You can't be Charmed or Frightened by elementals and fey. Disease and poison also no longer affect you.
  <br>`Boosts=StatusImmunity(SG_Disease);StatusImmunity(SG_Poisoned); StatusImmunity(SG_Charmed,ELEMENTAL,FEY);StatusImmunity(SG_Frightened,ELEMENTAL,FEY)`

**Spell candidates** (11 found)
- `Projectile_SleetStorm_WaterFrozen` - **Sleet Storm**
  <br>`SpellType=Projectile`  `SpellSuccess=BreakConcentration()`  `SpellProperties=GROUND:CreateSurface(9,1,WaterFrozen)`
- `Shout_WildMagic_SpikeGrowth` - **Wild Magic: Spike Growth** | Shape a piece of ground around yourself into hard spikes. A creature walking on the spikes takes [1] for every [2] it moves.
  <br>`SpellType=Shout`  `SpellProperties=GROUND:CreateSurface(4,3,SpikeGrowth)`
- `Target_CallLightning_LightningBolt` - **Activate Call Lightning** | Call down more lightning to hit all targets within range.
  <br>`SpellType=Target`  `SpellProperties=GROUND:SurfaceChange(Electrify);RemoveStatus(SELF,SANCTUARY);RemoveStatus(SELF,SANCTUARY_TRANQUILITY);`
- `Target_IceStorm` - **Ice Storm** | Impel a storm of hail and ice to crash from the sky, covering the ground and striking all objects and creatures within range.
  <br>`SpellType=Target`  `SpellSuccess=DealDamage(2d8,Bludgeoning,Magical);DealDamage(4d6,Cold,Magical)`  `SpellProperties=GROUND:CreateSurface(6,2,WaterFrozen);GROUND:SurfaceChange(Freeze);GROUND:SurfaceChange(Douse);RemoveStatus(BURNING)`
- `Target_PlantGrowth` - **Plant Growth** | Make weeds burst from the ground and smother the area. Creatures moving through the weeds have their movement speed quartered.
  <br>`SpellType=Target`  `SpellProperties=GROUND:CreateSurface(6,10,Overgrowth)`
- `Target_SleetStorm`
  <br>`SpellProperties=GROUND:Summon(802b8b51-1bcf-469d-8663-2f1dc9698982, 10,,,<em>SleetStorm</em>,SLEET_STORM);RemoveStatus(BURNING)`
- `Target_SpikeGrowth`
  <br>`SpellProperties=GROUND:CreateSurface(6,100,<em>SpikeGrowth</em>,true)`
- `Target_SpikeGrowth_Dryad`
  <br>`SpellType=Target`
- `Target_StinkingCloud`
  <br>`SpellProperties=GROUND:CreateSurface(6,10,<em>StinkingCloud</em>,true)`
- `Zone_LightningBolt` - **Lightning Bolt** | Call forth a blast of lightning that hits all creatures in the line of the eruption.
  <br>`SpellType=Zone`  `SpellSuccess=DealDamage(8d6,Lightning,Magical)`
- `Shout_Stench_Ghast`

### `CX_Druid_Moon_Boost`  -  _hybrid_
_Currently in manager_ - passives: `CombatWildShape`, `MAG_Druid_Wildshape_SpellResistance_Passive`, `WildStrike`, `WildStrike_2`; spells: `Projectile_Moonflare`, `Shout_WildShape_Bear_Polar_NPC`, `Target_ConjureAnimals_Container`, `Target_Moonbeam`

**Passive candidates** (2 found)
- `PrimalStrike` - **Primal Strike** | While in beast form, your attacks count as magical for the purpose of overcoming Resistance and Immunity to non-magical damage.
  <br>`Boosts=UnarmedMagicalProperty()`
- `CombatWildShape` _(already in manager)_ - **Combat Wild Shape** | You can use your Wild Shape as a bonus action, rather than an action.

**Spell candidates** (23 found, showing 14)
- `Projectile_AiHelper_MoonBeam`
  <br>`SpellType=Projectile`  `SpellProperties=ApplyStatus(MOONBEAM,100,1); DealDamage(2d10, Radiant);`
- `Shout_WildShape_Combat`
  <br>`SpellType=Shout`
- `Shout_WildShape_Combat_Badger`
  <br>`SpellType=Shout`
- `Shout_WildShape_Combat_Bear_Polar`
  <br>`SpellType=Shout`
- `Shout_WildShape_Combat_Cat`
  <br>`SpellType=Shout`
- `Shout_WildShape_Combat_DeepRothe`
  <br>`SpellType=Shout`
- `Shout_WildShape_Combat_Dilophosaurus`
  <br>`SpellType=Shout`
- `Shout_WildShape_Combat_Myrmidon_Air`
  <br>`SpellType=Shout`
- `Shout_WildShape_Combat_Myrmidon_Earth`
  <br>`SpellType=Shout`
- `Shout_WildShape_Combat_Myrmidon_Fire`
  <br>`SpellType=Shout`
- `Shout_WildShape_Combat_Myrmidon_Water`
  <br>`SpellType=Shout`
- `Shout_WildShape_Combat_Owlbear`
  <br>`SpellType=Shout`
- `Shout_Wildshape_Combat_Panther`
  <br>`SpellType=Shout`
- `Shout_WildShape_Combat_Raven`
  <br>`SpellType=Shout`

### `CX_Druid_Spores_Boost`  -  _hybrid_
_Currently in manager_ - passives: `MAG_Druid_Spore_ExtraSpores_Passive`, `MAG_Druid_Spore_NecroticSpellcasting_Passive`, `ShadowDruid_PoisonClaws`; spells: `Projectile_RayOfSickness`, `Shout_SymbioticEntity`, `Target_ChillTouch`, `Target_InflictWounds`, `Target_VampiricTouch`, `Target_WitherAndBloom`

**Passive candidates** (2 found)
- `FungalInfestation`
  <br>`Boosts=UnlockInterrupt(Interrupt_FungalInfestation)`
- `SpreadingSpores` - **Spreading Spores** | While Symbiotic Entity is active, you can create a cloud of Spreading Spores.

**Spell candidates** (12 found)
- `Target_Contagion` - **Contagion**
- `Target_Contagion_BlindingSickness` - **Contagion: Blinding Sickness**
- `Target_Contagion_FilthFever` - **Contagion: Filth Fever**
- `Target_Contagion_FleshRot` - **Contagion: Flesh Rot**
- `Target_Contagion_Mindfire` - **Contagion: Mindfire**
- `Target_Contagion_Seizure` - **Contagion: Seizure**
- `Target_Contagion_SlimyDoom` - **Contagion: Slimy Doom**
- `Target_FungalInfestation` - **Fungal Infestation** | Raise a mildewed, mould-encrusted zombie from a corpse.
  <br>`SpellType=Target`  `SpellProperties=TARGET:SwitchDeathType(Explode);GROUND:Summon(c7a75636-a101-4920-a603-58efb6558bcb,UntilLongRest,,,,SHADOWCURSE_SUMMON_CHECK,UNSUMMON_ABLE)`
- `Target_HaloOfSpores`
  <br>`SpellSuccess=DealDamage(LevelMapValue(<em>HaloOfSpores</em>),Necrotic,Magical);IF(HasStatus('SYMBIOTIC_ENTITY', context.Source)):DealDamage(LevelMapValue(HaloOfSpores),Necrotic,Magical)`
- `Target_SpreadingSpores` - **Spreading Spores** | Seed an area in deadly spores that deal [1] per turn to all creatures that inhale them, except you and your allies.
  <br>`SpellType=Target`  `SpellProperties=GROUND:Summon(c2900350-e3bc-47ca-b522-9ca9bb3661eb,10,Projectile_AiHelper_Summon_Weak,,SpreadingSporesStack,SPREADING_SPORES)`
- `Target_Slam_Slayer`
- `Shout_SymbioticEntity` _(already in manager)_ - **Symbiotic Entity** | Gain [1] and deal an additional [2] while you have them. Cast Halo of Spores with double damage.
  <br>`SpellType=Shout`  `SpellProperties=ApplyStatus(SYMBIOTIC_ENTITY,100,-1)`

---

## Fighter

### `CX_Fighter_Boost`  -  _martial_
_Currently in manager_ - passives: `FightingStyle_Dueling`, `FightingStyle_GreatWeaponFighting`, `FightingStyle_Protection`, `FightingStyle_TwoWeaponFighting`, `Indomitable_NPC`; spells: `Projectile_Jump`, `Shout_ActionSurge`, `Shout_SecondWind`, `Target_Shove_Trip`

**Passive candidates** (20 found, showing 18)
- `ExtraAttack`
- `ExtraAttack_2` - **Improved Extra Attack** | You can make two additional attacks after attacking with your main-hand weapon.
- `ExtraAttack_BonusTechnical`
- `FightingStyle_Archery` - **Archery** | You gain a +2 bonus to ranged weapon attacks.
  <br>`Boosts=RollBonus(RangedWeaponAttack, 2);RollBonus(RangedOffHandWeaponAttack, 2)`
- `FightingStyle_Defense` - **Defence** | You gain a +1 bonus to Armour Class while wearing armour.
  <br>`Boosts=AC(1)`
- `Indomitable` - **Indomitable** | You have become as durable as an iron golem. Whenever you fail a Saving Throw, you can roll again, using the new result instead.
  <br>`Boosts=UnlockInterrupt(Interrupt_Indomitable);ActionResource(Interrupt_Indomitable,1,0)`
- `LOW_Guildhall_ExtraAttack_DaggerSpecialist` - **Dagger Specialist** | This creature can throw up to 3 daggers per round.
- `MAG_Fighter_ActionSurge_AttackBonus_Gloves_Passive` - **Surge Accuracy** | When you use Action Surge, gain a +[1] bonus to Attack Rolls for the rest of your turn.
- `Slayer_ExtraAttack`
- `Slayer_ExtraAttack_2`
- `BestialFury` - **Bestial Fury** | Your bond with your companion has deepened, unlocking their inner strength and giving them an Extra Attack.
- `GOB_Boss_RecklessAttack` - **Crude Frenzy** | This goblin can make an additional free attack after making a Main Hand Attack, but the second attack has Disadvantage on its Attack Roll.
- `ThirstingBlade_Blade`
- `ThirstingBlade_Check` - **The Extra Attack gained by this feature doesn't stack with Extra Attacks gained from other class levels.**
- `WarPriest` - **War Priest** | When you make an unarmed or weapon attack, you can spend a War Priest Charge to make an additional attack as a bonus action.
- `WildStrike` - **Wild Strike** | You can make an additional attack after making an Unarmed Strike while in Wild Shape.
- `FightingStyle_Dueling` _(already in manager)_ - **Duelling** | When you are wielding a melee weapon that is not Two-Handed in one hand, and no weapon in the other, you deal an additional 2 damage with that weapon.
  <br>`Boosts=IF(FightingStyle_Dueling(context.Source)):CharacterWeaponDamage(2)`
- `FightingStyle_GreatWeaponFighting` _(already in manager)_ - **Great Weapon Fighting** | When you roll a 1 or 2 on a damage die for an attack with a two-handed melee weapon, that die is rerolled once.
  <br>`Boosts=IF(FightingStyle_GreatWeapon(context.Source)):Reroll(MeleeWeaponDamage,2,true)`

**Spell candidates** (3 found)
- `Shout_WildMagic_ActionSurge` - **Wild Magic: Action Surge** | You gain an additional action this turn.
  <br>`SpellType=Shout`  `SpellProperties=ApplyStatus(ACTION_SURGE,100,1)`
- `Shout_ActionSurge` _(already in manager)_ - **Action Surge** | Immediately gain an extra action to use this turn.
  <br>`SpellType=Shout`  `SpellProperties=ApplyStatus(ACTION_SURGE,100,1)`
- `Shout_SecondWind` _(already in manager)_ - **Second Wind** | Draw on your stamina to heal yourself.
  <br>`SpellType=Shout`  `SpellProperties=RegainHitPoints(1d10+ClassLevel(Fighter))`

### `CX_Fighter_BattleMaster_Boost`  -  _martial_
_Currently in manager_ - passives: `ImprovedCombatSuperiority`, `MenacingAttack`, `Riposte`, `SweepingAttack`

**Passive candidates** (14 found)
- `CommanderStrike_Maneuver` - **Commander's Strike** | Direct an ally to strike a foe. The ally uses a reaction on their next turn to make a weapon attack.
  <br>`Boosts=UnlockSpell(Target_CommandersStrike)`
- `LOW_Guildhall_SneakyRiposte` - **Sneaky Riposte** | Strike a foe that just missed you with an attack, inflicting Sneak Attack damage if you have Advantage.
- `DisarmingAttack` - **Disarming Attack** | Spend a superiority die to make an attack that deals an additional [1] damage and possibly forces the target to drop the weapons they are holding.
  <br>`Boosts=UnlockSpell(Target_DisarmingAttack);UnlockSpell(Projectile_DisarmingAttack)`
- `MAG_TheClover_OffHand_Passive` - **True Strike Riposte** | When a creature misses you with a melee attack, you may retaliate and gain True Strike.
  <br>`Boosts=UnlockInterrupt(Interrupt_TheClover_TrueStrike_Riposte)`
- `ManeuveringAttack` - **Manoeuvring Attack** | Spend a superiority die to make an attack that deals an additional [1] damage. On hit, select which friendly creature will gain half its movement speed. It will not provoke attacks of opportunity.
  <br>`Boosts=UnlockSpell(Target_ManeuveringAttack);UnlockSpell(Projectile_ManeuveringAttack)`
- `MartialAdept` - **Martial Adept** | You receive 1 (additional) superiority die.
  <br>`Boosts=ActionResource(SuperiorityDie,1,0)`
- `PrecisionAttack` - **Precision Attack** | You can expend one Superiority Die to add it to an attack roll.
- `PushingAttack` - **Pushing Attack** | Spend a superiority die to make an attack that deals an additional [2] damage and possibly pushes the target back [1].
  <br>`Boosts=UnlockSpell(Target_PushingAttack);UnlockSpell(Projectile_PushingAttack)`
- `Rally` - **Rally** | Expend a superiority die to grant an ally [1], bolstering their resolve.
  <br>`Boosts=UnlockSpell(Target_Rally)`
- `TripAttack` - **Trip Attack** | Spend a superiority die to make an attack that deals an additional [1] damage and possibly knocks the target Prone.
  <br>`Boosts=UnlockSpell(Target_TripAttack);UnlockSpell(Projectile_TripAttack)`
- `ImprovedCombatSuperiority` _(already in manager)_ - **Improved Combat Superiority** | The size of your Superiority Dice increases to 1d10.
- `MenacingAttack` _(already in manager)_ - **Menacing Attack** | Spend a superiority die to make an attack that deals an additional [1] damage and possibly Frightens the target.
  <br>`Boosts=UnlockSpell(Target_MenacingAttack);UnlockSpell(Projectile_MenacingAttack)`
- `Riposte` _(already in manager)_ - **Riposte** | When a hostile creature misses you with a melee attack, expend a superiority die to retaliate with a powerful strike that deals an additional [1] damage.
  <br>`Boosts=UnlockInterrupt(Interrupt_Riposte)`
- `SweepingAttack` _(already in manager)_ - **Sweeping Attack** | Swing your weapon in a rapid, sweeping arc to attack multiple enemies at once. Roll your superiority die for damage.
  <br>`Boosts=UnlockSpell(Zone_SweepingAttack)`

**Spell candidates** (13 found)
- `Projectile_DisarmingAttack` - **Disarming Attack (Ranged)** | Focus your shot on your foe's hands and possibly force them to drop the weapons they are holding.
  <br>`SpellType=Projectile`  `SpellSuccess=DealDamage(MainRangedWeapon + LevelMapValue(SuperiorityDie), MainRangedWeaponDamageType); ExecuteWeaponFunctors(MainHand);IF(not SavingThrow(Ability.Strength, ManeuverSaveDC())):Ap…`
- `Projectile_GoadingAttack` - **Goading Attack (Ranged)** | Goad an enemy into attacking only you. It gains Disadvantage on Attack Rolls against anyone but you.
  <br>`SpellType=Projectile`  `SpellSuccess=IF(not SavingThrow(Ability.Wisdom, ManeuverSaveDC())):ApplyStatus(GOADING_ATTACK,100,1);DealDamage(MainRangedWeapon + LevelMapValue(SuperiorityDie), MainRangedWeaponDamageType); Ex…`
- `Projectile_MenacingAttack` - **Menacing Attack (Ranged)** | Possibly Frighten your target. They'll have Disadvantage on Ability Checks and Attack Rolls and be unable to move.
  <br>`SpellType=Projectile`  `SpellSuccess=IF(not SavingThrow(Ability.Wisdom, ManeuverSaveDC(),AdvantageOnFrightened(), DisadvantageOnFrightened())):ApplyStatus(FRIGHTENED,100,2);DealDamage(MainRangedWeapon + LevelMapValue(…`
- `Projectile_TripAttack` - **Trip Attack (Ranged)** | A powerful shot that possibly knocks the target Prone.
  <br>`SpellType=Projectile`  `SpellSuccess=IF(not SavingThrow(Ability.Strength, ManeuverSaveDC())):ApplyStatus(PRONE,100,-1);DealDamage(MainRangedWeapon + LevelMapValue(SuperiorityDie), MainRangedWeaponDamageType); ExecuteW…`
- `Shout_PrecisionAttack` - **Precision Attack** | Your next weapon attack gets an Attack Roll bonus equal to your Superiority Die.
  <br>`SpellType=Shout`  `SpellProperties=ApplyStatus(SELF,PRECISION_ATTACK,100,-1)`
- `Target_DisarmingAttack` - **Disarming Attack (Melee)** | Focus your attack on your foe's hands and possibly force them to drop the weapons they are holding.
  <br>`SpellType=Target`  `SpellSuccess=IF(not SavingThrow(Ability.Strength, ManeuverSaveDC())):ApplyStatus(DISARM,100,0);DealDamage(MainMeleeWeapon + LevelMapValue(SuperiorityDie), MainMeleeWeaponDamageType); ExecuteWea…`
- `Target_GoadingAttack` - **Goading Attack (Melee)** | Goad an enemy into attacking only you. It gains Disadvantage on Attack Rolls against anyone but you.
  <br>`SpellType=Target`  `SpellSuccess=IF(not SavingThrow(Ability.Wisdom, ManeuverSaveDC())):ApplyStatus(GOADING_ATTACK,100,1);DealDamage(MainMeleeWeapon + LevelMapValue(SuperiorityDie), MainMeleeWeaponDamageType); Exec…`
- `Target_Legendary_ShieldBlow_Riposte` - **Bulwark Rebuke** | When a creature damages you, deal it [1] and possibly knock it Prone.
  <br>`SpellType=Target`  `SpellSuccess=DealDamage(2d4, Force);ApplyStatus(PRONE,100,1)`
- `Target_MenacingAttack` - **Menacing Attack (Melee)** | Possibly Frighten your target. They'll have Disadvantage on Ability Checks and Attack Rolls and be unable to move.
  <br>`SpellType=Target`  `SpellSuccess=IF(not SavingThrow(Ability.Wisdom, ManeuverSaveDC(),AdvantageOnFrightened(), DisadvantageOnFrightened())):ApplyStatus(FRIGHTENED,100,2);DealDamage(MainMeleeWeapon + LevelMapValue(S…`
- `Target_Riposte` - **Riposte**
- `Target_ShieldBlow_Riposte` - **Shield Blow** | When struck by a melee attack, your attacker must succeed a Dexterity Saving Throw or fall Prone.
  <br>`SpellType=Target`
- `Target_TripAttack` - **Trip Attack (Melee)** | A powerful attack that possibly knocks the target Prone.
  <br>`SpellType=Target`  `SpellSuccess=IF(not SavingThrow(Ability.Strength, ManeuverSaveDC())):ApplyStatus(PRONE,100,1);DealDamage(MainMeleeWeapon + LevelMapValue(SuperiorityDie), MainMeleeWeaponDamageType); ExecuteWeap…`
- `Zone_SweepingAttack` - **Sweeping Attack** | Swing your weapon in a rapid, sweeping arc to attack multiple enemies at once.
  <br>`SpellType=Zone`  `SpellSuccess=DealDamage(LevelMapValue(SuperiorityDie), MainWeaponDamageType);`  `SpellProperties=GROUND:ExecuteWeaponFunctors(MainHand);`

### `CX_Fighter_Champion_Boost`  -  _martial_
_Currently in manager_ - passives: `Goon_Impeded_Movement_2`, `MAG_Fighter_ActionSurge_AttackBonus_Gloves_Passive`

**Passive candidates** (4 found)
- `ImprovedCritical` - **Improved Critical Hit** | The number you need to roll a Critical Hit while attacking is reduced by 1. This effect can stack.
  <br>`Boosts=ReduceCriticalAttackThreshold(1)`
- `MAG_WYR_Orin_Bhaalist_Dagger_ImprovedCritical_Passive` - **Improved Critical** | The number you need to roll a Critical Hit while attacking is reduced by 1. This effect can stack.
  <br>`Boosts=ReduceCriticalAttackThreshold(1)`
- `RemarkableAthlete_Jump` - **Remarkable Athlete: Jump** | You're a master of your own body, your athletic prowess extended beyond the usual.Your Jump distance is increased by [1].
  <br>`Boosts=JumpMaxDistanceBonus(3)`
- `RemarkableAthlete_Proficiency` - **Remarkable Athlete: Proficiency** | You're a master of your own body, your athletic prowess extended beyond the usual. You can add half of your Proficiency Bonus to any Strength, Dexterity, and Constitution Checks that you are not Proficient in.
  <br>`Boosts=IF(not HasProficiencyBonus(context.CheckedAbility,context.CheckedSkill,context.Source) and CheckedPhysicalAbility(context.Source)):RollBonus(SkillCheck,ProficiencyBonus/2);IF(not H…`

**Spell candidates** (19 found, showing 14)
- `Rush_Aggressive`
  <br>`SpellType=Rush`
- `Rush_Charge_Minotaur`
  <br>`SpellType=<em>Rush</em>`
- `Rush_Charge_Minotaur_Ally`
  <br>`SpellType=Rush`
- `Rush_Charger_Attack`
  <br>`SpellType=<em>Rush</em>`
- `Rush_Charger_Push`
  <br>`SpellType=<em>Rush</em>`
- `Rush_ForceTunnel`
  <br>`SpellType=<em>Rush</em>`
- `Rush_GoldenLance`
  <br>`SpellType=<em>Rush</em>`
- `Rush_InfernalTrample`
  <br>`SpellType=Rush`  `SpellSuccess=DealDamage(1d4,Fire,Magical)`
- `Rush_Primal_Stampede`
  <br>`SpellType=<em>Rush</em>`
- `Rush_Rush`
  <br>`SpellType=<em>Rush</em>`
- `Rush_Rush_Boar`
  <br>`SpellType=<em>Rush</em>`
- `Rush_Rush_Boar_Summon`
  <br>`SpellType=<em>Rush</em>`
- `Rush_Rush_DeepRothe`
  <br>`SpellType=<em>Rush</em>`
- `Rush_SpringAttack`
  <br>`SpellType=<em>Rush</em>`

### `CX_Fighter_EldritchKnight_Boost`  -  _hybrid_
_Currently in manager_ - passives: `EldritchStrike`, `FinishingStrike`, `Mod_UNI_Bow_SpellslotRecharge_Passive`; spells: `Shout_Shield_Wizard`, `Target_BoomingBlade`, `Target_HideousLaughter`

**Passive candidates** (3 found)
- `WarMagic` - **War Magic** | You have honed your body and magic for war. After you cast a cantrip, you can make a weapon attack using a bonus action.
- `WarMagic_Githyanki` - **Githyanki War Magic** | After the githyanki casts a spell or cantrip, they can make a weapon attack using a bonus action.
- `EldritchStrike` _(already in manager)_ - **Eldritch Strike** | When you hit a creature with a weapon attack, it has Disadvantage on its next Saving Throw against a spell you cast before the end of your next turn.

**Spell candidates** (32 found, showing 14)
- `Projectile_ScorchingRay` - **Scorching Ray** | Hurl [2] rays of fire. Each ray deals [1].
  <br>`SpellType=Projectile`  `SpellSuccess=DealDamage(2d6,Fire,Magical)`  `SpellProperties=GROUND:SurfaceChange(Ignite);GROUND:SurfaceChange(Melt)`
- `Projectile_ScorchingRay_CircletOfBlasting`
  <br>`SpellType=Projectile`
- `Shout_ActionSurge` - **Action Surge** | Immediately gain an extra action to use this turn.
  <br>`SpellType=Shout`  `SpellProperties=ApplyStatus(ACTION_SURGE,100,1)`
- `Shout_Blur` - **Blur**
  <br>`SpellProperties=ApplyStatus(<em>BLUR</em>,100,10)`
- `Shout_FireShield` - **Fire Shield**
- `Shout_FireShield_Chill` - **Fire Shield: Chill**
- `Shout_FireShield_Warm` - **Fire Shield: Warm**
- `Shout_MageArmor_ArmorOfShadows` - **Invocation: Armour of Shadows** | Protective shadows surround you. They increase your Armour Class by 3.
  <br>`SpellType=Shout`  `SpellProperties=ApplyStatus(MAGE_ARMOR,100,-1)`
- `Shout_Shield_MindFlayer`
  <br>`SpellType=Shout`
- `Shout_Shield_Sorcerer`
  <br>`SpellType=Shout`
- `Shout_Shield_Warlock`
  <br>`SpellType=Shout`
- `Shout_WildMagic_ActionSurge` - **Wild Magic: Action Surge** | You gain an additional action this turn.
  <br>`SpellType=Shout`  `SpellProperties=ApplyStatus(ACTION_SURGE,100,1)`
- `Shout_WildMagic_Blur` - **Wild Magic: Blur**
  <br>`SpellProperties=ApplyStatus(<em>BLUR</em>,100,3)`
- `Shout_WildMagic_Shield` - **Wild Magic: Shield** | Armour Class is increased by 5 and you are immune to the effects of Magic Missile.
  <br>`SpellType=Shout`  `SpellProperties=ApplyStatus(SHIELD,100,1)`

---

## Monk

### `CX_Monk_Boost`  -  _martial_
_Currently in manager_ - passives: `DeflectMissiles`, `FlurryOfBlowsUnlock`, `Goon_Increased_Movement_2`, `MartialArts_BonusUnarmedStrike`, `MartialArts_UnarmedDamage`, `Mobile_DashAcrossDifficultTerrain`, `SecondStoryWork_Jumping`, `UnarmoredDefense_Monk`; spells: `Projectile_Jump`, `Target_Shove_Trip`, `Target_UnarmedStrike_Monk`

**Passive candidates** (9 found)
- `Ki_FlurryOfBlows` - **Flurry of Blows** | You can spend a ki point to deliver two swift punches as a bonus action.
- `MartialArts_DextrousUnarmedAttacks` - **Martial Arts: Dextrous Attacks** | Attacks with Monk Weapons and unarmed attacks scale with your Dexterity instead of your Strength if your Dexterity is higher.
  <br>`Boosts=MonkWeaponAttackOverride()`
- `MartialArts_Mastery` - **Martial Arts Mastery** | Your unique monastic training grants you Proficiency in Monk Weapons, which are shortswords and any simple melee weapons that don't have the two-handed or heavy property.
- `StunningStrike` - **Stunning Strike**
- `MAG_Monk_Healed_TempHP_Passive` - **Soul Protection** | When you are healed, gain [1]. While you have the temporary hit points gain a +[2] bonus to Saving Throws.
- `MAG_OfMissileSnaring_Gloves_Passive` - **Missile Snaring** | You can intercept missiles from ranged weapon attacks, reducing their damage by [1] + your Dexterity Modifier.
  <br>`Boosts=IF(not HasStatus('SG_Polymorph_BeastShape')):UnlockInterrupt(Interrupt_MAG_MissileSnaring)`
- `DeflectMissiles` _(already in manager)_ - **Deflect Missiles** | Use your reaction to reduce the damage from a ranged weapon attack by 1d10 + your Dexterity Modifier + your monk level.
- `MartialArts_BonusUnarmedStrike` _(already in manager)_ - **Martial Arts: Bonus Unarmed Strike** | After making an attack with a Monk Weapon or while unarmed, you can make another unarmed attack as a bonus action.
- `MartialArts_UnarmedDamage` _(already in manager)_ - **Martial Arts: Deft Strikes** | Attacks with Monk Weapons and unarmed attacks deal [1], unless their normal damage is higher.
  <br>`Boosts=MonkWeaponDamageDiceOverride(LevelMapValue(MartialArts))`

**Spell candidates** (6 found)
- `Shout_Dash_StepOfTheWind` - **Step of the Wind: Dash** | Double your movement speed. Jump no longer requires a bonus action.
  <br>`SpellType=Shout`  `SpellProperties=ApplyStatus(DASH,100,1); ApplyStatus(STEP_OF_THE_WIND,100,1)`
- `Shout_Disengage_StepOfTheWind` - **Step of the Wind: Disengage** | Spend [1] ki point to gain the Disengage action as a bonus action this turn.
  <br>`SpellType=Shout`  `SpellProperties=ApplyStatus(DISENGAGE,100,1); ApplyStatus(STEP_OF_THE_WIND,100,1)`
- `Shout_PatientDefense` - **Patient Defence** | Attack Rolls against you have Disadvantage, and you have Advantage on Dexterity Saving Throws.
  <br>`SpellType=Shout`  `SpellProperties=ApplyStatus(SELF,PATIENT_DEFENCE,100,1)`
- `Target_FlurryOfBlows` - **Flurry of Blows** | Punch twice in quick succession.
  <br>`SpellType=Target`  `SpellSuccess=DealDamage(UnarmedDamage , Bludgeoning);Cast2[DealDamage(UnarmedDamage , Bludgeoning)]`
- `Target_StunningStrike` - **Stunning Strike (Melee)** | Possibly Stuns the target.
  <br>`SpellType=Target`  `SpellSuccess=IF(not SavingThrow(Ability.Constitution, ManeuverSaveDC())):ApplyStatus(STUNNED,100,1); DealDamage(MainMeleeWeapon, MainMeleeWeaponDamageType); ExecuteWeaponFunctors(MainHand)`
- `Target_StunningStrike_Unarmed` - **Stunning Strike (Unarmed)**
  <br>`SpellType=Target`  `SpellSuccess=IF(not SavingThrow(Ability.Constitution, ManeuverSaveDC())):ApplyStatus(STUNNED,100,1);DealDamage(UnarmedDamage , Bludgeoning)`

### `CX_Monk_FourElements_Boost`  -  _hybrid_
_Currently in manager_ - passives: `ARP_KiPoint_2`, `MAG_BG_OfAges_Flail_Passive`, `MAG_Monk_Armor_WindStance_Passive`

**Passive candidates** (0 found)
- _(no hits - adjust search terms in terms.py)_

**Spell candidates** (9 found)
- `Projectile_FangsOfTheFireSnake` - **Fangs of the Fire Snake** | Hit your foe from afar. Your next melee attacks deal an additional [1].
  <br>`SpellType=Projectile`  `SpellSuccess=DealDamage(UnarmedDamage , Bludgeoning);DealDamage(1d10,Fire,Magical)`  `SpellProperties=GROUND:DealDamage(1d10,Fire);IF(not Player(context.Source)):ApplyStatus(SELF,AI_HELPER_EXTRAATTACK,100,1);ApplyStatus(SELF,FANGS_OF_THE_FIRE_SNAKE,100,1);ApplyStatus(SELF,MARTIAL_A…`
- `Target_FistOfUnbrokenAir`
  <br>`SpellSuccess=DealDamage(LevelMapValue(<em>FistOfUnbrokenAir</em>),Bludgeoning);Force(6);ApplyStatus(PRONE,100,1)`
- `Target_WaterWhip`
  <br>`SpellSuccess=DealDamage(LevelMapValue(<em>WaterWhip</em>),Bludgeoning);`
- `Target_WaterWhip_Prone`
  <br>`SpellSuccess=DealDamage(LevelMapValue(<em>WaterWhip</em>),Bludgeoning);ApplyStatus(PRONE,100,-1)`
- `Target_WaterWhip_Pull`
  <br>`SpellSuccess=DealDamage(LevelMapValue(<em>WaterWhip</em>),Bludgeoning);Force(-9, OriginToEntity, Neutral, false, true)`
- `Target_WaterWhip_Umberlee`
  <br>`SpellType=Target`
- `Zone_BurningHands` - **Burning Hands** | Each flammable target is hit with [1].
  <br>`SpellType=Zone`  `SpellSuccess=DealDamage(3d6, Fire,Magical)`  `SpellProperties=GROUND:SurfaceChange(Ignite);GROUND:SurfaceChange(Melt);TARGET:IF(Item()):ApplyStatus(BURNING,100,2);`
- `Zone_BurningHands_MephistophelesTiefling` - **Legacy of Cania: Burning Hands**
  <br>`SpellType=Zone`
- `Zone_BurningHands_Monk` - **Sweeping Cinder Strike** | Expel fire from your outstretched hands and ignite anything flammable.
  <br>`SpellType=Zone`  `SpellSuccess=DealDamage(LevelMapValue(BurningHands_Monk), Fire,Magical)`  `SpellProperties=GROUND:SurfaceChange(Ignite);GROUND:SurfaceChange(Melt);TARGET:IF(Item()):ApplyStatus(BURNING,100,2);ApplyStatus(SELF,MARTIAL_ARTS_BONUS_UNARMED_STRIKE,100,1)`

### `CX_Monk_OpenHand_Boost`  -  _martial_
_Currently in manager_ - passives: `MAG_Monk_Armor_MountainStance_Passive`, `MAG_Monk_Magic_ArmorEx_Passive`, `StunningStrike`

**Passive candidates** (0 found)
- _(no hits - adjust search terms in terms.py)_

**Spell candidates** (4 found)
- `Shout_WholenessOfBody` - **Wholeness of Body** | Regain half your Ki Points and enter a temporary state of Wholeness where you regain ki points and have an extra bonus action.
  <br>`SpellType=Shout`  `SpellProperties=RegainHitPoints(3*ClassLevel(Monk));RestoreResource(SELF,KiPoint,(ClassLevel(Monk)+1)/2,0);ApplyStatus(WHOLENESS_OF_BODY, 100, 3)`
- `Target_OpenHandTechnique_Knock` - **Flurry of Blows: Topple** | Punch twice in quick succession and possibly knock the target Prone.
  <br>`SpellType=Target`  `SpellSuccess=DealDamage(UnarmedDamage , Bludgeoning);Cast2[DealDamage(UnarmedDamage , Bludgeoning);IF(not SavingThrow(Ability.Dexterity, ManeuverSaveDC())):ApplyStatus(PRONE,100,1)]`
- `Target_OpenHandTechnique_NoReactions` - **Flurry of Blows: Stagger** | Punch twice in quick succession and Stagger the target, making it unable to take reactions.
  <br>`SpellType=Target`  `SpellSuccess=DealDamage(UnarmedDamage , Bludgeoning);Cast2[DealDamage(UnarmedDamage , Bludgeoning);ApplyStatus(OPEN_HAND_NO_REACTIONS,100,1)]`
- `Target_OpenHandTechnique_Push` - **Flurry of Blows: Push** | Punch twice in quick succession and possibly push the target [1] away.
  <br>`SpellType=Target`  `SpellSuccess=DealDamage(UnarmedDamage , Bludgeoning);Cast2[DealDamage(UnarmedDamage , Bludgeoning);IF(not SavingThrow(Ability.Strength, ManeuverSaveDC())):Force(5)]`

### `CX_Monk_Shadow_Boost`  -  _hybrid_
_Currently in manager_ - passives: `MAG_Monk_Armor_MountainStance_Passive`, `MAG_Monk_Martial_Lethality_Passive`, `SCL_MastiffPoachers_Ring_Passive`, `ShadowArts_MinorIllusion`, `UND_Justiciar_ChainShirt_Magic_Passive`

**Passive candidates** (1 found)
- `ShadowArts_MinorIllusion` _(already in manager)_ - **Shadow Arts: Minor Illusion** | Gain the Minor Illusion cantrip.

**Spell candidates** (29 found, showing 14)
- `Projectile_AiHelper_Silence`
  <br>`SpellType=Projectile`  `SpellProperties=ApplyStatus(SILENCED,100,1);`
- `Projectile_ArrowOfDarkness` - **Arrow of Darkness**
- `Projectile_Fly_Darkness_Raven`
  <br>`SpellType=Projectile`  `SpellProperties=GROUND:CreateSurface(3,2,DarknessCloud)`
- `Shout_Hide_ShadowArts` - **Shadow Arts: Hide**
  <br>`SpellType=Shout`
- `Shout_PassWithoutTrace` - **Pass Without Trace** | Call forth a veil of shadows and silence that gives you and all nearby companions a +10 bonus to Stealth Checks.
  <br>`SpellType=Shout`  `SpellProperties=ApplyStatus(PASS_WITHOUT_TRACE_AURA, 100, -1)`
- `Shout_PassWithoutTrace_Monk` - **Shadow Arts: Pass Without Trace**
  <br>`SpellType=Shout`  `SpellProperties=ApplyStatus(PASS_WITHOUT_TRACE_AURA_MONK, 100, -1)`
- `Shout_Silence_TollCollector_Face` - **Moral Confinement** | Unleash a roar that wounds and Silences nearby foes.
  <br>`SpellType=Shout`  `SpellSuccess=ApplyStatus(SILENCED, 100, 2)`  `SpellProperties=DealDamage(2d8+2, Psychic,Magical)`
- `Target_Darkness` - **Darkness**
- `Target_Darkness_Drider`
  <br>`SpellType=Target`
- `Target_Darkness_DrowMagic`
  <br>`SpellType=Target`
- `Target_Darkness_Monk` - **Shadow Arts: Darkness**
- `Target_Darkness_Sorcerer` - **Eyes of the Dark: Darkness**
- `Target_MinorIllusion` - **Minor Illusion** | Create an illusion that compels nearby creatures to investigate.
  <br>`SpellType=Target`  `SpellProperties=GROUND:Summon(a4d03902-0382-4f88-866d-3bb2225a69a3, 10,,,'MinorIllusionStack',MINOR_ILLUSION)`
- `Target_ShadowStep` - **Shadow Step** | Teleport from shadow to shadow. Afterwards, you have Advantage on your next melee Attack Roll.
  <br>`SpellType=Target`  `SpellProperties=GROUND:TeleportSource();GROUND:ApplyStatus(SELF,SHADOW_STEP,100,1)`

---

## Paladin

### `CX_Paladin_Boost`  -  _hybrid_
_Currently in manager_ - passives: `FightingStyle_Dueling`, `FightingStyle_GreatWeaponFighting`, `Goon_Summon_Potion_Healing_x1`, `Sentinel_OpportunityAdvantage`; spells: `Projectile_Jump`, `Shout_DivineFavor`, `Shout_Smite_`

**Passive candidates** (1 found)
- `ImprovedDivineSmite` - **Improved Divine Smite** | Your attacks are suffused with divine might.Melee weapon attacks deal an additional [1].
  <br>`Boosts=IF(IsMeleeAttack()):CharacterWeaponDamage(1d8,Radiant)`

**Spell candidates** (13 found)
- `Shout_DivineSense` - **Divine Sense** | Gain Advantage on Attack Rolls against celestials, fiends, and undead.
  <br>`SpellType=Shout`  `SpellProperties=ApplyStatus(DIVINE_SENSE,100, 2)`
- `Target_Bless`
  <br>`SpellProperties=ApplyStatus(<em>BLESS</em>, 100, 10)`
- `Target_Command_Approach` - **Command: Approach** | Command a creature to move towards you on its turn and do nothing else.
  <br>`SpellType=Target`  `SpellSuccess=ApplyStatus(COMMAND_APPROACH, 100, 1)`
- `Target_Command_Drop` - **Command: Drop** | Command a creature to drop its weapon.
  <br>`SpellType=Target`  `SpellSuccess=ApplyStatus(DISARM, 100, 1)`
- `Target_Command_Flee` - **Command: Flee** | Command a creature to flee from you on its turn and do nothing else.
  <br>`SpellType=Target`  `SpellSuccess=ApplyStatus(COMMAND_FLEE, 100, 1)`
- `Target_Command_Grovel` - **Command: Grovel** | Command a creature to fall Prone immediately.
  <br>`SpellType=Target`  `SpellSuccess=ApplyStatus(COMMAND_GROVEL, 100, 1)`
- `Target_Command_Halt` - **Command: Halt** | Command a creature to halt, preventing it from moving or taking any type of action.
- `Target_LayOnHands` - **Lay on Hands** | Use your blessed touch to heal a creature or cure it of all diseases and poisons.
  <br>`SpellType=Target`
- `Target_LayOnHands_BigHeal` - **Lay on Hands: Greater Healing**
  <br>`SpellType=Target`  `SpellProperties=TARGET:RegainHitPoints(4*ClassLevel(Paladin))`
- `Target_LayOnHands_Cure` - **Lay on Hands: Cure** | Imbue your hands with divine power to cure all diseases and poisons affecting a creature.
  <br>`SpellType=Target`  `SpellProperties=RemoveStatus(SG_Poisoned);RemoveStatus(SG_Disease);RemoveStatus(ASTARION_WEAK)`
- `Target_LayOnHands_SmallHeal` - **Lay on Hands: Lesser Healing** | Imbue your hands with divine power to heal a target.
  <br>`SpellType=Target`  `SpellProperties=TARGET:RegainHitPoints(2*ClassLevel(Paladin))`
- `Target_ShieldOfFaith` - **Shield of Faith** | Protect a creature from attacks: increase its Armour Class by 2.
  <br>`SpellType=Target`  `SpellProperties=ApplyStatus(SHIELD_OF_FAITH,100,-1)`
- `Target_VoiceOfCommand` - **Voice of Command** | Command an ally i

### `CX_Paladin_Ancients_Boost`  -  _hybrid_
_Currently in manager_ - passives: `ARP_ChannelOath_1`, `DivineHealth`; spells: `Shout_HealingRadiance`

**Passive candidates** (0 found)
- _(no hits - adjust search terms in terms.py)_

**Spell candidates** (18 found, showing 14)
- `Projectile_AiHelper_MoonBeam`
  <br>`SpellType=Projectile`  `SpellProperties=ApplyStatus(MOONBEAM,100,1); DealDamage(2d10, Radiant);`
- `Projectile_EnsnaringStrike` - **Ensnaring Strike (Ranged)** | Your attack summons thorny vines that possibly Ensnare your target.
  <br>`SpellType=Projectile`  `SpellSuccess=IF(not SavingThrow(Ability.Strength, SourceSpellDC(),AdvantageOnRestrained(),DisadvantageOnRestrained())):ApplyStatus(ENSNARING_STRIKE,100,10);DealDamage(MainRangedWeapon, MainRang…`
- `Target_EnsnaringStrike` - **Ensnaring Strike (Melee)** | Your attack summons thorny vines that possibly Ensnare your target.
  <br>`SpellType=Target`  `SpellSuccess=IF(not SavingThrow(Ability.Strength, SourceSpellDC(),AdvantageOnRestrained(),DisadvantageOnRestrained())):ApplyStatus(ENSNARING_STRIKE,100,10);DealDamage(MainMeleeWeapon, MainMelee…`
- `Target_MistyStep` - **Misty Step** | Surrounded by silver mist, you teleport to an unoccupied space you can see.
  <br>`SpellType=Target`  `SpellProperties=GROUND:TeleportSource();`
- `Target_MistyStep_Elemental_Air`
  <br>`SpellType=Target`
- `Target_MistyStep_Elemental_Earth`
  <br>`SpellType=Target`
- `Target_MistyStep_Elemental_Fire`
  <br>`SpellType=Target`
- `Target_MistyStep_Elemental_Water`
  <br>`SpellType=Target`
- `Target_MistyStep_Free`
  <br>`SpellType=Target`  `SpellProperties=GROUND:TeleportSource();GROUND:RemoveStatus(SELF,MISTY_ESCAPE_INVISIBLE)`
- `Target_MistyStep_Myrmidon_Air` - **Elemental Warp**
  <br>`SpellType=Target`
- `Target_MistyStep_Myrmidon_Earth`
  <br>`SpellType=Target`
- `Target_MistyStep_Myrmidon_Fire`
  <br>`SpellType=Target`
- `Target_MistyStep_Myrmidon_Water`
  <br>`SpellType=Target`
- `Target_MistyStep_Shadow_TEST`
  <br>`SpellType=Target`

### `CX_Paladin_Devotion_Boost`  -  _hybrid_
_Currently in manager_ - passives: `ARP_ChannelOath_1`, `DarkDevotion`, `Goon_Aura_of_Devotion_Passive`; spells: `Shout_SacredWeapon`, `Target_Bless`, `Target_HolyRebuke`, `Target_Smite_Divine`

**Passive candidates** (0 found)
- _(no hits - adjust search terms in terms.py)_

**Spell candidates** (7 found)
- `Target_Sanctuary`
  <br>`SpellProperties=AI_IGNORE:ApplyStatus(<em>SANCTUARY</em>,100,10);AI_ONLY:ApplyStatus(AI_HELPER_BUFF,100,10)`
- `Target_Sanctuary_Cultist`
  <br>`SpellType=Target`
- `Target_Sanctuary_Drider`
  <br>`SpellProperties=AI_IGNORE:ApplyStatus(<em>SANCTUARY</em>,100,1);AI_ONLY:ApplyStatus(AI_HELPER_BUFF,100,10)`
- `Target_ShieldOfFaith` - **Shield of Faith** | Protect a creature from attacks: increase its Armour Class by 2.
  <br>`SpellType=Target`  `SpellProperties=ApplyStatus(SHIELD_OF_FAITH,100,-1)`
- `Projectile_Net_Kuotoa`
- `Target_CallLightning_LightningBolt`
  <br>`SpellProperties=GROUND:SurfaceChange(Electrify);RemoveStatus(SELF,<em>SANCTUARY</em>);RemoveStatus(SELF,SANCTUARY_TRANQUILITY);`
- `Shout_SacredWeapon` _(already in manager)_ - **Sacred Weapon** | Turn your weapon into a Sacred Weapon. It has a higher chance of hitting, and emits a bright light.
  <br>`SpellType=Shout`  `SpellProperties=ApplyEquipmentStatus(MainHand, SACRED_WEAPON,100, 10); AI_ONLY:ApplyStatus(AI_HELPER_BUFF_LARGE,100,10)`

### `CX_Paladin_Vengeance_Boost`  -  _hybrid_
_Currently in manager_ - passives: `ARP_ChannelOath_1`, `Goon_Aura_of_Protection_Passive`, `Sentinel_Attack`; spells: `Target_HoldPerson`, `Target_HuntersMark`, `Target_Smite_Wrathful`, `Target_VowOfEnmity`

**Passive candidates** (1 found)
- `RelentlessAvenger` - **Relentless Avenger** | If you hit an enemy with an Opportunity Attack, your movement speed increases by [1] on your next turn.

**Spell candidates** (24 found, showing 14)
- `Projectile_Solution_Oil_Bane_Destroy` - **Oil of Bane**
  <br>`SpellType=Projectile`
- `Target_Bane`
  <br>`SpellSuccess=ApplyStatus(<em>BANE</em>, 100, 10)`
- `Target_Bane_Drider`
  <br>`SpellType=Target`
- `Target_Bane_ThiefOfFiveFates` - **Invocation: Bane**
  <br>`SpellType=Target`
- `Target_BanesWrath` - **Bane's Wrath**
- `Target_Haste`
  <br>`SpellProperties=ApplyStatus(<em>HASTE</em>,100,10)`
- `Target_HoldPerson_Redcap`
  <br>`SpellType=Target`
- `Target_HuntersMark_Reapply` - **Reapply Hunter's Mark** | Shift your Hunter's Mark to a new creature without using a spell slot.
  <br>`SpellType=Target`  `SpellProperties=ApplyStatus(SELF,HUNTERS_MARK_OWNER,100,-1,,,,,true);ApplyStatus(HUNTERS_MARK,100,-1,,,,,true);RemoveStatus(SELF,HUNTERS_MARK_REAPPLY)`
- `Target_MistyStep` - **Misty Step** | Surrounded by silver mist, you teleport to an unoccupied space you can see.
  <br>`SpellType=Target`  `SpellProperties=GROUND:TeleportSource();`
- `Target_MistyStep_Elemental_Air`
  <br>`SpellType=Target`
- `Target_MistyStep_Elemental_Earth`
  <br>`SpellType=Target`
- `Target_MistyStep_Elemental_Fire`
  <br>`SpellType=Target`
- `Target_MistyStep_Elemental_Water`
  <br>`SpellType=Target`
- `Target_MistyStep_Free`
  <br>`SpellType=Target`  `SpellProperties=GROUND:TeleportSource();GROUND:RemoveStatus(SELF,MISTY_ESCAPE_INVISIBLE)`

### `CX_Paladin_Oathbreaker_Boost`  -  _hybrid_
_Currently in manager_ - passives: `ARP_ChannelOath_1`, `Goon_Aura_of_Hate_Passive`, `Mod_MAG_Sarevok_OfChaos_Greatsword_Leeching_Passive`, `TouchOfDeath`; spells: `Shout_Dreadful_Aspect`, `Shout_HellishRebuke`, `Shout_SpiritShroud`, `Target_ControlUndead`, `Target_SummonShadowspawn`

**Passive candidates** (1 found)
- `ControlUndead_Immune` - **Control Undead Immunity** | This creature is so rife with the cryptly fortitude of undeath that it simply cannot be controlled.
  <br>`Boosts=StatusImmunity(CONTROL_UNDEAD);`

**Spell candidates** (19 found, showing 14)
- `Projectile_AiHelper_HungerOfHadar`
  <br>`SpellType=Projectile`  `SpellProperties=ApplyStatus(VOID_START,100,1);ApplyStatus(VOID_END,100,1);`
- `Projectile_Jump_AnimateDead_Ghoul_Flying`
  <br>`SpellType=Projectile`
- `Projectile_Solution_Oil_Bane_Destroy` - **Oil of Bane**
  <br>`SpellType=Projectile`
- `Target_AnimateDead`
  <br>`SpellType=Target`
- `Target_AnimateDead_FlyingGhoul` - **Animate Dead: Flying Ghoul** | Create a flying ghoul that specialises in melee combat.
  <br>`SpellType=Target`  `SpellProperties=TARGET:SwitchDeathType(Explode);GROUND:IF(HasPassive('UndeadThrall_BetterSummon',context.Source)):Summon(1d7bd5b7-1879-452d-980f-34a5ba58a389,UntilLongRest,,,'AnimateDeadStack',UND…`
- `Target_AnimateDead_Ghoul` - **Animate Dead: Ghoul** | Create a ghoul that specialises in melee combat.
  <br>`SpellType=Target`  `SpellProperties=TARGET:SwitchDeathType(Explode);GROUND:IF(HasPassive('UndeadThrall_BetterSummon',context.Source)):Summon(405e65e2-a6c9-4418-9de6-b06978d033b7,UntilLongRest,,,'AnimateDeadStack',UND…`
- `Target_AnimateDead_Skeleton` - **Animate Dead: Skeleton** | Create a skeleton that specialises in ranged combat.
  <br>`SpellType=Target`  `SpellProperties=SwitchDeathType(Explode);Summon(6c06cda2-6e13-4663-a6f6-c4bb7564c10f, UntilLongRest,,,'AnimateDeadStack',UNSUMMON_ABLE,SHADOWCURSE_SUMMON_CHECK)`
- `Target_AnimateDead_Surgeon` - **Lovely Assistant** | The Surgeon reanimates the corpse of one of his nurses.
  <br>`SpellType=Target`  `SpellProperties=AI_IGNORE:Resurrect(100,25,Undead); AI_IGNORE:RestoreResource(Movement,100%,0); AI_IGNORE:RestoreResource(ActionPoint,1,0); AI_IGNORE:RestoreResource(BonusActionPoint,1,0); AI_ONLY…`
- `Target_AnimateDead_Zombie` - **Animate Dead: Zombie** | Create a zombie that specialises in melee combat.
  <br>`SpellType=Target`  `SpellProperties=SwitchDeathType(Explode);Summon(c2a2c269-ede8-4887-99f1-e0c044cc0c75,UntilLongRest,,,'AnimateDeadStack',UNSUMMON_ABLE,SHADOWCURSE_SUMMON_CHECK)`
- `Target_Bane`
  <br>`SpellSuccess=ApplyStatus(<em>BANE</em>, 100, 10)`
- `Target_Bane_Drider`
  <br>`SpellType=Target`
- `Target_Bane_ThiefOfFiveFates` - **Invocation: Bane**
  <br>`SpellType=Target`
- `Target_BanesWrath` - **Bane's Wrath**
- `Target_Claws_AnimateDead_Ghoul`
  <br>`SpellType=Target`  `SpellSuccess=DealDamage(max(1,3d6+UnarmedMeleeAbilityModifier),Slashing);AI_IGNORE:TARGET:IF(SpellDoesntApplyToElvesOrUndead(Ability.Constitution,5)):ApplyStatus(PARALYZED,100,2)`

---

## Ranger

### `CX_Ranger_Boost`  -  _hybrid_
_Currently in manager_ - passives: `CrossbowExpert_Wounding`, `FightingStyle_Archery`; spells: `Projectile_Jump`

**Passive candidates** (24 found, showing 18)
- `ExtraAttack`
- `ExtraAttack_2` - **Improved Extra Attack** | You can make two additional attacks after attacking with your main-hand weapon.
- `ExtraAttack_BonusTechnical`
- `FavoredEnemy_BountyHunter` - **Bounty Hunter** | You gain Proficiency in Investigation. Creatures you hit with Ensnaring Strike (either ranged or melee) have Disadvantage on their Saving Throw.
  <br>`Boosts=ProficiencyBonus(Skill,Investigation)`
- `FavoredEnemy_KeeperOfTheVeil` - **Keeper of the Veil** | You specialise in hunting creatures from other planes of existence. You gain Proficiency in Arcana, and can cast Protection from Evil and Good.
  <br>`Boosts=ProficiencyBonus(Skill,Arcana);UnlockSpell(Target_ProtectionFromEvilAndGood,Singular,None,UntilRest,Wisdom)`
- `FavoredEnemy_MageBreaker` - **Mage Breaker** | You have a history of battling spellcasters. You gain Proficiency in Arcana and can cast True Strike.
  <br>`Boosts=ProficiencyBonus(Skill,Arcana); UnlockSpell(Target_TrueStrike,,,,Wisdom)`
- `FavoredEnemy_RangerKnight` - **Ranger Knight** | You have sworn to serve a crown or nation and seek to bring its foes to ruin. Gain Skill Proficiency in History and Armour Proficiency with Heavy Armour.
  <br>`Boosts=ProficiencyBonus(Skill,History); Proficiency(HeavyArmor)`
- `FavoredEnemy_SanctifiedStalker` - **Sanctified Stalker** | You swore to hunt the enemies of a holy or druidic order. You gain Proficiency in Religion and can cast Sacred Flame.
  <br>`Boosts=ProficiencyBonus(Skill,Religion);UnlockSpell(Target_SacredFlame,,,,Wisdom)`
- `LOW_Guildhall_ExtraAttack_DaggerSpecialist` - **Dagger Specialist** | This creature can throw up to 3 daggers per round.
- `NaturalExplorer` - **Natural Explorer** | Your skills as a ranger are unmatched. Choose one Skill you are already Proficient in. Your Proficiency Bonus for that Skill is doubled.
- `NaturalExplorer_BeastTamer` - **Beast Tamer** | You have cultivated a strong bond with animals. You can cast Find Familiar without expending a spell slot.
  <br>`Boosts=UnlockSpell(Target_FindFamiliar_Ritual)`
- `NaturalExplorer_ExpertClimber` - **Expert Climber** | You have conquered mountains and scaled towering trees. Climbing does not cost you movement speed.
- `NaturalExplorer_UrbanTracker` - **Urban Tracker** | An expert at navigating the wild within the city, you gain Proficiency in Sleight of Hand.
  <br>`Boosts=ProficiencyBonus(Skill,SleightOfHand)`
- `NaturalExplorer_WastelandWander_Cold` - **Wasteland Wanderer: Cold** | You have spent endless days surviving desolate tundras. You gain Resistance to Cold damage.
  <br>`Boosts=Resistance(Cold, Resistant)`
- `NaturalExplorer_WastelandWander_Fire` - **Wasteland Wanderer: Fire** | You have spent endless days surviving forbidding deserts. You gain Resistance to Fire damage.
  <br>`Boosts=Resistance(Fire, Resistant)`
- `NaturalExplorer_WastelandWander_Poison` - **Wasteland Wanderer: Poison** | You have spent endless days surviving fetid swamps. You gain Resistance to Poison damage.
  <br>`Boosts=Resistance(Poison, Resistant)`
- `Slayer_ExtraAttack`
- `Slayer_ExtraAttack_2`

**Spell candidates** (11 found)
- `Projectile_EnsnaringStrike` - **Ensnaring Strike (Ranged)** | Your attack summons thorny vines that possibly Ensnare your target.
  <br>`SpellType=Projectile`  `SpellSuccess=IF(not SavingThrow(Ability.Strength, SourceSpellDC(),AdvantageOnRestrained(),DisadvantageOnRestrained())):ApplyStatus(ENSNARING_STRIKE,100,10);DealDamage(MainRangedWeapon, MainRang…`
- `Projectile_HailOfThorns` - **Hail of Thorns** | The thorns deal [1] to the target and then explode. The explosion deals an additional [2] to the target and surrounding creatures.
  <br>`SpellType=Projectile`  `SpellSuccess=TARGET:IF(Attack(AttackType.RangedWeaponAttack)):DealDamage(MainRangedWeapon, MainRangedWeaponDamageType);TARGET:AOE:IF(not HasStatus('SHIELD_MASTER') or not HasActionResource('Rea…`
- `Projectile_LightningArrow` - **Lightning Arrow** | After the arrow hits, smaller bolts snake out from the target toward nearby creatures.
  <br>`SpellType=Projectile`  `SpellSuccess=DealDamage(2d8,Lightning,Magical); TARGET:IF(Attack(AttackType.RangedSpellAttack)):DealDamage(4d8,Lightning,Magical)`
- `Shout_WildMagic_SpikeGrowth` - **Wild Magic: Spike Growth** | Shape a piece of ground around yourself into hard spikes. A creature walking on the spikes takes [1] for every [2] it moves.
  <br>`SpellType=Shout`  `SpellProperties=GROUND:CreateSurface(4,3,SpikeGrowth)`
- `Target_EnsnaringStrike` - **Ensnaring Strike (Melee)** | Your attack summons thorny vines that possibly Ensnare your target.
  <br>`SpellType=Target`  `SpellSuccess=IF(not SavingThrow(Ability.Strength, SourceSpellDC(),AdvantageOnRestrained(),DisadvantageOnRestrained())):ApplyStatus(ENSNARING_STRIKE,100,10);DealDamage(MainMeleeWeapon, MainMelee…`
- `Target_HuntersMark` - **Hunter's Mark** | Mark a creature as your quarry to deal an additional [1] whenever you hit it with a weapon attack.
  <br>`SpellType=Target`  `SpellProperties=ApplyStatus(SELF,HUNTERS_MARK_OWNER,100,-1);ApplyStatus(HUNTERS_MARK,100,-1)`
- `Target_HuntersMark_Reapply` - **Reapply Hunter's Mark** | Shift your Hunter's Mark to a new creature without using a spell slot.
  <br>`SpellType=Target`  `SpellProperties=ApplyStatus(SELF,HUNTERS_MARK_OWNER,100,-1,,,,,true);ApplyStatus(HUNTERS_MARK,100,-1,,,,,true);RemoveStatus(SELF,HUNTERS_MARK_REAPPLY)`
- `Target_SpikeGrowth`
  <br>`SpellProperties=GROUND:CreateSurface(6,100,<em>SpikeGrowth</em>,true)`
- `Target_SpikeGrowth_Dryad`
  <br>`SpellType=Target`
- `Target_Volley` - **Volley**
- `Zone_ConjureBarrage_Melee` - **Channel your weapon's essence into a destructive, widespread volley.**

### `CX_Ranger_BeastMaster_Boost`  -  _hybrid_
_Currently in manager_ - passives: `CompanionsBond`, `NaturalExplorer_BeastTamer`; spells: `Shout_BladeWard`, `Shout_ZephyrStrike`, `Target_HealingWord`, `Target_RangersCompanion`, `Target_SummonBeast`

**Passive candidates** (2 found)
- `BestialFury` - **Bestial Fury** | Your bond with your companion has deepened, unlocking their inner strength and giving them an Extra Attack.
- `ExceptionalTraining` - **Exceptional Training** | Your animal companion can Dash, Disengage, and Help as a bonus action.

**Spell candidates** (22 found, showing 14)
- `Target_FindFamiliar`
  <br>`SpellType=Target`
- `Target_FindFamiliar_Boo` - **Find Familiar: Boo** | Summon your adorable, occasionally violent, and above all faithful companion, Boo.
  <br>`SpellType=Target`  `SpellProperties=GROUND:Summon(6f65f77f-4583-4dd7-be15-b737d0175061,Permanent,Projectile_AiHelper_Summon_Weak,,'FindFamiliarStack',UNSUMMON_ABLE,SHADOWCURSE_SUMMON_CHECK);`
- `Target_FindFamiliar_Cat` - **Find Familiar: Cat** | Summon a cat familiar that can Meow to distract your enemies.
  <br>`SpellType=Target`  `SpellProperties=GROUND:IF(IsImprovedPactOfTheChain()):Summon(be212ed5-a622-4560-96be-0ee27ea1f913,Permanent,,,'FindFamiliarStack',UNSUMMON_ABLE,EXTRA_ATTACK_THIRSTING_BLADE_TECHNICAL,SHADOWCURSE_S…`
- `Target_FindFamiliar_Cat_Ritual`
  <br>`SpellType=Target`  `SpellProperties=GROUND:IF(IsImprovedPactOfTheChain()):Summon(be212ed5-a622-4560-96be-0ee27ea1f913,Permanent,,,'FindFamiliarStack',UNSUMMON_ABLE,EXTRA_ATTACK_THIRSTING_BLADE_TECHNICAL,SHADOWCURSE_S…`
- `Target_FindFamiliar_Crab` - **Find Familiar: Crab** | Summon a crab familiar that can slow enemies with its Crippling Pinch.
  <br>`SpellType=Target`  `SpellProperties=GROUND:IF(IsImprovedPactOfTheChain()):Summon(48cda2b7-04bc-40c2-81f5-1dddabcd15ab,Permanent,,,'FindFamiliarStack',UNSUMMON_ABLE,EXTRA_ATTACK_THIRSTING_BLADE_TECHNICAL,SHADOWCURSE_S…`
- `Target_FindFamiliar_Crab_Ritual` - **Find Familiar: Crab** | Summon a crab familiar that can slow enemies with its Crippling Pinch.
  <br>`SpellType=Target`  `SpellProperties=GROUND:IF(IsImprovedPactOfTheChain()):Summon(48cda2b7-04bc-40c2-81f5-1dddabcd15ab,Permanent,,,'FindFamiliarStack',UNSUMMON_ABLE,EXTRA_ATTACK_THIRSTING_BLADE_TECHNICAL,SHADOWCURSE_S…`
- `Target_FindFamiliar_Dog` - **Find Familiar: Scratch** | Summon the best boy. Scratch's keen nose can discover many things hidden around the world.
  <br>`SpellType=Target`  `SpellProperties=GROUND:Summon(b5deaa14-03b5-41c6-8372-7a9d758b4dfb, Permanent,Projectile_AiHelper_Summon_Weak,,'FindFamiliarStack',UNSUMMON_ABLE,SHADOWCURSE_SUMMON_CHECK);`
- `Target_FindFamiliar_Frog` - **Find Familiar: Frog** | Summon a frog familiar who can spread its Bufotoxin to enemies.
  <br>`SpellType=Target`  `SpellProperties=GROUND:IF(IsImprovedPactOfTheChain()):Summon(4521a4d1-0940-41de-b4c2-0314b8c8f32d, Permanent,,,'FindFamiliarStack',UNSUMMON_ABLE,EXTRA_ATTACK_THIRSTING_BLADE_TECHNICAL,SHADOWCURSE_…`
- `Target_FindFamiliar_Frog_Ritual` - **Find Familiar: Frog** | Summon a frog familiar who can spread its Bufotoxin to enemies.
  <br>`SpellType=Target`  `SpellProperties=GROUND:IF(IsImprovedPactOfTheChain()):Summon(4521a4d1-0940-41de-b4c2-0314b8c8f32d, Permanent,,,'FindFamiliarStack',UNSUMMON_ABLE,EXTRA_ATTACK_THIRSTING_BLADE_TECHNICAL,SHADOWCURSE_…`
- `Target_FindFamiliar_Rat` - **Find Familiar: Rat** | Summon a rat familiar with an Infectious Bite.
  <br>`SpellType=Target`  `SpellProperties=GROUND:IF(IsImprovedPactOfTheChain()):Summon(d779b7f9-2c7b-4f85-b914-f09e00c117f2, Permanent,,,'FindFamiliarStack',UNSUMMON_ABLE,EXTRA_ATTACK_THIRSTING_BLADE_TECHNICAL,SHADOWCURSE_…`
- `Target_FindFamiliar_Rat_Ritual` - **Find Familiar: Rat** | Summon a rat familiar with an Infectious Bite.
  <br>`SpellType=Target`  `SpellProperties=GROUND:IF(IsImprovedPactOfTheChain()):Summon(d779b7f9-2c7b-4f85-b914-f09e00c117f2, Permanent,,,'FindFamiliarStack',UNSUMMON_ABLE,EXTRA_ATTACK_THIRSTING_BLADE_TECHNICAL,SHADOWCURSE_…`
- `Target_FindFamiliar_Raven` - **Find Familiar: Raven** | Summon a raven familiar that can Blind enemies with its beak.
  <br>`SpellType=Target`  `SpellProperties=GROUND:IF(IsImprovedPactOfTheChain()):Summon(ecdffa46-80bd-41d2-8a50-4460a2810672, Permanent,,,'FindFamiliarStack',UNSUMMON_ABLE,EXTRA_ATTACK_THIRSTING_BLADE_TECHNICAL,SHADOWCURSE_…`
- `Target_FindFamiliar_Raven_Ritual` - **Find Familiar: Raven** | Summon a raven familiar that can Blind enemies with its beak.
  <br>`SpellType=Target`  `SpellProperties=GROUND:IF(IsImprovedPactOfTheChain()):Summon(ecdffa46-80bd-41d2-8a50-4460a2810672, Permanent,,,'FindFamiliarStack',UNSUMMON_ABLE,EXTRA_ATTACK_THIRSTING_BLADE_TECHNICAL,SHADOWCURSE_…`
- `Target_FindFamiliar_Ritual`
  <br>`SpellType=Target`

### `CX_Ranger_GloomStalker_Boost`  -  _hybrid_
_Currently in manager_ - passives: `DevilsSight`, `MAG_Shadow_Blinding_Bow_Passive`; spells: `Shout_AbsorbElements`, `Target_Darkness`, `Target_MistyStep`

**Passive candidates** (3 found)
- `DreadAmbusher` - **Dread Ambusher** | You specialise in taking out foes swiftly and ruthlessly.You gain a +[1] bonus to Initiative. On the first turn of combat, your movement speed increases by [2], and you can make an attack that deals an additional [3] damage.
  <br>`Boosts=Initiative(3)`
- `IronMind` - **Iron Mind** | You have honed your ability to resist the mind-altering powers of your prey. You gain Proficiency in Wisdom and Intelligence Saving Throws.
  <br>`Boosts=ProficiencyBonus(SavingThrow,Wisdom);ProficiencyBonus(SavingThrow,Intelligence)`
- `StalkersFlurry` - **Stalker's Flurry** | You are swift enough to turn a miss into a new strike. When you miss with a weapon attack, you can make another weapon attack for free.

**Spell candidates** (10 found)
- `Projectile_DreadAmbusher` - **Dread Ambusher (Ranged)** | On the first turn of each combat, ambush a target with an additional swift and precise shot.
  <br>`SpellType=Projectile`  `SpellSuccess=DealDamage(max(1,MainRangedWeapon+1d8), MainRangedWeaponDamageType); ExecuteWeaponFunctors(MainHand)`  `SpellProperties=GROUND:DealDamage(MainRangedWeapon, MainRangedWeaponDamageType);GROUND:ExecuteWeaponFunctors(MainHand);IF(not Player(context.Source)):ApplyStatus(SELF,AI_HELPER_EXTRAATTACK,100,1)`
- `Projectile_ScorchingRay` - **Scorching Ray** | Hurl [2] rays of fire. Each ray deals [1].
  <br>`SpellType=Projectile`  `SpellSuccess=DealDamage(2d6,Fire,Magical)`  `SpellProperties=GROUND:SurfaceChange(Ignite);GROUND:SurfaceChange(Melt)`
- `Projectile_ScorchingRay_CircletOfBlasting`
  <br>`SpellType=Projectile`
- `Shout_DisguiseSelf` - **Disguise Self** | Magically change all aspects of your appearance.
  <br>`SpellType=Shout`
- `Shout_DisguiseSelf_MaskOfManyFaces` - **Shapeshift**
  <br>`SpellType=Shout`
- `Shout_Hide_DreadAmbusher` - **Dread Ambusher: Hide**
  <br>`SpellType=Shout`
- `Shout_PassWithoutTrace` - **Pass Without Trace** | Call forth a veil of shadows and silence that gives you and all nearby companions a +10 bonus to Stealth Checks.
  <br>`SpellType=Shout`  `SpellProperties=ApplyStatus(PASS_WITHOUT_TRACE_AURA, 100, -1)`
- `Target_DreadAmbusher` - **Dread Ambusher (Melee)** | On the first turn of each combat, ambush a target with an additional swift and precise attack.
  <br>`SpellType=Target`  `SpellSuccess=DealDamage(max(1,MainMeleeWeapon+1d8), MainMeleeWeaponDamageType);ExecuteWeaponFunctors(MainHand)`
- `Target_FogCloud`
  <br>`SpellProperties=GROUND:CreateSurface(4.5,10,<em>FogCloud</em>,true)`
- `Shout_WildMagic_Fog`
  <br>`SpellProperties=GROUND:CreateSurface(6,3,<em>FogCloud</em>)`

### `CX_Ranger_Hunter_Boost`  -  _hybrid_
_Currently in manager_ - passives: `HordeBreaker`, `MAG_BonusAttack_AgainstMarked_Passive`, `StalkersFlurry`; spells: `Projectile_HailOfThorns`, `Target_HuntersMark`, `Target_Web`

**Passive candidates** (6 found)
- `ColossusSlayer`
- `EscapeTheHorde` - **Escape the Horde** | Opportunity Attacks against you have Disadvantage.
  <br>`Boosts=IF(IsReactionAttack(context.Source)):Disadvantage(AttackTarget)`
- `GiantKiller` - **Giant Killer** | If a Large or bigger creature attacks you, you can use your reaction to make a melee attack.
  <br>`Boosts=UnlockInterrupt(Interrupt_GiantKiller)`
- `MultiattackDefense` - **Multiattack Defence** | When an enemy attacks you, they have a -[1] penalty to additional Attack Rolls against you until the start of their next turn.
- `IncorporealMovement` - **Incorporeal Movement**
- `HordeBreaker` _(already in manager)_ - **Horde Breaker** | Target two creatures standing close to each other, attacking them in quick succession.
  <br>`Boosts=UnlockSpell(Target_HordeBreaker,Singular);UnlockSpell(Projectile_HordeBreaker,Singular)`

**Spell candidates** (8 found)
- `Projectile_HordeBreaker` - **Horde Breaker (Ranged)** | Target two creatures standing close to each other. Shoot the first creature and get a free shot at the second.
  <br>`SpellType=Projectile`  `SpellSuccess=TARGET:DealDamage(MainRangedWeapon, MainRangedWeaponDamageType); ExecuteWeaponFunctors(MainHand)`  `SpellProperties=TARGET:ApplyStatus(HORDE_BREAKER_TECHNICAL,100,1);ApplyStatus(SELF,HORDE_BREAKER,100,1);ApplyStatus(SELF,HORDE_BREAKER_TECHNICAL,100,1);GROUND:DealDamage(MainRangedWeapon, MainRang…`
- `Projectile_HordeBreaker_Free` - **Horde Breaker Follow-Up (Ranged)** | Follow up on your horde breaker with a second attack.
  <br>`SpellType=Projectile`  `SpellProperties=RemoveStatus(SELF,HORDE_BREAKER);RemoveStatus(HORDE_BREAKER_TARGET);GROUND:ExecuteWeaponFunctors(MainHand)`
- `Projectile_LightningArrow` - **Lightning Arrow** | After the arrow hits, smaller bolts snake out from the target toward nearby creatures.
  <br>`SpellType=Projectile`  `SpellSuccess=DealDamage(2d8,Lightning,Magical); TARGET:IF(Attack(AttackType.RangedSpellAttack)):DealDamage(4d8,Lightning,Magical)`
- `Target_HordeBreaker` - **Horde Breaker (Melee)** | Target two creatures standing close to each other. Attack the first creature and get a free shot at the second.
  <br>`SpellType=Target`  `SpellSuccess=TARGET:DealDamage(MainMeleeWeapon, MainMeleeWeaponDamageType); ExecuteWeaponFunctors(MainHand)`  `SpellProperties=TARGET:ApplyStatus(HORDE_BREAKER_TECHNICAL,100,1);ApplyStatus(SELF,HORDE_BREAKER,100,1);ApplyStatus(SELF,HORDE_BREAKER_TECHNICAL,100,1);GROUND:DealDamage(MainMeleeWeapon, MainMelee…`
- `Target_HordeBreaker_Free` - **Horde Breaker Follow-Up (Melee)** | Follow up on your horde breaker with a second attack.
  <br>`SpellType=Target`  `SpellProperties=RemoveStatus(SELF,HORDE_BREAKER);RemoveStatus(HORDE_BREAKER_TARGET);GROUND:DealDamage(MainMeleeWeapon, MainMeleeWeaponDamageType);GROUND:ExecuteWeaponFunctors(MainHand)`
- `Target_Volley` - **Volley**
- `Zone_ConjureBarrage_Melee` - **Channel your weapon's essence into a destructive, widespread volley.**
- `Projectile_HailOfThorns` _(already in manager)_ - **Hail of Thorns** | The thorns deal [1] to the target and then explode. The explosion deals an additional [2] to the target and surrounding creatures.
  <br>`SpellType=Projectile`  `SpellSuccess=TARGET:IF(Attack(AttackType.RangedWeaponAttack)):DealDamage(MainRangedWeapon, MainRangedWeaponDamageType);TARGET:AOE:IF(not HasStatus('SHIELD_MASTER') or not HasActionResource('Rea…`

---

## Rogue

### `CX_Rogue_Boost`  -  _martial_
_Currently in manager_ - passives: `Assassinate_Initiative`, `SneakAttack_Unlock`; spells: `Projectile_Jump`, `Projectile_SneakAttack`, `Shout_Disengage_CunningAction`, `Target_SneakAttack`

**Passive candidates** (10 found)
- `Evasion` - **Evasion** | Your agility lets you dodge out of the way of certain spells.When a spell or effect would deal half damage on a successful Dexterity Saving Throw, it deals no damage if you succeed, and only half damage if you fail.
  <br>`Boosts=AreaDamageEvade()`
- `LOW_Cistern_Evasion` - **Morphic Evasion** | Whenever you fail a Saving Throw against an attack from a non-hostile creature, you may succeed instead.
- `MAG_DexteritySavingThrow_Evasion` - **Dextrous Evasion** | When you fail a Dexterity Saving Throw, you can use your reaction to succeed instead.
  <br>`Boosts=UnlockInterrupt(Interrupt_RingOfEvasion)`
- `MAG_LegendaryEvasion_Protection_Resource_Passive`
- `MAG_Necromancy_Evasion` - **Necromantic Evasion** | When you fail a Saving Throw against necromancy spells or spells cast by undead foes, you can use your reaction to succeed instead.
  <br>`Boosts=UnlockInterrupt(Interrupt_Scarab_Of_Protection)`
- `ReliableTalent` - **Reliable Talent** | When you make an Ability Check with a Skill you are Proficient with, the lowest result you can roll on the die is [1].
  <br>`Boosts=IF(HasProficiencyBonus(context.CheckedAbility,context.CheckedSkill,context.Source)):MinimumRollResult(RawAbility,10);IF(HasProficiencyBonus(context.CheckedAbility,context.CheckedSk…`
- `UncannyDodge` - **Uncanny Dodge**
- `DisplacerBeast_Avoidance`
- `MAG_Infernal_Metal_Legendary_Resistance_Passive` - **Infernal Evasion** | When you fail a Saving Throw, you may use your reaction to succeed instead.
  <br>`Boosts=UnlockInterrupt(Interrupt_Legendary_InfernalResistance)`
- `SneakAttack_Unlock` _(already in manager)_
  <br>`Boosts=UnlockInterrupt(Interrupt_SneakAttack);UnlockInterrupt(Interrupt_SneakAttack_Critical);UnlockSpell(Target_SneakAttack);UnlockSpell(Projectile_SneakAttack)`

**Spell candidates** (27 found, showing 14)
- `Projectile_SneakAttack_Rakish` - **Rakish Sneak Attack (Ranged)** | Deal extra damage to a foe you have Advantage against. You can also use this attack without Advantage if there are no other combatants within [1] of the target, or if you have an ally within that range.
  <br>`SpellType=Projectile`
- `Projectile_SneakAttack_Swarm`
  <br>`SpellType=Projectile`
- `Shout_Dash`
- `Shout_Dash_BonusAction` - **Dash: Bonus Action**
  <br>`SpellType=Shout`
- `Shout_Dash_CunningAction` - **Cunning Action: Dash**
  <br>`SpellType=Shout`
- `Shout_Dash_HookHorror`
  <br>`SpellType=Shout`
- `Shout_Dash_StepOfTheWind`
  <br>`SpellProperties=ApplyStatus(<em>DASH</em>,100,1); ApplyStatus(STEP_OF_THE_WIND,100,1)`
- `Shout_Disengage`
  <br>`SpellProperties=AI_IGNORE:ApplyStatus(<em>DISENGAGE</em>,100,1);AI_ONLY:IF(HasStatus('FLANKED')):ApplyStatus(<em>DISENGAGE</em>,100,1);`
- `Shout_Disengage_BonusAction` - **Disengage: Bonus Action** | Retreat safely: moving won't provoke Opportunity Attacks.
  <br>`SpellType=Shout`
- `Shout_Disengage_Goblin`
  <br>`SpellProperties=TARGET:ApplyStatus(<em>DISENGAGE</em>,100,1);`
- `Shout_Disengage_StepOfTheWind` - **Step of the Wind: Disengage** | Spend [1] ki point to gain the Disengage action as a bonus action this turn.
  <br>`SpellType=Shout`  `SpellProperties=ApplyStatus(DISENGAGE,100,1); ApplyStatus(STEP_OF_THE_WIND,100,1)`
- `Shout_Hide` - **Hide** | Hide from enemies
- `Shout_Hide_BonusAction` - **Cunning Action: Hide**
  <br>`SpellType=Shout`
- `Shout_Hide_DreadAmbusher` - **Dread Ambusher: Hide**
  <br>`SpellType=Shout`

### `CX_Rogue_ArcaneTrickster_Boost`  -  _hybrid_
_Currently in manager_ - passives: `Goon_Target_Longstrider_Passive`, `MageHandLegerdemain`; spells: `Shout_Shield_Wizard`, `Target_BoomingBlade`, `Target_CloudOfDaggers`, `Target_HideousLaughter`, `Target_MageHand`

**Passive candidates** (4 found)
- `MAG_ArcaneTrickster_Ring_Passive` - **Illusion Quickening** | After hitting a creature with a weapon attack, you can cast illusion or enchantment spells as a bonus action.
- `MagicalAmbush` - **Magical Ambush** | While you are Hidden, your targets have Disadvantage on Saving Throws against your spells.
- `UNI_Bow_SpellslotRecharge_Passive` - **Arcane Vehemence** | Once per Short Rest, you regain a Level 1 spell slot when you land a Critical Hit with the Spellthief.
- `MageHandLegerdemain` _(already in manager)_ - **Mage Hand Legerdemain** | When you cast Mage Hand, the spectral hand is invisible and permanent.
  <br>`Boosts=UnlockSpellVariant(SpellId('Target_MageHand'),ModifyTooltipDescription())`

**Spell candidates** (37 found, showing 14)
- `Projectile_Potion_Destroy_Invisibility` - **Potion of Invisibility**
  <br>`SpellType=Projectile`  `SpellProperties=GROUND:CreateSurface(1,,PotionInvisibilityCloud);`
- `Shout_Blur` - **Blur**
  <br>`SpellProperties=ApplyStatus(<em>BLUR</em>,100,10)`
- `Shout_FireShield` - **Fire Shield**
- `Shout_FireShield_Chill` - **Fire Shield: Chill**
- `Shout_FireShield_Warm` - **Fire Shield: Warm**
- `Shout_Invisibility_Duergar`
  <br>`SpellType=Shout`
- `Shout_Invisibility_Imp`
  <br>`SpellProperties=AI_IGNORE:ApplyStatus(<em>INVISIBILITY</em>,100,-1);AI_ONLY:ApplyStatus(<em>INVISIBILITY</em>,100,2);`
- `Shout_Invisibility_MistyEscape` - **Cloaking Mist** | Turn Invisible after casting Misty Step.
  <br>`SpellType=Shout`  `SpellProperties=ApplyStatus(MISTY_ESCAPE_INVISIBLE,100,1);`
- `Shout_Invisibility_Myrmidon_Air` - **Invisibility**
- `Shout_Invisibility_Quasit`
  <br>`SpellType=Shout`
- `Shout_Invisibility_ShadarKai_GloomWeaver` - **Invisibility** | Become Invisible. The spell ends if you attack, take an action or take damage.
  <br>`SpellType=Shout`  `SpellProperties=ApplyStatus(INVISIBILITY_SHADARKAI_GLOOMWEAVER,100,1);`
- `Shout_InvisibilityField_Orthon`
  <br>`SpellProperties=ApplyStatus(<em>INVISIBILITY</em>,100,2);`
- `Shout_SeeInvisibility` - **See Invisibility**
- `Shout_SeeInvisibility_ThirdEye` - **Third Eye: See Invisibility**

### `CX_Rogue_Assassin_Boost`  -  _martial_
_Currently in manager_ - passives: `Assassinate_Ambush`, `Assassinate_Resource`, `UND_ServantOfBoooal`

**Passive candidates** (3 found)
- `Assassinate_Initiative` - **Assassinate: Initiative** | You are deadliest against unprepared enemies. In combat, you have Advantage on Attack Rolls against creatures that haven't taken a turn yet.
  <br>`Boosts=IF(Combat(context.Source) and Combat() and not HadTurnInCombat()):Advantage(AttackRoll)`
- `Assassinate_Ambush` _(already in manager)_ - **Assassinate: Ambush** | Any successful Attack Roll against a Surprised creature is a Critical Hit.
  <br>`Boosts=IF(HasStatus('SURPRISED')):CriticalDamageOnHit()`
- `Assassinate_Resource` _(already in manager)_ - **Assassin's Alacrity** | Quick as an alley cat in a rain-dark city, you immediately restore your action and bonus action at the start of combat.

**Spell candidates** (6 found)
- `Shout_Hide` - **Hide** | Hide from enemies
- `Shout_Hide_BonusAction` - **Cunning Action: Hide**
  <br>`SpellType=Shout`
- `Shout_Hide_DreadAmbusher` - **Dread Ambusher: Hide**
  <br>`SpellType=Shout`
- `Shout_Hide_ShadowArts` - **Shadow Arts: Hide**
  <br>`SpellType=Shout`
- `Shout_HideInPlainSight` - **Hide in Plain Sight**
- `Shout_Inkblot` - **Create a cloud of magical darkness and immediately attempt to Hide.**

### `CX_Rogue_Thief_Boost`  -  _martial_
_Currently in manager_ - passives: `FastHands`, `GOB_PainPriest_Dagger_Passive`, `MAG_BarbMonk_Dexterity_Passive`

**Passive candidates** (4 found)
- `SecondStoryWork` - **Second-Story Work: Falling** | You've mastered the art of falling and gain resistance to Falling damage.
  <br>`Boosts=FallDamageMultiplier(0.5)`
- `SecondStoryWork_Climbing` - **Second-Story Work: Climbing** | Climbing no longer costs you extra movement speed.
- `SecondStoryWork_Jumping` - **Second-Story Work: Jumping** | Your jumping distance is increased.
- `FastHands` _(already in manager)_ - **Fast Hands** | Gain an additional bonus action.
  <br>`Boosts=ActionResource(BonusActionPoint,1,0)`

**Spell candidates** (16 found, showing 14)
- `Shout_Dash`
- `Shout_Dash_BonusAction` - **Dash: Bonus Action**
  <br>`SpellType=Shout`
- `Shout_Dash_CunningAction` - **Cunning Action: Dash**
  <br>`SpellType=Shout`
- `Shout_Dash_HookHorror`
  <br>`SpellType=Shout`
- `Shout_Dash_StepOfTheWind`
  <br>`SpellProperties=ApplyStatus(<em>DASH</em>,100,1); ApplyStatus(STEP_OF_THE_WIND,100,1)`
- `Shout_Disengage_CunningAction` - **Cunning Action: Disengage** | Retreat safely: moving won't provoke Opportunity Attacks.
  <br>`SpellType=Shout`
- `Shout_Hide` - **Hide** | Hide from enemies
- `Shout_Hide_BonusAction` - **Cunning Action: Hide**
  <br>`SpellType=Shout`
- `Shout_Hide_DreadAmbusher` - **Dread Ambusher: Hide**
  <br>`SpellType=Shout`
- `Shout_Hide_ShadowArts` - **Shadow Arts: Hide**
  <br>`SpellType=Shout`
- `Shout_HideInPlainSight` - **Hide in Plain Sight**
- `Shout_SteelWatcher_Quadruped_Dash`
  <br>`SpellType=Shout`  `SpellProperties=ApplyStatus(STEELWATCHER_QUADRUPED_DASH,100,1)`
- `Projectile_MobileShooting` - **After using Dash or Disengage this turn, you can make a ranged attack as a bonus action.**
- `Shout_ExpeditiousRetreat`
  <br>`SpellProperties=IF(HasStatus('<em>DASH</em>')):ApplyStatus(DASH_STACKED,100,1);IF(not HasStatus('<em>DASH</em>')):ApplyStatus(<em>DASH</em>,100,1);ApplyStatus(EXPEDITIOUS_RETREAT, 100, -1)`

---

## Sorcerer

### `CX_Sorcerer_Boost`  -  _caster_
_Currently in manager_ - passives: `Goon_Target_MageArmor_Passive`; spells: `Projectile_Jump`

**Passive candidates** (10 found)
- `Metamagic_Careful` - **Metamagic: Careful Spell**
- `Metamagic_Distant` - **Metamagic: Distant Spell**
- `Metamagic_Distant_NPC`
- `Metamagic_Empowered` - **Metamagic: Empowered Spell** | Increase the cost of spells that deal direct damage by [1] Sorcery Point to roll their damage with Advantage.You can use Empowered Spell in combination with other Metamagic.
  <br>`Boosts=Reroll(Damage,20,true);UnlockSpellVariant(EmpoweredSpellCheck(),ModifyUseCosts(Add,SorceryPoint,1,0))`
- `Metamagic_Extended` - **Metamagic: Extended Spell**
- `Metamagic_Heightened` - **Metamagic: Heightened Spell**
- `Metamagic_Quickened` - **Metamagic: Quickened Spell**
- `Metamagic_Subtle` - **Metamagic: Subtle Spell**
- `Metamagic_Twinned` - **Metamagic: Twinned Spell**
- `WildMagic_SorceryPoints`

**Spell candidates** (19 found, showing 14)
- `Projectile_ChromaticOrb` - **Chromatic Orb** | Hurl a sphere that deals [1] and possibly creates a surface on impact. Alternatively, choose a different type of damage.
  <br>`SpellType=Projectile`  `SpellProperties=GROUND:CreateSurface(2,2,Acid)`
- `Projectile_ChromaticOrb_Acid` - **Chromatic Orb: Acid** | Hurl caustic energy that damages the target and creates an Acid surface on impact.
  <br>`SpellType=Projectile`  `SpellSuccess=DealDamage(2d8,Acid,Magical)`  `SpellProperties=GROUND:CreateSurface(2,2,Acid)`
- `Projectile_ChromaticOrb_Acid_BookOfAncientSecrets`
  <br>`SpellType=Projectile`
- `Projectile_ChromaticOrb_BookOfAncientSecrets`
  <br>`SpellType=Projectile`
- `Projectile_ChromaticOrb_Cold` - **Chromatic Orb: Cold** | Hurl freezing energy that damages the target and creates a frosty surface to knock creatures Prone.
  <br>`SpellType=Projectile`  `SpellSuccess=DealDamage(2d8,Cold,Magical);RemoveStatus(BURNING)`  `SpellProperties=GROUND:SurfaceChange(Freeze);GROUND:CreateSurface(2,2,WaterFrozen)`
- `Projectile_ChromaticOrb_Fire` - **Chromatic Orb: Fire** | Hurl fiery energy that damages the target and creates a Burning surface on impact.
  <br>`SpellType=Projectile`  `SpellSuccess=DealDamage(2d8,Fire,Magical)`  `SpellProperties=GROUND:SurfaceChange(Ignite);GROUND:SurfaceChange(Melt);GROUND:CreateSurface(2,2,Fire)`
- `Projectile_ChromaticOrb_IceMephit`
  <br>`SpellType=Projectile`
- `Projectile_ChromaticOrb_Lightning` - **Chromatic Orb: Lightning** | Hurl lightning energy that damages the target and creates an electrified surface on impact.
  <br>`SpellType=Projectile`  `SpellSuccess=DealDamage(2d8,Lightning,Magical)`  `SpellProperties=GROUND:SurfaceChange(Electrify);GROUND:CreateSurface(2,2,WaterElectrified)`
- `Projectile_ChromaticOrb_Poison` - **Chromatic Orb: Poison** | Hurl poisonous energy that damages the target and creates a bubbling surface to Poison creatures.
  <br>`SpellType=Projectile`  `SpellSuccess=DealDamage(2d8,Poison,Magical)`  `SpellProperties=GROUND:CreateSurface(2,2,Poison)`
- `Projectile_ChromaticOrb_Thunder` - **Chromatic Orb: Thunder** | Hurl a sphere of thunderous energy.
  <br>`SpellType=Projectile`  `SpellSuccess=DealDamage(3d8,Thunder,Magical)`
- `Projectile_Fireball` - **Fireball**
- `Projectile_Fireball_Dragon` - **Fire Breath**
  <br>`SpellType=Projectile`  `SpellSuccess=DealDamage(14d6,Fire,Magical);ApplyStatus(BURNING,100,2)`
- `Projectile_MagicMissile` - **Magic Missile** | Shoot [2] magical darts, each dealing [1]. They always hit their target.
  <br>`SpellType=Projectile`  `SpellProperties=DealDamage(1d4+1,Force,Magical)`
- `Projectile_MagicMissile_MindFlayer`
  <br>`SpellType=Projectile`

### `CX_Sorcerer_DraconicBloodline_Boost`  -  _caster_
_Currently in manager_ - passives: `DraconicResilience`; spells: `Projectile_IceKnife`, `Projectile_RayOfSickness`, `Projectile_WitchBolt`, `Zone_BurningHands`, `Zone_CausticBrew`

**Passive candidates** (19 found, showing 18)
- `DraconicAncestry_Black` - **Draconic Ancestry: Black (Acid)** | At Level 6, spells that deal Acid damage are more powerful, and you can become resistant to Acid damage.
  <br>`Boosts=UnlockSpell(Target_Grease,AddChildren,d136c5d9-0ff0-43da-acce-a74a07f8d6bf,,Charisma)`
- `DraconicAncestry_Blue` - **Draconic Ancestry: Blue (Lightning)** | At Level 6, spells that deal Lightning damage are more powerful, and you can become resistant to Lightning damage.
  <br>`Boosts=UnlockSpell(Projectile_WitchBolt,AddChildren,d136c5d9-0ff0-43da-acce-a74a07f8d6bf,,Charisma)`
- `DraconicAncestry_Brass` - **Draconic Ancestry: Brass (Fire)** | At Level 6, spells that deal Fire damage are more powerful, and you can become resistant to Fire damage.
  <br>`Boosts=UnlockSpell(Target_Sleep,AddChildren,d136c5d9-0ff0-43da-acce-a74a07f8d6bf,,Charisma)`
- `DraconicAncestry_Bronze` - **Draconic Ancestry: Bronze (Lightning)** | At Level 6, spells that deal Lightning damage are more powerful, and you can become resistant to Lightning damage.
  <br>`Boosts=UnlockSpell(Target_FogCloud,AddChildren,d136c5d9-0ff0-43da-acce-a74a07f8d6bf,,Charisma)`
- `DraconicAncestry_Copper` - **Draconic Ancestry: Copper (Acid)** | At Level 6, spells that deal Acid damage are more powerful, and you can become resistant to Acid damage.
  <br>`Boosts=UnlockSpell(Target_HideousLaughter,AddChildren,d136c5d9-0ff0-43da-acce-a74a07f8d6bf,,Charisma)`
- `DraconicAncestry_Gold` - **Draconic Ancestry: Gold (Fire)** | At Level 6, spells that deal Fire damage are more powerful, and you can become resistant to Fire damage.
  <br>`Boosts=UnlockSpell(Shout_DisguiseSelf,AddChildren,d136c5d9-0ff0-43da-acce-a74a07f8d6bf,,Charisma)`
- `DraconicAncestry_Green` - **Draconic Ancestry: Green (Poison)** | At Level 6, spells that deal Poison damage are more powerful, and you can become resistant to Poison damage.
  <br>`Boosts=UnlockSpell(Projectile_RayOfSickness,AddChildren,d136c5d9-0ff0-43da-acce-a74a07f8d6bf,,Charisma)`
- `DraconicAncestry_Red` - **Draconic Ancestry: Red (Fire)** | At Level 6, spells that deal Fire damage are more powerful, and you can become resistant to Fire damage.
  <br>`Boosts=UnlockSpell(Zone_BurningHands,AddChildren,d136c5d9-0ff0-43da-acce-a74a07f8d6bf,,Charisma)`
- `DraconicAncestry_Silver` - **Draconic Ancestry: Silver (Cold)** | At Level 6, spells that deal Cold damage are more powerful, and you can become resistant to Cold damage.
  <br>`Boosts=UnlockSpell(Shout_FeatherFall,AddChildren,d136c5d9-0ff0-43da-acce-a74a07f8d6bf,,Charisma)`
- `DraconicAncestry_White` - **Draconic Ancestry: White (Cold)** | At Level 6, spells that deal Cold damage are more powerful, and you can become resistant to Cold damage.
  <br>`Boosts=UnlockSpell(Shout_ArmorOfAgathys,AddChildren,d136c5d9-0ff0-43da-acce-a74a07f8d6bf,,Charisma)`
- `ElementalAffinity_Damage` - **Elemental Affinity: Damage** | When you cast a spell that deals damage of the type associated with your draconic ancestry, you add your Charisma Modifier to the damage.
- `ElementalAffinity_Resistance_Acid` - **Elemental Affinity: Acid Resistance** | When you cast a spell that deals Acid damage, you can spend 1 Sorcery Point to gain Resistance to Acid damage until your next Long Rest.
- `ElementalAffinity_Resistance_Check` - **Elemental Affinity: Resistance** | When you cast a spell that deals damage of the type associated with your draconic ancestry, you can spend 1 Sorcery Point to gain Resistance to that damage type.
  <br>`Boosts=UnlockInterrupt(Interrupt_ElementalAffinity)`
- `ElementalAffinity_Resistance_Cold` - **Elemental Affinity: Cold Resistance** | When you cast a spell that deals Cold damage, you can spend 1 Sorcery Point to gain Resistance to Cold damage until your next Long Rest.
- `ElementalAffinity_Resistance_Fire` - **Elemental Affinity: Fire Resistance** | When you cast a spell that deals Fire damage, you can spend 1 Sorcery Point to gain Resistance to Fire damage until your next Long Rest.
- `ElementalAffinity_Resistance_Lightning` - **Elemental Affinity: Lightning Resistance** | When you cast a spell that deals Lightning damage, you can spend 1 Sorcery Point to gain Resistance to Lightning damage until your next Long Rest.
- `ElementalAffinity_Resistance_Poison` - **Elemental Affinity: Poison Resistance** | When you cast a spell that deals Poison damage, you can spend 1 Sorcery Point to gain Resistance to Poison damage until your next Long Rest.
- `LOW_GreaseWizard_ElementalAffinity`

**Spell candidates** (30 found, showing 14)
- `Projectile_AiHelper_Fear_Aura`
  <br>`SpellType=Projectile`  `SpellProperties=IF(Enemy()):ApplyStatus(FRIGHTENED,100,2)`
- `Projectile_ChromaticOrb` - **Chromatic Orb** | Hurl a sphere that deals [1] and possibly creates a surface on impact. Alternatively, choose a different type of damage.
  <br>`SpellType=Projectile`  `SpellProperties=GROUND:CreateSurface(2,2,Acid)`
- `Projectile_ChromaticOrb_Acid` - **Chromatic Orb: Acid** | Hurl caustic energy that damages the target and creates an Acid surface on impact.
  <br>`SpellType=Projectile`  `SpellSuccess=DealDamage(2d8,Acid,Magical)`  `SpellProperties=GROUND:CreateSurface(2,2,Acid)`
- `Projectile_ChromaticOrb_Acid_BookOfAncientSecrets`
  <br>`SpellType=Projectile`
- `Projectile_ChromaticOrb_BookOfAncientSecrets`
  <br>`SpellType=Projectile`
- `Projectile_ChromaticOrb_Cold` - **Chromatic Orb: Cold** | Hurl freezing energy that damages the target and creates a frosty surface to knock creatures Prone.
  <br>`SpellType=Projectile`  `SpellSuccess=DealDamage(2d8,Cold,Magical);RemoveStatus(BURNING)`  `SpellProperties=GROUND:SurfaceChange(Freeze);GROUND:CreateSurface(2,2,WaterFrozen)`
- `Projectile_ChromaticOrb_Fire` - **Chromatic Orb: Fire** | Hurl fiery energy that damages the target and creates a Burning surface on impact.
  <br>`SpellType=Projectile`  `SpellSuccess=DealDamage(2d8,Fire,Magical)`  `SpellProperties=GROUND:SurfaceChange(Ignite);GROUND:SurfaceChange(Melt);GROUND:CreateSurface(2,2,Fire)`
- `Projectile_ChromaticOrb_IceMephit`
  <br>`SpellType=Projectile`
- `Projectile_ChromaticOrb_Lightning` - **Chromatic Orb: Lightning** | Hurl lightning energy that damages the target and creates an electrified surface on impact.
  <br>`SpellType=Projectile`  `SpellSuccess=DealDamage(2d8,Lightning,Magical)`  `SpellProperties=GROUND:SurfaceChange(Electrify);GROUND:CreateSurface(2,2,WaterElectrified)`
- `Projectile_ChromaticOrb_Poison` - **Chromatic Orb: Poison** | Hurl poisonous energy that damages the target and creates a bubbling surface to Poison creatures.
  <br>`SpellType=Projectile`  `SpellSuccess=DealDamage(2d8,Poison,Magical)`  `SpellProperties=GROUND:CreateSurface(2,2,Poison)`
- `Projectile_ChromaticOrb_Thunder` - **Chromatic Orb: Thunder** | Hurl a sphere of thunderous energy.
  <br>`SpellType=Projectile`  `SpellSuccess=DealDamage(3d8,Thunder,Magical)`
- `Projectile_Fireball` - **Fireball**
- `Projectile_Fireball_Dragon` - **Fire Breath**
  <br>`SpellType=Projectile`  `SpellSuccess=DealDamage(14d6,Fire,Magical);ApplyStatus(BURNING,100,2)`
- `Projectile_Fly_DragonWings`
  <br>`SpellType=Projectile`

### `CX_Sorcerer_WildMagic_Boost`  -  _caster_
_Currently in manager_ - passives: `TidesOfChaos`, `WildMagic`; spells: `Target_ChaosBolt`

**Passive candidates** (4 found)
- `BendLuck` - **Bend Luck** | When a creature you can see makes an Attack Roll, Ability Check, or a Saving Throws, you can use your reaction and spend 2 Sorcery Point to roll 1d4, applying the number rolled as a bonus or penalty (your choice) to the creature's roll.
  <br>`Boosts=UnlockSpell(Target_BendLuck);UnlockInterrupt(Interrupt_BendLuck_Bonus);UnlockInterrupt(Interrupt_BendLuck_Malus)`
- `ControlledChaos` - **Controlled Chaos** | Foes may suffer a Wild Magic Surge while casting spells near your fluctuating magic.
  <br>`Boosts=UnlockInterrupt(Interrupt_ControlledChaos)`
- `TidesOfChaos_Unlock`
  <br>`Boosts=UnlockInterrupt(Interrupt_TidesOfChaos)`
- `TidesOfChaos` _(already in manager)_ - **Tides of Chaos**

**Spell candidates** (35 found, showing 14)
- `Projectile_MagicMissile` - **Magic Missile** | Shoot [2] magical darts, each dealing [1]. They always hit their target.
  <br>`SpellType=Projectile`  `SpellProperties=DealDamage(1d4+1,Force,Magical)`
- `Projectile_MagicMissile_MindFlayer`
  <br>`SpellType=Projectile`
- `Projectile_WildMagic_Heal`
  <br>`SpellType=Projectile`  `SpellProperties=RegainHitPoints(1d4)`
- `Shout__WildMagic` - **Wild Magic Surge** | Your spellcasting can unleash unpredictable surges of untamed magic.
  <br>`SpellType=Shout`
- `Shout__WildMagic_Activate` - **Wild Magic Surge** | Your spellcasting can unleash unpredictable surges of untamed magic.
  <br>`SpellType=Shout`
- `Shout_Rage_WildMagic` - **Rage: Wild Magic** | Enter a Rage that releases all the magic roiling inside of you, causing a random magical effect.
  <br>`SpellType=Shout`  `SpellProperties=AI_IGNORE:TriggerRandomCast(1,0,WildMagicBarbarian);IF(ClassLevelHigherOrEqualThan(1,'Barbarian') and not ClassLevelHigherOrEqualThan(9,'Barbarian')):ApplyStatus(RAGE,100,10);IF(Cl…`
- `Shout_WildMagic_ActionSurge` - **Wild Magic: Action Surge** | You gain an additional action this turn.
  <br>`SpellType=Shout`  `SpellProperties=ApplyStatus(ACTION_SURGE,100,1)`
- `Shout_WildMagic_Blur` - **Wild Magic: Blur** | Each creature within [1] becomes Blurred.
  <br>`SpellType=Shout`  `SpellProperties=ApplyStatus(BLUR,100,3)`
- `Shout_WildMagic_Burning` - **Wild Magic: Burning** | Each creature and item within [1] starts burning and takes [2] per turn.
  <br>`SpellType=Shout`  `SpellProperties=ApplyStatus(WILD_MAGIC_BURNING,100,5)`
- `Shout_WildMagic_Cambion` - **Wild Magic: Cambion** | Summon a cambion from the fiery nexus of the Nine Hells. It is hostile to everyone.
  <br>`SpellType=Shout`  `SpellProperties=GROUND:Spawn(d9889d28-ca01-41f2-973e-275bbc8e2fe1)`
- `Shout_WildMagic_CatsAndDogs` - **Wild Magic: Cats and Dogs** | Each creature within [1] is randomly transformed into either a cat or a dog.
  <br>`SpellType=Shout`  `SpellSuccess=ApplyStatus(WILDMAGIC_CAT,100,2)`
- `Shout_WildMagic_Enchant` - **Wild Magic: Enchant Weapons** | Enchant the weapon of each creature within [1]. Their next attack is a Critical Hit and deals an additional [2].
  <br>`SpellType=Shout`  `SpellProperties=ApplyStatus(WILD_MAGIC_ENCHANT_CHARACTER,100,-1);ApplyEquipmentStatus(MainHand,WILD_MAGIC_ENCHANT,100,-1)`
- `Shout_WildMagic_EnlargeReduce` - **Wild Magic: Enlarge/Reduce** | Each creature within [1] is randomly Enlarged or Reduced.
  <br>`SpellType=Shout`  `SpellSuccess=ApplyStatus(ENLARGE,100,3)`
- `Shout_WildMagic_Entangle` - **Wild Magic: Entangle** | Create a vine surface around yourself, slowing down creatures, possibly Entangling them.
  <br>`SpellType=Shout`  `SpellProperties=GROUND:CreateSurface(4,3,Vines)`

### `CX_Sorcerer_StormSorcery_Boost`  -  _caster_

**Passive candidates** (4 found)
- `HeartOfTheStorm` - **Heart of the Storm** | When you cast a spell of Level 1 or higher that deals Lightning or Thunder damage, you cause a small, local storm. All enemies within [2] take [1] or [3].
  <br>`Boosts=UnlockInterrupt(Interrupt_HeartOfTheStorm_Lightning);UnlockInterrupt(Interrupt_HeartOfTheStorm_Thunder)`
- `HeartOfTheStorm_Resistance` - **Heart of the Storm: Resistance** | You are Resistant to Lightning and Thunder damage.
  <br>`Boosts=Resistance(Lightning, Resistant);Resistance(Thunder, Resistant)`
- `StormsFury` - **Storm's Fury** | When you are hit by a melee attack, you deal [1] to the attacker and potentially push them away.
  <br>`Boosts=UnlockInterrupt(Interrupt_StormsFury)`
- `TempestuousMagic` - **Tempestuous Magic** | After you cast a Level 1 spell or higher you can Fly as a bonus action until the end of your turn without receiving Opportunity Attacks.

**Spell candidates** (7 found)
- `Projectile_Fly_TempestuousMagic` - **Tempestuous Magic: Flight** | Fly to a nearby spot without receiving Opportunity Attacks.
  <br>`SpellType=Projectile`
- `Target_CallLightning` - **Call Lightning** | Lightning strikes all targets within range. Then for 10 turns, you can call down lightning again without expending a spell slot.
  <br>`SpellType=Target`  `SpellSuccess=DealDamage(3d10,Lightning,Magical)`  `SpellProperties=GROUND:ApplyStatus(SELF,CALL_LIGHTNING_TECHNICAL,100,10);GROUND:SurfaceChange(Electrify)`
- `Target_CallLightning_LightningBolt` - **Activate Call Lightning** | Call down more lightning to hit all targets within range.
  <br>`SpellType=Target`  `SpellProperties=GROUND:SurfaceChange(Electrify);RemoveStatus(SELF,SANCTUARY);RemoveStatus(SELF,SANCTUARY_TRANQUILITY);`
- `Target_Shatter` - **Shatter**
- `Zone_GustOfWind` - **Gust of Wind** | Summon a strong wind that clears all clouds and pushes creatures back [1], forcing them Off Balance.
  <br>`SpellType=Zone`  `SpellSuccess=Force(5); IF(not Item()):ApplyStatus(OFF_BALANCED,100,1)`  `SpellProperties=GROUND:SurfaceClearLayer(Cloud); RemoveStatus(BURNING);`
- `Zone_LightningBolt` - **Lightning Bolt** | Call forth a blast of lightning that hits all creatures in the line of the eruption.
  <br>`SpellType=Zone`  `SpellSuccess=DealDamage(8d6,Lightning,Magical)`
- `Zone_Thunderwave` - **Thunderwave**

---

## Warlock

### `CX_Warlock_Boost`  -  _caster_
_Currently in manager_ - passives: `AgonizingBlast`, `MAG_Zhentarim_Demonspirit_Gloves_Passive`; spells: `Projectile_EldritchBlast`, `Projectile_Jump`, `Target_Hex`, `Target_SummonShadowspawn`

**Passive candidates** (14 found)
- `DevilsSight` - **Devil's Sight** | You can see normally in darkness, both magical and non-magical, to a distance of [1].
  <br>`Boosts=DarkvisionRangeMin(24);ActiveCharacterLight(c46e7ba8-e746-7020-5146-287474d7b9f7);StatusImmunity(BLINDED_DARKNESS);IgnoreSurfaceCover(SurfaceDarknessCloud)`
- `Lifedrinker`
  <br>`Boosts=IF(IsMeleeWeaponAttack()):CharacterWeaponDamage(CharismaModifier,Necrotic)`
- `LOW_RaphaelImp_AgonizingBlast`
  <br>`Boosts=IF(SpellId('Projectile_LOW_RaphaelImp_EldritchBlast')):DamageBonus(CharismaModifier,Force)`
- `LOW_RaphaelImp_RepellingBlast`
- `PactOfTheBlade` - **Pact of the Blade** | You can Summon a pact weapon, or Bind the one you are wielding, making it magical.
  <br>`Boosts=UnlockSpell(Shout_PactOfTheBlade);UnlockSpell(Shout_PactOfTheBlade_Bind)`
- `PactOfTheBlade_Hex` - **Hexblade warlocks who already have Bind Hexed Weapon do not gain this Bind.**
  <br>`Boosts=IF(not HasPassive('HexWarrior',context.Source)):UnlockSpell(Shout_PactOfTheBlade);IF(not HasPassive('HexWarrior',context.Source)):UnlockSpell(Shout_PactOfTheBlade_Bind);`
- `PactOfTheChain` - **Pact of the Chain** | Gain the service of a familiar, a fey spirit that takes a form of your choosing. This can be an animal, imp, or quasit.
  <br>`Boosts=UnlockSpell(Target_FindFamiliar_Ritual);UnlockSpell(Target_PactOfTheChain_Imp);UnlockSpell(Target_PactOfTheChain_Quasit)`
- `PactOfTheTome` - **Pact of the Tome** | Your patron grants you a grimoire called 'The Book of Shadows', which allows you to cast Guidance, Vicious Mockery, and Thorn Whip.
  <br>`Boosts=UnlockSpell(Target_Guidance);UnlockSpell(Target_ViciousMockery);UnlockSpell(Target_ThornWhip)`
- `RepellingBlast` - **Repelling Blast** | When you hit a creature with Eldritch Blast, you can push the creature up to [1] away from you.
- `LOW_Chasm_Mangle_Pushback` - **Propelling Strike** | On a hit, push the target [1] away from you.
- `LOW_HouseOfGrief_Cultists_Sight` - **Born into Darkness** | This creature can see through magical and non-magical darkness, and cannot be Blinded.
  <br>`Boosts=DarkvisionRangeMin(24);ActiveCharacterLight(e278f6a0-26d7-49be-b11a-9b84bc313c3c);StatusImmunity(BLINDED_DARKNESS);StatusImmunity(SG_Blinded);IgnoreSurfaceCover(SurfaceDarknessClou…`
- `ThirstingBlade_Blade`
- `ThirstingBlade_Tome`
  <br>`Boosts=UnlockSpell(Target_AnimateDead,Singular,,UntilRest,Charisma);UnlockSpell(Target_CallLightning,Singular,,UntilRest,Charisma);UnlockSpell(Target_Haste,Singular,,UntilRest,Charisma)`
- `AgonizingBlast` _(already in manager)_ - **Agonising Blast** | When you cast Eldritch Blast, add your Charisma Modifier to the damage it deals, unless it is negative.
  <br>`Boosts=IF(SpellId('Projectile_EldritchBlast') and IsCharismaModifierPositive()):DamageBonus(CharismaModifier,Force)`

**Spell candidates** (41 found, showing 14)
- `Projectile_AiHelper_HungerOfHadar`
  <br>`SpellType=Projectile`  `SpellProperties=ApplyStatus(VOID_START,100,1);ApplyStatus(VOID_END,100,1);`
- `Shout_ArmorOfAgathys` - **Armour of Agathys** | Gain [1] and deal [2] to any creature that hits you with a melee attack.
  <br>`SpellType=Shout`  `SpellProperties=ApplyStatus(ARMOR_OF_AGATHYS, 100, -1)`
- `Shout_PactOfTheBlade` - **Pact of the Blade** | Summon a weapon to your hand. It uses the wielder's Spellcasting Ability Modifier, and its damage is magical.
  <br>`SpellType=Shout`
- `Shout_PactOfTheBlade_Battleaxe` - **Pact of the Blade: Battleaxe** | Summon a battleaxe.
  <br>`SpellType=Shout`  `SpellProperties=SummonInInventory(407954e3-71e4-4611-9221-0ba3ea71d6e8,Permanent,1,true,true,true,,,PactBlade,PACT_BLADE)`
- `Shout_PactOfTheBlade_Bind` - **Bind Pact Weapon** | Bind to your main hand weapon. Its damage becomes magical, you cannot drop or throw it, and you become Proficient with it if you weren't already.
  <br>`SpellType=Shout`  `SpellProperties=ApplyEquipmentStatus(MainHand, PACT_BLADE,100, -1)`
- `Shout_PactOfTheBlade_Dismiss` - **Dismiss Pact Weapon** | Dismiss your pact weapon.
  <br>`SpellType=Shout`
- `Shout_PactOfTheBlade_Glaive` - **Pact of the Blade: Glaive** | Summon a glaive.
  <br>`SpellType=Shout`  `SpellProperties=SummonInInventory(e7dab8bd-8037-4d8e-9c4e-ebec705912aa,Permanent,1,true,true,true,,,PactBlade,PACT_BLADE)`
- `Shout_PactOfTheBlade_Greatsword` - **Pact of the Blade: Greatsword** | Summon a greatsword.
  <br>`SpellType=Shout`  `SpellProperties=SummonInInventory(e90936db-7f65-446c-819d-c7fc6ba44d6c,Permanent,1,true,true,true,,,PactBlade,PACT_BLADE)`
- `Shout_PactOfTheBlade_Hex`
  <br>`SpellType=Shout`
- `Shout_PactOfTheBlade_Hexblade_Battleaxe`
  <br>`SpellType=Shout`  `SpellProperties=SummonInInventory(407954e3-71e4-4611-9221-0ba3ea71d6e8,Permanent,1,true,true,true,,,PactBlade,HEXBLADE_BIND);ApplyStatus(SELF,HEXBLADE_BIND_TECHNICAL,100,-1);`
- `Shout_PactOfTheBlade_Hexblade_Flail` - **Pact of the Blade: Flail** | Summon a flail.
  <br>`SpellType=Shout`  `SpellProperties=SummonInInventory(02376e06-56bf-429b-890f-e52f5d275262,Permanent,1,true,true,true,,,PactBlade,HEXBLADE_BIND);ApplyStatus(SELF,HEXBLADE_BIND_TECHNICAL,100,-1);`
- `Shout_PactOfTheBlade_Hexblade_Glaive`
  <br>`SpellType=Shout`  `SpellProperties=SummonInInventory(e7dab8bd-8037-4d8e-9c4e-ebec705912aa,Permanent,1,true,true,true,,,PactBlade,HEXBLADE_BIND);ApplyStatus(SELF,HEXBLADE_BIND_TECHNICAL,100,-1);`
- `Shout_PactOfTheBlade_Hexblade_Greatsword`
  <br>`SpellType=Shout`  `SpellProperties=SummonInInventory(e90936db-7f65-446c-819d-c7fc6ba44d6c,Permanent,1,true,true,true,,,PactBlade,HEXBLADE_BIND);ApplyStatus(SELF,HEXBLADE_BIND_TECHNICAL,100,-1);`
- `Shout_PactOfTheBlade_Hexblade_Maul` - **Pact of the Blade: Maul** | Summon a maul.
  <br>`SpellType=Shout`  `SpellProperties=SummonInInventory(b92fcaf1-2895-4faa-b952-1d21bf94acba,Permanent,1,true,true,true,,,PactBlade,HEXBLADE_BIND);ApplyStatus(SELF,HEXBLADE_BIND_TECHNICAL,100,-1);`

### `CX_Warlock_Archfey_Boost`  -  _caster_
_Currently in manager_ - passives: `BeguilingDefenses`, `EldritchSpear`, `FeyAncestry`, `FeyTouched_Charisma`, `MaddeningHex`, `MistyEscape`, `PactOfTheChain`; spells: `Goon_Target_Invisibility_Greater_Resource_1`, `Shout_Blink`, `Target_CalmEmotions`, `Target_Sleep`

**Passive candidates** (3 found)
- `MistyEscape_ShadarKai_GloomWeaver` - **Misty Presence** | After taking damage this character may turn Invisible.
- `BeguilingDefenses` _(already in manager)_ - **Beguiling Defences** | You have built stoic barriers in your heart and mind, and cannot be Charmed.
  <br>`Boosts=StatusImmunity(SG_Charmed)`
- `MistyEscape` _(already in manager)_ - **Misty Escape** | Upon taking damage, become Invisible. On your next turn, you can cast Misty Step, though this will break your invisibility.
  <br>`Boosts=UnlockInterrupt(Interrupt_MistyEscape);ActionResource(Interrupt_MistyEscape,1,0)`

**Spell candidates** (24 found, showing 14)
- `Projectile_Potion_Destroy_Sleep` - **Potion of Sleep**
  <br>`SpellType=Projectile`  `SpellProperties=ApplyStatus(SLEEP,100,3,,,,not SavingThrow(Ability.Constitution,11, AdvantageOnPoisoned()))`
- `Shout_FeyPresence` - **Fey Presence: Beguiling** | Charm nearby foes with the feywild's beguiling, seductive magics.
  <br>`SpellType=Shout`  `SpellSuccess=ApplyStatus(CHARMED,100,2)`
- `Shout_FeyPresence_Frightened` - **Fey Presence: Disturbing** | Frighten nearby foes with the feywild's distressing, flustering magics.
  <br>`SpellType=Shout`  `SpellSuccess=ApplyStatus(FRIGHTENED,100,2)`
- `Target_Eyebite_Asleep` - **Eyebite: Asleep**
- `Target_FaerieFire` - **Faerie Fire** | All targets within the light turn visible, and Attack Rolls against them have Advantage.
  <br>`SpellType=Target`  `SpellSuccess=ApplyStatus(FAERIE_FIRE, 100, 10)`
- `Target_FaerieFire_Drider`
  <br>`SpellType=Target`
- `Target_FaerieFire_DrowMagic` - **Drow Magic: Faerie Fire**
  <br>`SpellType=Target`
- `Target_GlyphOfWarding_Sleep` - **Glyph of Warding: Sleep**
- `Target_MistyStep` - **Misty Step** | Surrounded by silver mist, you teleport to an unoccupied space you can see.
  <br>`SpellType=Target`  `SpellProperties=GROUND:TeleportSource();`
- `Target_MistyStep_Elemental_Air`
  <br>`SpellType=Target`
- `Target_MistyStep_Elemental_Earth`
  <br>`SpellType=Target`
- `Target_MistyStep_Elemental_Fire`
  <br>`SpellType=Target`
- `Target_MistyStep_Elemental_Water`
  <br>`SpellType=Target`
- `Target_MistyStep_Free`
  <br>`SpellType=Target`  `SpellProperties=GROUND:TeleportSource();GROUND:RemoveStatus(SELF,MISTY_ESCAPE_INVISIBLE)`

### `CX_Warlock_Fiend_Boost`  -  _caster_
_Currently in manager_ - passives: `DarkOnesBlessing`, `DevilsSight`, `GraspOfHadar`, `NPC_SummonGildedHellsboar`; spells: `Projectile_Fireball`, `Projectile_ScorchingRay`, `Target_Confusion`, `Target_ORI_Wyll_SummonCambion`, `Zone_BurningHands`

**Passive candidates** (3 found)
- `DarkOnesOwnLuck` - **Dark One's Own Luck** | Call on your patron to change your fate and add a 1d10 to an Ability Check.
  <br>`Boosts=RollBonus(SkillCheck,1d10);RollBonus(RawAbility,1d10)`
- `FiendishResilience` - **Fiendish Resilience** | Choose a damage type and become Resistant to it. You can pick a new damage type each Short Rest.
  <br>`Boosts=UnlockSpell(Target_Fiendish_Resilience_Container)`
- `DarkOnesBlessing` _(already in manager)_ - **Dark One's Blessing** | When you reduce a hostile creature to [1], this gift from your patron grants you [2].

**Spell candidates** (12 found)
- `Projectile_Fireball_Dragon` - **Fire Breath**
  <br>`SpellType=Projectile`  `SpellSuccess=DealDamage(14d6,Fire,Magical);ApplyStatus(BURNING,100,2)`
- `Projectile_ScorchingRay_CircletOfBlasting`
  <br>`SpellType=Projectile`
- `Target_Command_Approach` - **Command: Approach** | Command a creature to move towards you on its turn and do nothing else.
  <br>`SpellType=Target`  `SpellSuccess=ApplyStatus(COMMAND_APPROACH, 100, 1)`
- `Target_Command_Drop` - **Command: Drop** | Command a creature to drop its weapon.
  <br>`SpellType=Target`  `SpellSuccess=ApplyStatus(DISARM, 100, 1)`
- `Target_Command_Flee` - **Command: Flee** | Command a creature to flee from you on its turn and do nothing else.
  <br>`SpellType=Target`  `SpellSuccess=ApplyStatus(COMMAND_FLEE, 100, 1)`
- `Target_Command_Grovel` - **Command: Grovel** | Command a creature to fall Prone immediately.
  <br>`SpellType=Target`  `SpellSuccess=ApplyStatus(COMMAND_GROVEL, 100, 1)`
- `Target_Command_Halt` - **Command: Halt** | Command a creature to halt, preventing it from moving or taking any type of action.
- `Target_VoiceOfCommand` - **Voice of Command** | Command an ally i
- `Zone_BurningHands_MephistophelesTiefling` - **Legacy of Cania: Burning Hands**
  <br>`SpellType=Zone`
- `Projectile_Fireball` _(already in manager)_ - **Fireball**
- `Projectile_ScorchingRay` _(already in manager)_ - **Scorching Ray** | Hurl [2] rays of fire. Each ray deals [1].
  <br>`SpellType=Projectile`  `SpellSuccess=DealDamage(2d6,Fire,Magical)`  `SpellProperties=GROUND:SurfaceChange(Ignite);GROUND:SurfaceChange(Melt)`
- `Zone_BurningHands` _(already in manager)_ - **Burning Hands** | Each flammable target is hit with [1].
  <br>`SpellType=Zone`  `SpellSuccess=DealDamage(3d6, Fire,Magical)`  `SpellProperties=GROUND:SurfaceChange(Ignite);GROUND:SurfaceChange(Melt);TARGET:IF(Item()):ApplyStatus(BURNING,100,2);`

### `CX_Warlock_GreatOldOne_Boost`  -  _caster_
_Currently in manager_ - passives: `BookOfAncientSecrets`, `ClarifiedMortality`, `EntropicWard`, `LanceOfLethargy`, `Thought_Shield_Psychic_Reflection`, `Thought_Shield_Psychic_Resistance`; spells: `Target_BestowCurse`, `Target_BlackTentacles`, `Target_DissonantWhispers`, `Target_DominatePerson`, `Target_HideousLaughter`

**Passive candidates** (1 found)
- `EntropicWard` _(already in manager)_ - **Entropic Ward** | As a reaction, you can impose Disadvantage on an Attack Roll against you.If the attack misses, you gain Advantage on your next Attack Roll against your attacker for 1 turn.
  <br>`Boosts=UnlockInterrupt(Interrupt_EntropicWard);ActionResource(Interrupt_EntropicWard_Charge,1,0)`

**Spell candidates** (7 found)
- `Shout_DetectThoughts` - **Detect Thoughts** | Focus your mind to read the thoughts of certain creatures while talking to them.
  <br>`SpellType=Shout`  `SpellProperties=ApplyStatus(DETECT_THOUGHTS,100,-1)`
- `Target_Confusion`
  <br>`SpellSuccess=AI_IGNORE:ApplyStatus(<em>CONFUSION</em>,100,3); AI_ONLY:ApplyStatus(PARALYZED,100,3)`
- `Target_ConfusionRay_Spectator` - **Confusion Ray**
- `Target_PhantasmalKiller` - **Phantasmal Killer** | Haunt a creature with its worst nightmares. It takes [1] per turn, cannot move, has Disadvantage on Ability Checks and Attack Rolls.
  <br>`SpellType=Target`  `SpellSuccess=ApplyStatus(PHANTASMAL_KILLER,100,10)`
- `Zone_MindScreech_Nurse`
  <br>`SpellSuccess=DealDamage(4d6,Psychic,Magical); Force(3, OriginToTarget); ApplyStatus(<em>CONFUSION</em>,100,2)`
- `Target_DissonantWhispers` _(already in manager)_ - **Dissonant Whispers**
- `Target_HideousLaughter` _(already in manager)_ - **Tasha's Hideous Laughter** | Leave a creature Prone with laughter, without the ability to get up.
  <br>`SpellType=Target`  `SpellSuccess=ApplyStatus(HIDEOUS_LAUGHTER,100,10)`

---

## Wizard

### `CX_Wizard_Boost`  -  _caster_
_Currently in manager_ - passives: `Goon_Target_MageArmor_Passive`, `MagicResistance`; spells: `Projectile_ChromaticOrb`, `Projectile_Jump`

**Passive candidates** (0 found)
- _(no hits - adjust search terms in terms.py)_

**Spell candidates** (34 found, showing 14)
- `Projectile_Fireball` - **Fireball**
- `Projectile_Fireball_Dragon` - **Fire Breath**
  <br>`SpellType=Projectile`  `SpellSuccess=DealDamage(14d6,Fire,Magical);ApplyStatus(BURNING,100,2)`
- `Projectile_MagicMissile` - **Magic Missile** | Shoot [2] magical darts, each dealing [1]. They always hit their target.
  <br>`SpellType=Projectile`  `SpellProperties=DealDamage(1d4+1,Force,Magical)`
- `Projectile_MagicMissile_MindFlayer`
  <br>`SpellType=Projectile`
- `Shout_FireShield` - **Fire Shield**
- `Shout_FireShield_Chill` - **Fire Shield: Chill**
- `Shout_FireShield_Warm` - **Fire Shield: Warm**
- `Shout_Shield_MindFlayer`
  <br>`SpellType=Shout`
- `Shout_Shield_Sorcerer`
  <br>`SpellType=Shout`
- `Shout_Shield_Warlock`
  <br>`SpellType=Shout`
- `Shout_Shield_Wizard` - **Shield**
- `Shout_WildMagic_Shield` - **Wild Magic: Shield** | Armour Class is increased by 5 and you are immune to the effects of Magic Missile.
  <br>`SpellType=Shout`  `SpellProperties=ApplyStatus(SHIELD,100,1)`
- `Target_Counterspell` - **Counterspell**
- `Target_Counterspell_Failure` - **Failed Counterspell**
  <br>`SpellType=Target`

### `CX_Wizard_Abjuration_Boost`  -  _caster_
_Currently in manager_ - passives: `ArcaneWard`, `ArcaneWard_Cast`, `ArcaneWard_Damage`, `Divination_School_Abjuration`; spells: `Shout_AbsorbElements`, `Shout_BladeWard`, `Shout_Shield_Wizard`, `Target_IntellectFortress`

**Passive candidates** (7 found)
- `MAG_Druid_Wildshape_SpellResistance_Passive` - **Lunar Bestial Fortitude** | You have a +[1] bonus to Armour Class. You also have Advantage on Saving Throws against spells. This effect persists while using your druidic Wild Shape ability.
  <br>`Boosts=IF(IsSpell()):Advantage(AllSavingThrows);AC(2)`
- `MAG_SpellResistance_Passive` - **Spell Resistance** | You have Advantage on Saving Throws against spells.
  <br>`Boosts=IF(IsSpell()):Advantage(AllSavingThrows)`
- `ImprovedAbjuration` - **Improved Abjuration** | Each time you take a Short Rest, the intensity of your Arcane Ward increases by an amount equal to your wizard level.
- `ProjectedWard` - **Projected Ward** | When a nearby ally takes damage and you have an active Arcane Ward, you can sacrifice your ward to reduce the damage they take.
  <br>`Boosts=UnlockInterrupt(Interrupt_ProjectedWard)`
- `ArcaneWard` _(already in manager)_ - **Arcane Ward**
- `ArcaneWard_Cast` _(already in manager)_
- `ArcaneWard_Damage` _(already in manager)_

**Spell candidates** (26 found, showing 14)
- `Shout_ArmorOfAgathys` - **Armour of Agathys** | Gain [1] and deal [2] to any creature that hits you with a melee attack.
  <br>`SpellType=Shout`  `SpellProperties=ApplyStatus(ARMOR_OF_AGATHYS, 100, -1)`
- `Shout_FireShield` - **Fire Shield**
- `Shout_FireShield_Chill` - **Fire Shield: Chill**
- `Shout_FireShield_Warm` - **Fire Shield: Warm**
- `Shout_Shield_MindFlayer`
  <br>`SpellType=Shout`
- `Shout_Shield_Sorcerer`
  <br>`SpellType=Shout`
- `Shout_Shield_Warlock`
  <br>`SpellType=Shout`
- `Shout_WildMagic_Shield` - **Wild Magic: Shield** | Armour Class is increased by 5 and you are immune to the effects of Magic Missile.
  <br>`SpellType=Shout`  `SpellProperties=ApplyStatus(SHIELD,100,1)`
- `Target_Banishment` - **Banishment**
- `Target_Counterspell` - **Counterspell**
- `Target_Counterspell_Failure` - **Failed Counterspell**
  <br>`SpellType=Target`
- `Target_CounterSpell_Mindflayer`
  <br>`SpellType=Target`
- `Target_Counterspell_Success` - **Nullify another creature's spell as a reaction. The spell must be 3rd Level or lower. If it is higher, you must succeed a Check to nullify it, the difficulty of which is based on the spell's Level.**
  <br>`SpellType=Target`
- `Target_LesserRestoration` - **Lesser Restoration** | Cure a creature from disease, poison, paralysis or blindness.
  <br>`SpellType=Target`  `SpellProperties=RemoveStatus(SG_Poisoned);RemoveStatus(SG_Disease);RemoveStatus(SG_Paralyzed);RemoveStatus(SG_Blinded);RemoveStatus(ASTARION_WEAK)`

### `CX_Wizard_Conjuration_Boost`  -  _caster_
_Currently in manager_ - passives: `FocusedConjuration`; spells: `Projectile_AcidSplash`, `Projectile_IceKnife`, `Shout_SwordBurst`, `Target_CreateWater`, `Target_MistyStep`, `Target_SpiritualWeapon`, `Target_Summon_MudMephit`, `Target_Web`

**Passive candidates** (1 found)
- `FocusedConjuration` _(already in manager)_ - **Focused Conjuration** | Damage taken while you are Concentrating on a Conjuration spell will not break your Concentration.
  <br>`Boosts=ConcentrationIgnoreDamage(Conjuration)`

**Spell candidates** (24 found, showing 14)
- `Projectile_DeathBurst_Died_GreaseMephit`
  <br>`SpellType=Projectile`  `SpellSuccess=IF(HasStatus('MEPHIT_DAMAGE')):DealDamage(4d6,Force);IF(not HasStatus('MEPHIT_DAMAGE')):DealDamage(2d6,Force);RemoveStatus(MEPHIT_DAMAGE)`  `SpellProperties=GROUND:CreateSurface(3,3,Grease)`
- `Target_CloudOfDaggers` - **Cloud of Daggers** | Conjure a cloud of spinning daggers that attack anyone inside.
  <br>`SpellType=Target`  `SpellProperties=AI_IGNORE:GROUND:Summon(0ba4af65-19d0-4a31-9a42-2c365462841b, 10,,,,CLOUD_OF_DAGGERS_AURA);AI_ONLY:DealDamage(4d4,Slashing)`
- `Target_ConjureElemental_Elemental_Air` - **Conjure Elemental: Air Elemental** | The air elemental can use Primordial Gales, Gushing Air, and can Shock your foes.
  <br>`SpellType=Target`  `SpellProperties=GROUND:Summon(284b9c7f-1e04-48b7-af41-9029d1fa753c, -1,Projectile_AiHelper_Summon_Strong,,'ConjureElemetnalStack',UNSUMMON_ABLE,SHADOWCURSE_SUMMON_CHECK)`
- `Target_ConjureElemental_Elemental_Earth` - **Conjure Elemental: Earth Elemental** | The earth elemental can use Seismic Strike, Soil-Clogged Slam, and can create sludgy mud surfaces while walloping your foes.
  <br>`SpellType=Target`  `SpellProperties=GROUND:Summon(2ad47124-e41a-460e-b97a-f8e9efd32ed8, -1,Projectile_AiHelper_Summon_Strong,,'ConjureElemetnalStack',UNSUMMON_ABLE,SHADOWCURSE_SUMMON_CHECK)`
- `Target_ConjureElemental_Elemental_Fire` - **Conjure Elemental: Fire Elemental** | The fire elemental can use Smouldering Touch, Erupting Cinder, and can make your foes Burn.
  <br>`SpellType=Target`  `SpellProperties=GROUND:Summon(88a6c664-877c-4d6e-81ad-dd377df2634e, -1,Projectile_AiHelper_Summon_Strong,,'ConjureElemetnalStack',UNSUMMON_ABLE,SHADOWCURSE_SUMMON_CHECK)`
- `Target_ConjureElemental_Elemental_Water` - **Conjure Elemental: Water Elemental** | The water elemental can use Winter's Breath, Slam, and can mete out cold punishment upon foes with its fists.
  <br>`SpellType=Target`  `SpellProperties=GROUND:Summon(f21e144a-3237-4faa-a99c-a15e1937bc2c, -1,Projectile_AiHelper_Summon_Strong,,'ConjureElemetnalStack',UNSUMMON_ABLE,SHADOWCURSE_SUMMON_CHECK)`
- `Target_ConjureElemental_Myrmidon_Air` - **Conjure Elemental: Air Myrmidon** | The myrmidon can cast Invisibility, Electrified Flail, and Raging Vortex.
  <br>`SpellType=Target`  `SpellProperties=GROUND:Summon(15928ca3-b38b-4303-9c1c-9945e5e719a1, -1,Projectile_AiHelper_Summon_Strong,,'ConjureElemetnalStack',UNSUMMON_ABLE,SHADOWCURSE_SUMMON_CHECK)`
- `Target_ConjureElemental_Myrmidon_Earth` - **Conjure Elemental: Earth Myrmidon** | The myrmidon can cast Muck to Metal, Sludgy Sling, and Burrow.
  <br>`SpellType=Target`  `SpellProperties=GROUND:Summon(b5bd29ba-8105-4123-920f-a2c64a4e1dfc, -1,Projectile_AiHelper_Summon_Strong,,'ConjureElemetnalStack',UNSUMMON_ABLE,SHADOWCURSE_SUMMON_CHECK)`
- `Target_ConjureElemental_Myrmidon_Fire` - **Conjure Elemental: Fire Myrmidon** | The myrmidon can cast Scorching Strike, Myrmidon's Immolation, and Cinderous Swipe.
  <br>`SpellType=Target`  `SpellProperties=GROUND:Summon(7794f082-5483-42d2-9d5c-ee6a99de8703, -1,Projectile_AiHelper_Summon_Strong,,'ConjureElemetnalStack',UNSUMMON_ABLE,SHADOWCURSE_SUMMON_CHECK)`
- `Target_ConjureElemental_Myrmidon_Water` - **Conjure Elemental: Water Myrmidon** | The myrmidon can cast Hiemal Strike, Healing Vapours, and Explosive Icicle.
  <br>`SpellType=Target`  `SpellProperties=GROUND:Summon(b79527a1-a83d-4b23-82d5-a02b01638469, -1,Projectile_AiHelper_Summon_Strong,,'ConjureElemetnalStack',UNSUMMON_ABLE,SHADOWCURSE_SUMMON_CHECK)`
- `Target_Grease`
  <br>`SpellProperties=GROUND:CreateSurface(4,10,<em>Grease</em>)`
- `Target_MistyStep_Elemental_Air`
  <br>`SpellType=Target`
- `Target_MistyStep_Elemental_Earth`
  <br>`SpellType=Target`
- `Target_MistyStep_Elemental_Fire`
  <br>`SpellType=Target`

### `CX_Wizard_Divination_Boost`  -  _caster_
_Currently in manager_ - passives: `CAMP_Volo_ErsatzEye`, `DevilsSight`; spells: `Shout_SeeInvisibility`, `Target_Darkness`, `Target_FaerieFire`, `Target_ShockingGrasp`, `Target_TollTheDead`

**Passive candidates** (26 found, showing 18)
- `Portent` - **Portent** | Your dreams grant you glimpses that let you influence the future. After each Long Rest, you gain two random Portent Dice. During the day, you can use your reaction to change the die of any Attack Roll or Saving Throw rolled near you to one…
- `ThirdEye` - **Raven Sight** | The raven cannot be blinded.
- `Divination_Ally_Help`
- `Divination_Damage_Acid`
- `Divination_Damage_Bludgeoning`
- `Divination_Damage_Cold`
- `Divination_Damage_Fire`
- `Divination_Damage_Force`
- `Divination_Damage_Lightning`
- `Divination_Damage_Necrotic`
- `Divination_Damage_Piercing`
- `Divination_Damage_Poison`
- `Divination_Damage_Psychic`
- `Divination_Damage_Radiant`
- `Divination_Damage_Slashing`
- `Divination_Damage_Thunder`
- `Divination_Enemy_Killed`
- `Divination_School_Abjuration`

**Spell candidates** (25 found, showing 14)
- `Projectile_AiHelper_Fear_Aura`
  <br>`SpellType=Projectile`  `SpellProperties=IF(Enemy()):ApplyStatus(FRIGHTENED,100,2)`
- `Shout_DetectThoughts` - **Detect Thoughts** | Focus your mind to read the thoughts of certain creatures while talking to them.
  <br>`SpellType=Shout`  `SpellProperties=ApplyStatus(DETECT_THOUGHTS,100,-1)`
- `Shout_Fear_TollCollector_Face` - **Blind Terror** | Frighten and Blind a foe.
  <br>`SpellType=Shout`  `SpellSuccess=ApplyStatus(FRIGHTENED, 100, 2)`  `SpellProperties=DealDamage(2d8+2, Psychic,Magical)`
- `Shout_Slow_TollCollector_Face`
  <br>`SpellSuccess=ApplyStatus(<em>SLOW</em>, 100, 2);`
- `Shout_WildMagic_Fog` - **Wild Magic: Fog** | Create a cloud of fog arou
- `Shout_WildMagic_Slow` - **Wild Magic: Slow** | You are Slowed.
  <br>`SpellType=Shout`  `SpellProperties=ApplyStatus(SLOW,100,2)`
- `Target_FearRay_Spectator` - **Fear Ray**
- `Target_FogCloud` - **Fog Cloud**
- `Target_HoldPerson` - **Hold Person** | Hold a humanoid enemy still. They can't move, act or react. Attacks from within [1] are always Critical Hits.
  <br>`SpellType=Target`  `SpellSuccess=ApplyStatus(HOLD_PERSON,100,10)`
- `Target_HoldPerson_Redcap`
  <br>`SpellType=Target`
- `Target_Portent_Interrupt` - **Portent** | Change the die of a nearby Attack Roll or Saving Throw.
  <br>`SpellType=Target`
- `Target_Slow`
  <br>`SpellSuccess=ApplyStatus(<em>SLOW</em>,100,10)`
- `Zone_Fear` - **Fear**
- `Shout_FrightfulPresence_Dragon_Skeletal` - **Exude terror, instilling Fear in your foes.**

### `CX_Wizard_Enchantment_Boost`  -  _caster_
_Currently in manager_ - passives: `Divination_School_Enchantment`, `MAG_Psychic_MentalFatigue_Gloves_Passive`; spells: `Target_HoldPerson`, `Target_MindSliver`, `Target_MindWhip`, `Target_ViciousMockery`

**Passive candidates** (2 found)
- `InstinctiveCharm` - **Instinctive Charm** | Charm an enemy attacking you. They will attack a new target if possible as a reaction.
  <br>`Boosts=UnlockInterrupt(Interrupt_InstinctiveCharm)`
- `SplitEnchantment` - **Split Enchantment** | You know your enchantments inside and out. You can target 2 creatures with Enchantment spells that would normally only target 1 creature.
  <br>`Boosts=UnlockSpellVariant(SplitEnchantmentProjectileSpellCheck(),ModifyNumberOfTargets(AdditiveBase,1,false),ModifyTooltipDescription(),ModifyIconGlow());UnlockSpellVariant(SplitEnchantme…`

**Spell candidates** (13 found)
- `Target_CharmPerson` - **Charm Person** | Charm a humanoid to prevent it from attacking you. You gain Advantage on Charisma Checks in dialogue.
  <br>`SpellType=Target`  `SpellSuccess=ApplyStatus(CHARMED,100,10)`
- `Target_CharmPerson_Cultist`
  <br>`SpellType=Target`
- `Target_CharmPerson_Vampire`
  <br>`SpellType=Target`
- `Target_Confusion`
  <br>`SpellSuccess=AI_IGNORE:ApplyStatus(<em>CONFUSION</em>,100,3); AI_ONLY:ApplyStatus(PARALYZED,100,3)`
- `Target_ConfusionRay_Spectator` - **Confusion Ray**
- `Target_DominatePerson` - **Dominate Person** | Make a humanoid fight alongside you. Every time the creature takes damage, it makes a Wisdom Saving Throw against your domination. Allies cannot be dominated.
  <br>`SpellType=Target`  `SpellSuccess=ApplyStatus(DOMINATE_PERSON,100,10);`
- `Target_DominatePerson_Mindflayer` - **Mind Flayer Domination** | Dominate a nearby humanoid. Allies are unaffected.
  <br>`SpellType=Target`
- `Target_HideousLaughter` - **Tasha's Hideous Laughter** | Leave a creature Prone with laughter, without the ability to get up.
  <br>`SpellType=Target`  `SpellSuccess=ApplyStatus(HIDEOUS_LAUGHTER,100,10)`
- `Target_HoldPerson_Redcap`
  <br>`SpellType=Target`
- `Target_HypnoticGaze` - **Hypnotic Gaze** | Charm and Incapacitate a creature. It cannot attack you. It cannot act.
  <br>`SpellType=Target`  `SpellSuccess=ApplyStatus(HYPNOTIC_GAZE,100,2);ApplyStatus(SELF,HYPNOTIC_GAZE_OWNER,100,2)`
- `Target_HypnoticGaze_Maintain` - **Maintain Hypnotic Gaze** | Maintain your Hypnotic Gaze to extend its duration.
  <br>`SpellType=Target`  `SpellProperties=ApplyStatus(HYPNOTIC_GAZE,100,2);SetStatusDuration(SELF,HYPNOTIC_GAZE_OWNER,2)`
- `Zone_MindScreech_Nurse`
  <br>`SpellSuccess=DealDamage(4d6,Psychic,Magical); Force(3, OriginToTarget); ApplyStatus(<em>CONFUSION</em>,100,2)`
- `Target_HoldPerson` _(already in manager)_ - **Hold Person** | Hold a humanoid enemy still. They can't move, act or react. Attacks from within [1] are always Critical Hits.
  <br>`SpellType=Target`  `SpellSuccess=ApplyStatus(HOLD_PERSON,100,10)`

### `CX_Wizard_Evocation_Boost`  -  _caster_
_Currently in manager_ - passives: `PotentCantrip`, `WarCaster_OpportunitySpell`; spells: `Projectile_FireBolt`, `Shout_AbsorbElements`, `Target_DragonsBreath`, `Zone_BurningHands`, `Zone_RimesBindingIce`

**Passive candidates** (4 found)
- `EmpoweredEvocation` - **Empowered Evocation** | Your grasp of Evocation magic has tightened, and you can add your Intelligence Modifier to damage rolls with any Evocation spells.
  <br>`Boosts=IF(IsSpell() and IsSpellSchool(SpellSchool.Evocation)):DamageBonus(max(0, IntelligenceModifier))`
- `SculptSpells` - **Sculpt Spells** | Create pockets of safety within your Evocation spells. Allies automatically succeed their Saving Throws against these spells and take no damage from them.
- `ArmyArcana` - **Army Arcana** | Create pockets of safety within your spells. Allies automatically succeed their Saving Throws against your spells and take no damage from them.
- `PotentCantrip` _(already in manager)_ - **Potent Cantrip** | Your cantrips become harder to evade entirely.When a creature succeeds its Saving Throw against one of your cantrips, it still takes half the cantrip's damage, but suffers no additional effects.

**Spell candidates** (9 found)
- `Projectile_Fireball` - **Fireball**
- `Projectile_Fireball_Dragon` - **Fire Breath**
  <br>`SpellType=Projectile`  `SpellSuccess=DealDamage(14d6,Fire,Magical);ApplyStatus(BURNING,100,2)`
- `Projectile_ScorchingRay` - **Scorching Ray** | Hurl [2] rays of fire. Each ray deals [1].
  <br>`SpellType=Projectile`  `SpellSuccess=DealDamage(2d6,Fire,Magical)`  `SpellProperties=GROUND:SurfaceChange(Ignite);GROUND:SurfaceChange(Melt)`
- `Projectile_ScorchingRay_CircletOfBlasting`
  <br>`SpellType=Projectile`
- `Target_CallLightning_LightningBolt` - **Activate Call Lightning** | Call down more lightning to hit all targets within range.
  <br>`SpellType=Target`  `SpellProperties=GROUND:SurfaceChange(Electrify);RemoveStatus(SELF,SANCTUARY);RemoveStatus(SELF,SANCTUARY_TRANQUILITY);`
- `Target_IceStorm` - **Ice Storm** | Impel a storm of hail and ice to crash from the sky, covering the ground and striking all objects and creatures within range.
  <br>`SpellType=Target`  `SpellSuccess=DealDamage(2d8,Bludgeoning,Magical);DealDamage(4d6,Cold,Magical)`  `SpellProperties=GROUND:CreateSurface(6,2,WaterFrozen);GROUND:SurfaceChange(Freeze);GROUND:SurfaceChange(Douse);RemoveStatus(BURNING)`
- `Target_Shatter` - **Shatter**
- `Zone_LightningBolt` - **Lightning Bolt** | Call forth a blast of lightning that hits all creatures in the line of the eruption.
  <br>`SpellType=Zone`  `SpellSuccess=DealDamage(8d6,Lightning,Magical)`
- `Zone_Thunderwave` - **Thunderwave**

### `CX_Wizard_Illusion_Boost`  -  _caster_
_Currently in manager_ - spells: `Shout_Blur`, `Shout_MirrorImage`, `Shout_ShadowBlade`, `Target_ImprovedMinorIllusion`, `Target_Silence`

**Passive candidates** (2 found)
- `IllusorySelf` - **Illusory Self** | You can magically fashion an illusory duplicate of yourself when attacked, causing your foe to automatically miss that attack.
  <br>`Boosts=UnlockInterrupt(Interrupt_IllusorySelf);ActionResource(Interrupt_IllusorySelf_Charge,1,0)`
- `ShadowArts_MinorIllusion` - **Shadow Arts: Minor Illusion** | Gain the Minor Illusion cantrip.

**Spell candidates** (23 found, showing 14)
- `Projectile_Potion_Destroy_Invisibility` - **Potion of Invisibility**
  <br>`SpellType=Projectile`  `SpellProperties=GROUND:CreateSurface(1,,PotionInvisibilityCloud);`
- `Shout_Invisibility_Duergar`
  <br>`SpellType=Shout`
- `Shout_Invisibility_Imp`
  <br>`SpellProperties=AI_IGNORE:ApplyStatus(<em>INVISIBILITY</em>,100,-1);AI_ONLY:ApplyStatus(<em>INVISIBILITY</em>,100,2);`
- `Shout_Invisibility_MistyEscape` - **Cloaking Mist** | Turn Invisible after casting Misty Step.
  <br>`SpellType=Shout`  `SpellProperties=ApplyStatus(MISTY_ESCAPE_INVISIBLE,100,1);`
- `Shout_Invisibility_Myrmidon_Air` - **Invisibility**
- `Shout_Invisibility_Quasit`
  <br>`SpellType=Shout`
- `Shout_Invisibility_ShadarKai_GloomWeaver` - **Invisibility** | Become Invisible. The spell ends if you attack, take an action or take damage.
  <br>`SpellType=Shout`  `SpellProperties=ApplyStatus(INVISIBILITY_SHADARKAI_GLOOMWEAVER,100,1);`
- `Shout_InvisibilityField_Orthon`
  <br>`SpellProperties=ApplyStatus(<em>INVISIBILITY</em>,100,2);`
- `Shout_SeeInvisibility` - **See Invisibility**
- `Shout_SeeInvisibility_ThirdEye` - **Third Eye: See Invisibility**
- `Shout_SeeInvisibility_TrainedEye` - **See Invisibility**
- `Shout_WildMagic_Blur` - **Wild Magic: Blur**
  <br>`SpellProperties=ApplyStatus(<em>BLUR</em>,100,3)`
- `Target_FogCloud`
  <br>`SpellProperties=GROUND:CreateSurface(4.5,10,<em>FogCloud</em>,true)`
- `Target_Invisibility`
  <br>`SpellProperties=AI_IGNORE:ApplyStatus(<em>INVISIBILITY</em>,100,10);AI_ONLY:ApplyStatus(<em>INVISIBILITY</em>,100,2)`

### `CX_Wizard_Necromancy_Boost`  -  _caster_
_Currently in manager_ - passives: `GrimHarvest`, `MAG_Necromancy_Evasion`, `Reaper`; spells: `Target_ChillTouch`, `Target_SappingSting`, `Target_TollTheDead`

**Passive candidates** (2 found)
- `InuredtoUndeath` - **Inured to Undeath** | You have steeped yourself so completely in death that you are Resistant to Necrotic damage, and moreover your hit point maximum cannot be reduced.
  <br>`Boosts=Resistance(Necrotic,Resistant);StatusImmunity(HARM);StatusImmunity(CURSE_MUMMY);StatusImmunity(INCUBUS_DRAININGKISS);StatusImmunity(HP_REDUCTION_VAMPIRE);StatusImmunity(LIFE_DRAIN)…`
- `GrimHarvest` _(already in manager)_ - **Grim Harvest** | Once per turn, if you kill a creature with a spell, you regain hit points equal to twice the spell slot level used - thrice if it's a Necromancy spell. Undead and constructs are unaffected.

**Spell candidates** (19 found, showing 14)
- `Projectile_Hag_Double_RayOfSickness`
  <br>`SpellType=Projectile`
- `Projectile_Hag_RayOfSickness`
  <br>`SpellType=Projectile`
- `Projectile_Jump_AnimateDead_Ghoul_Flying`
  <br>`SpellType=Projectile`
- `Projectile_RayOfSickness` - **Ray of Sickness** | Possibly Poisons the target.
  <br>`SpellType=Projectile`  `SpellSuccess=IF(not SavingThrow(Ability.Constitution, SourceSpellDC(),AdvantageOnPoisoned())):ApplyStatus(POISONED,100,2);DealDamage(2d8,Poison,Magical)`
- `Projectile_RayOfSickness_BookOfAnceintSecrets`
  <br>`SpellType=Projectile`
- `Target_AnimateDead`
  <br>`SpellType=Target`
- `Target_AnimateDead_FlyingGhoul` - **Animate Dead: Flying Ghoul** | Create a flying ghoul that specialises in melee combat.
  <br>`SpellType=Target`  `SpellProperties=TARGET:SwitchDeathType(Explode);GROUND:IF(HasPassive('UndeadThrall_BetterSummon',context.Source)):Summon(1d7bd5b7-1879-452d-980f-34a5ba58a389,UntilLongRest,,,'AnimateDeadStack',UND…`
- `Target_AnimateDead_Ghoul` - **Animate Dead: Ghoul** | Create a ghoul that specialises in melee combat.
  <br>`SpellType=Target`  `SpellProperties=TARGET:SwitchDeathType(Explode);GROUND:IF(HasPassive('UndeadThrall_BetterSummon',context.Source)):Summon(405e65e2-a6c9-4418-9de6-b06978d033b7,UntilLongRest,,,'AnimateDeadStack',UND…`
- `Target_AnimateDead_Skeleton` - **Animate Dead: Skeleton** | Create a skeleton that specialises in ranged combat.
  <br>`SpellType=Target`  `SpellProperties=SwitchDeathType(Explode);Summon(6c06cda2-6e13-4663-a6f6-c4bb7564c10f, UntilLongRest,,,'AnimateDeadStack',UNSUMMON_ABLE,SHADOWCURSE_SUMMON_CHECK)`
- `Target_AnimateDead_Surgeon` - **Lovely Assistant** | The Surgeon reanimates the corpse of one of his nurses.
  <br>`SpellType=Target`  `SpellProperties=AI_IGNORE:Resurrect(100,25,Undead); AI_IGNORE:RestoreResource(Movement,100%,0); AI_IGNORE:RestoreResource(ActionPoint,1,0); AI_IGNORE:RestoreResource(BonusActionPoint,1,0); AI_ONLY…`
- `Target_AnimateDead_Zombie` - **Animate Dead: Zombie** | Create a zombie that specialises in melee combat.
  <br>`SpellType=Target`  `SpellProperties=SwitchDeathType(Explode);Summon(c2a2c269-ede8-4887-99f1-e0c044cc0c75,UntilLongRest,,,'AnimateDeadStack',UNSUMMON_ABLE,SHADOWCURSE_SUMMON_CHECK)`
- `Target_CircleOfDeath` - **Circle of Death** | Sculpt a massive sphere of entropic energy around a creature. Devastate the target and all surrounding creatures.
  <br>`SpellType=Target`  `SpellSuccess=DealDamage(8d6,Necrotic,Magical)`
- `Target_Claws_AnimateDead_Ghoul`
  <br>`SpellType=Target`  `SpellSuccess=DealDamage(max(1,3d6+UnarmedMeleeAbilityModifier),Slashing);AI_IGNORE:TARGET:IF(SpellDoesntApplyToElvesOrUndead(Ability.Constitution,5)):ApplyStatus(PARALYZED,100,2)`
- `Target_Devour_Ghoul_AnimateDead` - **Devour** | Bite a knocked out, prone or sleeping target, and deal [1]. Heal that many hit points.
  <br>`SpellType=Target`  `SpellSuccess=DealDamage(max(1,3d10+UnarmedMeleeAbilityModifier),Slashing);RegainHitPoints(SELF,DamageDone,Undead)`

### `CX_Wizard_Transmutation_Boost`  -  _caster_
_Currently in manager_ - passives: `Goon_Target_Longstrider_Passive`; spells: `Shout_FeatherFall`, `Target_Haste`, `Target_Slow`

**Passive candidates** (1 found)
- `Shapechanger` - **Shapechanger** | You can cast the Polymorph spell without expending a spell slot.
  <br>`Boosts=UnlockSpell(Target_Polymorph_Shapechanger)`

**Spell candidates** (49 found, showing 14)
- `Shout_Enlarge_Duergar` - **Enlarge**
- `Shout_MagicAllergy_Enlarge`
- `Shout_MagicAllergy_Polymorph` - **Magic Allergy: Panther Polymorph**
- `Shout_Slow_TollCollector_Face`
  <br>`SpellSuccess=ApplyStatus(<em>SLOW</em>, 100, 2);`
- `Shout_WildMagic_EnlargeReduce` - **Wild Magic: Enlarge/Reduce** | Each creature within [1] is randomly Enlarged or Reduced.
  <br>`SpellType=Shout`  `SpellSuccess=ApplyStatus(ENLARGE,100,3)`
- `Shout_WildMagic_Polymorph` - **Wild Magic: Polymorph** | You are transformed into a beast.
  <br>`SpellType=Shout`  `SpellProperties=ApplyStatus(POLYMORPH_SHEEP,100,2)`
- `Shout_WildMagic_Slow` - **Wild Magic: Slow** | You are Slowed.
  <br>`SpellType=Shout`  `SpellProperties=ApplyStatus(SLOW,100,2)`
- `Target_EnhanceAbility` - **Enhance Ability** | Bestow a magical enhancement upon an ally. They gain Advantage on Ability Checks with a chosen Ability.
  <br>`SpellType=Target`
- `Target_EnhanceAbility_BearsEndurance` - **Bear's Endurance** | Creature gains Advantage on Constitution Checks and gains [1].
  <br>`SpellType=Target`  `SpellProperties=ApplyStatus(BEARS_ENDURANCE, 100, -1)`
- `Target_EnhanceAbility_BullsStrength` - **Bull's Strength** | Creature gains Advantage on Strength Checks, and its carrying capacity is doubled.
  <br>`SpellType=Target`  `SpellProperties=ApplyStatus(BULLS_STRENGTH, 100, -1)`
- `Target_EnhanceAbility_CatsGrace` - **Cat's Grace** | Creature gains Advantage on Dexterity Checks and only takes half damage from falling.
  <br>`SpellType=Target`  `SpellProperties=ApplyStatus(CATS_GRACE, 100, -1)`
- `Target_EnhanceAbility_EaglesSplendor` - **Eagle's Splendour** | Creature gains Advantage on Charisma Checks.
  <br>`SpellType=Target`  `SpellProperties=ApplyStatus(EAGLES_SPLENDOR, 100, -1)`
- `Target_EnhanceAbility_FoxsCunning` - **Fox's Cunning** | Creature gains Advantage on Intelligence Checks.
  <br>`SpellType=Target`  `SpellProperties=ApplyStatus(FOXS_CUNNING, 100, -1)`
- `Target_EnhanceAbility_OwlsWisdom` - **Owl's Wisdom** | Creature gains Advantage on Wisdom Checks.
  <br>`SpellType=Target`  `SpellProperties=ApplyStatus(OWLS_WISDOM, 100, -1)`

---
## MystraSpells & 5eSpells — new spell candidates (manual pass, not from norbyte_harvest)

_Added 2026-09-12 by parsing the active `MystrasSpells.pak` and `5eSpells.pak` mods directly (not scraped from bg3.norbyte.dev - these two mods are user-installed content, not indexed there). Full cross-mod overlap/dedup analysis: `research/mystra_5espells_compat_report.md`._

Full deduplicated new-spell catalog from both mods (173 spells - identical-ID collisions and cross-mod duplicates collapsed to a single entry), sorted by Level -> School -> Damage/Utility Type, same convention as the rest of this file. Not yet assigned to specific `CX_*_Boost` sections above - skim and cherry-pick like the rest of this document. **Slot column**: `No` = cantrip/ritual, action-point only - do not grant these through a spell-slot resource, they need an at-will/innate cast instead.


### Cantrip

- `Shout_SwordBurst` - **Sword Burst** | Conjuration / Force | Slot: No
- `Target_Infestation` - **Infestation** | Conjuration / Poison | Slot: No
- `Target_MindSliver` - **Mind Sliver** | Enchantment / Debuff/Control | Slot: No
- `Target_Frostbite` - **Frostbite** | Evocation / Cold | Slot: No
- `Target_GreenFlameBlade` - **Green-Flame Blade** | Evocation / Fire | Slot: No
- `Target_LightningLure` - **Lightning Lure** | Evocation / Lightning | Slot: No
- `Shout_HandOfRadiance` - **Hand of Radiance** | Evocation / Radiant | Slot: No
- `Shout_WordOfRadiance` - **Word of Radiance** | Evocation / Radiant | Slot: No
- `Target_BoomingBladeMove` - **Mystra's Booming Blade** | Evocation / Thunder | Slot: No
- `Shout_Thunderclap` - **Thunderclap** | Evocation / Thunder | Slot: No
- `Projectile_LarlochsMinorDrain` - **Larloch's Minor Drain** | Necromancy / Necrotic | Slot: No
- `Projectile_SappingSting` - **Sapping Sting** | Necromancy / Necrotic | Slot: No
- `Target_ControlFlames` - **Control Flames** | Transmutation / Buff/Utility | Slot: No
- `Shout_Druidcraft` - **Druidcraft** | Transmutation / Buff/Utility | Slot: No
- `Target_MagicStone` - **Magic Stone** | Transmutation / Buff/Utility | Slot: No
- `Target_MoldEarth` - **Mold Earth** | Transmutation / Buff/Utility | Slot: No
- `Target_Prestidigitation` - **Prestidigitation** | Transmutation / Buff/Utility | Slot: No
- `Target_ShapeWater` - **Shape Water** | Transmutation / Buff/Utility | Slot: No
- `Target_Gust` - **Gust** | Transmutation / Force | Slot: No
- `Target_PrimalSavagery` - **Primal Savagery** | Transmutation / Poison | Slot: No
- `Target_CreateBonfire` - **Create Bonfire** | Conjuration / Fire | Slot: No
- `Projectile_Moonflare` - **Moonflare** | Evocation / Radiant | Slot: No
- `Target_SpareTheDying` - **Spare the Dying** | ? / Buff/Utility | Slot: No

### 1st Level

- `Shout_AbsorbElements` - **Absorb Elements** | Abjuration / Buff/Utility | Slot: Yes
- `Target_Snare` - **Snare** | Abjuration / Debuff/Control | Slot: Yes
- `Target_UnseenServant` - **Unseen Servant** | Conjuration / Buff/Utility | Slot: Yes
- `Target_UnseenServant_Ritual` - **Unseen Servant: Ritual** | Conjuration / Buff/Utility | Slot: No
- `Target_BeastBond` - **Beast Bond** | Divination / Buff/Utility | Slot: Yes
- `Shout_DetectEvilAndGood` - **Detect Evil and Good** | Divination / Buff/Utility | Slot: Yes
- `Shout_DetectMagic` - **Detect Magic** | Divination / Buff/Utility | Slot: Yes
- `Shout_DetectMagic_Ritual` - **Detect Magic: Ritual** | Divination / Buff/Utility | Slot: No
- `Target_GiftOfAlacrity` - **Gift of Alacrity** | Divination / Buff/Utility | Slot: Yes
- `Target_SuddenAwakening` - **Sudden Awakening** | Enchantment / Buff/Utility | Slot: Yes
- `Target_IdInsinuation` - **Id Insinuation** | Enchantment / Psychic | Slot: Yes
- `Zone_AcidStream` - **Acid Stream** | Evocation / Acid | Slot: Yes
- `Zone_CausticBrew` - **Tasha's Caustic Brew** | Evocation / Acid | Slot: Yes
- `Shout_EarthTremor` - **Earth Tremor** | Evocation / Bludgeoning | Slot: Yes
- `Target_Ceremony_Ritual` - **Ceremony: Ritual** | Evocation / Buff/Utility | Slot: No
- `Target_ChaosBolt` - **Chaos Bolt** | Evocation / Buff/Utility | Slot: Yes
- `Shout_MagicMissile_Jim` - **Jim's Magic Missile** | Evocation / Buff/Utility | Slot: Yes
- `Zone_FrostFingers` - **Frost Fingers** | Evocation / Cold | Slot: Yes
- `Target_Ceremony` - **Ceremony** | Evocation / Debuff/Control | Slot: Yes
- `Target_CauseFear` - **Cause Fear** | Necromancy / Debuff/Control | Slot: Yes
- `Shout_ZephyrStrike` - **Zephyr Strike** | Transmutation / Buff/Utility | Slot: Yes
- `Throw_Catapult` - **Catapult** | Transmutation / Debuff/Control | Slot: Yes
- `Target_MagnifyGravity` - **Magnify Gravity** | Transmutation / Force | Slot: Yes

### 2nd Level

- `Shout_MentalBarrier` - **Mental Barrier** | Abjuration / Buff/Utility | Slot: Yes
- `Target_SummonBeast` - **Summon Beast** | Conjuration / Acid | Slot: Yes
- `Target_DustDevil` - **Dust Devil** | Conjuration / Buff/Utility | Slot: Yes
- `Target_HealingElixir` - **Healing Elixir** | Conjuration / Buff/Utility | Slot: Yes
- `Target_HealingSpirit` - **Healing Spirit** | Conjuration / Buff/Utility | Slot: Yes
- `Zone_SprayOfCards` - **Spray of Cards** | Conjuration / Debuff/Control | Slot: Yes
- `Target_VortexWarp` - **Vortex Warp** | Conjuration / Debuff/Control | Slot: Yes
- `Target_FlockOfFamiliars` - **Flock of Familiars** | Conjuration / Psychic | Slot: Yes
- `Shout_SummonMoonblade_Container` - **Summon Moonblade** | Conjuration / Summon | Slot: Yes
- `Shout_BorrowedKnowledge` - **Borrowed Knowledge** | Divination / Buff/Utility | Slot: Yes
- `Shout_FindTraps` - **Find Traps** | Divination / Buff/Utility | Slot: Yes
- `Target_MindSpike` - **Mind Spike** | Divination / Psychic | Slot: Yes
- `Target_SilveryBarbs` - **Silvery Barbs** | Enchantment / Buff/Utility | Slot: Yes
- `Target_ZoneofTruth` - **Zone of Truth** | Enchantment / Buff/Utility | Slot: Yes
- `Projectile_GlowingCoin_Jim` - **Jim's Glowing Coin** | Enchantment / Debuff/Control | Slot: Yes
- `Target_MindWhip` - **Tasha's Mind Whip** | Enchantment / Psychic | Slot: Yes
- `Target_ContinualFlame` - **Continual Flame** | Evocation / Buff/Utility | Slot: Yes
- `Shout_WardingWind` - **Warding Wind** | Evocation / Buff/Utility | Slot: Yes
- `Zone_RimesBindingIce` - **Rime's Binding Ice** | Evocation / Cold | Slot: Yes
- `Target_SnillocsSnowballStorm` - **Snilloc's Snowball Storm** | Evocation / Debuff/Control | Slot: Yes
- `Zone_AganazzarsScorcher` - **Aganazzar's Scorcher** | Evocation / Fire | Slot: Yes
- `Shout_ShadowBlade_Spell` - **Mystra's Shadow Blade** | Illusion / Buff/Utility | Slot: Yes
- `Target_NathairsMischief` - **Nathair's Mischief** | Illusion / Debuff/Control | Slot: Yes
- `Target_GentleRepose` - **Gentle Repose** | Necromancy / Buff/Utility | Slot: Yes
- `Target_WitherAndBloom` - **Wither and Bloom** | Necromancy / Necrotic | Slot: Yes
- `Target_MaximiliansEarthenGrasp` - **Maximilian's Earthen Grasp** | Transmutation / Bludgeoning | Slot: Yes
- `Shout_AlterSelf` - **Alter Self** | Transmutation / Buff/Utility | Slot: Yes
- `Shout_BeastAspect` - **Bestial Growth** | Transmutation / Buff/Utility | Slot: Yes
- `Target_DragonsBreath` - **Dragon's Breath** | Transmutation / Buff/Utility | Slot: Yes
- `Target_ForceWeapon` - **Force Weapon** | Transmutation / Buff/Utility | Slot: Yes
- `Shout_KineticJaunt` - **Kinetic Jaunt** | Transmutation / Buff/Utility | Slot: Yes
- `Target_Earthbind` - **Earthbind** | Transmutation / Debuff/Control | Slot: Yes
- `Target_Pyrotechnics` - **Pyrotechnics** | Transmutation / Debuff/Control | Slot: Yes
- `Projectile_VolleyOfArrows` - **Volley of Arrows** | Transmutation / Piercing | Slot: Yes

### 3rd Level

- `Target_MagicCircle` - **Magic Circle** | Abjuration / Buff/Utility | Slot: Yes
- `Target_Nondetection` - **Nondetection** | Abjuration / Buff/Utility | Slot: Yes
- `Target_ConjureAnimals_Container` - **Conjure Animals** | Conjuration / Buff/Utility | Slot: Yes
- `Target_CreateFoodAndWater` - **Create Food and Water** | Conjuration / Buff/Utility | Slot: Yes
- `Teleportation_ThunderStep` - **Thunder Step** | Conjuration / Buff/Utility | Slot: Yes
- `Target_FreedomOfTheWaves` - **Freedom of the Waves** | Conjuration / Debuff/Control | Slot: Yes
- `Target_TidalWave` - **Tidal Wave** | Conjuration / Debuff/Control | Slot: Yes
- `Target_SummonShadowspawn` - **Summon Shadowspawn** | Conjuration / Necrotic | Slot: Yes
- `Target_SummonLesserDemons` - **Summon Lesser Demons** | Conjuration / Psychic | Slot: Yes
- `Target_SummonFey_Container` - **Summon Fey** | Conjuration / Summon | Slot: Yes
- `Shout_SenseVitals` - **Sense Vitals** | Divination / Buff/Utility | Slot: Yes
- `Target_Catnap` - **Catnap** | Enchantment / Buff/Utility | Slot: Yes
- `Target_EnemiesAbound` - **Enemies Abound** | Enchantment / Buff/Utility | Slot: Yes
- `Target_IntellectFortress` - **Intellect Fortress** | Enchantment / Buff/Utility | Slot: Yes
- `Target_MotivationalSpeech` - **Motivational Speech** | Enchantment / Buff/Utility | Slot: Yes
- `Shout_InciteGreed` - **Incite Greed** | Enchantment / Debuff/Control | Slot: Yes
- `Target_Antagonize` - **Antagonize** | Enchantment / Psychic | Slot: Yes
- `Shout_BlindFaith` - **Blind Faith** | Evocation / Buff/Utility | Slot: Yes
- `Projectile_MinuteMeteors` - **Minute Meteors** | Evocation / Buff/Utility | Slot: Yes
- `Zone_PsionicBlast` - **Psionic Blast** | Evocation / Force | Slot: Yes
- `Zone_PulseWave` - **Pulse Wave** | Evocation / Force | Slot: Yes
- `Shout_DiscordantMelody` - **Discordant Melody** | Evocation / Thunder | Slot: Yes
- `Shout_SpiritShroud` - **Spirit Shroud** | Necromancy / Debuff/Control | Slot: Yes
- `Target_LifeTransference` - **Life Transference** | Necromancy / Healing | Slot: Yes
- `Target_FlameArrows` - **Flame Arrows** | Transmutation / Buff/Utility | Slot: Yes
- `Target_VenomousBarbs` - **Venomous Barbs** | Transmutation / Buff/Utility | Slot: Yes
- `Target_WaterWalk` - **Water Walk** | Transmutation / Buff/Utility | Slot: Yes
- `Shout_AshardalonsStride` - **Ashardalon's Stride** | Transmutation / Debuff/Control | Slot: Yes
- `Target_EruptingEarth` - **Erupting Earth** | Transmutation / Debuff/Control | Slot: Yes

### 4th Level

- `Shout_AuraOfLife` - **Aura of Life** | Abjuration / Buff/Utility | Slot: Yes
- `Shout_AuraOfPurity` - **Aura of Purity** | Abjuration / Buff/Utility | Slot: Yes
- `Target_SummonAberration` - **Summon Aberration** | Conjuration / Acid | Slot: Yes
- `Target_SummonGreaterDemon` - **Summon Greater Demon** | Conjuration / Fire | Slot: Yes
- `Target_SummonConstruct` - **Summon Construct** | Conjuration / Necrotic | Slot: Yes
- `Target_SummonBeholderkin` - **Summon Aberration: Beholderkin** | Conjuration / Psychic | Slot: Yes
- `Target_SummonElemental` - **Summon Elemental** | Conjuration / Summon | Slot: Yes
- `Target_ArcaneEye` - **Arcane Eye** | Divination / Psychic | Slot: Yes
- `Target_CharmMonster` - **Charm Monster** | Enchantment / Buff/Utility | Slot: Yes
- `Target_EgoWhip` - **Ego Whip** | Enchantment / Debuff/Control | Slot: Yes
- `Shout_MesmersLullaby` - **Mesmer's Lullaby** | Enchantment / Debuff/Control | Slot: Yes
- `Target_DreamSleep` - **Dream** | Enchantment / Psychic | Slot: Yes
- `Projectile_RaulothimsPsychicLance` - **Raulothim's Psychic Lance** | Enchantment / Psychic | Slot: Yes
- `Projectile_VitriolicSphere` - **Vitriolic Sphere** | Evocation / Acid | Slot: Yes
- `Target_StormSphere` - **Storm Sphere** | Evocation / Bludgeoning | Slot: Yes
- `Projectile_WebOfFire` - **Web of Fire** | Evocation / Fire | Slot: Yes
- `Target_GravitySinkhole` - **Gravity Sinkhole** | Evocation / Force | Slot: Yes
- `Target_IllusoryWeapon` - **Illusory Weapon** | Illusion / Buff/Utility | Slot: Yes
- `Shout_ShadowOfMoil` - **Shadow of Moil** | Necromancy / Buff/Utility | Slot: Yes
- `Target_ControlWater_Container` - **Control Water** | Transmutation / Buff/Utility | Slot: Yes
- `Shout_GuardianOfNature` - **Guardian of Nature** | Transmutation / Buff/Utility | Slot: Yes
- `Target_StoneShape_Container` - **Stone Shape** | Transmutation / Buff/Utility | Slot: Yes
- `Target_ElementalBane` - **Elemental Bane** | Transmutation / Debuff/Control | Slot: Yes

### 5th Level

- `Shout_AntilifeShell` - **Antilife Shell** | Abjuration / Buff/Utility | Slot: Yes
- `Target_AstralDisjunction` - **Astral Disjunction** | Abjuration / Buff/Utility | Slot: Yes
- `Shout_CircleOfPower` - **Circle of Power** | Abjuration / Buff/Utility | Slot: Yes
- `Target_BigbyHand` - **Bigby's Hand** | Conjuration / Buff/Utility | Slot: Yes
- `Target_FarStep` - **Far Step** | Conjuration / Buff/Utility | Slot: Yes
- `Teleportation_TeleportationCircle` - **Teleportation Circle** | Conjuration / Buff/Utility | Slot: Yes
- `ProjectileStrike_ConjureVolley` - **Conjure Volley** | Conjuration / Debuff/Control | Slot: Yes
- `Target_InfernalCalling` - **Infernal Calling** | Conjuration / Fire | Slot: Yes
- `Target_SummonDragon` - **Summon Draconic Spirit** | Conjuration / Fire | Slot: Yes
- `Target_SteelWindStrike` - **Steel Wind Strike** | Conjuration / Force | Slot: Yes
- `Shout_CommuneWithNature` - **Commune with Nature** | Divination / Buff/Utility | Slot: Yes
- `Target_SynapticStatic` - **Synaptic Static** | Enchantment / Psychic | Slot: Yes
- `Target_Maelstrom` - **Maelstrom** | Evocation / Bludgeoning | Slot: Yes
- `Target_HolyWeapon` - **Holy Weapon** | Evocation / Buff/Utility | Slot: Yes
- `Target_Immolation` - **Immolation** | Evocation / Fire | Slot: Yes
- `Target_Dawn` - **Dawn** | Evocation / Radiant | Slot: Yes
- `Target_Mislead` - **Mislead** | Illusion / Buff/Utility | Slot: Yes
- `Target_RaiseDead` - **Raise Dead** | Necromancy / Buff/Utility | Slot: Yes
- `Target_DanseMacabre_Container` - **Danse Macabre** | Necromancy / Necrotic | Slot: Yes
- `Projectile_Enervation` - **Enervation** | Necromancy / Necrotic | Slot: Yes
- `Target_MacabreExplosion` - **Macabre Explosion** | Necromancy / Necrotic | Slot: Yes
- `Projectile_NegativeEnergyFlood` - **Negative Energy Flood** | Necromancy / Necrotic | Slot: Yes
- `Target_SkillEmpowerment` - **Skill Empowerment** | Transmutation / Buff/Utility | Slot: Yes
- `Shout_SwiftQuiver` - **Swift Quiver** | Transmutation / Buff/Utility | Slot: Yes

### 6th Level

- `Shout_PrimordialWard` - **Primordial Ward** | Abjuration / Buff/Utility | Slot: Yes
- `Target_ConjureFey` - **Conjure Fey** | Conjuration / Acid | Slot: Yes
- `Target_PsychicCrush` - **Psychic Crush** | Enchantment / Psychic | Slot: Yes
- `Zone_Fissure` - **Fissure** | Evocation / Force | Slot: Yes
- `Shout_ElementalInvestiture` - **Elemental Investiture** | Transmutation / Buff/Utility | Slot: Yes
- `Shout_TensersTransformation` - **Tenser's Transformation** | Transmutation / Buff/Utility | Slot: Yes
- `Target_TrueSeeing` - **True Seeing** | Transmutation / Buff/Utility | Slot: Yes
- `Target_LesserRegenerate` - **Lesser Regeneration** | Transmutation / Healing | Slot: Yes

### 7th Level

- `Target_FingerOfDeath` - **Finger of Death** | Necromancy / Necrotic | Slot: Yes
- `Target_Regenerate` - **Regenerate** | Transmutation / Healing | Slot: Yes

### 8th Level

- `Shout_HolyAura` - **Holy Aura** | Abjuration / Buff/Utility | Slot: Yes
- `Target_MindBlank` - **Mind Blank** | Abjuration / Buff/Utility | Slot: Yes
- `Target_Feeblemind` - **Feeblemind** | Enchantment / Buff/Utility | Slot: Yes
- `Target_DominateMonster` - **Dominate Monster** | Enchantment / Debuff/Control | Slot: Yes

### 9th Level

- `Target_Foresight` - **Foresight** | Divination / Buff/Utility | Slot: Yes
- `Target_PowerWordKill` - **Power Word: Kill** | Enchantment / Buff/Utility | Slot: Yes
- `Target_PowerWordHeal` - **Power Word: Heal** | Evocation / Healing | Slot: Yes
---

_Done in 0s._
