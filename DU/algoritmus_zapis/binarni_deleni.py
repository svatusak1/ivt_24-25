import time

def binarni_deleni(seznam: list[int], cislo: int) -> int | None:
    right = len(seznam)
    left = 0 
    
    while not (right - left == 0 or right - left == 1):
        half = round((right-left)/2)
        if seznam[left+half] > cislo:
            right = half
        elif seznam[left+half] < cislo:
            left = half
        else:
            return left + half

    return None

start = time.perf_counter_ns()

res = binarni_deleni([1,4, 5, 14, 66, 77, 90], 14)

print('it took: ', (time.perf_counter_ns() - start), 'nanosecons')

