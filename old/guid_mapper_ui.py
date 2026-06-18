import json
import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

from monsterStatBlock import MonsterStatBlock
from generateCombatExtenderBlocks import CombatExtenderBlockGenerator
from alterStatistics import alterStatistics

BASE_DIR = os.path.dirname(__file__)
DEFAULT_INPUT = os.path.join(BASE_DIR, "guid_mapper_input.json")
DEFAULT_CLONES_OUTPUT = os.path.join(BASE_DIR, "clonesAndOverrides", "combat_extender_clones.json")
DEFAULT_OVERRIDES_OUTPUT = os.path.join(BASE_DIR, "clonesAndOverrides", "combat_extender_overrides.json")


class GuidMapperUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("GUID Mapper UI")
        self.geometry("1280x760")
        self.blocks = []
        self.current_file = None
        self.selected_index = None

        self.create_widgets()
        self.load_input(DEFAULT_INPUT)

    def create_widgets(self):
        file_frame = ttk.Frame(self)
        file_frame.pack(fill="x", pady=6, padx=6)

        ttk.Label(file_frame, text="Input file:").pack(side="left")
        self.file_entry = ttk.Entry(file_frame, width=70)
        self.file_entry.pack(side="left", padx=6, fill="x", expand=True)
        ttk.Button(file_frame, text="Browse…", command=self.browse_input).pack(side="left", padx=4)
        ttk.Button(file_frame, text="Reload", command=self.reload_input).pack(side="left", padx=4)
        ttk.Button(file_frame, text="Save", command=self.save_input).pack(side="left", padx=4)
        ttk.Button(file_frame, text="Save As…", command=self.save_input_as).pack(side="left", padx=4)

        main_pane = ttk.PanedWindow(self, orient="horizontal")
        main_pane.pack(fill="both", expand=True, padx=6, pady=6)

        left_frame = ttk.Frame(main_pane)
        right_frame = ttk.Frame(main_pane)
        main_pane.add(left_frame, weight=3)
        main_pane.add(right_frame, weight=2)

        self.create_treeview(left_frame)
        self.create_detail_panel(right_frame)
        self.create_bulk_panel(right_frame)
        self.create_generate_panel(right_frame)

    def create_treeview(self, parent):
        columns = ["FullGuid", "Handle", "Act", "Location", "Type", "ClassArchetype", "MonsterArchetype", "HealthOverride"]
        self.tree = ttk.Treeview(parent, columns=columns, show="headings", selectmode="browse")
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=140, anchor="w")
        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)

        vsb = ttk.Scrollbar(parent, orient="vertical", command=self.tree.yview)
        hsb = ttk.Scrollbar(parent, orient="horizontal", command=self.tree.xview)
        self.tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

        self.tree.pack(fill="both", expand=True, side="top")
        vsb.pack(side="right", fill="y")
        hsb.pack(side="bottom", fill="x")

    def create_detail_panel(self, parent):
        detail_frame = ttk.LabelFrame(parent, text="Selected GUID Entry")
        detail_frame.pack(fill="both", expand=False, padx=6, pady=6)

        self.detail_fields = {}
        labels = ["FullGuid", "Handle", "Act", "Location", "Type", "SubType", "ClassArchetype", "MonsterArchetype", "HealthOverride", "PassivesToAdd", "SpellsToAdd", "CloneTemplateGuid", "CloneDisplayName", "Notes"]
        for idx, label in enumerate(labels):
            ttk.Label(detail_frame, text=label + ":").grid(row=idx, column=0, sticky="nw", padx=4, pady=2)
            entry = tk.Text(detail_frame, height=1 if label not in ["PassivesToAdd", "SpellsToAdd", "Notes"] else 3, width=44)
            entry.grid(row=idx, column=1, sticky="ew", padx=4, pady=2)
            detail_frame.grid_columnconfigure(1, weight=1)
            self.detail_fields[label] = entry

        ttk.Button(detail_frame, text="Apply changes", command=self.apply_detail_changes).grid(row=len(labels), column=0, columnspan=2, pady=6)

    def create_bulk_panel(self, parent):
        bulk_frame = ttk.LabelFrame(parent, text="Bulk actions")
        bulk_frame.pack(fill="x", padx=6, pady=6)

        ttk.Label(bulk_frame, text="Match text:").grid(row=0, column=0, sticky="w", padx=4, pady=2)
        self.bulk_match = ttk.Entry(bulk_frame, width=30)
        self.bulk_match.grid(row=0, column=1, sticky="w", padx=4, pady=2)

        ttk.Label(bulk_frame, text="Match type:").grid(row=1, column=0, sticky="w", padx=4, pady=2)
        self.match_type = ttk.Combobox(bulk_frame, values=["FullGuid", "Handle", "ClassArchetype", "MonsterArchetype"], state="readonly")
        self.match_type.current(0)
        self.match_type.grid(row=1, column=1, sticky="w", padx=4, pady=2)

        ttk.Label(bulk_frame, text="Health override:").grid(row=2, column=0, sticky="w", padx=4, pady=2)
        self.bulk_health = ttk.Entry(bulk_frame, width=30)
        self.bulk_health.grid(row=2, column=1, sticky="w", padx=4, pady=2)

        ttk.Label(bulk_frame, text="Location:").grid(row=3, column=0, sticky="w", padx=4, pady=2)
        self.bulk_location = ttk.Entry(bulk_frame, width=30)
        self.bulk_location.grid(row=3, column=1, sticky="w", padx=4, pady=2)

        ttk.Label(bulk_frame, text="Passives to add (comma-separated):").grid(row=4, column=0, sticky="w", padx=4, pady=2)
        self.bulk_passives = ttk.Entry(bulk_frame, width=30)
        self.bulk_passives.grid(row=4, column=1, sticky="w", padx=4, pady=2)

        ttk.Label(bulk_frame, text="Spells to add (comma-separated):").grid(row=5, column=0, sticky="w", padx=4, pady=2)
        self.bulk_spells = ttk.Entry(bulk_frame, width=30)
        self.bulk_spells.grid(row=5, column=1, sticky="w", padx=4, pady=2)

        ttk.Button(bulk_frame, text="Apply bulk update", command=self.apply_bulk_update).grid(row=6, column=0, columnspan=2, pady=8)

    def create_generate_panel(self, parent):
        gen_frame = ttk.LabelFrame(parent, text="Generate output")
        gen_frame.pack(fill="x", padx=6, pady=6)

        self.generate_output_label = ttk.Label(gen_frame, text="Output folder: clonesAndOverrides/")
        self.generate_output_label.pack(anchor="w", padx=4, pady=4)
        ttk.Button(gen_frame, text="Generate CombatExtender JSON", command=self.generate_combat_extender_json).pack(padx=4, pady=4)
        ttk.Button(gen_frame, text="Export current JSON", command=self.export_current_json).pack(padx=4, pady=4)

    def browse_input(self):
        path = filedialog.askopenfilename(title="Select guid_mapper input JSON", filetypes=[("JSON files", "*.json")])
        if path:
            self.load_input(path)

    def reload_input(self):
        if self.current_file:
            self.load_input(self.current_file)

    def load_input(self, path):
        try:
            blocks = MonsterStatBlock.load_from_json_file(path)
        except Exception as exc:
            messagebox.showerror("Load failed", f"Could not load file:\n{exc}")
            return

        self.blocks = blocks
        self.current_file = path
        self.file_entry.delete(0, tk.END)
        self.file_entry.insert(0, path)
        self.refresh_tree()
        messagebox.showinfo("Loaded", f"Loaded {len(blocks)} GUID entries from {os.path.basename(path)}")

    def save_input(self):
        if not self.current_file:
            self.save_input_as()
            return
        self._save_to_path(self.current_file)

    def save_input_as(self):
        path = filedialog.asksaveasfilename(title="Save guid_mapper input as", defaultextension=".json", filetypes=[("JSON files", "*.json")])
        if path:
            self.current_file = path
            self.file_entry.delete(0, tk.END)
            self.file_entry.insert(0, path)
            self._save_to_path(path)

    def _save_to_path(self, path):
        try:
            MonsterStatBlock.save_to_json_file(self.blocks, path)
            messagebox.showinfo("Saved", f"Saved {len(self.blocks)} entries to {os.path.basename(path)}")
        except Exception as exc:
            messagebox.showerror("Save failed", f"Could not write file:\n{exc}")

    def refresh_tree(self):
        self.tree.delete(*self.tree.get_children())
        for idx, block in enumerate(self.blocks):
            row = [block.full_guid, block.handle, block.act, block.location, block.type, block.classArchetype, block.monsterArchetype, block.health_override or ""]
            self.tree.insert("", "end", iid=str(idx), values=row)

    def on_tree_select(self, event):
        selected = self.tree.selection()
        if not selected:
            return
        self.selected_index = int(selected[0])
        block = self.blocks[self.selected_index]
        self.detail_fields["FullGuid"].delete("1.0", tk.END)
        self.detail_fields["FullGuid"].insert(tk.END, block.full_guid or "")
        self.detail_fields["Handle"].delete("1.0", tk.END)
        self.detail_fields["Handle"].insert(tk.END, block.handle or "")
        self.detail_fields["Act"].delete("1.0", tk.END)
        self.detail_fields["Act"].insert(tk.END, block.act or "")
        self.detail_fields["Location"].delete("1.0", tk.END)
        self.detail_fields["Location"].insert(tk.END, block.location or "")
        self.detail_fields["Type"].delete("1.0", tk.END)
        self.detail_fields["Type"].insert(tk.END, block.type or "")
        self.detail_fields["SubType"].delete("1.0", tk.END)
        self.detail_fields["SubType"].insert(tk.END, block.subtype or "")
        self.detail_fields["ClassArchetype"].delete("1.0", tk.END)
        self.detail_fields["ClassArchetype"].insert(tk.END, block.classArchetype or "")
        self.detail_fields["MonsterArchetype"].delete("1.0", tk.END)
        self.detail_fields["MonsterArchetype"].insert(tk.END, block.monsterArchetype or "")
        self.detail_fields["HealthOverride"].delete("1.0", tk.END)
        self.detail_fields["HealthOverride"].insert(tk.END, str(block.health_override or ""))
        self.detail_fields["PassivesToAdd"].delete("1.0", tk.END)
        self.detail_fields["PassivesToAdd"].insert(tk.END, ", ".join(block.passives_to_add or []))
        self.detail_fields["SpellsToAdd"].delete("1.0", tk.END)
        self.detail_fields["SpellsToAdd"].insert(tk.END, ", ".join(block.spells_to_add or []))
        self.detail_fields["CloneTemplateGuid"].delete("1.0", tk.END)
        self.detail_fields["CloneTemplateGuid"].insert(tk.END, block.clone_template_guid or "")
        self.detail_fields["CloneDisplayName"].delete("1.0", tk.END)
        self.detail_fields["CloneDisplayName"].insert(tk.END, block.clone_display_name or "")
        self.detail_fields["Notes"].delete("1.0", tk.END)
        self.detail_fields["Notes"].insert(tk.END, block.notes or "")

    def apply_detail_changes(self):
        if self.selected_index is None:
            messagebox.showwarning("No selection", "Please select a GUID entry first.")
            return
        block = self.blocks[self.selected_index]
        block.handle = self.detail_fields["Handle"].get("1.0", tk.END).strip()
        block.act = self.detail_fields["Act"].get("1.0", tk.END).strip()
        block.location = self.detail_fields["Location"].get("1.0", tk.END).strip()
        block.type = self.detail_fields["Type"].get("1.0", tk.END).strip()
        block.subtype = self.detail_fields["SubType"].get("1.0", tk.END).strip()
        block.classArchetype = self.detail_fields["ClassArchetype"].get("1.0", tk.END).strip()
        block.monsterArchetype = self.detail_fields["MonsterArchetype"].get("1.0", tk.END).strip()
        health_text = self.detail_fields["HealthOverride"].get("1.0", tk.END).strip()
        block.health_override = int(health_text) if health_text.isdigit() else 0
        block.passives_to_add = [token.strip() for token in self.detail_fields["PassivesToAdd"].get("1.0", tk.END).split(",") if token.strip()]
        block.spells_to_add = [token.strip() for token in self.detail_fields["SpellsToAdd"].get("1.0", tk.END).split(",") if token.strip()]
        block.clone_template_guid = self.detail_fields["CloneTemplateGuid"].get("1.0", tk.END).strip()
        block.clone_display_name = self.detail_fields["CloneDisplayName"].get("1.0", tk.END).strip()
        block.notes = self.detail_fields["Notes"].get("1.0", tk.END).strip()
        self.refresh_tree()
        messagebox.showinfo("Updated", "Selected entry updated.")

    def apply_bulk_update(self):
        phrase = self.bulk_match.get().strip()
        if not phrase:
            messagebox.showwarning("Missing match text", "Enter a match phrase before running a bulk update.")
            return

        match_type = self.match_type.get()
        health_text = self.bulk_health.get().strip()
        location = self.bulk_location.get().strip()
        passives = [token.strip() for token in self.bulk_passives.get().split(",") if token.strip()]
        spells = [token.strip() for token in self.bulk_spells.get().split(",") if token.strip()]

        if health_text and not health_text.isdigit():
            messagebox.showerror("Invalid health", "Health override must be a whole number.")
            return
        health_value = int(health_text) if health_text else None

        if match_type == "FullGuid":
            if location:
                alterStatistics.add_location_by_guid(self.blocks, phrase, location)
            if health_value is not None:
                alterStatistics.set_health_override_by_full_guid(self.blocks, phrase, health_value)
            if passives or spells:
                alterStatistics.add_by_full_guid(self.blocks, phrase, passives_to_add=passives or None, spells_to_add=spells or None)
        elif match_type == "Handle":
            if location:
                messagebox.showwarning("Location not supported", "Location bulk update only works with FullGuid matching.")
            if health_value is not None:
                alterStatistics.set_health_override_by_handle(self.blocks, phrase, health_value)
            if passives or spells:
                alterStatistics.add_by_handle(self.blocks, phrase, passives_to_add=passives or None, spells_to_add=spells or None)
        elif match_type == "ClassArchetype":
            if health_value is not None:
                alterStatistics.set_health_override_by_class_archetype(self.blocks, phrase, health_value, exact_match=False)
            if passives or spells:
                alterStatistics.add_by_class_archetype(self.blocks, phrase, "", passives_to_add=passives or None, spells_to_add=spells or None)
        elif match_type == "MonsterArchetype":
            if health_value is not None:
                alterStatistics.set_health_override_by_monster_archetype(self.blocks, phrase, health_value, exact_match=False)
            if passives or spells:
                alterStatistics.add_by_class_archetype(self.blocks, "", phrase, passives_to_add=passives or None, spells_to_add=spells or None)

        self.refresh_tree()
        messagebox.showinfo("Bulk update", "Bulk update complete.")

    def generate_combat_extender_json(self):
        if not self.blocks:
            messagebox.showwarning("No data", "Load a guid_mapper input file before generating output.")
            return
        try:
            clean_blocks = MonsterStatBlock.deduplicate(self.blocks)
            clones = CombatExtenderBlockGenerator.generate_clones(clean_blocks)
            overrides = CombatExtenderBlockGenerator.generate_overrides(clean_blocks)
            os.makedirs(os.path.dirname(DEFAULT_CLONES_OUTPUT), exist_ok=True)
            CombatExtenderBlockGenerator.save_json({"Clones": clones}, DEFAULT_CLONES_OUTPUT)
            CombatExtenderBlockGenerator.save_json({"Overrides": overrides}, DEFAULT_OVERRIDES_OUTPUT)
            messagebox.showinfo("Generated", f"Saved output to:\n{DEFAULT_CLONES_OUTPUT}\n{DEFAULT_OVERRIDES_OUTPUT}")
        except Exception as exc:
            messagebox.showerror("Generation failed", f"Could not generate CombatExtender files:\n{exc}")

    def export_current_json(self):
        if not self.blocks:
            messagebox.showwarning("No data", "Load a guid_mapper input file before exporting.")
            return
        path = filedialog.asksaveasfilename(title="Export current JSON", defaultextension=".json", filetypes=[("JSON files", "*.json")])
        if path:
            self._save_to_path(path)


if __name__ == "__main__":
    os.chdir(BASE_DIR)
    app = GuidMapperUI()
    app.mainloop()
