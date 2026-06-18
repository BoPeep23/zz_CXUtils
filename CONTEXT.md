# zz_CXUtils — Project Context

## Purpose

This directory contains a personal toolset for managing `CombatExtender.json`, a configuration file for the **Combat Extender** Baldur's Gate 3 mod. It has no effect on the game itself — all game-relevant files live in the parent `Script Extender/` directory and must never be modified by this toolset.

## Repository Layout

```
Script Extender/
├── CombatExtender.json          ← The actual mod config. Source of truth for the live game.
├── CombatExtender_Cazmir.json   ← Variant config (Cazmir playthrough)
└── zz_CXUtils/                  ← All tooling lives here; nothing here affects the game
    ├── guid_mapper_master.json          ← Master GUID registry (primary working file)
    ├── guid_mapper_master_alteredStats.json  ← Output of alterStatistics.py
    ├── monsterStatBlock.py              ← Core data model (MonsterStatBlock class)
    ├── alterStatistics.py               ← Bulk stat modifications on blocks
    ├── sanitizeFields.py                ← Field normalization / schema enforcement
    ├── discoverFields.py                ← Auto-populate fields from maps + notes
    ├── organizeBlocks.py                ← Sort/order blocks without changing values
    ├── generateCombatExtenderBlocks.py  ← Final output: Clones + Overrides JSON
    ├── generateDictionaries.py          ← Metadata generation (indexes, summaries)
    ├── listFieldValues.py               ← Utility: enumerate unique values for a field
    ├── convertHandlesToMaps.py          ← Convert handle .txt lists → monster_archetype_map.json
    ├── convertMapListToDict.py          ← Convert list-form map JSON → dict form
    ├── maps/                            ← Lookup maps used by discoverFields.py
    │   ├── class_archetype_map.json
    │   ├── monster_archetype_map.json
    │   ├── type_map.json
    │   ├── subtype_map.json
    │   ├── location_map.json
    │   ├── spell_map.json
    │   ├── profiles.json
    │   └── organizeSpellMap.py          ← Utility to sort/dedup spell_map.json
    ├── metadata/                        ← Generated reference files (do not hand-edit)
    │   ├── metadata_guids_by_location.json
    │   ├── metadata_guids_by_type.json
    │   ├── metadata_passives_and_spells.json
    │   ├── metadata_sorted_guids.json
    │   ├── metadata_sorted_guids_unique.json
    │   └── unique_location_values.txt
    ├── clonesAndOverrides/              ← Final output blocks ready to paste into CombatExtender.json
    │   ├── combat_extender_clones.json
    │   └── combat_extender_overrides.json
    └── old/                             ← Archived prior versions (ignore)
```

---

## Core Data Model: `MonsterStatBlock` (`monsterStatBlock.py`)

Every GUID entry is represented as a `MonsterStatBlock` object. The JSON schema maps to:

| JSON Field          | Python Property       | Mutability | Notes |
|---------------------|-----------------------|------------|-------|
| `Handle`            | `handle`              | Immutable | Set by game, short creature name (e.g. `"Imp"`) |
| `FullGuid`          | `full_guid`           | Immutable | Combined 2 fields set by game; Primary key; format: `<Handle>_<Guid>` |
| `Act`               | `act`                 | Auto-populated | `"1"`, `"2"`, `"3"`, `"Global"`, `"Camp"`, `"Unknown"` |
| `Location`          | `location`            | Semi-stable | Normalized location key, 3 tiers (e.g. `"WYRM_ROCK_PRISON"`) |
| `Type`              | `type`                | Stable | D&D creature type, immutable once set (e.g. `"Fiend"`, `"Undead"`) |
| `SubType`           | `subtype`             | Semi-stable | More specific type (e.g. `"Imp"`, `"Skeleton"`, `"Half-Orc"`) |
| `ClassArchetype`    | `classArchetype`      | Custom/user-set | Organizational grouping by D&D class |
| `MonsterArchetype`  | `monsterArchetype`    | Custom/user-set | Organizational grouping by monster identity |
| `Profiles`          | `profiles`            | Rarely changed | List of profile strings |
| `HealthOverride`    | `health_override`     | Mutable | Custom HP value; `0` means no override |
| `PassivesToAdd`     | `passives_to_add`     | Mutable list | Passive abilities to inject into the creature |
| `SpellsToAdd`       | `spells_to_add`       | Mutable list | Spells to inject into the creature |
| `CloneTemplateGuid` | `clone_template_guid` | Mutable | Source GUID to clone from, don't need if the source GUID is the same block |
| `CloneDisplayName`  | `clone_display_name`  | Mutable | Display name for the clone |
| `Corpse`            | `corpse`              | Boolean | True if this entry represents a corpse/dead variant (NOT Undead creatures) |
| `Notes`             | `notes`               | Freeform | Human-readable notes; used by discoverFields for inference |

The master JSON file wraps all entries under a top-level `"Guids"` list:
```json
{ "Guids": [ { "Handle": "...", "FullGuid": "...", ... }, ... ] }
```

`FullGuid` is the unique key. When two entries share a `FullGuid`, `deduplicate()` merges them: lists are unioned, blank string fields are filled in by the non-blank value.

---

## File Roles

### Goal 1: Modify/sanitize `guid_mapper_master.json`

These scripts read from `guid_mapper_master.json` and write a modified output file:

- **`sanitizeFields.py`** — Ensures all expected fields exist with correct defaults; normalizes Act values from location prefix patterns; converts stale Notes lists to strings; removes obsolete fields (`Class`, `Distance`, `Entity`, `Guid`).

- **`alterStatistics.py`** — Adds passives/spells or sets HealthOverride on blocks matched by handle, FullGuid, ClassArchetype, MonsterArchetype, or any combination of those + Act/Location/Type/SubType/Corpse. Match phrases support semicolon-delimited OR logic (e.g. `"2;3"` matches Act 2 or Act 3).

- **`discoverFields.py`** — Auto-populates `ClassArchetype`, `MonsterArchetype`, `SubType`, and `Type` fields on blank entries by matching handle/notes/FullGuid against lookup maps in `maps/`. Uses `!`-suffix for whole-word match and `useLongerMatches`/`oneWordMatch` flags in `monster_archetype_map.json`. Writes debug output to `output.txt`.

- **`organizeBlocks.py`** — Sorts blocks by `[Act, Location, Type, ClassArchetype, Handle]` without changing any field values. Location ordering follows a hardcoded `LOCATION_ORDER` prefix list (S_GLO_, S_CAMP_, ... S_END_).

### Goal 2: Generate metadata/reference files

- **`generateDictionaries.py`** — Produces all `metadata/` files: guids-by-location, guids-by-type, passives+spells master lists, sorted guid lists, and clones/overrides preview dicts. Reads from `guid_mapper_master.json`.

- **`listFieldValues.py`** — Extracts all unique non-empty values for a given field name into a `.txt` file in `metadata/`. Edit `FIELD_NAME` at top of script before running.

- **`convertHandlesToMaps.py`** — Converts `metadata/unique_handle_values.txt` into `maps/monster_archetype_map.json`. Lines ending in `?` → `oneWordMatch=True`, `!` → `useLongerMatches=True`, `*` → `oneWordMatch=True`.

- **`convertMapListToDict.py`** — Migrates `monster_archetype_map.json` from list format to dict format (keyed by `archetypeName`).

- **`maps/organizeSpellMap.py`** — Sorts and deduplicates `spell_map.json` → `spell_map_updated.json`.

### Final Output

- **`generateCombatExtenderBlocks.py`** — The endpoint of the pipeline. Reads `guid_mapper_master.json`, deduplicates, and writes:
  - `clonesAndOverrides/combat_extender_clones.json` — `{"Clones": { FullGuid: {DisplayName, Template?} }}`
  - `clonesAndOverrides/combat_extender_overrides.json` — `{"Overrides": { FullGuid: {Passives?, Spells?, HealthOverride?} }}`

  These are the blocks meant to be copied into the live `CombatExtender.json`.

---

## Typical Workflow

1. **Populate new GUIDs** — Add raw entries (Handle + FullGuid minimum) to `guid_mapper_master.json`.
2. **Sanitize** — Run `sanitizeFields.py` to normalize fields and add missing defaults.
3. **Discover** — Run `discoverFields.py` to auto-populate Type/SubType/ClassArchetype/MonsterArchetype from maps.
4. **Alter** — Run `alterStatistics.py` (or call its static methods) to bulk-add passives/spells/health overrides.
5. **Organize** — Run `organizeBlocks.py` to sort the master file.
6. **Generate output** — Run `generateCombatExtenderBlocks.py` to produce the final Clone/Override blocks.
7. **Metadata** — Run `generateDictionaries.py` anytime to refresh the `metadata/` reference files.

---

## Key Conventions

- `guid_mapper_master.json` is the single source of truth. All scripts read from it; outputs go to separate files.
- `FullGuid` format: `<SceneName>_<CreatureName>_<UUID>`. The scene prefix determines Act via `sanitizeFields.populate_act_field`.
- Match phrases in `alterStatistics` use substring containment by default. Semicolons (`;`) act as OR within a single field filter.
- `maps/*.json` files are the only lookup tables. They are hand-curated; do not auto-overwrite without review.
- `metadata/` and `clonesAndOverrides/` are fully generated — safe to regenerate at any time.
- `old/` contains archived versions — ignore unless rolling back.
- Nothing in `zz_CXUtils/` affects the live game. `CombatExtender.json` in the parent directory is the only file that matters to the mod.