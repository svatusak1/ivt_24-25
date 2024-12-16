file = open("input.txt")

matrix = []
for line in file:
    matrix.append(list(line)[:-1])

render_pole = [[0 for i in range(len(matrix[0]))] for x in range(len(matrix))]
for line in matrix:
    print(line)

string_to_find = "XMAS"

count = 0

def get_next(x, y, dir):
    if ( 0 <= x+dir[0] < len(matrix[y]) ) and (0 <= y+dir[1] < len(matrix)):
        return matrix[y + dir[1]][x+dir[0]]
    return None

def find_valid(x, y):
    string = "MAS"
    res = 0
    directions = [
            [1, 0],
            [0, 1],
            [1, 1],
            [-1, 0],
            [0, -1],
            [-1, -1],
            [-1, 1],
            [1, -1]
    ]

    for dir in directions:
        index_in_string = 0
        x_cord = x
        y_cord = y
        add = True
        while index_in_string < len(string):
            next = get_next(x_cord, y_cord, dir)
            if not next and dir in [[-1, 0], [1, 0]]:
                y_cord += dir[0] 
                if not (0 <= y_cord < len(matrix) ):
                    add = False
                    break

                if not (-len(matrix[0]) < x_cord < len(matrix[0]) ):
                    x_cord = 0

                next = matrix[y_cord][x_cord]
            if not string[index_in_string] == next:
                add = False
                break
            index_in_string += 1
            x_cord += dir[0]
            y_cord += dir[1]

        if add:
            print(dir, x, y)
            res += 1

    return res


for y in range(len(matrix)):
    for x in range(len(matrix[0])):
        if matrix[y][x] == 'X':
            count += find_valid(x, y)

print(count)




