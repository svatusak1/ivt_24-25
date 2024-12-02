import math

cache = {}

def square_root(cislo: float) -> float:
    if cislo < 0:
        raise Exception("odmocnina ze zaporneho cisla neexistuje")
    if cache.get(cislo):
        return cache[cislo]
    result = math.sqrt(cislo)
    cache[cislo] = result
    return result

print(square_root(49))
