# zz_CXUtils — Project Context

## Purpose

This directory contains a personal toolset for managing `CombatExtender.json`, a configuration file for the **Combat Extender** Baldur's Gate 3 mod. Most of this toolset works on local files only and has no effect on the game itself, but `generateCombatExtenderBlocks.py` is the one exception: it writes directly into the live `CombatExtender.json` at `C:\Users\Tyler\AppData\Local\Larian Studios\Baldur's Gate 3\Script Extender\CombatExtender.json` (merging into the `Clones`/`Overrides` keys, overwriting entries by `FullGuid`, leaving every other key untouched). All other scripts here are local-only and must not be changed to write outside this repo without the same explicit review.

## Repository Layout

```
Script Extender/
├── CombatExtender.json          ← The actual mod config. Source of truth for the live game. Written to directly by generateCombatExtenderBlocks.py.
├── CombatExtender_Cazmir.json   ← Variant config (Cazmir playthrough)
└── zz_CXUtils/                  ← All tooling lives here; nothing here affects the game
    ├── guid_mapper_master.json          ← Master GUID registry (primary working file)
    ├── monsterStatBlock.py              ← Core data model (MonsterStatBlock class)
    ├── sanitizeFields.py                ← Field normalization / schema enforcement
    ├── discoverFields.py                ← Auto-populate fields from maps + notes; sole path for applying stats (via profile_to_modifications_improvements_map.json)
    ├── organizeBlocks.py                ← Sort/order blocks without changing values
    ├── generateCombatExtenderBlocks.py  ← Final output: Clones + Overrides JSON
    ├── generateDictionaries.py          ← Metadata generation (indexes, summaries)
    ├── listFieldValues.py               ← Utility: enumerate unique values for a field
    ├── convertHandlesToMaps.py          ← Convert handle .txt lists → monster_archetype_map.json
    ├── convertMapListToDict.py          ← Convert list-form map JSON → dict form
    ├── maps/                            ← Lookup maps used by discoverFields.py
    │   ├── profile_to_modifications_improvements_map.json ← THE stat-application map: ApplyStats/MatchCombos + randomization per entry
    │   ├── class_archetype_map.json
    │   ├── monster_archetype_map.json
    │   ├── type_map.json
    │   ├── subtype_map.json
    │   ├── location_map.json
    │   ├── spell_map.json
    │   
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
    ├── dryrun/                          ← Always-present preview folder for --dry-run output (gitignored contents)
    ├── archive/                         ← Auto-generated timestamped backups on every save (gitignored)
    └── old/                             ← Archived/defunct prior versions, incl. alterStatistics.py and
                                            filter_blocks_and_apply.py (superseded by profile_to_modifications_improvements_map.json) — ignore unless rolling back
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
| `HealthOverride`    | `health_override`     | Mutable | Custom HP value; `0` means no override |
| `PassivesToAdd`     | `passives_to_add`     | Mutable list | Passive abilities to inject into the creature |
| `SpellsToAdd`       | `spells_to_add`       | Mutable list | Spells to inject into the creature |
| `CloneTemplateGuid` | `clone_template_guid` | Mutable | Source GUID to clone from, don't need if the source GUID is the same block |
| `CloneDisplayName`  | `clone_display_name`  | Mutable | Display name for the clone |
| `Corpse`            | `corpse`              | Boolean | True if this entry represents a corpse/dead variant (NOT Undead creatures) |
| `Notes`             | `notes`               | Freeform | Human-readable notes; used by discoverFields for inference |
| `MapApplied`        | `map_applied`         | Boolean | True once `discoverFields.apply_handle_map` has applied an entry's fixed `ApplyStats` to this block; prevents future runs from overwriting them |
| `RandomizationApplied` | `randomization_applied` | Boolean | True once `apply_handle_map` has applied an entry's `RandomPassives`/`RandomSpells`/`HealthOverrideRange` to this block. Independent of `MapApplied` — an entry with only randomization (no `ApplyStats`) sets this without setting `MapApplied` |
| `LockBlock`         | `lock_block`          | Boolean | True freezes the block from ALL further mutation by `apply_handle_map` — both hard stats and randomization, unconditionally, even if the matching entry sets `OverrideStaticLock`/`OverrideRandomLock` |

The master JSON file wraps all entries under a top-level `"Guids"` list:
```json
{ "Guids": [ { "Handle": "...", "FullGuid": "...", ... }, ... ] }
```

`FullGuid` is the unique key. When two entries share a `FullGuid`, `deduplicate()` merges them: lists are unioned, blank string fields are filled in by the non-blank value.

---

## File Roles

### Goal 1: Modify/sanitize `guid_mapper_master.json`

These scripts read from `guid_mapper_master.json` and write a modified output file:

- **`sanitizeFields.py`** — Ensures all expected fields exist with correct defaults; normalizes Act values from location prefix patterns; converts stale Notes lists to strings; removes obsolete fields (`Class`, `Distance`, `Entity`, `Guid`, `Profiles`). Runs regardless of `LockBlock` — this is schema hygiene, not stat application.

- **`discoverFields.py`** — Two kinds of logic:
  - Categorical auto-population (`update_class_archetype_based_on_notes`, `update_monster_archetype_based_on_handle`, `update_subtype_based_on_notes`, `update_type_based_on_notes`, `extract_armor_class_from_notes`) — fills blank `ClassArchetype`/`MonsterArchetype`/`SubType`/`Type`/`ArmorClass` by matching handle/notes/FullGuid against lookup maps in `maps/`. Uses `!`-suffix for whole-word match and `useLongerMatches`/`oneWordMatch` flags in `monster_archetype_map.json`. Writes debug output to `output.txt`.
  - **`apply_handle_map`** — **the sole path for applying stats to blocks.** Reads `maps/profile_to_modifications_improvements_map.json`; for each entry, matches blocks via `MatchCombos` (see below) and applies `ApplyStaticStats` (fixed fields, gated/tracked by `LockStaticModifications`) and/or `ApplyRandomStats` (`RandomPassives`+`RandomPassiveCount`, `RandomSpells`+`RandomSpellCount`, `HealthOverrideRange`; gated/tracked independently by `LockRandomModifications`). `LockBlock` always skips a block entirely, for both parts, regardless of any entry's `OverrideStaticLock`/`OverrideRandomLock`. `alterStatistics.py` and `filter_blocks_and_apply.py` (the old direct-editing/filter-cluster systems) are archived to `old/` — defunct, no longer wired to anything.

  `profile_to_modifications_improvements_map.json` entry shape:
  ```json
  {
    "Entry Name": {
      "StopUpdates": false,
      "ApplyStaticStats": {
        "StopUpdates": false, "OverrideStaticLock": false, "SetStaticLock": true,
        "Type": "...", "ArmorClass": 15, "PassivesToAdd": ["..."], "...": "..."
      },
      "MatchCombos": [ { "Handle": "...", "MonsterArchetype": "..." } ],
      "ApplyRandomStats": {
        "StopUpdates": false, "OverrideRandomLock": false, "SetRandomLock": true,
        "RandomPassives": ["P1", "P2", "P3"], "RandomPassiveCount": 2,
        "RandomSpells": ["S1", "S2"], "RandomSpellCount": 1,
        "HealthOverrideRange": [10, 20]
      }
    }
  }
  ```
  Top-level `StopUpdates` skips the entry entirely (both tiers). Each of
  `ApplyStaticStats`/`ApplyRandomStats` has its own `StopUpdates` (skip just
  that tier for this entry), `OverrideStaticLock`/`OverrideRandomLock`
  (default `false`; ignore the block's existing lock for this entry, forcing
  re-application), and `SetStaticLock`/`SetRandomLock` (default `true`;
  set `false` to apply without locking the block for that tier).
  `ApplyRandomStats` is only present on entries that use randomization.
  A `MatchCombo` is satisfied when every valid field/value pair substring-matches (case-insensitive) the same field on the block; a combo needs at least one valid pair after filtering blanks or it matches nothing (never everything). Valid combo values: non-blank string, bool, int, or float — list-valued fields (`PassivesToAdd`/`SpellsToAdd`) and `HealthOverride` are never valid combo fields. `HealthOverrideRange`, when it resolves to a usable range (not blank, no zero, high ≥ low), takes priority over `ApplyStats.HealthOverride` entirely for that entry.

  **Packaging (randomization only):** any entry in `RandomPassives`/`RandomSpells` (in any random-modifications map, not just this one) can bundle multiple passives/spells into one roll by joining them with `;` (e.g. `"PackA;PackB"`). The pool entry is still picked/counted as a single roll against `RandomPassiveCount`/`RandomSpellCount`, but each `;`-separated piece is added individually to `PassivesToAdd`/`SpellsToAdd`. A packaged entry is treated as already-rolled (and excluded from future re-picks) only once every one of its pieces is already present on the block.

- **`organizeBlocks.py`** — Sorts blocks by `[Act, Location, Type, ClassArchetype, Handle]` without changing any field values. Location ordering follows a hardcoded `LOCATION_ORDER` prefix list (S_GLO_, S_CAMP_, ... S_END_).

### Goal 2: Generate metadata/reference files

- **`generateDictionaries.py`** — Produces all `metadata/` files: guids-by-location, guids-by-type, passives+spells master lists, sorted guid lists, and clones/overrides preview dicts. Reads from `guid_mapper_master.json`.

- **`listFieldValues.py`** — Extracts all unique non-empty values for a given field name into a `.txt` file in `metadata/`. Edit `FIELD_NAME` at top of script before running.

- **`convertHandlesToMaps.py`** — Converts `metadata/unique_handle_values.txt` into `maps/monster_archetype_map.json`. Lines ending in `?` → `oneWordMatch=True`, `!` → `useLongerMatches=True`, `*` → `oneWordMatch=True`.

- **`convertMapListToDict.py`** — Migrates `monster_archetype_map.json` from list format to dict format (keyed by `archetypeName`).

### Final Output

- **`generateCombatExtenderBlocks.py`** — The endpoint of the pipeline. Reads `guid_mapper_master.json`, deduplicates, and writes:
  - `clonesAndOverrides/combat_extender_clones.json` — `{"Clones": { FullGuid: {DisplayName, Template?} }}`
  - `clonesAndOverrides/combat_extender_overrides.json` — `{"Overrides": { FullGuid: {Passives?, Spells?, HealthOverride?} }}`
  - the live `CombatExtender.json` itself, via `merge_into_combat_extender()` — merges the above into its `Clones`/`Overrides` keys (overwriting by `FullGuid`), leaving all other keys (`Health`, `Damage`, `ArmourClass`, ...) untouched.

  `generate_clones`/`generate_overrides` run unfiltered over every block. `generate_clones_by_field_combo`/`generate_overrides_by_field_combo` take optional `Location`/`ClassArchetype`/`MonsterArchetype`/`Handle` substring filters (case-insensitive, all non-empty filters must match) for one-off targeted generation.

---

## Typical Workflow

1. **Populate new GUIDs** — Add raw entries (Handle + FullGuid minimum) to `guid_mapper_master.json`.
2. **Sanitize** — Run `sanitizeFields.py` to normalize fields and add missing defaults.
3. **Discover + Apply** — Edit `maps/profile_to_modifications_improvements_map.json` (ApplyStats/MatchCombos/randomization), then run `python discoverFields.py --dry-run` to preview (writes `dryrun/guid_mapper_master_dryrun.json` and a change summary, touches nothing real), then rerun without `--dry-run` to commit — this both auto-populates Type/SubType/ClassArchetype/MonsterArchetype from maps and applies `profile_to_modifications_improvements_map.json`. Changes touching more than 25% of blocks prompt for confirmation before saving.
4. **Organize** — Run `organizeBlocks.py` to sort the master file.
5. **Generate output** — Run `generateCombatExtenderBlocks.py` to produce the final Clone/Override blocks.
6. **Metadata** — Run `generateDictionaries.py` anytime to refresh the `metadata/` reference files.

---

## Key Conventions

- `guid_mapper_master.json` is the single source of truth. All scripts read from it; outputs go to separate files.
- `FullGuid` format: `<SceneName>_<CreatureName>_<UUID>`. The scene prefix determines Act via `sanitizeFields.populate_act_field`.
- **`profile_to_modifications_improvements_map.json` (via `discoverFields.apply_handle_map`) is the only sanctioned way to apply stats to blocks.** `alterStatistics.py` and `filter_blocks_and_apply.py` are archived/defunct.
- `maps/*.json` files are the only lookup tables. They are hand-curated; do not auto-overwrite without review.
- `metadata/` and `clonesAndOverrides/` are fully generated — safe to regenerate at any time.
- `archive/` (auto-generated, gitignored) holds a timestamped pre-overwrite snapshot from every `MonsterStatBlock.save_to_json_file` call — a rollback point. `dryrun/` holds the always-present `--dry-run` preview output (gitignored contents).
- `old/` contains archived/defunct versions, including `alterStatistics.py` and `filter_blocks_and_apply.py` — ignore unless rolling back.
- `CombatExtender.json` in the parent directory is the only file that matters to the mod, and `generateCombatExtenderBlocks.py` is the only script permitted to write to it directly (via `merge_into_combat_extender()`). Every other script in `zz_CXUtils/` is local-only.