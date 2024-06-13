class Bojovnik:
    def __init__(self, jmeno):
        self.jmeno = jmeno
        self._zivot = 100
        self._level = 1
        self._xp = 0

    def utok(self, protivnik):
        poskozeni = 10
        protivnik._zivot -= poskozeni
        return f"{self.jmeno} útočí na {protivnik.jmeno} a způsobuje {poskozeni} poškození.", "red"

    def specialni_utok(self, protivnik):
        poskozeni = 15
        protivnik._zivot -= poskozeni
        return f"{self.jmeno} používá speciální útok na {protivnik.jmeno} a způsobuje {poskozeni} poškození.", "blue"

    def pridat_xp(self, xp):
        self._xp += xp
        if self._xp >= 100:
            self._xp -= 100
            self._level += 1
            self._zivot = 100
            return f"{self.jmeno} dosáhl úrovně {self._level}!"
        return f"{self.jmeno} získal {xp} XP."

    def to_dict(self):
        return {
            "jmeno": self.jmeno,
            "zivot": self._zivot,
            "level": self._level,
            "xp": self._xp
        }

    @classmethod
    def from_dict(cls, data):
        bojovnik = cls(data["jmeno"])
        bojovnik._zivot = data["zivot"]
        bojovnik._level = data["level"]
        bojovnik._xp = data["xp"]
        return bojovnik

class Sermir(Bojovnik):
    def specialni_utok(self, protivnik):
        poskozeni = 20
        protivnik._zivot -= poskozeni
        return f"{self.jmeno} provádí speciální útok na {protivnik.jmeno} a způsobuje {poskozeni} poškození.", "blue"

class Lukostrelec(Bojovnik):
    def specialni_utok(self, protivnik):
        poskozeni = 15
        protivnik._zivot -= poskozeni
        return f"{self.jmeno} vystřeluje speciální šíp na {protivnik.jmeno} a způsobuje {poskozeni} poškození.", "blue"

class Mag(Bojovnik):
    def specialni_utok(self, protivnik):
        poskozeni = 25
        protivnik._zivot -= poskozeni
        return f"{self.jmeno} sesílá kouzlo na {protivnik.jmeno} a způsobuje {poskozeni} poškození.", "blue"

class Tank(Bojovnik):
    def specialni_utok(self, protivnik):
        poskozeni = 10
        protivnik._zivot -= poskozeni
        self._zivot += 10  # Tank se léčí při speciálním útoku
        return f"{self.jmeno} provádí speciální útok na {protivnik.jmeno}, způsobuje {poskozeni} poškození a léčí se o 10 HP.", "blue"

class Healer(Bojovnik):
    def specialni_utok(self, spojenec):
        leceni = 20
        spojenec._zivot += leceni
        if spojenec._zivot > 100:
            spojenec._zivot = 100
        return f"{self.jmeno} léčí {spojenec.jmeno} o {leceni} HP.", "green"

class Berserker(Bojovnik):
    def specialni_utok(self, protivnik):
        poskozeni = 30
        self._zivot -= 10  # Berserker si způsobí škodu
        protivnik._zivot -= poskozeni
        return f"{self.jmeno} provádí zuřivý útok na {protivnik.jmeno}, způsobuje {poskozeni} poškození a ztrácí 10 HP.", "blue"

class Assassin(Bojovnik):
    def specialni_utok(self, protivnik):
        poskozeni = 35
        protivnik._zivot -= poskozeni
        return f"{self.jmeno} provádí smrtící úder na {protivnik.jmeno} a způsobuje {poskozeni} poškození.", "blue"

class Boss(Bojovnik):
    def __init__(self, jmeno):
        super().__init__(jmeno)
        self._zivot = 200  # Boss má více zdraví než ostatní bojovníci

    def utok(self, protivnik):
        poskozeni = 15
        protivnik._zivot -= poskozeni
        return f"{self.jmeno} útočí na {protivnik.jmeno} a způsobuje {poskozeni} poškození.", "red"
