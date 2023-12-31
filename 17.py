import functools
from enum import Enum
import sys


def get_weight(coords):
    y, x = coords
    if x < 0 or x >= len(input[0]):
        return None
    if y < 0 or y >= len(input):
        return None
    return int(input[coords[0]][coords[1]])


class Direction(Enum):
    UP = 4
    DOWN = 3
    LEFT = 2
    RIGHT = 1


def get_surrounds(coords, last_three):
    y, x = coords
    surrounds = [((y - 1, x), Direction.UP), ((y + 1, x), Direction.DOWN), ((y, x - 1), Direction.LEFT),
                 ((y, x + 1), Direction.RIGHT)]
    result = set()
    for item in surrounds:
        if not is_straight(last_three + [item[1]]):
            coordinates, direction = item
            weight = get_weight(coordinates)
            if weight is not None:
                result.add((coordinates, weight, direction))
    return result


def is_straight(lst):
    if len(lst) > 3:
        first_element = lst[0]
        return all(element == first_element for element in lst)
    return False


f = open("input.txt", "r")
input = [[char for char in line] for line in f.read().splitlines()]

visited = set()
node_dict = {}
current_distance = 0
current_node = ((0, 0), get_weight((0, 0)), Direction.RIGHT)
dest_y, dest_x = (len(input) - 1, len(input[0]) - 1)
unvisited = set()
for y in range(0, len(input)):
    for x in range(0, len(input[0])):
        unvisited.add((y, x))

last_three_steps = []
while current_node[0] != (dest_y, dest_x):
    if len(last_three_steps) > 3:
        last_three_steps = [last_three_steps[-3],last_three_steps[-2],last_three_steps[-1]]
    visited.add(current_node[0])
    if isinstance(current_node[2], list):
        last_three_steps.extend(current_node[2])
    else:
        last_three_steps.append(current_node[2])
    neighbours = get_surrounds(current_node[0], last_three_steps)
    for neighbour in neighbours:
        coordinates, weight, direction = neighbour
        if coordinates in node_dict:
            if weight + current_distance < node_dict[neighbour[0]][1]:
                node_dict[coordinates] = (coordinates, weight + current_distance, last_three_steps + [direction])
        else:
            node_dict[coordinates] = (coordinates, weight + current_distance, last_three_steps + [direction])
    unvisited_nodes_with_distances = list(
        filter(lambda x: x[0] in (unvisited & node_dict.keys() - visited), node_dict.items()))
    if len(unvisited_nodes_with_distances) > 0:
        current_node = min(unvisited_nodes_with_distances, key=lambda x: x[1])[1]
        current_distance = current_node[1]
        last_three_steps = current_node[2]
    else:
        print(node_dict[(dest_y, dest_x)])
        exit(0)

print(node_dict[(12, 12)])
for y in range(0, len(input)):
    for x in range(0, len(input[0])):
        if (y, x) in visited:
            print('#', end='')
        else:
            print(input[y][x], end='')
    print('')
