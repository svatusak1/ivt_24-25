cache = {}

def rozhodni(jmeno:str) -> str:
    even = 0
    odd = 0
    for i in jmeno:
        i = i.upper()
        if mapa.get(i):
            i = mapa[i]
        if ord(i) % 2 == 0:
            even += 1
        else:
            odd += 1
    return "cervena" if even > odd else "zelena"

mapa = {
    "Á": "A",
    "É": "E",
    "Í": "I",
    "Ó": "O",
    "Ú": "U",
    "Č": "C",
    "Š": "S",
    "Ř": "R",
    "Ž": "Z",
    "Ť": "T"
}
    

while True:
    inp = input()
    if cache.get(inp):
        print(cache[inp])
        print("z kese")
    else:
        res = rozhodni(inp)
        print(res)
        cache[inp] = res
