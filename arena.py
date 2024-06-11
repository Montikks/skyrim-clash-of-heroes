import tkinter as tk
import pygame
from bojovnici import Bojovnik, Boss, Lukostrelec, Sermir, Mag, Tank, Healer, Berserker

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

class Arena:
    def __init__(self, typ, tym1, boss, text_area):
        self.typ = typ
        self.tym1 = tym1
        self.boss = boss
        self.text_area = text_area
        self.scores = {bojovnik.jmeno: 0 for bojovnik in tym1}
        self.scores[boss.jmeno] = 0
        self.vlivy = {
            "Les": self.vliv_les,
            "Hory": self.vliv_hory,
            "Jeskyne": self.vliv_jeskyne,
            "Poušť": self.vliv_poust,
            "Město": self.vliv_mesto
        }

    def vliv_les(self, bojovnik):
        if isinstance(bojovnik, Lukostrelec):
            bojovnik._poskozeni += 5
            self.text_area.insert(tk.END, f"{bojovnik.jmeno} má bonus za boj v lese: +5 poškození!\n")

    def vliv_hory(self, bojovnik):
        if isinstance(bojovnik, Sermir):
            bojovnik._zivot += 20
            self.text_area.insert(tk.END, f"{bojovnik.jmeno} má bonus za boj v horách: +20 životů!\n")

    def vliv_jeskyne(self, bojovnik):
        if isinstance(bojovnik, Mag):
            bojovnik._poskozeni += 10
            self.text_area.insert(tk.END, f"{bojovnik.jmeno} má bonus za boj v jeskyni: +10 poškození!\n")

    def vliv_poust(self, bojovnik):
        if isinstance(bojovnik, Berserker):
            bojovnik._poskozeni += 10
            self.text_area.insert(tk.END, f"{bojovnik.jmeno} má bonus za boj v poušti: +10 poškození!\n")

    def vliv_mesto(self, bojovnik):
        if isinstance(bojovnik, Tank):
            bojovnik._zivot += 30
            self.text_area.insert(tk.END, f"{bojovnik.jmeno} má bonus za boj ve městě: +30 životů!\n")

    def aplikuj_vlivy(self):
        if self.typ in self.vlivy:
            for bojovnik in self.tym1 + [self.boss]:
                self.vlivy[self.typ](bojovnik)

    def zacni_boj(self):
        self.aplikuj_vlivy()
        while len(self.tym1) > 0 and self.boss._zivot > 0:
            bojovnik1 = self.tym1[0]
            bojovnik2 = self.boss

            self.text_area.insert(tk.END, f"{bojovnik1.utok(bojovnik2)}\n")
            self.text_area.see(tk.END)
            self.text_area.update_idletasks()
            if bojovnik2._zivot <= 0:
                self.text_area.insert(tk.END, f"{bojovnik1.jmeno} zabil {bojovnik2.jmeno}!\n")
                self.scores[bojovnik1.jmeno] += 1
                bojovnik1.pridat_xp(50)
                zvuk_vitezstvi.play()
                break

            self.text_area.insert(tk.END, f"{bojovnik2.utok(bojovnik1)}\n")
            self.text_area.see(tk.END)
            self.text_area.update_idletasks()
            if bojovnik1._zivot <= 0:
                self.text_area.insert(tk.END, f"{bojovnik2.jmeno} zabil {bojovnik1.jmeno}!\n")
                self.scores[bojovnik2.jmeno] += 1
                self.tym1.pop(0)  # Odstraníme mrtvého bojovníka

        if len(self.tym1) > 0:
            self.text_area.insert(tk.END, "Tým 1 vyhrál!\n")
            zvuk_vitezstvi.play()
        else:
            self.text_area.insert(tk.END, "Boss vyhrál!\n")
            zvuk_porazka.play()

        self.text_area.insert(tk.END, "Skóre:\n")
        for bojovnik, score in self.scores.items():
            self.text_area.insert(tk.END, f"{bojovnik}: {score}\n")

    def use_item(self, bojovnik, item):
        message = bojovnik.use_item(item)
        self.text_area.insert(tk.END, f"{message}\n")
        self.text_area.see(tk.END)
        self.text_area.update_idletasks()

    def to_dict(self):
        return {
            "typ": self.typ,
            "tym1": [bojovnik.to_dict() for bojovnik in self.tym1],
            "boss": self.boss.to_dict()
        }

    @classmethod
    def from_dict(cls, data):
        tym1 = [Bojovnik.from_dict(bojovnik) for bojovnik in data["tym1"]]
        boss = Boss.from_dict(data["boss"])
        return cls(data["typ"], tym1, boss, None)
