file = open("input.txt")

rules = []

for line in file:
    if line ==  "\n":
        break
    left, right = line[:-1].split("|")
    rules.append([int(left), int(right)])

updates = []

for line in file:
    updates.append([int(x) for x in line.split(",")])

def check(update):
    for i, page in enumerate(update):
        for rule in rules:
            if rule[0] == page:
                x = i
                while x >= 0:
                    if update[x] == rule[1]:
                        return False
                    x -= 1

            if rule[1] == page:
                x = i
                while x < len(update):
                    if update[x] == rule[0]:
                        return False
                    x += 1
    return True

count = 0

for update in updates:
    if not check(update):
        print(update)
        repair(update)
        print(update)
        count += update[len(update)//2]

print(count)
