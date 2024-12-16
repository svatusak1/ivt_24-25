import math

cache :dict[float,float] = {}

def square_root(cislo: float) -> float:
    if cislo < 0:
        raise Exception("odmocnina ze zaporneho cisla neexistuje")
    if cache.get(cislo):
        return cache[cislo]
    result :float = math.sqrt(cislo)
    cache[cislo] = result
    return result

while True:
    print(square_root(float(input())))
