import tkinter as tk
from bojovnici import Boss

class Tower:
    def __init__(self, bojovnici, text_area):
        self.bojovnici = bojovnici
        self.text_area = text_area
        self.level = 1
        self.enemies = self.generate_enemies()

    def generate_enemies(self):
        # Generujte nepřátele podle úrovně
        enemies = []
        for _ in range(self.level):
            enemies.append(Boss(f"Enemy {self.level}"))
        return enemies

    def start(self):
        self.text_area.insert(tk.END, "Začíná Tower Defense!\n")
        self.boj()

    def boj(self):
        while self.bojovnici and self.enemies:
            for bojovnik in self.bojovnici:
                if self.enemies:
                    enemy = self.enemies[0]
                    self.text_area.insert(tk.END, f"{bojovnik.jmeno} útočí na {enemy.jmeno}!\n")
                    self.text_area.insert(tk.END, bojovnik.utok(enemy))
                    if enemy._zivot <= 0:
                        self.enemies.remove(enemy)
                        self.text_area.insert(tk.END, f"{enemy.jmeno} je poražen!\n")
                        # Získání zkušeností po poražení nepřítele
                        bojovnik.ziskat_zkusenosti(20)
            for enemy in self.enemies:
                if self.bojovnici:
                    bojovnik = self.bojovnici[0]
                    self.text_area.insert(tk.END, f"{enemy.jmeno} útočí na {bojovnik.jmeno}!\n")
                    self.text_area.insert(tk.END, enemy.utok(bojovnik))
                    if bojovnik._zivot <= 0:
                        self.bojovnici.remove(bojovnik)
                        self.text_area.insert(tk.END, f"{bojovnik.jmeno} je poražen!\n")

        if not self.bojovnici:
            self.text_area.insert(tk.END, "Vaši bojovníci byli poraženi! Musíte začít znovu.\n")
        elif not self.enemies:
            self.text_area.insert(tk.END, f"Úroveň {self.level} byla vyčištěna! Pokračujte na další úroveň.\n")
            self.level += 1
            self.enemies = self.generate_enemies()
            self.boj()

    def use_item(self, bojovnik, item):
        zprava = item.apply(bojovnik)
        self.text_area.insert(tk.END, zprava + "\n")
