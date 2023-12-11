import functools
from enum import Enum

class Direction(Enum):
    NORTH = 4
    SOUTH = 3
    EAST = 2
    WEST = 1

move_south = lambda y, x: ((y + 1, x), Direction.SOUTH)
move_north = lambda y, x: ((y - 1, x), Direction.NORTH)
move_east = lambda y, x: ((y, x + 1), Direction.EAST)
move_west = lambda y, x: ((y, x - 1), Direction.WEST)

v_pipe = lambda coords, direction_moving: move_south(*coords) if direction_moving == Direction.SOUTH else move_north(*coords)
h_pipe = lambda coords, direction_moving: move_east(*coords) if direction_moving == Direction.EAST else move_west(*coords)
l_pipe = lambda coords, direction_moving: move_east(*coords) if direction_moving == Direction.SOUTH else move_north(*coords)
j_pipe = lambda coords, direction_moving: move_west(*coords) if direction_moving == Direction.SOUTH else move_north(*coords)
s_pipe = lambda coords, direction_moving: move_west(*coords) if direction_moving == Direction.NORTH else move_south(*coords)
f_pipe = lambda coords, direction_moving: move_east(*coords) if direction_moving == Direction.NORTH else move_south(*coords)

pipes = {
    '|': v_pipe,
    '-': h_pipe,
    'L': l_pipe,
    'J': j_pipe,
    '7': s_pipe,
    'F': f_pipe,
}

vertical_movers = {'|', 'J', 'L', '7', 'F'}
horizontal_movers = {'-', 'J', 'L', '7', 'F'}
def get_pipe_from_coords(coords):
    return lines[coords[0]][coords[1]]

def get_starting_coords():
    for y in range(0, len(lines)):
        for x in range(0, len(lines[0])):
            if lines[y][x] == 'S':
                return y, x
    return None


def is_inside(coords):
    intersections = 0
    for j in range(coords[1], len(lines[0])):
        if (coords[0], j) in path_coords and get_pipe_from_coords((coords[0], j)) in ['|', 'L', 'J']:
            intersections += 1
    return intersections % 2 != 0


f = open("input.txt", "r")
lines = [[char for char in line] for line in f.read().splitlines()]


starting_position = get_starting_coords()
starting_position = (starting_position[0], starting_position[1] + 1)
steps = 1
direction = Direction.EAST

path_coords = {get_starting_coords(), starting_position}

while get_pipe_from_coords(starting_position) != 'S':
    steps += 1
    next = pipes.get(get_pipe_from_coords(starting_position))(starting_position, direction)
    direction = next[1]
    starting_position = next[0]
    path_coords.add(starting_position)

answer = 0

for y in range(0, len(lines)):
    for x in range(0, len(lines[0])):
        if (y, x) not in path_coords :
            if is_inside((y, x)):
                answer += 1

print(answer)