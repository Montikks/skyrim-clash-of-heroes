import random
import pygame

# Inicializace pygame
pygame.mixer.init()

# Načtení zvuků
zvuk_utok = pygame.mixer.Sound("sounds/utok.wav")
zvuk_vitezstvi = pygame.mixer.Sound("sounds/vitezstvi.wav")
zvuk_porazka = pygame.mixer.Sound("sounds/porazka.wav")

# Nastavení hlasitosti
zvuk_utok.set_volume(0.05)
zvuk_vitezstvi.set_volume(0.05)
zvuk_porazka.set_volume(0.05)


# Základní třída Bojovnik
class Bojovnik:
    def __init__(self, jmeno):
        self.jmeno = jmeno
        self._zivot = 100
        self._poskozeni = 10
        self._xp = 0

    def utok(self, protivnik):
        protivnik._zivot -= self._poskozeni
        return f"{self.jmeno} útočí na {protivnik.jmeno} a způsobuje {self._poskozeni} poškození!"

    def pridat_xp(self, xp):
        self._xp += xp
        if self._xp >= 100:
            self._zivot += 20
            self._poskozeni += 5
            self._xp = 0
            return f"{self.jmeno} postoupil na vyšší úroveň!"
        return f"{self.jmeno} získal {xp} XP."

    def to_dict(self):
        return {
            "jmeno": self.jmeno,
            "zivot": self._zivot,
            "poskozeni": self._poskozeni,
            "xp": self._xp
        }

    @classmethod
    def from_dict(cls, data):
        instance = cls(data["jmeno"])
        instance._zivot = data["zivot"]
        instance._poskozeni = data["poskozeni"]
        instance._xp = data["xp"]
        return instance


class Sermir(Bojovnik):
    def __init__(self, jmeno):
        super().__init__(jmeno)
        self._zivot = 120
        self._poskozeni = 15


class Lukostrelec(Bojovnik):
    def __init__(self, jmeno):
        super().__init__(jmeno)
        self._zivot = 80
        self._poskozeni = 20


class Mag(Bojovnik):
    def __init__(self, jmeno):
        super().__init__(jmeno)
        self._zivot = 70
        self._poskozeni = 25


class Tank(Bojovnik):
    def __init__(self, jmeno):
        super().__init__(jmeno)
        self._zivot = 150
        self._poskozeni = 10


class Healer(Bojovnik):
    def __init__(self, jmeno):
        super().__init__(jmeno)
        self._zivot = 90
        self._poskozeni = 5

    def heal(self, ally):
        ally._zivot += 20
        return f"{self.jmeno} léčí {ally.jmeno} za 20 životů!"


class Berserker(Bojovnik):
    def __init__(self, jmeno):
        super().__init__(jmeno)
        self._zivot = 100
        self._poskozeni = 30


class Boss(Bojovnik):
    def __init__(self, jmeno):
        super().__init__(jmeno)
        self._zivot = 300
        self._poskozeni = 25

