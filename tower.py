import tkinter as tk
from bojovnici import Bojovnik, Boss
import random

class Tower:
    def __init__(self, bojovnici, text_area):
        self.bojovnici = bojovnici
        self.text_area = text_area
        self.level = 1
        self.enemies = self.generate_enemies()
        self.obtiznost = "Střední"  # Default difficulty level

    def set_obtiznost(self, obtiznost):
        self.obtiznost = obtiznost

    def generate_enemies(self):
        enemies = []
        for i in range(3):
            enemies.append(Boss(f"Enemy {self.level}"))
        return enemies

    def start(self):
        self.text_area.insert(tk.END, "Začíná Tower Defense!\n")
        self.boj()

    def boj(self):
        for bojovnik in self.bojovnici:
            if bojovnik._zivot > 0:
                enemy = random.choice([e for e in self.enemies if e._zivot > 0])
                vysledek, barva = bojovnik.utok(enemy)
                self.text_area.insert(tk.END, vysledek + "\n")
                self.text_area.tag_add("utok", "end-2l", "end-1l")
                self.text_area.tag_config("utok", foreground=barva)
                self.aktualizovat_zdravotni_stav()
                if enemy._zivot <= 0:
                    self.text_area.insert(tk.END, f"{enemy.jmeno} byl poražen!\n")
                    if all(e._zivot <= 0 for e in self.enemies):
                        self.level_up()
                        return
                vysledek, barva = enemy.utok(bojovnik)
                self.text_area.insert(tk.END, vysledek + "\n")
                self.text_area.tag_add("utok", "end-2l", "end-1l")
                self.text_area.tag_config("utok", foreground=barva)
                self.aktualizovat_zdravotni_stav()
                if bojovnik._zivot <= 0:
                    self.text_area.insert(tk.END, f"{bojovnik.jmeno} byl poražen!\n")
                    if all(b._zivot <= 0 for b in self.bojovnici):
                        self.text_area.insert(tk.END, "Všichni vaši bojovníci byli poraženi. Konec hry.\n")
                        return
        self.text_area.after(1000, self.boj)

    def level_up(self):
        self.level += 1
        self.text_area.insert(tk.END, f"Úspěšně jste dokončili úroveň {self.level - 1}! Postupujete na úroveň {self.level}.\n")
        self.enemies = self.generate_enemies()
        for bojovnik in self.bojovnici:
            if bojovnik._zivot > 0:
                zprava = bojovnik.pridat_xp(50)
                self.text_area.insert(tk.END, zprava + "\n")
        self.boj()

    def aktualizovat_zdravotni_stav(self):
        for i, bojovnik in enumerate(self.bojovnici):
            self.text_area.insert(tk.END, f"{bojovnik.jmeno}: {bojovnik._zivot} HP\n")
        for enemy in self.enemies:
            self.text_area.insert(tk.END, f"{enemy.jmeno}: {enemy._zivot} HP\n")

    def to_dict(self):
        return {
            "bojovnici": [bojovnik.to_dict() for bojovnik in self.bojovnici],
            "level": self.level,
            "enemies": [enemy.to_dict() for enemy in self.enemies],
            "obtiznost": self.obtiznost
        }

    @classmethod
    def from_dict(cls, data, text_area):
        tower = cls([Bojovnik.from_dict(b) for b in data["bojovnici"]], text_area)
        tower.level = data["level"]
        tower.enemies = [Boss.from_dict(e) for e in data["enemies"]]
        tower.obtiznost = data["obtiznost"]
        return tower
