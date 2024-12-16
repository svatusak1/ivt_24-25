file = open("input.txt")


out= 0

def check_valid(index, text):
    start_str = "mul("
    res = []
    i = 0
    while i < 3:
        i += 1
        if (index + i > len(text) - 1) or not (text[index+i] == start_str[i]):
            return False

    i += 1
    if not text[index+i].isnumeric():
        return False

    item = []

    while text[index+i].isnumeric():
        item.append(text[index+i])
        i+=1
    res.append(int("".join(item)))

    if not text[index+i] == ',':
        return False
    i+=1

    item = []

    if not text[index+i].isnumeric():
        return False

    while text[index+i].isnumeric():
        item.append(text[index+i])
        i+=1

    res.append(int("".join(item)))

    if not text[index+i] == ')':
        return False

    return res[0] * res[1]


for line in file:
    for i in range(len(line)):
        if line[i] == 'm':
            out += check_valid(i, line)
        

print(out)
