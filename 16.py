import functools
from enum import Enum
import sys

sys.setrecursionlimit(4000)

class TrackedDict(dict):
    def __init__(self, *args, **kwargs):
        super(TrackedDict, self).__init__(*args, **kwargs)
        self.changes = []

    def __setitem__(self, key, value):
        if key not in self or self[key] != value:
            print(f"Setting {key} to {value}")
        super(TrackedDict, self).__setitem__(key, value)

    def __delitem__(self, key):
        if key in self:
            self.changes.append(f"Deleting {key}")
        super(TrackedDict, self).__delitem__(key)


class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4


def reverse_direction(direction):
    if direction == Direction.UP:
        return Direction.DOWN
    if direction == Direction.DOWN:
        return Direction.UP
    if direction == Direction.LEFT:
        return Direction.RIGHT
    if direction == Direction.RIGHT:
        return Direction.LEFT


def switch_direction(current_direction, object):
    new_direction = Direction.UP
    if current_direction == Direction.UP:
        new_direction = Direction.LEFT
    if current_direction == Direction.DOWN:
        new_direction = Direction.RIGHT
    if current_direction == Direction.RIGHT:
        new_direction = Direction.DOWN
    if current_direction == Direction.LEFT:
        new_direction = Direction.UP
    return new_direction if object == '\\' else reverse_direction(new_direction)


def move_beam(coords, direction):
    y, x = coords
    if direction == Direction.UP:
        y -= 1
    if direction == Direction.RIGHT:
        x += 1
    if direction == Direction.LEFT:
        x -= 1
    if direction == Direction.DOWN:
        y += 1
    if valid_position((y, x)):
        return y, x
    else:
        return None


def valid_position(coords):
    y, x = coords
    if y < 0 or y >= len(input):
        return False
    if x < 0 or x >= len(input[0]):
        return False
    return True


f = open("input.txt", "r")
input = f.read()
input = [[char for char in line] for line in input.splitlines()]

visited_coords_cache = {}


def get_energized_from_start(coords, direction):
    visited = set()
    if coords is None:
        return visited
    if (coords, direction) in visited_coords_cache:
        if visited_coords_cache[(coords, direction)] is not None:
            return set(visited_coords_cache[(coords, direction)])
        else:
            return {coords}
    else:
        visited_coords_cache[(coords, direction)] = None
    visited = visited | {coords}
    y, x = coords
    if input[y][x] == '.':
        visited = visited | (get_energized_from_start(move_beam(coords, direction), direction))
    if input[y][x] in ['\\', '/']:
        new_direction = switch_direction(direction, input[y][x])
        visited = visited | (get_energized_from_start(move_beam(coords, new_direction), new_direction))
    if input[y][x] == '-':
        if direction.value > 2:
            visited = visited | (get_energized_from_start(move_beam(coords, direction), direction))
        else:
            visited = visited | (get_energized_from_start(move_beam(coords, Direction.RIGHT), Direction.RIGHT))
            visited = visited | (get_energized_from_start(move_beam(coords, Direction.LEFT), Direction.LEFT))
    if input[y][x] == '|':
        if direction.value <= 2:
            visited = visited | (get_energized_from_start(move_beam(coords, direction), direction))
        else:
            visited = visited | (get_energized_from_start(move_beam(coords, Direction.UP), Direction.UP))
            visited = visited | (get_energized_from_start(move_beam(coords, Direction.DOWN), Direction.DOWN))
    visited_coords_cache[(coords, direction)] = frozenset(visited)
    return set(visited)


curr_max = 0

# for i in range(0, 4):
#     energised_tiles = get_energized_from_start((0, i), Direction.DOWN)
#     for y in range(0, len(input)):
#         for x in range(0, len(input[0])):
#             if (y, x) in energised_tiles:
#                 print('#', end='')
#             else:
#                 print(input[y][x], end='')
#         print('')
#     print('')
#     print((len(set(energised_tiles))))
# print(visited_coords_cache[(0,1), Direction.LEFT])
total = len(input[0]) + len(input[0]) + len(input) + len(input)
for i in range(0, len(input[0])):
    energised_tiles = len(get_energized_from_start((len(input) - 1, i), Direction.UP))
    curr_max = energised_tiles if energised_tiles > curr_max else curr_max
    print((i / total) * 100)
    visited_coords_cache.clear()
for i in range(0, len(input[0])):
    energised_tiles = len(get_energized_from_start((0, i), Direction.DOWN))
    curr_max = energised_tiles if energised_tiles > curr_max else curr_max
    visited_coords_cache.clear()
    print((i / total) * 100)

for i in range(0, len(input)):
    energised_tiles = len(get_energized_from_start((i, len(input[0]) - 1), Direction.LEFT))
    curr_max = energised_tiles if energised_tiles > curr_max else curr_max
    visited_coords_cache.clear()
    print((i / total) * 100)
for i in range(0, len(input)):
    energised_tiles = len(get_energized_from_start((i, 0), Direction.RIGHT))
    curr_max = energised_tiles if energised_tiles > curr_max else curr_max
    visited_coords_cache.clear()
    print((i / total) * 100)



print(curr_max)
# 6931, 6882, 6659
