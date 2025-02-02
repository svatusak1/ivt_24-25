from dataclasses import dataclass
from enum import Enum

class Specializace(Enum):
    KARDIOLOG = 0
    NEFROLOG = 1
    KINESTEZIOLOG = 2
    ANESTEZIOLOG = 3
    CHIRURG = 4

@dataclass
class Lekar:
    jmeno: str
    specializace: Specializace


class Pohlavi(Enum):
    MUZ = 0
    ZENA = 1
    JINE = 2

class Stavy(Enum):
    SPATNY = 0
    PROSTREDNI = 1
    DOBRY = 2
    CO_TU_DELA = 3

@dataclass
class Pacient:
    rodne_cislo: int
    jmeno: str
    pohlavy: Pohlavi
    stav: Stavy


class Ordinace():
    def __init__(self, specializace: str, hlavni_lekar: Lekar, pomocni_lekari: list[Lekar], pacienti: list[Pacient]) -> None:
        self.specializace: Specializace = specializace
        self.hlavni_lekar: Lekar = hlavni_lekar
        self.pomocni_lekari: list[Lekar] = pomocni_lekari
        self.pacienti: list[Pacient] = pacienti

    def prirad_hlavniho_lekare(self, lekar: Lekar) -> None:
        self.hlavni_lekar = lekar

    def pridej_pomocne_lekare(self, *lekari: list[Lekar]) -> None:
        for lekar in lekari:
            self.pomocni_lekari.append(lekar)

    def odeber_pomocne_lekare(self, *lekari: list[Lekar]) -> None:
        for lekar in lekari:
            self.pomocni_lekari.remove(lekar)

    def pridej_pacienty(self, *pacienti) -> None:
        for pacient in pacienti:
            self.pacienti.append(pacient)

    def odeber_pacienty(self, *pacienti) -> None:
        for pacient in pacienti:
            self.pacienti.remove(pacient)

class Nemocnice():
    def __init__(self):
        self.container: list[Ordinace] = []

    def pridej_ordinace(self, *ordinace: list[Ordinace]):
        for item in ordinace:
            self.container.append(item)

if __name__ == "__main__":
    nemocnice = Nemocnice()
    lekar1 = Lekar("Petr Kos", Specializace.CHIRURG)
    lekar2 = Lekar("Jarmila Jirankova", Specializace.ANESTEZIOLOG)
    pacient1 = Pacient(8007, "Chrobak Tom", Pohlavi.MUZ, Stavy.SPATNY)
    pacient2 = Pacient(215, "Ferdinand Krysanec", Pohlavi.JINE, Stavy.CO_TU_DELA)

    ord1 = Ordinace(Specializace.ANESTEZIOLOG, lekar1, [lekar2], [pacient1, pacient2])
    nemocnice.pridej_ordinace(ord1)




