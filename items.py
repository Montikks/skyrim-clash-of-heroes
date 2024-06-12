class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def apply(self, bojovnik):
        pass

class HealthPotion(Item):
    def __init__(self):
        super().__init__("Health Potion", "Heals 50 HP")

    def apply(self, bojovnik):
        bojovnik._zivot += 50
        if bojovnik._zivot > bojovnik._zivot_max:
            bojovnik._zivot = bojovnik._zivot_max
        return f"{bojovnik.jmeno} použil {self.name} a vyléčil se za 50 HP!"

class DamageBoost(Item):
    def __init__(self):
        super().__init__("Damage Boost", "Increases damage by 10 for the next battle")

    def apply(self, bojovnik):
        bojovnik._poskozeni += 10
        return f"{bojovnik.jmeno} použil {self.name} a zvýšil své poškození o 10!"

class DefenseBoost(Item):
    def __init__(self):
        super().__init__("Defense Boost", "Increases defense by 10 for the next battle")

    def apply(self, bojovnik):
        # Assuming bojovnik has a defense attribute
        bojovnik._zivot += 10  # This is a placeholder, should be adjusted based on actual defense logic
        return f"{bojovnik.jmeno} použil {self.name} a zvýšil svou obranu o 10!"

class SpeedBoost(Item):
    def __init__(self):
        super().__init__("Speed Boost", "Increases speed by 10 for the next battle")

    def apply(self, bojovnik):
        # Assuming bojovnik has a speed attribute
        bojovnik._rychlost += 10  # This is a placeholder, should be adjusted based on actual speed logic
        return f"{bojovnik.jmeno} použil {self.name} a zvýšil svou rychlost o 10!"

class ManaPotion(Item):
    def __init__(self):
        super().__init__("Mana Potion", "Restores 50 Mana")

    def apply(self, bojovnik):
        if hasattr(bojovnik, '_mana'):
            bojovnik._mana += 50
            return f"{bojovnik.jmeno} použil {self.name} a obnovil si 50 Many!"
        else:
            return f"{bojovnik.jmeno} nemá žádnou manu!"
