file = open("input.txt.")

left = []
right = []

for line in file:
    left_item, right_item = line.split()
    left.append(int(left_item))
    right.append(int(right_item))

sim_score = 0
for item in left:
    sim_score += right.count(item) * item

print(sim_score)


