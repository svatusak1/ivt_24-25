import time


def binarni_puleni(seznam: list[int], cislo: int) -> int | None:
    right = len(seznam) - 1
    left = 0 
    
    while left <= right:
        half = (left+right) // 2

        if seznam[half] == cislo:
            return half

        if seznam[half] > cislo:
            right = half -1

        else:
            left = half + 1

    return None


start = time.perf_counter_ns()
res = binarni_puleni([1,4, 5, 15, 66, 77, 90], 14)
print('it took', time.perf_counter_ns() - start, 'nanoseconds')
print("result: ", res)

