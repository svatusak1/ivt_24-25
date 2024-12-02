import time
import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(1000000000)

def faktorial(cislo: int) -> int:
    return 1 if cislo == 1 else cislo * faktorial(cislo-1)

def faktorial_iter(cislo: int) -> int:
    vysledek = cislo
    for i in range(cislo-1, 1, -1):
        vysledek *= i

    return vysledek

while True:
    num = input()

    start = time.time()

    faktorial(int(num))

    end = time.time()

    print("rekurzivni faktorial: ", end-start)

    start = time.time()

    faktorial_iter(int(num))

    end = time.time()

    print("iterativni faktorial: ", end-start)
