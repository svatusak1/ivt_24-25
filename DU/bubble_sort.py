def bubble_sort(seznam: list[int]) -> list[int]:
    switched = True
    len_seznam = len(seznam)

    i = 0
    while switched:
        switched = False
        i = 0

        while i < len_seznam-1:
            if seznam[i] > seznam[i+1]:
                seznam[i], seznam[i+1] = seznam[i+1], seznam[i]
                switched = True
            i += 1

        len_seznam -= 1
    return seznam


print(bubble_sort([2, 4, 5, 2, 5, 1, 9]))
