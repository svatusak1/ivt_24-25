pole = [603, 1000, 240, 652, 59, 135, 613, 179, 30, 317, 541, 895, 985, 639, 270, 824, 37, 64, 555, 327, 235, 444, 599, 569, 906, 694, 834, 746, 816, 110, 39, 50, 629, 968, 497, 626, 928, 354, 800, 925, 432, 733, 649, 145, 221, 928, 636, 107, 1000, 957, 874, 734, 398, 665, 205, 662, 973, 345, 552, 533, 792, 418, 304, 309, 397, 201, 483, 594, 73, 90, 95, 429, 324, 290, 125, 885, 212, 6, 316, 192, 23, 457, 621, 863, 531, 574, 885, 222, 771, 44, 995, 96, 32, 453, 682, 40, 100, 893, 487, 150]

def prefix_soucet(pole: list[int]) -> list[int]:
    if not pole:
        return []

    pole_S: list[int] = [pole[0]]

    for i, prvek in zip(range(1, len(pole)), pole[1:]):
        pole_S.append(pole_S[i-1] + prvek)

    return pole_S

print(sum(pole))
pole_soucty = prefix_soucet(pole)
print(pole_soucty)