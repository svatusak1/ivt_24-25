def binarni_deleni(seznam: list[int], cislo: int) -> int | None:
    left = 0 
    right = len(seznam)
    if right == 0:
        return None
    half = round((right-left)/2)

    while not (right - left == 0 or right - left == 1):
        half = round((right-left)/2)
        if seznam[left+half] > cislo:
            right = half
        elif seznam[left+half] < cislo:
            left = half
        else:
            return left + half

    return None

print(binarni_deleni([1,4, 5, 14, 66, 77, 90], 14))


