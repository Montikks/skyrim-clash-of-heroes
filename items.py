class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def apply(self, bojovnik):
        raise NotImplementedError("This method should be overridden by subclasses")


class HealthPotion(Item):
    def __init__(self):
        super().__init__("Health Potion", "Restores 50 health points")

    def apply(self, bojovnik):
        bojovnik._zivot += 50
        return f"{bojovnik.jmeno} použil {self.name} a získal 50 životů."


class DamageBoost(Item):
    def __init__(self):
        super().__init__("Damage Boost", "Increases damage by 10 for one battle")

    def apply(self, bojovnik):
        bojovnik._poskozeni += 10
        return f"{bojovnik.jmeno} použil {self.name} a jeho poškození se zvýšilo o 10."


class DefenseBoost(Item):
    def __init__(self):
        super().__init__("Defense Boost", "Increases defense by 10 for one battle")

    def apply(self, bojovnik):
        bojovnik._zivot += 10
        return f"{bojovnik.jmeno} použil {self.name} a jeho obrana se zvýšila o 10."
