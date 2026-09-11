# Search-term map: CX passive -> thematic Norbyte queries.
# Terms are AND-joined with the type filter, e.g.  type:passive & <term>
# Keep terms narrow: the search page only returns the first 30 hits.
#
# Tokenisation notes (observed):
#  - camelCase splits ("DreadAmbusher" matches), so does underscore.
#  - a term with spaces becomes multiple AND clauses.
#  - single evocative English words ("Fireball", "Darkness") match the
#    Target_/Projectile_/Zone_ spell names reliably; guessed exact IDs often miss.

TERMS = {
    # ---- generic ---------------------------------------------------------
    "CX_Boss_Boost": {
        "role": "boss",
        "passive": ["LegendaryResistance", "LegendaryActionResistance", "Indomitable",
                    "Unstoppable", "Relentless", "DamageReduction", "MagicResistance"],
        "spell": ["ActionSurge", "Indomitable", "SecondWind", "Frightful", "Roar"],
    },
    "CX_MiniBoss_Boost": {
        "role": "boss",
        "passive": ["Elite", "Veteran", "Hardened", "Bolstered", "Resilient",
                    "MagicResistance"],
        "spell": ["ActionSurge", "SecondWind", "Enrage", "Menacing"],
    },
    "CX_Magic_Boost": {
        "role": "caster",
        "passive": ["ArcaneAcuity", "PotentCantrip", "EmpoweredEvocation", "WarCaster",
                    "MAGGloves", "SpellSave"],
        "spell": ["MagicMissile", "Counterspell", "MirrorImage", "Slow", "ScorchingRay",
                  "Haste"],
    },
    "CX_Martial_Boost": {
        "role": "martial",
        "passive": ["ExtraAttack", "GreatWeaponMaster", "Sentinel", "HeavyArmorMaster",
                    "SecondWind", "Indomitable", "SavageAttacker", "PolearmMaster"],
        "spell": ["ActionSurge", "SecondWind", "Cleave", "Rush", "PommelStrike"],
    },
    # ---- barbarian -----------------------------------------------------
    "CX_Barbarian_Boost": {
        "role": "martial",
        "passive": ["RecklessAttack", "DangerSense", "FeralInstinct", "BrutalCritical",
                    "RelentlessRage", "FastMovement", "PrimalChampion"],
        "spell": ["Rage", "Enrage", "RecklessAttack", "Roar"],
    },
    "CX_Barbarian_Berserker_Boost": {
        "role": "martial",
        "passive": ["Frenzy", "MindlessRage", "IntimidatingPresence", "Berserker",
                    "Retaliation"],
        "spell": ["Frenzy", "IntimidatingPresence", "Frenzied", "Rage"],
    },
    "CX_Barbarian_WildMagic_Boost": {
        "role": "hybrid",
        "passive": ["WildMagicBarbarian", "MagicAwareness", "BolsteringMagic",
                    "UnstableBacklash", "WildSurge"],
        "spell": ["WildMagic", "Teleport", "MagicMissile", "Rage"],
    },
    "CX_Barbarian_Wildheart_Boost": {
        "role": "martial",
        "passive": ["AnimalAspect", "BestialHeart", "RageOfTheWilds", "Wildheart",
                    "AspectOf", "TotemSpirit", "BerserkerHeart"],
        "spell": ["AnimalAspect", "AspectOf", "Rage", "Roar"],
    },
    # ---- bard --------------------------------------------------------
    "CX_Bard_Boost": {
        "role": "caster",
        "passive": ["BardicInspiration", "Countercharm", "JackOfAllTrades", "SongOfRest",
                    "FontOfInspiration"],
        "spell": ["ViciousMockery", "Heroism", "Sleep", "Countercharm", "HideousLaughter",
                  "Bane"],
    },
    "CX_Bard_Lore_Boost": {
        "role": "caster",
        "passive": ["CuttingWords", "CollegeOfLore", "MagicalSecrets", "PeerlessSkill",
                    "BonusProficiencies"],
        "spell": ["CuttingWords", "Counterspell", "Command", "Bane", "Dissonant"],
    },
    "CX_Bard_Swords_Boost": {
        "role": "hybrid",
        "passive": ["BladeFlourish", "DefensiveFlourish", "SlashingFlourish",
                    "MobileFlourish", "CollegeOfSwords", "TwoWeaponFighting"],
        "spell": ["Flourish", "BladeFlourish", "ViciousMockery"],
    },
    "CX_Bard_Valor_Boost": {
        "role": "hybrid",
        "passive": ["CombatInspiration", "CollegeOfValor", "ExtraAttack", "ValourBard"],
        "spell": ["CombatInspiration", "Heroism", "Haste", "Bless"],
    },
    # ---- cleric -----------------------------------------------------
    "CX_Cleric_Boost": {
        "role": "caster",
        "passive": ["TurnUndead", "ChannelDivinity", "DivineIntervention", "BlessedStrikes",
                    "DestroyUndead"],
        "spell": ["TurnUndead", "Bless", "GuardianOfFaith", "SpiritGuardians", "HoldPerson",
                  "MassHealing"],
    },
    "CX_Cleric_Knowledge_Boost": {
        "role": "caster",
        "passive": ["KnowledgeDomain", "KnowledgeOfTheAges", "ReadThoughts",
                    "BlessingsOfKnowledge", "VisionsOfThePast"],
        "spell": ["DetectThoughts", "HoldPerson", "Command", "Counterspell", "Bane"],
    },
    "CX_Cleric_Life_Boost": {
        "role": "caster",
        "passive": ["LifeDomain", "DiscipleOfLife", "BlessedHealer", "SupremeHealing",
                    "PreserveLife"],
        "spell": ["HealingWord", "MassHealing", "CureWounds", "PreserveLife", "Revivify",
                  "Heal"],
    },
    "CX_Cleric_Light_Boost": {
        "role": "caster",
        "passive": ["LightDomain", "WardingFlare", "ImprovedFlareBlessing",
                    "CoronaOfLight", "RadianceOfTheDawn"],
        "spell": ["WardingFlare", "Fireball", "Faeriefire", "RadianceOfTheDawn", "Daylight",
                  "ScorchingRay"],
    },
    "CX_Cleric_Nature_Boost": {
        "role": "caster",
        "passive": ["NatureDomain", "AcolyteOfNature", "DampenElements", "CharmAnimals",
                    "DivineStrike"],
        "spell": ["SpikeGrowth", "CharmPerson", "Thunderwave", "Barkskin", "ConjureAnimals",
                  "CallLightning"],
    },
    "CX_Cleric_Trickery_Boost": {
        "role": "caster",
        "passive": ["TrickeryDomain", "BlessingOfTheTrickster", "InvokeDuplicity",
                    "CloakOfShadows", "DivineStrike"],
        "spell": ["InvokeDuplicity", "Invisibility", "Blur", "MirrorImage",
                  "PassWithoutTrace", "Confusion"],
    },
    "CX_Cleric_Tempest_Boost": {
        "role": "caster",
        "passive": ["TempestDomain", "DestructiveWrath", "WrathOfTheStorm",
                    "ThunderboltStrike", "StormBorne"],
        "spell": ["WrathOfTheStorm", "LightningBolt", "CallLightning", "Thunderwave",
                  "Shatter", "Shocking"],
    },
    "CX_Cleric_War_Boost": {
        "role": "hybrid",
        "passive": ["WarDomain", "WarPriest", "GuidedStrike", "WarGodsBlessing",
                    "AvatarOfBattle", "DivineStrike"],
        "spell": ["WarPriest", "GuidedStrike", "SpiritualWeapon", "Bless", "ShieldOfFaith",
                  "CrusadersMantle"],
    },
    # ---- druid -----------------------------------------------------
    "CX_Druid_Boost": {
        "role": "caster",
        "passive": ["WildShape", "NaturalRecovery", "BeastSpells", "Archdruid",
                    "PrimalStrike"],
        "spell": ["WildShape", "CallLightning", "Entangle", "SpikeGrowth", "ConjureAnimals",
                  "Moonbeam"],
    },
    "CX_Druid_Land_Boost": {
        "role": "caster",
        "passive": ["CircleOfTheLand", "LandsStride", "NaturesWard", "NaturesSanctuary"],
        "spell": ["SleetStorm", "SpikeGrowth", "IceStorm", "LightningBolt", "StinkingCloud",
                  "PlantGrowth"],
    },
    "CX_Druid_Moon_Boost": {
        "role": "hybrid",
        "passive": ["CircleOfTheMoon", "CombatWildShape", "LunarForm", "PrimalStrike",
                    "ElementalWildShape", "ThousandForms"],
        "spell": ["CombatWildShape", "WildShape", "Moonbeam", "Starfire"],
    },
    "CX_Druid_Spores_Boost": {
        "role": "hybrid",
        "passive": ["CircleOfSpores", "HaloOfSpores", "SymbioticEntity",
                    "FungalInfestation", "SpreadingSpores", "FungalBody"],
        "spell": ["SymbioticEntity", "HaloOfSpores", "FungalInfestation", "SpreadingSpores",
                  "Contagion"],
    },
    # ---- fighter --------------------------------------------------
    "CX_Fighter_Boost": {
        "role": "martial",
        "passive": ["SecondWind", "ActionSurge", "Indomitable", "FightingStyle",
                    "ExtraAttack", "StudiedAttacks"],
        "spell": ["ActionSurge", "SecondWind", "Indomitable"],
    },
    "CX_Fighter_BattleMaster_Boost": {
        "role": "martial",
        "passive": ["CombatSuperiority", "Maneuver", "KnowYourEnemy", "Superiority",
                    "Riposte"],
        "spell": ["Maneuver", "TripAttack", "DisarmingAttack", "MenacingAttack", "Riposte",
                  "PrecisionAttack", "GoadingAttack", "SweepingAttack"],
    },
    "CX_Fighter_Champion_Boost": {
        "role": "martial",
        "passive": ["ImprovedCritical", "RemarkableAthlete", "SuperiorCritical",
                    "Survivor", "AdditionalFightingStyle"],
        "spell": ["ActionSurge", "SecondWind", "Rush"],
    },
    "CX_Fighter_EldritchKnight_Boost": {
        "role": "hybrid",
        "passive": ["WeaponBond", "EldritchKnight", "WarMagic", "EldritchStrike",
                    "ArcaneCharge"],
        "spell": ["Shield", "MageArmor", "Blur", "ScorchingRay", "MistyStep",
                  "ActionSurge"],
    },
    # ---- monk ----------------------------------------------------
    "CX_Monk_Boost": {
        "role": "martial",
        "passive": ["MartialArts", "FlurryOfBlows", "PatientDefense", "StepOfTheWind",
                    "DeflectMissiles", "StunningStrike", "DiamondSoul", "EmptyBody"],
        "spell": ["FlurryOfBlows", "PatientDefense", "StepOfTheWind", "StunningStrike",
                  "KiPoints"],
    },
    "CX_Monk_FourElements_Boost": {
        "role": "hybrid",
        "passive": ["FourElements", "ElementalAttunement", "FangsOfTheFireSnake",
                    "FistOfFourThunders", "ShapeTheFlowingRiver", "RideTheWind"],
        "spell": ["FangsOfTheFireSnake", "FistOfUnbrokenAir", "FistOfFourThunders",
                  "SweepingCinderStrike", "WaterWhip", "BurningHands"],
    },
    "CX_Monk_OpenHand_Boost": {
        "role": "martial",
        "passive": ["OpenHand", "OpenHandTechnique", "WholenessOfBody", "ManifestationOf",
                    "QuiveringPalm", "TranquilityOfMind"],
        "spell": ["OpenHandTechnique", "QuiveringPalm", "WholenessOfBody", "Manifestation"],
    },
    "CX_Monk_Shadow_Boost": {
        "role": "hybrid",
        "passive": ["WayOfShadow", "ShadowArts", "ShadowStep", "OpportunistStrike",
                    "ShadowStrike"],
        "spell": ["ShadowStep", "ShadowArts", "PassWithoutTrace", "Darkness", "Silence",
                  "MinorIllusion"],
    },
    # ---- paladin -----------------------------------------------
    "CX_Paladin_Boost": {
        "role": "hybrid",
        "passive": ["DivineSmite", "LayOnHands", "DivineSense", "AuraOfProtection",
                    "AuraOfCourage", "ImprovedDivineSmite", "CleansingTouch"],
        "spell": ["DivineSmite", "LayOnHands", "DivineSense", "ShieldOfFaith", "Bless",
                  "Command"],
    },
    "CX_Paladin_Ancients_Boost": {
        "role": "hybrid",
        "passive": ["OathOfTheAncients", "AuraOfWarding", "TurnTheFaithless",
                    "ElderChampion", "NaturesWrath"],
        "spell": ["NaturesWrath", "AuraOfWarding", "EnsnaringStrike", "Moonbeam",
                  "MistyStep", "PlantGrowth"],
    },
    "CX_Paladin_Devotion_Boost": {
        "role": "hybrid",
        "passive": ["OathOfDevotion", "SacredWeapon", "TurnTheUnholy", "AuraOfDevotion",
                    "HolyNimbus"],
        "spell": ["SacredWeapon", "ProtectionFromEvil", "ShieldOfFaith", "Sanctuary",
                  "HolyNimbus"],
    },
    "CX_Paladin_Vengeance_Boost": {
        "role": "hybrid",
        "passive": ["OathOfVengeance", "VowOfEnmity", "RelentlessAvenger",
                    "SoulOfVengeance", "AvengingAngel", "AbjureEnemy"],
        "spell": ["VowOfEnmity", "HuntersMark", "Bane", "MistyStep", "HoldPerson", "Haste"],
    },
    "CX_Paladin_Oathbreaker_Boost": {
        "role": "hybrid",
        "passive": ["Oathbreaker", "ControlUndead", "DreadfulAspect", "AuraOfHate",
                    "SupernaturalResistance"],
        "spell": ["ControlUndead", "DreadfulAspect", "AnimateDead", "Bane", "InflictWounds",
                  "HungerOfHadar"],
    },
    # ---- ranger -----------------------------------------------
    "CX_Ranger_Boost": {
        "role": "hybrid",
        "passive": ["FavoredEnemy", "NaturalExplorer", "PrimevalAwareness", "FeralSenses",
                    "FoeSlayer", "ExtraAttack"],
        "spell": ["HuntersMark", "EnsnaringStrike", "HailOfThorns", "LightningArrow",
                  "SpikeGrowth", "Volley"],
    },
    "CX_Ranger_BeastMaster_Boost": {
        "role": "hybrid",
        "passive": ["BeastMaster", "RangersCompanion", "BestialFury", "ShareSpells",
                    "ExceptionalTraining"],
        "spell": ["RangersCompanion", "FindFamiliar", "AnimalCompanion", "ConjureAnimals",
                  "CommandCompanion"],
    },
    "CX_Ranger_GloomStalker_Boost": {
        "role": "hybrid",
        "passive": ["GloomStalker", "DreadAmbusher", "UmbralShroud", "IronMind",
                    "StalkersFlurry", "ShadowyDodge"],
        "spell": ["DreadAmbusher", "UmbralShroud", "DisguiseSelf", "FogCloud",
                  "PassWithoutTrace", "ScorchingRay"],
    },
    "CX_Ranger_Hunter_Boost": {
        "role": "hybrid",
        "passive": ["ColossusSlayer", "GiantKiller", "HordeBreaker", "MultiattackDefense",
                    "StandAgainstTheTide", "EscapeTheHorde"],
        "spell": ["Volley", "WhirlwindAttack", "HordeBreaker", "HailOfThorns",
                  "LightningArrow"],
    },
    # ---- rogue ----------------------------------------------
    "CX_Rogue_Boost": {
        "role": "martial",
        "passive": ["SneakAttack", "CunningAction", "UncannyDodge", "Evasion",
                    "ReliableTalent", "SlipperyMind", "StrokeOfLuck"],
        "spell": ["SneakAttack", "CunningAction", "Dash", "Disengage", "Hide"],
    },
    "CX_Rogue_ArcaneTrickster_Boost": {
        "role": "hybrid",
        "passive": ["ArcaneTrickster", "MagicalAmbush", "VersatileTrickster",
                    "SpellThief", "Legerdemain"],
        "spell": ["MageHand", "Shield", "Blur", "SilentImage", "Invisibility",
                  "HideousLaughter"],
    },
    "CX_Rogue_Assassin_Boost": {
        "role": "martial",
        "passive": ["Assassinate", "AssassinsInitiative", "DeathStrike", "Infiltration"],
        "spell": ["Assassinate", "DeathStrike", "Hide", "Disguise"],
    },
    "CX_Rogue_Thief_Boost": {
        "role": "martial",
        "passive": ["FastHands", "SecondStoryWork", "ThiefsReflexes"],
        "spell": ["CunningAction", "FastHands", "Dash", "Hide"],
    },
    # ---- sorcerer -------------------------------------------
    "CX_Sorcerer_Boost": {
        "role": "caster",
        "passive": ["Metamagic", "FontOfMagic", "SorceryPoints", "CarefulSpell",
                    "TwinnedSpell", "QuickenedSpell", "HeightenedSpell", "DistantSpell",
                    "EmpoweredSpell", "ExtendedSpell", "SubtleSpell"],
        "spell": ["ChromaticOrb", "Fireball", "HoldPerson", "MagicMissile", "Haste",
                  "Metamagic"],
    },
    "CX_Sorcerer_DraconicBloodline_Boost": {
        "role": "caster",
        "passive": ["DraconicBloodline", "DraconicAncestry", "DraconicResilience",
                    "ElementalAffinity", "DraconicPresence", "DragonWings"],
        "spell": ["ChromaticOrb", "Fireball", "Fear", "BurningHands", "Command",
                  "DragonWings"],
    },
    "CX_Sorcerer_WildMagic_Boost": {
        "role": "caster",
        "passive": ["WildMagicSorcery", "TidesOfChaos", "BendLuck", "ControlledChaos"],
        "spell": ["TidesOfChaos", "WildMagic", "MagicMissile", "Confusion", "ChaosBolt"],
    },
    "CX_Sorcerer_StormSorcery_Boost": {
        "role": "caster",
        "passive": ["StormSorcery", "Tempestuous", "WindSpeaker", "HeartOfTheStorm",
                    "StormGuide", "StormsFury", "WindSoul"],
        "spell": ["TempestuousMagic", "LightningBolt", "Thunderwave", "Shatter",
                  "CallLightning", "GustOfWind"],
    },
    # ---- warlock -------------------------------------------
    "CX_Warlock_Boost": {
        "role": "caster",
        "passive": ["EldritchInvocation", "AgonizingBlast", "RepellingBlast", "DevilsSight",
                    "PactOfTheBlade", "PactOfTheChain", "PactOfTheTome", "MysticArcanum",
                    "Lifedrinker"],
        "spell": ["EldritchBlast", "Hex", "ArmorOfAgathys", "HungerOfHadar", "Counterspell",
                  "PactOfTheBlade"],
    },
    "CX_Warlock_Archfey_Boost": {
        "role": "caster",
        "passive": ["Archfey", "FeyPresence", "MistyEscape", "BeguilingDefenses",
                    "DarkDelirium"],
        "spell": ["FeyPresence", "MistyStep", "FaerieFire", "Sleep", "CalmEmotions",
                  "PhantasmalForce"],
    },
    "CX_Warlock_Fiend_Boost": {
        "role": "caster",
        "passive": ["TheFiend", "DarkOnesBlessing", "DarkOnesOwnLuck", "FiendishResilience",
                    "HurlThroughHell"],
        "spell": ["HurlThroughHell", "DarkOnesOwnLuck", "Fireball", "ScorchingRay",
                  "Command", "BurningHands"],
    },
    "CX_Warlock_GreatOldOne_Boost": {
        "role": "caster",
        "passive": ["GreatOldOne", "AwakenedMind", "EntropicWard", "ThoughtShield",
                    "CreateThrall"],
        "spell": ["EntropicWard", "HideousLaughter", "Dissonant", "DetectThoughts",
                  "PhantasmalKiller", "Confusion"],
    },
    # ---- wizard -------------------------------------------
    "CX_Wizard_Boost": {
        "role": "caster",
        "passive": ["ArcaneRecovery", "SpellMastery", "SignatureSpell"],
        "spell": ["MagicMissile", "Shield", "MistyStep", "Fireball", "Counterspell",
                  "HoldPerson"],
    },
    "CX_Wizard_Abjuration_Boost": {
        "role": "caster",
        "passive": ["AbjurationSavant", "ArcaneWard", "ProjectedWard", "ImprovedAbjuration",
                    "SpellResistance"],
        "spell": ["Shield", "Counterspell", "ArmorOfAgathys", "Banishment",
                  "ProtectionFromEnergy", "LesserRestoration"],
    },
    "CX_Wizard_Conjuration_Boost": {
        "role": "caster",
        "passive": ["ConjurationSavant", "MinorConjuration", "BenignTransposition",
                    "FocusedConjuration", "DurableSummons"],
        "spell": ["ConjureElemental", "ConjureMinorElemental", "CloudOfDaggers", "Grease",
                  "StinkingCloud", "MistyStep"],
    },
    "CX_Wizard_Divination_Boost": {
        "role": "caster",
        "passive": ["DivinationSavant", "Portent", "ExpertDivination", "ThirdEye",
                    "GreaterPortent"],
        "spell": ["Portent", "DetectThoughts", "Fear", "HoldPerson", "Slow", "Fog"],
    },
    "CX_Wizard_Enchantment_Boost": {
        "role": "caster",
        "passive": ["EnchantmentSavant", "HypnoticGaze", "InstinctiveCharm",
                    "SplitEnchantment", "AlterMemories"],
        "spell": ["HypnoticGaze", "HoldPerson", "Confusion", "HideousLaughter",
                  "DominatePerson", "CharmPerson"],
    },
    "CX_Wizard_Evocation_Boost": {
        "role": "caster",
        "passive": ["EvocationSavant", "SculptSpells", "PotentCantrip",
                    "EmpoweredEvocation", "Overchannel"],
        "spell": ["Fireball", "LightningBolt", "Shatter", "IceStorm", "ScorchingRay",
                  "Thunderwave"],
    },
    "CX_Wizard_Illusion_Boost": {
        "role": "caster",
        "passive": ["IllusionSavant", "MinorIllusion", "MalleableIllusions",
                    "IllusorySelf", "IllusoryReality"],
        "spell": ["MirrorImage", "Blur", "Invisibility", "PhantasmalForce", "SilentImage",
                  "FogCloud"],
    },
    "CX_Wizard_Necromancy_Boost": {
        "role": "caster",
        "passive": ["NecromancySavant", "GrimHarvest", "UndeadThralls", "InuredToUndeath",
                    "CommandUndead"],
        "spell": ["AnimateDead", "InflictWounds", "RayOfSickness", "VampiricTouch",
                  "CircleOfDeath", "ChillTouch"],
    },
    "CX_Wizard_Transmutation_Boost": {
        "role": "caster",
        "passive": ["TransmutationSavant", "MinorAlchemy", "TransmutersStone",
                    "Shapechanger", "MasterTransmuter"],
        "spell": ["Haste", "Slow", "Enlarge", "Polymorph", "EnhanceAbility", "Knock"],
    },
}
