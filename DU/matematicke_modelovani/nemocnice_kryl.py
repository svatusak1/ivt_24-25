from enum import Enum
from dataclasses import dataclass
from random import randint, choice, sample, seed

class TypPacienta(Enum):
    HYPOCHONDR = 0
    NORMAL = 1
    RAMBO = 2

@dataclass
class Pacient:
    rodne_cislo: str
    jmeno_prijmeni: str
    vek: int
    typ: TypPacienta
    pohlavi_zena: bool


class Specializace(Enum):
    NEFROLOGIE = 0
    NEUROLOGIE = 1
    KARDIOLOGIE = 2
    CHIRURGIE = 3
    ORL = 4


class Zkusenost(Enum):
    ZELENAC = 0
    NORMAL = 1
    EXPERT = 2

@dataclass
class Lekar:
    jmeno_prijmeni: str
    specializace: Specializace
    zkusenost: Zkusenost

class Ordinace:
    def __init__(self, specializace: Specializace, hlavni_lekar: Lekar, pomocny_lekar: Lekar, pacienti: list[Pacient], kapacita: int):
        self.specializace = specializace
        self.hlavni_lekar = hlavni_lekar
        self.pomocny_lekar = pomocny_lekar
        self.pacienti = pacienti
        self.kapacita = kapacita

    def pridej_pacienta(self, pacient: Pacient) -> None:
        if self.kapacita > len(self.pacienti):
            self.pacienti.append(pacient)
        else:
            raise Exception('kapacita plna')
    def vypis_hypochondry(self) -> None:
        for pacient in self.pacienti:
            if pacient.typ == TypPacienta.HYPOCHONDR:
                print(pacient)

    def volna_kapacita(self) -> bool:
        return True if self.kapacita > len(self.pacienti) else False



class Nemocnice:
    def __init__(self, ordinace: list[Ordinace]) -> None:
        self.ordinace = ordinace

    def vypis_typy_ordinaci(self) -> list[Specializace]:
        ret = []
        for ord in self.ordinace:
            if not ord.specializace in ret:
                ret.append(ord.specializace)
        return ret
    def volne_ordinace(self) -> list[Ordinace]:
        ret: list[Ordinace] = []
        for ord in self.ordinace:
            if ord.volna_kapacita:
                ret.append(ord)
        return ret
    def vsichni_pacienti(self) -> list[Pacient]:
        pacienti: list[Pacient] = []
        for ord in self.ordinace:
            for pacient in ord.pacienti:
                pacienti.append(pacienti)
        return pacienti
    def experti(self) -> list[Lekar]:
        ret: list[Lekar] = []
        for ord in self.ordinace:
            if ord.hlavni_lekar != None and ord.hlavni_lekar.zkusenost == Zkusenost.EXPERT:
                ret.append(ord.hlavni_lekar)
            if ord.pomocny_lekar != None and ord.pomocny_lekar.zkusenost == Zkusenost.EXPERT:
                ret.append(ord.pomocny_lekar)
        return ret


    def umi_specializaci(self, specializace: Specializace) -> bool:
        for ord in self.ordinace:
            if ord.hlavni_lekar != None and ord.hlavni_lekar.specializace == specializace:
                return True
            if ord.pomocny_lekar != None and ord.pomocny_lekar.specializace == specializace:
                return True
        return False




def generuj_nemocnici(tisk: bool, pocet_ordinaci) -> Nemocnice:
    seed(42)

    # Helper functions
    def generate_pacient(rodne_cislo, jmeno_prijmeni):
        vek = randint(1, 100)
        typ = choice(list(TypPacienta))
        pohlavi_zena = choice([True, False])
        return Pacient(rodne_cislo, jmeno_prijmeni, vek, typ, pohlavi_zena)

    def generate_lekar(jmeno_prijmeni, specializace, zkusenost):
        return Lekar(jmeno_prijmeni, specializace, zkusenost)

    # Generate shared patients
    shared_pacienti = [
        generate_pacient(f"{100000+idx}{idx}", f"Shared Pacient {idx}") for idx in range(5)
    ]

    # Generate ordinace and nemocnice
    ordinace_list = []
    specializace_list = list(Specializace)

    for i in range(pocet_ordinaci):
        specializace = specializace_list[i % len(specializace_list)]
        hlavni_lekar = generate_lekar(f"Hlavni Lekar {i}", specializace, choice(list(Zkusenost)))
        pomocny_lekar = generate_lekar(f"Pomocny Lekar {i}", choice(list(Specializace)), choice(list(Zkusenost))) if i % 2 == 0 else None

        pacienti = shared_pacienti + [
            generate_pacient(f"{100000+i}{j}", f"Pacient {i}-{j}") for j in range(7)
        ]
        pacienti = sample(pacienti, len(pacienti))  # Shuffle patients

        ordinace_list.append(
            Ordinace(
                specializace=specializace,
                hlavni_lekar=hlavni_lekar,
                pomocny_lekar=pomocny_lekar,
                pacienti=pacienti,
                kapacita = randint(10, 500)
            )
        )

    nemocnice = Nemocnice(ordinace=ordinace_list)

    # Output for verification
    if tisk:
        for ord in nemocnice.ordinace:
            print(f"Ordinace: {ord.specializace}")
            print(f"kapacita: {ord.kapacita}")
            print(f"  Hlavni lekar: {ord.hlavni_lekar}")
            if ord.pomocny_lekar:
                print(f"  Pomocny lekar: {ord.pomocny_lekar}")
            print("  Pacienti:")
            for pacient in ord.pacienti:
                print(f"    {pacient}")
            print()
    return nemocnice

nemocnice = generuj_nemocnici(True, 4)

print("typy ordinaci: ", nemocnice.vypis_typy_ordinaci())
print("hypochondri: ")
nemocnice.ordinace[0].vypis_hypochondry()
print("")
print("kapacita volna?", nemocnice.ordinace[0].volna_kapacita())
print("volne ordinace: ", nemocnice.volne_ordinace())
print("experti: ", nemocnice.experti())
print("umi specializaci? (ORL)", nemocnice.umi_specializaci(Specializace.ORL))

"""
*Pacient*
- rodné číslo
- jméno + příjmení
- věk
- typ: hypochondr, normal, superman

*Lékař*
- jméno + příjmení
- zkušenost: zaučuji se, normal, expert
- obor: kardio, nefro, neuro, orl, interna, radio, gynekologie

*Ordinace*
- název: jakékoliv pojmenování
- kapacita
- seznam pacientů
- hlavní lékař
- pomocný lékař

*Nemocnice*
- seznam ordinací

*Dynamika*
- ordinaci předěláme na normální třídu
- na ordinaci bychom chtěli následující metody:

1. přidej pacienta: signalizuje výjimkou, pokud je ordinace přes kapacitu
2. vrať všechny hypochondry
3. má ordinace volnou kapacitu?: vrací boolean true/false

- nemocnici předěláme na normální třídu
- na nemocnici bychom chtěli následující metody:

1. vrať seznam všech specializací, které nemocnice nabízí
   (procházením ordinací a sběrem jejich specializací)
2. vrať seznam ordinací, které mají ještě volnou kapacitu
3. vrať seznam všech pacientů nemocnice
4. vrať seznam všech expertů v nemocnici
5. umí specializaci?: vrací true/false podle toho zda hlavní nebo pomocný
   lékař některé z ordinací má danou specializaci
"""
