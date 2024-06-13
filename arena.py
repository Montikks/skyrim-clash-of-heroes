import tkinter as tk
from bojovnici import Bojovnik, Boss
import random

class Arena:
    def __init__(self, typ, bojovnici, boss, text_area, root):
        self.typ = typ
        self.bojovnici = bojovnici
        self.boss = boss
        self.text_area = text_area
        self.root = root

    def zacni_boj(self):
        self.text_area.insert(tk.END, f"Boj začíná v aréně typu {self.typ}!\n")
        self.root.after(1000, self.kolo_boje)

    def kolo_boje(self):
        for bojovnik in self.bojovnici:
            if bojovnik._zivot > 0:
                vysledek, barva = bojovnik.utok(self.boss)
                self.text_area.insert(tk.END, vysledek + "\n")
                self.text_area.tag_add("utok", "end-2l", "end-1l")
                self.text_area.tag_config("utok", foreground=barva)
                self.aktualizovat_zdravotni_stav()
                if self.boss._zivot <= 0:
                    self.text_area.insert(tk.END, f"{self.boss.jmeno} byl poražen!\n")
                    self.ziskat_xp()
                    return
                vysledek, barva = self.boss.utok(bojovnik)
                self.text_area.insert(tk.END, vysledek + "\n")
                self.text_area.tag_add("utok", "end-2l", "end-1l")
                self.text_area.tag_config("utok", foreground=barva)
                self.aktualizovat_zdravotni_stav()
                if bojovnik._zivot <= 0:
                    self.text_area.insert(tk.END, f"{bojovnik.jmeno} byl poražen!\n")
        self.root.after(1000, self.kolo_boje)

    def aktualizovat_zdravotni_stav(self):
        for i, bojovnik in enumerate(self.bojovnici):
            self.text_area.insert(tk.END, f"{bojovnik.jmeno}: {bojovnik._zivot} HP\n")
        self.text_area.insert(tk.END, f"{self.boss.jmeno}: {self.boss._zivot} HP\n")

    def ziskat_xp(self):
        for bojovnik in self.bojovnici:
            if bojovnik._zivot > 0:
                zprava = bojovnik.pridat_xp(50)
                self.text_area.insert(tk.END, zprava + "\n")
