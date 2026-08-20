import json
import os
import shutil
from datetime import datetime

class MonsterStatBlock:
    # Fields that are never relevant for a Corpse=True block (static scenery,
    # not a fighter). sanitizeFields strips these to blank/zero on every run;
    # discoverFields.apply_handle_map never writes them onto a corpse block,
    # even if a matched entry's ApplyStats/randomization includes them.
    CORPSE_EXCLUDED_FIELDS = {
        'ClassArchetype', 'ArmorClass', 'HealthOverride', 'OriginalHealth',
        'Level', 'PassivesToAdd', 'SpellsToAdd', 'MapApplied', 'RandomizationApplied',
    }

    def __init__(self, handle=None, full_guid=None, act=None, location=None, type_=None, sub_type=None,
                 classArchetype=None, monsterArchetype=None, armor_class=0, health_override=0,
                 original_health=0, level=0, passives_to_add=None, spells_to_add=None,
                 clone_template_guid=None, clone_display_name=None, notes=None, corpse=None,
                 map_applied=None, randomization_applied=None, lock_block=None):
        self._handle = handle
        self._full_guid = full_guid
        self._act = act
        self._location = location
        self._type = type_
        self._sub_type = sub_type
        self._classArchetype = classArchetype
        self._monsterArchetype = monsterArchetype
        self._armor_class = armor_class
        self._health_override = health_override
        self._original_health = original_health
        self._level = level
        self._passives_to_add = passives_to_add or []
        self._spells_to_add = spells_to_add or []
        self._clone_template_guid = clone_template_guid
        self._clone_display_name = clone_display_name
        self._notes = notes
        self._corpse = corpse
        self._map_applied = map_applied
        self._randomization_applied = randomization_applied
        self._lock_block = lock_block

    # ── Properties ──────────────────────────────────────────────────────────

    @property
    def handle(self):
        return self._handle

    @handle.setter
    def handle(self, value):
        self._handle = value

    @property
    def full_guid(self):
        return self._full_guid

    @full_guid.setter
    def full_guid(self, value):
        self._full_guid = value

    @property
    def act(self):
        return self._act

    @act.setter
    def act(self, value):
        self._act = value

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, value):
        self._location = value

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value

    @property
    def subtype(self):
        return self._sub_type

    @subtype.setter
    def subtype(self, value):
        self._sub_type = value

    @property
    def classArchetype(self):
        return self._classArchetype

    @classArchetype.setter
    def classArchetype(self, value):
        self._classArchetype = value

    @property
    def monsterArchetype(self):
        return self._monsterArchetype

    @monsterArchetype.setter
    def monsterArchetype(self, value):
        self._monsterArchetype = value

    @property
    def armor_class(self):
        return self._armor_class

    @armor_class.setter
    def armor_class(self, value):
        self._armor_class = value

    @property
    def health_override(self):
        return self._health_override

    @health_override.setter
    def health_override(self, value):
        self._health_override = value

    @property
    def original_health(self):
        return self._original_health

    @original_health.setter
    def original_health(self, value):
        self._original_health = value

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        self._level = value

    @property
    def passives_to_add(self):
        return self._passives_to_add

    @passives_to_add.setter
    def passives_to_add(self, value):
        self._passives_to_add = value

    @property
    def spells_to_add(self):
        return self._spells_to_add

    @spells_to_add.setter
    def spells_to_add(self, value):
        self._spells_to_add = value

    @property
    def clone_template_guid(self):
        return self._clone_template_guid

    @clone_template_guid.setter
    def clone_template_guid(self, value):
        self._clone_template_guid = value

    @property
    def clone_display_name(self):
        return self._clone_display_name

    @clone_display_name.setter
    def clone_display_name(self, value):
        self._clone_display_name = value

    @property
    def notes(self):
        return self._notes

    @notes.setter
    def notes(self, value):
        self._notes = value

    @property
    def corpse(self):
        return self._corpse

    @corpse.setter
    def corpse(self, value):
        self._corpse = value

    @property
    def map_applied(self):
        return self._map_applied

    @map_applied.setter
    def map_applied(self, value):
        self._map_applied = value

    @property
    def randomization_applied(self):
        return self._randomization_applied

    @randomization_applied.setter
    def randomization_applied(self, value):
        self._randomization_applied = value

    @property
    def lock_block(self):
        return self._lock_block

    @lock_block.setter
    def lock_block(self, value):
        self._lock_block = value

    # ── Serialization ────────────────────────────────────────────────────────

    def to_dict(self, for_json=False):
        """for_json=False (default) always includes every field - used for
        snapshot()/diff_from_snapshot() so diffs can still detect a field
        changing even when the block is/becomes a corpse. for_json=True is
        for actual file output: on a Corpse=True block it omits
        CORPSE_EXCLUDED_FIELDS entirely instead of writing them as blank/zero,
        since those fields are never meaningful for static scenery."""
        d = {
            'Handle': self._handle,
            'FullGuid': self._full_guid,
            'Act': self._act,
            'Location': self._location,
            'Type': self._type,
            'SubType': self._sub_type,
            'ClassArchetype': self._classArchetype,
            'MonsterArchetype': self._monsterArchetype,
            'ArmorClass': self._armor_class,
            'HealthOverride': self._health_override,
            'OriginalHealth': self._original_health,
            'Level': self._level,
            'PassivesToAdd': self._passives_to_add,
            'SpellsToAdd': self._spells_to_add,
            'CloneTemplateGuid': self._clone_template_guid,
            'CloneDisplayName': self._clone_display_name,
            'Notes': self._notes,
            'Corpse': self._corpse,
            'MapApplied': self._map_applied,
            'RandomizationApplied': self._randomization_applied,
            'LockBlock': self._lock_block,
        }
        if for_json and self._corpse:
            for field in self.CORPSE_EXCLUDED_FIELDS:
                d.pop(field, None)
        return d

    @classmethod
    def from_dict(cls, data):
        full_guid = data.get('FullGuid')
        if not full_guid and 'Name' in data and 'Guid' in data:
            full_guid = f"{data['Name']}_{data['Guid']}"

        def _or_default(key, default):
            value = data.get(key, default)
            return default if value is None else value

        instance = cls(
            handle=_or_default('Handle', ""),
            full_guid=full_guid,
            act=_or_default('Act', ""),
            location=_or_default('Location', ""),
            type_=_or_default('Type', ""),
            sub_type=_or_default('SubType', ""),
            classArchetype=_or_default('ClassArchetype', ""),
            monsterArchetype=_or_default('MonsterArchetype', ""),
            armor_class=_or_default('ArmorClass', 0),
            health_override=_or_default('HealthOverride', 0),
            original_health=_or_default('OriginalHealth', 0),
            level=_or_default('Level', 0),
            passives_to_add=_or_default('PassivesToAdd', []),
            spells_to_add=_or_default('SpellsToAdd', []),
            clone_template_guid=_or_default('CloneTemplateGuid', ""),
            clone_display_name=_or_default('CloneDisplayName', ""),
            notes=_or_default('Notes', ""),
            corpse=_or_default('Corpse', False),
            map_applied=_or_default('MapApplied', False),
            randomization_applied=_or_default('RandomizationApplied', False),
            lock_block=_or_default('LockBlock', False),
        )
        known_fields = {
            'Handle', 'FullGuid', 'Act', 'Location', 'Type', 'SubType',
            'ClassArchetype', 'MonsterArchetype',
            'ArmorClass', 'HealthOverride', 'OriginalHealth', 'Level',
            'CloneTemplateGuid', 'CloneDisplayName',
            'SpellsToAdd', 'PassivesToAdd', 'Notes', 'Corpse',
            'MapApplied', 'LockBlock', 'RandomizationApplied',
        }
        for key, value in data.items():
            if key not in known_fields:
                setattr(instance, key, value)
        return instance

    @staticmethod
    def act_key(act):
        """Map an Act value to its top-level JSON key: numeric Acts become
        'Act1'/'Act2'/etc., blank Acts fold into 'Unknown', and any other
        string (e.g. 'Global', 'Camp') is used as-is."""
        a = (act or "").strip()
        if not a:
            return "Unknown"
        if a.isdigit():
            return f"Act{a}"
        return a

    @classmethod
    def load_from_json_file(cls, file_path):
        with open(file_path, 'r') as f:
            data = json.load(f)
        if 'Guids' in data:
            # Legacy single-list format.
            entries = data.get('Guids', [])
        else:
            entries = [entry for group in data.values() for entry in group]
        return [cls.from_dict(entry) for entry in entries]

    @classmethod
    def save_to_json_file(cls, blocks, file_path, archive=True):
        """Writes blocks to file_path. When archive=True (default) and file_path
        already exists, the pre-overwrite contents are copied into an archive/
        folder alongside file_path first, timestamped, as a rollback point."""
        if archive and os.path.exists(file_path):
            archive_dir = os.path.join(os.path.dirname(file_path), "archive")
            os.makedirs(archive_dir, exist_ok=True)
            stem, ext = os.path.splitext(os.path.basename(file_path))
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            shutil.copy2(file_path, os.path.join(archive_dir, f"{stem}_{timestamp}{ext}"))

        grouped = {}
        for block in blocks:
            grouped.setdefault(cls.act_key(block.act), []).append(block)

        def _sort_key(key):
            if key.startswith('Act') and key[3:].isdigit():
                return (0, int(key[3:]), key)
            return (1, 0, key)

        data = {
            key: [block.to_dict(for_json=True) for block in grouped[key]]
            for key in sorted(grouped, key=_sort_key)
        }
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=4)

    @classmethod
    def populate_full_guid(blocks):
        for block in blocks:
            if not block.full_guid and hasattr(block, 'Name') and hasattr(block, 'Guid'):
                block.full_guid = f"{getattr(block, 'Name')}_{getattr(block, 'Guid')}"

    @staticmethod
    def deduplicate(blocks):
        def _is_blank_string(value):
            return isinstance(value, str) and value.strip() == ""

        def _should_replace(existing_value, incoming_value):
            if incoming_value is None:
                return False
            if isinstance(incoming_value, str):
                return (existing_value is None or _is_blank_string(existing_value)) and not _is_blank_string(incoming_value)
            return existing_value is None

        deduped = {}
        for block in blocks:
            key = block.full_guid
            if key not in deduped:
                deduped[key] = block
            else:
                existing = deduped[key]
                existing.spells_to_add = sorted(set(existing.spells_to_add + block.spells_to_add))
                existing.passives_to_add = sorted(set(existing.passives_to_add + block.passives_to_add))
                if _should_replace(existing.handle, block.handle):
                    existing.handle = block.handle
                if _should_replace(existing.act, block.act):
                    existing.act = block.act
                if _should_replace(existing.location, block.location):
                    existing.location = block.location
                if _should_replace(existing.type, block.type):
                    existing.type = block.type
                if _should_replace(existing.health_override, block.health_override):
                    existing.health_override = block.health_override
                # OriginalHealth: keep whichever is non-zero (immutable once set).
                if (not existing.original_health) and block.original_health:
                    existing.original_health = block.original_health
                if _should_replace(existing.clone_template_guid, block.clone_template_guid):
                    existing.clone_template_guid = block.clone_template_guid
                if _should_replace(existing.clone_display_name, block.clone_display_name):
                    existing.clone_display_name = block.clone_display_name
                if _should_replace(existing.corpse, block.corpse):
                    existing.corpse = block.corpse
                if _should_replace(existing.classArchetype, block.classArchetype):
                    existing._classArchetype = block._classArchetype
                if _should_replace(existing.monsterArchetype, block.monsterArchetype):
                    existing.monsterArchetype = block.monsterArchetype
                if _should_replace(existing.subtype, block.subtype):
                    existing.subtype = block.subtype
                if existing.notes and block.notes:
                    existing.notes += "; " + block.notes
                elif _should_replace(existing.notes, block.notes):
                    existing.notes = block.notes
                existing.map_applied = existing.map_applied or block.map_applied
                existing.lock_block = existing.lock_block or block.lock_block
                existing.randomization_applied = existing.randomization_applied or block.randomization_applied
        return list(deduped.values())

    @staticmethod
    def snapshot(blocks):
        """Captures each block's current field values, keyed by FullGuid, for
        later comparison via diff_from_snapshot() once the blocks have been
        mutated in place."""
        return {block.full_guid: block.to_dict() for block in blocks}

    @staticmethod
    def diff_from_snapshot(before_snapshot, blocks):
        """Compares each block's current field values against a prior
        snapshot(). Returns {FullGuid: {field: (old_value, new_value)}},
        including only blocks/fields that actually changed."""
        diffs = {}
        for block in blocks:
            old = before_snapshot.get(block.full_guid, {})
            new = block.to_dict()
            changed = {k: (old.get(k), v) for k, v in new.items() if old.get(k) != v}
            if changed:
                diffs[block.full_guid] = changed
        return diffs

    @staticmethod
    def confirm_large_change(diffs, blocks, threshold=0.25, target_description="guid_mapper_master.json"):
        """If diffs touch more than `threshold` fraction of blocks, prompts the
        user to confirm before proceeding. Returns True if it's OK to proceed
        (either the change is under threshold, or the user confirmed it)."""
        if not blocks:
            return True
        changed_fraction = len(diffs) / len(blocks)
        if changed_fraction <= threshold:
            return True
        pct = changed_fraction * 100
        answer = input(
            f"This run would change {len(diffs)} of {len(blocks)} blocks "
            f"({pct:.1f}%) in {target_description}. Continue? [y/N]: "
        )
        return answer.strip().lower() in ("y", "yes")