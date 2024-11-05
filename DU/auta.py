
class Auto:

    def __init__(self, vyrobce: str, model: str, objem_motoru: int, vykon: int):
        self._vyrobce = vyrobce
        self._model = model
        self._objem_motoru = objem_motoru
        self._vykon = vykon

    def __eq__(self, other):
        return all( getattr(self, x[0]) == getattr(other, x[1]) \
            for x in zip([a for a in dir(other) if not a.startswith('__')], \
                         [a for a in dir(self) if not a.startswith('__')] ) )

a1 = Auto("Skoda", "Octavie", 2, 4)
a2 = Auto("Skoda", "Octavie", 2, 4)

if a1 == a2:
    print("stejna")
