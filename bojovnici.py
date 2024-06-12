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
        self._zivot_max = 100
        self._uroven = 1
        self._zkusenosti = 0
        self._dalsi_uroven = 100  # Zkušenosti potřebné pro další úroveň

    def utok(self, protivnik):
        poskozeni = random.randint(0, self._poskozeni)
        protivnik._zivot -= poskozeni
        return f"{self.jmeno} útočí na {protivnik.jmeno} a způsobuje {poskozeni} poškození!"

    def ziskat_zkusenosti(self, zkusenosti):
        self._zkusenosti += zkusenosti
        if self._zkusenosti >= self._dalsi_uroven:
            self._uroven_up()

    def _uroven_up(self):
        self._uroven += 1
        self._zkusenosti -= self._dalsi_uroven
        self._dalsi_uroven = int(self._dalsi_uroven * 1.5)  # Zvyšování náročnosti pro další úroveň
        self._zivot_max += 20  # Zvýšení maximálního zdraví při úrovni nahoru
        self._zivot = self._zivot_max
        self._poskozeni += 5  # Zvýšení poškození při úrovni nahoru
        print(f"{self.jmeno} postoupil na úroveň {self._uroven}!")

class Sermir(Bojovnik):
    def __init__(self, jmeno):
        super().__init__(jmeno)
        self._zivot = 150
        self._poskozeni = 15

class Lukostrelec(Bojovnik):
    def __init__(self, jmeno):
        super().__init__(jmeno)
        self._zivot = 100
        self._poskozeni = 20

class Mag(Bojovnik):
    def __init__(self, jmeno):
        super().__init__(jmeno)
        self._zivot = 80
        self._poskozeni = 25

class Tank(Bojovnik):
    def __init__(self, jmeno):
        super().__init__(jmeno)
        self._zivot = 200
        self._poskozeni = 10

class Healer(Bojovnik):
    def __init__(self, jmeno):
        super().__init__(jmeno)
        self._zivot = 90
        self._poskozeni = 5
        self._mana = 100  # Přidání atributu mana

    def uzdraveni(self, spojenci):
        if self._mana >= 10:
            self._mana -= 10
            for spojenec in spojenci:
                spojenec._zivot += 20
                if spojenec._zivot > spojenec._zivot_max:
                    spojenec._zivot = spojenec._zivot_max
            return f"{self.jmeno} uzdravil své spojence za 20 HP!"
        else:
            return f"{self.jmeno} nemá dostatek many pro uzdravení!"

class Berserker(Bojovnik):
    def __init__(self, jmeno):
        super().__init__(jmeno)
        self._zivot = 120
        self._poskozeni = 30

class Assassin(Bojovnik):
    def __init__(self, jmeno):
        super().__init__(jmeno)
        self._zivot = 60
        self._poskozeni = 35
        self._rychlost = 20  # Přidání nové vlastnosti rychlost

    def utok(self, protivnik):
        if random.random() < 0.2:
            kriticke_poskozeni = self._poskozeni * 2
            protivnik._zivot -= kriticke_poskozeni
            return f"{self.jmeno} útočí na {protivnik.jmeno} a způsobuje kritický zásah za {kriticke_poskozeni} poškození!"
        else:
            return super().utok(protivnik)

class Boss(Bojovnik):
    def __init__(self, jmeno):
        super().__init__(jmeno)
        self._zivot = 300
        self._poskozeni = 20


