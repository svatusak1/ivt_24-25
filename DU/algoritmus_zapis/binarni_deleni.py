def binarni_deleni(seznam: list[int], cislo: int) -> int | None:
    right = len(seznam)
    left = 0 
    
    while right - left > 1:
        half = round((right-left)/2)
        if seznam[left+half] > cislo:
            right = half
        elif seznam[left+half] < cislo:
            left = half
        else:
            return left + half

    return None

print(binarni_deleni([1,4, 5, 14, 66, 77, 90], 14))

