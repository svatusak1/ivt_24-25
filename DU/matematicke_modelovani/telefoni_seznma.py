from dataclasses import dataclass

@dataclass
class Person():
    _name: str
    _phone_number: str

class PhoneRecords():
    def __init__(self):
        self._container = []
        self._map = {}

    def add_person(self, *persons: list[Person]) -> None:
        for person in persons:
            self._container.append(person)
            self._map[person._phone_number] = person

    def find_by_prefix(self, pref: str) -> list[Person]:
        ret = []
        for item in self._container:
            if item._name[:len(pref)] == pref:
                ret.append(item)
        return ret

    def find_by_phone_number(self, number: str) -> Person:
        return self._map[number]
        

klara = Person("klara", "+420 999 888 777")
petr = Person("petr", "+420 700 888 777")
recs = PhoneRecords()
recs.add_person(klara, petr)
print(recs.find_by_prefix("kl"))
print(recs.find_by_phone_number("+420 700 888 777"))
