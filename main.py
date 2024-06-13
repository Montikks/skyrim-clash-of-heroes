import tkinter as tk
from tkinter import ttk
from bojovnici import Sermir, Lukostrelec, Mag, Boss, Tank, Healer, Berserker, Assassin, Bojovnik
from arena import Arena
from tower import Tower
import json
import os

class Aplikace:
    def __init__(self, root):
        self.root = root
        self.root.title("Skyrim: Clash of Heroes")

        self.main_frame = tk.Frame(root)
        self.main_frame.pack()

        self.typ_arena = tk.StringVar()
        self.typ_arena.set("Les")
        self.bojovnici = []
        self.boss = None
        self.bojovnik_typy = [("Sermir", Sermir), ("Lukostrelec", Lukostrelec), ("Mag", Mag),
                              ("Tank", Tank), ("Healer", Healer), ("Berserker", Berserker), ("Assassin", Assassin)]

        self.nadpis = tk.Label(self.main_frame, text="Vyberte herní režim:")
        self.nadpis.pack()

        self.arena_button = tk.Button(self.main_frame, text="Arena", command=self.vyber_arena)
        self.arena_button.pack()

        self.tower_button = tk.Button(self.main_frame, text="Tower", command=self.vyber_tower)
        self.tower_button.pack()

        self.save_button = tk.Button(self.main_frame, text="Uložit hru", command=self.ulozit_hru)
        self.save_button.pack()

        self.load_button = tk.Button(self.main_frame, text="Načíst hru", command=self.nacist_hru)
        self.load_button.pack()

        self.text_area = tk.Text(self.main_frame)
        self.text_area.pack()

        self.indikatory_frame = tk.Frame(root)
        self.indikatory_frame.pack()

        self.obtiznost_var = tk.StringVar(value="Střední")
        self.specialni_utok_button = tk.Button(self.main_frame, text="Speciální útok", command=self.spec_utok)
        self.specialni_utok_button.pack()

    def format_text(self, text, tag):
        self.text_area.insert(tk.END, text + "\n")
        self.text_area.tag_add(tag, "end-2l", "end-1l")
        if tag == "utok":
            self.text_area.tag_config(tag, foreground="red")
        elif tag == "specialni":
            self.text_area.tag_config(tag, foreground="blue")
        elif tag == "zprava":
            self.text_area.tag_config(tag, foreground="green")
        elif tag == "chyba":
            self.text_area.tag_config(tag, foreground="orange")

    def vyber_arena(self):
        self.okno_vyber = tk.Toplevel(self.root)
        self.okno_vyber.title("Vyberte bojovníky a arénu")

        tk.Label(self.okno_vyber, text="Vyberte tři bojovníky:").pack()

        self.bojovnici_vars = []
        for typ, _ in self.bojovnik_typy:
            var = tk.StringVar(value=typ)
            chk = tk.Checkbutton(self.okno_vyber, text=typ, variable=var, onvalue=typ, offvalue="")
            chk.pack()
            self.bojovnici_vars.append(var)

        tk.Label(self.okno_vyber, text="Vyberte typ arény:").pack()
        self.arena_typy = ["Les", "Hory", "Jeskyne"]
        self.arena_var = tk.StringVar(value=self.arena_typy[0])
        for typ in self.arena_typy:
            tk.Radiobutton(self.okno_vyber, text=typ, variable=self.arena_var, value=typ).pack()

        tk.Label(self.okno_vyber, text="Vyberte obtížnost:").pack()
        self.obtiznosti = ["Lehká", "Střední", "Těžká"]
        for obtiznost in self.obtiznosti:
            tk.Radiobutton(self.okno_vyber, text=obtiznost, variable=self.obtiznost_var, value=obtiznost).pack()

        self.potvrdit_button = tk.Button(self.okno_vyber, text="Potvrdit", command=self.potvrdit_arena)
        self.potvrdit_button.pack()

    def potvrdit_arena(self):
        for var in self.bojovnici_vars:
            typ = var.get()
            for jmeno, cls in self.bojovnik_typy:
                if typ == jmeno:
                    self.bojovnici.append(cls(jmeno))
        self.typ_arena.set(self.arena_var.get())
        self.boss = Boss("Alduin")
        self.okno_vyber.destroy()
        self.zacni_hru()

    def vyber_tower(self):
        self.okno_vyber_tower = tk.Toplevel(self.root)
        self.okno_vyber_tower.title("Vyberte bojovníky pro Tower Defense")

        tk.Label(self.okno_vyber_tower, text="Vyberte tři bojovníky:").pack()

        self.bojovnici_vars_tower = []
        for typ, _ in self.bojovnik_typy:
            var = tk.StringVar(value=typ)
            chk = tk.Checkbutton(self.okno_vyber_tower, text=typ, variable=var, onvalue=typ, offvalue="")
            chk.pack()
            self.bojovnici_vars_tower.append(var)

        self.potvrdit_button_tower = tk.Button(self.okno_vyber_tower, text="Potvrdit", command=self.potvrdit_vyber_tower)
        self.potvrdit_button_tower.pack()

    def potvrdit_vyber_tower(self):
        for var in self.bojovnici_vars_tower:
            typ = var.get()
            for jmeno, cls in self.bojovnik_typy:
                if typ == jmeno:
                    self.bojovnici.append(cls(jmeno))
        self.okno_vyber_tower.destroy()
        self.start_tower()

    def zacni_hru(self):
        self.arena = Arena(self.typ_arena.get(), self.bojovnici, self.boss, self.text_area, self.root)
        self.arena.zacni_boj()
        self.aktualizovat_indikatory()

    def start_tower(self):
        self.tower = Tower(self.bojovnici, self.text_area)
        self.tower.set_obtiznost(self.obtiznost_var.get())
        self.tower.start()
        self.aktualizovat_indikatory()

    def ulozit_hru(self):
        data = {
            "bojovnici": [bojovnik.to_dict() for bojovnik in self.bojovnici],
            "boss": self.boss.to_dict() if self.boss else None,
            "arena_typ": self.typ_arena.get(),
            "tower_level": self.tower.level if self.tower else None,
            "tower_obtiznost": self.tower.obtiznost if self.tower else None
        }
        with open("ulozena_hra.json", "w") as f:
            json.dump(data, f)
        self.format_text("Hra byla uložena.", "zprava")

    def nacist_hru(self):
        if os.path.exists("ulozena_hra.json"):
            with open("ulozena_hra.json", "r") as f:
                data = json.load(f)
            self.bojovnici = [Bojovnik.from_dict(b) for b in data["bojovnici"]]
            self.boss = Boss.from_dict(data["boss"]) if data["boss"] else None
            self.typ_arena.set(data["arena_typ"])
            if data.get("tower_level"):
                self.tower = Tower.from_dict(data, self.text_area)
                self.format_text(f"Načtena Tower Defense hra na úrovni {self.tower.level} s obtížností {self.tower.obtiznost}.", "zprava")
            else:
                self.zacni_hru()
        else:
            self.format_text("Žádná uložená hra nebyla nalezena.", "chyba")

    def aktualizovat_indikatory(self):
        for widget in self.indikatory_frame.winfo_children():
            widget.destroy()

        for bojovnik in self.bojovnici:
            tk.Label(self.indikatory_frame, text=f"{bojovnik.jmeno}: {bojovnik._zivot} HP, Level: {bojovnik._level}, XP: {bojovnik._xp}/100").pack()
        if self.boss:
            tk.Label(self.indikatory_frame, text=f"{self.boss.jmeno}: {self.boss._zivot} HP").pack()

    def spec_utok(self):
        if self.bojovnici and self.boss:
            for bojovnik in self.bojovnici:
                if bojovnik._zivot > 0:
                    vysledek, barva = bojovnik.specialni_utok(self.boss)
                    self.format_text(vysledek, "specialni")
                    self.aktualizovat_zdravotni_stav()
                    if self.boss._zivot <= 0:
                        self.format_text(f"{self.boss.jmeno} byl poražen!", "zprava")
                        break
                    vysledek, barva = self.boss.utok(bojovnik)
                    self.format_text(vysledek, "utok")
                    self.aktualizovat_zdravotni_stav()
                    if bojovnik._zivot <= 0:
                        self.format_text(f"{bojovnik.jmeno} byl poražen!", "chyba")
                        break
        else:
            self.format_text("Nejsou k dispozici žádní bojovníci nebo boss!", "chyba")

if __name__ == "__main__":
    root = tk.Tk()
    app = Aplikace(root)
    root.mainloop()
