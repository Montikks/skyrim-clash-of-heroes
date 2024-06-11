import tkinter as tk
from tkinter import messagebox, ttk
import json
import os
from bojovnici import Sermir, Lukostrelec, Mag, Boss, Tank, Healer, Berserker
from arena import Arena
from items import HealthPotion, DamageBoost, DefenseBoost
import pygame

# Inicializace pygame
pygame.mixer.init()

# Načtení zvuků
zvuk_utok = pygame.mixer.Sound("sounds/utok.wav")
zvuk_vitezstvi = pygame.mixer.Sound("sounds/vitezstvi.wav")
zvuk_porazka = pygame.mixer.Sound("sounds/porazka.wav")

# Nastavení hlasitosti
zvuk_utok.set_volume(0.2)
zvuk_vitezstvi.set_volume(0.2)
zvuk_porazka.set_volume(0.2)


class Aplikace:
    def __init__(self, master):
        self.master = master
        master.title("Skyrim: Clash of Heroes")

        self.label = ttk.Label(master, text="Vítejte v Skyrim: Clash of Heroes!")
        self.label.pack()

        self.vyber_bojovniky_button = ttk.Button(master, text="Vyber bojovníky", command=self.vyber_bojovniky)
        self.vyber_bojovniky_button.pack()

        self.skoncit_button = ttk.Button(master, text="Konec", command=master.quit)
        self.skoncit_button.pack()

        self.zobrazit_skore_button = ttk.Button(master, text="Zobrazit skóre", command=self.zobrazit_skore)
        self.zobrazit_skore_button.pack()

        self.ulozit_hru_button = ttk.Button(master, text="Uložit hru", command=self.ulozit_hru)
        self.ulozit_hru_button.pack()

        self.nacist_hru_button = ttk.Button(master, text="Načíst hru", command=self.nacist_hru)
        self.nacist_hru_button.pack()

        self.bojovnici = []
        self.boss = Boss("Alduin")
        self.arena_typ = tk.StringVar()
        self.arena = None

        self.skore_soubor = "skore.json"
        self.hra_soubor = "hra.json"
        self.nacist_skore()

        self.text_area = tk.Text(master, height=15, width=50)
        self.text_area.pack()

        self.indikatory_frame = ttk.Frame(master)
        self.indikatory_frame.pack()

        # Textové pole pro zobrazování zpráv
        self.message_label = ttk.Label(master, text="")
        self.message_label.pack()

        # Panel pro výběr a použití předmětů
        self.items = [HealthPotion(), DamageBoost(), DefenseBoost()]

        self.item_frame = ttk.Frame(master)
        self.item_frame.pack()

        self.item_label = ttk.Label(self.item_frame, text="Vyberte předmět:")
        self.item_label.pack(side=tk.LEFT)

        self.item_var = tk.StringVar()
        self.item_menu = ttk.OptionMenu(self.item_frame, self.item_var, *[item.name for item in self.items])
        self.item_menu.pack(side=tk.LEFT)

        self.bojovnik_var = tk.StringVar()
        self.bojovnik_menu = ttk.OptionMenu(self.item_frame, self.bojovnik_var, "")
        self.bojovnik_menu.pack(side=tk.LEFT)

        self.use_item_button = ttk.Button(self.item_frame, text="Použít předmět", command=self.pouzit_predmet)
        self.use_item_button.pack(side=tk.LEFT)

    def pouzit_predmet(self):
        if not self.arena:
            self.zobrazit_zpravu("Hra ještě nezačala!", True)
            return

        if not self.bojovnici:
            self.zobrazit_zpravu("Nejsou vybráni žádní bojovníci!", True)
            return

        selected_item_name = self.item_var.get()
        selected_item = next(item for item in self.items if item.name == selected_item_name)
        selected_bojovnik_name = self.bojovnik_var.get()
        selected_bojovnik = next(bojovnik for bojovnik in self.bojovnici if bojovnik.jmeno == selected_bojovnik_name)
        self.arena.use_item(selected_bojovnik, selected_item)
        self.aktualizovat_zdravotni_stav()  # Aktualizace zdravotního stavu po použití předmětu

    def nacist_skore(self):
        if os.path.exists(self.skore_soubor):
            with open(self.skore_soubor, "r") as soubor:
                self.skore = json.load(soubor)
        else:
            self.skore = []

    def ulozit_skore(self):
        with open(self.skore_soubor, "w") as soubor:
            json.dump(self.skore, soubor)

    def aktualizovat_skore(self, skore):
        self.skore.append(skore)
        self.skore = sorted(self.skore, key=lambda x: x["body"], reverse=True)[:10]
        self.ulozit_skore()

    def zobrazit_skore(self):
        skore_okno = tk.Toplevel(self.master)
        skore_okno.title("Skóre")

        tk.Label(skore_okno, text="Top 10 skóre").pack()
        for zaznam in self.skore:
            tk.Label(skore_okno, text=f"{zaznam['jmeno']}: {zaznam['body']} bodů").pack()

    def ulozit_hru(self):
        if hasattr(self, 'arena'):
            data = {
                "arena": self.arena.to_dict(),
                "bojovnici": [bojovnik.to_dict() for bojovnik in self.bojovnici],
                "boss": self.boss.to_dict()
            }
            with open(self.hra_soubor, "w") as soubor:
                json.dump(data, soubor)
            self.zobrazit_zpravu("Hra byla úspěšně uložena!")
        else:
            self.zobrazit_zpravu("Není žádná hra k uložení!", True)

    def nacist_hru(self):
        if os.path.exists(self.hra_soubor):
            with open(self.hra_soubor, "r") as soubor:
                data = json.load(soubor)
                self.arena = Arena.from_dict(data["arena"])
                self.bojovnici = [Bojovnik.from_dict(b) for b in data["bojovnici"]]
                self.boss = Boss.from_dict(data["boss"])
                self.zacni_hru(True)
        else:
            self.zobrazit_zpravu("Není žádná uložená hra k načtení!", True)

    def zobrazit_zpravu(self, zprava, chyba=False):
        self.message_label.config(text=zprava)
        if chyba:
            self.message_label.config(foreground="red")
        else:
            self.message_label.config(foreground="green")

    def vyber_bojovniky(self):
        self.bojovnici = []
        self.okno_vyber = tk.Toplevel(self.master)
        self.okno_vyber.title("Vyber bojovníky")

        tk.Label(self.okno_vyber, text="Vyberte 3 bojovníky:").pack()

        self.vyber_seznam = tk.Listbox(self.okno_vyber, selectmode=tk.MULTIPLE)
        for bojovnik in ["Sermir", "Lukostrelec", "Mag", "Tank", "Healer", "Berserker"]:
            self.vyber_seznam.insert(tk.END, bojovnik)
        self.vyber_seznam.pack()

        self.potvrdit_button = ttk.Button(self.okno_vyber, text="Potvrdit", command=self.potvrdit_vyber)
        self.potvrdit_button.pack()

    def potvrdit_vyber(self):
        vybrani_bojovnici = self.vyber_seznam.curselection()
        for index in vybrani_bojovnici:
            bojovnik_typ = self.vyber_seznam.get(index)
            if bojovnik_typ == "Sermir":
                self.bojovnici.append(Sermir(bojovnik_typ))
            elif bojovnik_typ == "Lukostrelec":
                self.bojovnici.append(Lukostrelec(bojovnik_typ))
            elif bojovnik_typ == "Mag":
                self.bojovnici.append(Mag(bojovnik_typ))
            elif bojovnik_typ == "Tank":
                self.bojovnici.append(Tank(bojovnik_typ))
            elif bojovnik_typ == "Healer":
                self.bojovnici.append(Healer(bojovnik_typ))
            elif bojovnik_typ == "Berserker":
                self.bojovnici.append(Berserker(bojovnik_typ))

        if len(self.bojovnici) == 3:
            self.vyber_arenu()
            self.bojovnik_menu['menu'].delete(0, 'end')
            for bojovnik in self.bojovnici:
                self.bojovnik_menu['menu'].add_command(label=bojovnik.jmeno,
                                                       command=tk._setit(self.bojovnik_var, bojovnik.jmeno))
        else:
            self.zobrazit_zpravu("Musíte vybrat přesně 3 bojovníky!", True)

    def vyber_arenu(self):
        self.okno_arena = tk.Toplevel(self.master)
        self.okno_arena.title("Vyber arénu")

        tk.Label(self.okno_arena, text="Vyberte typ arény:").pack()

        for typ in ["Les", "Hory", "Jeskyne", "Poušť", "Město"]:
            ttk.Radiobutton(self.okno_arena, text=typ, variable=self.arena_typ, value=typ).pack()

        self.potvrdit_arena_button = ttk.Button(self.okno_arena, text="Potvrdit", command=self.potvrdit_arena)
        self.potvrdit_arena_button.pack()

    def potvrdit_arena(self):
        if self.arena_typ.get():
            self.okno_arena.destroy()
            self.okno_vyber.destroy()
            self.zacni_hru()
        else:
            self.zobrazit_zpravu("Musíte vybrat typ arény!", True)

    def aktualizovat_indikatory(self):
        for widget in self.indikatory_frame.winfo_children():
            widget.destroy()

        self.health_labels_bojovnici = []
        self.health_labels_boss = None

        for i, bojovnik in enumerate(self.bojovnici):
            health_label = ttk.Label(self.indikatory_frame, text=f"{bojovnik.jmeno}: {bojovnik._zivot} HP")
            health_label.pack()
            self.health_labels_bojovnici.append(health_label)

        self.health_labels_boss = ttk.Label(self.indikatory_frame, text=f"{self.boss.jmeno}: {self.boss._zivot} HP")
        self.health_labels_boss.pack()

    def aktualizovat_zdravotni_stav(self):
        for i, bojovnik in enumerate(self.bojovnici):
            self.health_labels_bojovnici[i].config(text=f"{bojovnik.jmeno}: {bojovnik._zivot} HP")

        self.health_labels_boss.config(text=f"{self.boss.jmeno}: {self.boss._zivot} HP")

    def zacni_hru(self, loaded=False):
        if not loaded:
            self.arena = Arena(self.arena_typ.get(), self.bojovnici, self.boss, self.text_area)

        self.text_area.delete("1.0", tk.END)
        self.aktualizovat_indikatory()
        self.arena.zacni_boj()
        celkove_skore = sum(self.arena.scores[bojovnik.jmeno] for bojovnik in self.bojovnici)
        self.aktualizovat_skore({"jmeno": "Hráč", "body": celkove_skore})
        self.zobrazit_zpravu("Boj skončil!")
        self.aktualizovat_zdravotni_stav()


# Hlavní část programu
root = tk.Tk()
app = Aplikace(root)
root.mainloop()
