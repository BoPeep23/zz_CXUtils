import json
import os

class MonsterStatBlock:
    def __init__(self, handle=None, full_guid=None, act=None, location=None, type_=None, sub_type=None,
                 classArchetype=None, monsterArchetype=None, profiles=None, armor_class=0, health_override=0,
                 original_health_override=0, passives_to_add=None, spells_to_add=None,
                 clone_template_guid=None, clone_display_name=None, corpse=None, notes=None):
        self._handle = handle
        self._full_guid = full_guid
        self._act = act
        self._location = location
        self._type = type_
        self._sub_type = sub_type
        self._classArchetype = classArchetype
        self._monsterArchetype = monsterArchetype
        self._profiles = profiles or []
        self._armor_class = armor_class
        self._health_override = health_override
        self._original_health_override = original_health_override
        self._passives_to_add = passives_to_add or []
        self._spells_to_add = spells_to_add or []
        self._clone_template_guid = clone_template_guid
        self._clone_display_name = clone_display_name
        self._corpse = corpse
        self._notes = notes

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
    def profiles(self):
        return self._profiles

    @profiles.setter
    def profiles(self, value):
        self._profiles = value

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
    def original_health_override(self):
        return self._original_health_override

    @original_health_override.setter
    def original_health_override(self, value):
        self._original_health_override = value

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
    def corpse(self):
        return self._corpse

    @corpse.setter
    def corpse(self, value):
        self._corpse = value

    @property
    def notes(self):
        return self._notes

    @notes.setter
    def notes(self, value):
        self._notes = value

    # ── Serialization ────────────────────────────────────────────────────────

    def to_dict(self):
        return {
            'Handle': self._handle,
            'FullGuid': self._full_guid,
            'Act': self._act,
            'Location': self._location,
            'Type': self._type,
            'SubType': self._sub_type,
            'ClassArchetype': self._classArchetype,
            'MonsterArchetype': self._monsterArchetype,
            'Profiles': self._profiles,
            'ArmorClass': self._armor_class,
            'HealthOverride': self._health_override,
            'OriginalHealthOverride': self._original_health_override,
            'PassivesToAdd': self._passives_to_add,
            'SpellsToAdd': self._spells_to_add,
            'CloneTemplateGuid': self._clone_template_guid,
            'CloneDisplayName': self._clone_display_name,
            'Corpse': self._corpse,
            'Notes': self._notes,
        }

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
            profiles=_or_default('Profiles', []),
            armor_class=_or_default('ArmorClass', 0),
            health_override=_or_default('HealthOverride', 0),
            original_health_override=_or_default('OriginalHealthOverride', 0),
            passives_to_add=_or_default('PassivesToAdd', []),
            spells_to_add=_or_default('SpellsToAdd', []),
            clone_template_guid=_or_default('CloneTemplateGuid', ""),
            clone_display_name=_or_default('CloneDisplayName', ""),
            corpse=_or_default('Corpse', False),
            notes=_or_default('Notes', "")
        )
        known_fields = {
            'Handle', 'FullGuid', 'Act', 'Location', 'Type', 'SubType',
            'ClassArchetype', 'MonsterArchetype', 'Profiles',
            'ArmorClass', 'HealthOverride', 'OriginalHealthOverride',
            'CloneTemplateGuid', 'CloneDisplayName',
            'SpellsToAdd', 'PassivesToAdd', 'Notes', 'Corpse',
        }
        for key, value in data.items():
            if key not in known_fields:
                setattr(instance, key, value)
        return instance

    @classmethod
    def load_from_json_file(cls, file_path):
        with open(file_path, 'r') as f:
            data = json.load(f)
        return [cls.from_dict(entry) for entry in data.get('Guids', [])]

    @classmethod
    def save_to_json_file(cls, blocks, file_path):
        data = {'Guids': [block.to_dict() for block in blocks]}
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
                # OriginalHealthOverride: keep whichever is non-zero (immutable once set).
                if (not existing.original_health_override) and block.original_health_override:
                    existing.original_health_override = block.original_health_override
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
                if (existing.profiles is None or len(existing.profiles) == 0) and block.profiles:
                    existing.profiles = block.profiles
                if existing.notes and block.notes:
                    existing.notes += "; " + block.notes
                elif _should_replace(existing.notes, block.notes):
                    existing.notes = block.notes
        return list(deduped.values())