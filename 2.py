import functools

f = open("input.txt", "r")

def find_overs(arr):
    id, body = arr.split(':')
    body = map(lambda l: l.split(','), body.split(';'))
    flattened_list = [item for sublist in body for item in sublist]
    return get_power_of_max_cubes(flattened_list)


def get_power_of_max_cubes(game):
    max_red = 0
    max_green = 0
    max_blue = 0
    for item in game:
        item = item.split()
        max_red = replace_max(item, max_red, 'red')
        max_green = replace_max(item, max_green, 'green')
        max_blue = replace_max(item, max_blue, 'blue')
    return max_red * max_green * max_blue


def replace_max(item, current_max, colour):
    if item[1] == colour:
        number_of_cubes = int(item[0])
        if number_of_cubes > current_max:
            return number_of_cubes
    return current_max


def sum(a, b):
    return a + b

answer_array = map(find_overs, f.read().splitlines())
print(functools.reduce(sum, answer_array))
