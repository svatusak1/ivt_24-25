from math import sqrt, pow
import time
from typing import Callable

cache = {}
def fibonaci(n: int) -> int:
    if cache.get(n):
        return cache[n]
    #  print("n = " + str(n))
    if n == 1:
        return 1
    if n <= 0:
        return 0
    a: int = fibonaci(n-1)
    b: int = fibonaci(n-2)
    res: int = a + b
    cache[n] = res
    return res

def fb(n:int) -> int:
    a: int = 0
    b: int = 1
    c: int = 1

    i: int = 3

    while i <= n:
        a = b
        b = c
        c = a+b
        i += 1

    return c

def matrix_multiplication2x2(mat1: list[list[int]], mat2: list[list[int]]) -> list[list[int]]:

    return [
        [mat1[0][0]*mat2[0][0]+mat1[0][1]*mat2[1][0], mat1[0][0]*mat2[0][1]+mat1[0][1]*mat2[1][1]],
        [mat1[1][0]*mat2[0][0]+mat1[1][1]*mat2[1][0], mat1[1][0]*mat2[0][1]+mat1[1][1]*mat2[1][1]]
    ]

def print_mat2x2(mat: list[list[int]]) -> None:
        
    for i in mat:
        print(i)
    print()

def matfb(n: int) -> int:
    y_0: list[list[int]] = [[1, 1], [1, 0]]
    y_n: list[list[int]] = y_0

    if n <=0:
        return 0
    if n == 1:
        return 1

    for i in range(n-2):
        y_n = matrix_multiplication2x2(y_n, y_0)

    return y_n[0][0]


def formfb(n: int) -> int:
    return round(pow((sqrt(5)+1)/2, n)/sqrt(5))

def time_it(function: Callable[[int], int], inp: int = 100) -> float:

    start = time.time()
    function(inp)
    end = time.time()
    return end - start

func_times = []

for i in [fibonaci, fb, matfb, formfb]:
    func_times.append((str(i), time_it(i, 995)))
    print(func_times[-1][0] + "run for: " + str(func_times[-1][1]) + " seconds")


func_times.sort(key = lambda time: time[1])

print()
print(func_times[0][0] + "was the fastest")


