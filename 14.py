f = open("input.txt", "r")
input = [[char for char in line] for line in f.read().splitlines()]


def rotate_clockwise(matrix):
    return [list(row) for row in zip(*matrix[::-1])]


def roll_balls(matrix):
    for x in range(0, len(matrix[0])):
        last_free_spot = 0
        for y in range(0, len(matrix)):
            if matrix[y][x] == 'O':
                if y > last_free_spot:
                    matrix[y][x] = '.'
                    matrix[last_free_spot][x] = 'O'
                    last_free_spot += 1
            elif matrix[y][x] == '#':
                last_free_spot = y + 1
            while (last_free_spot < len(matrix)) and matrix[last_free_spot][x] != '.':
                last_free_spot += 1


def count_weight_north(matrix):
    count = 0
    for index, element in enumerate(matrix):
        count += (len(matrix) - index) * element.count('O')
    return count

period_dict = {}
iterations = 0
while iterations <= 10000:
    if iterations % 4 == 0 and iterations != 0:
        weight_north = count_weight_north(input)
        if weight_north not in period_dict.keys():
            period_dict[weight_north] = [iterations / 4]
        else:
            period_dict[weight_north].append(iterations / 4)
    roll_balls(input)
    input = rotate_clockwise(input)
    iterations += 1

period_array = list(filter(lambda x: len(x[1]) > 5, period_dict.items()))[0][1]
period = period_array[5] - period_array[3]
point = 1000000000
while point > (iterations / 4 / 2):
    point -= period
for number in period_dict.keys():
    if point in period_dict[number]:
        print(number)
