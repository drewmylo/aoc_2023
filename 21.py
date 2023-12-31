import functools

input = [[char for char in line] for line in open("input.txt", "r").read().splitlines()]

start = ()

# find start
for y in range(0, len(input)):
    for x in range(0, len(input[0])):
        if input[y][x] == 'S':
            start = (y, x)
            input[y][x] = '.'


@functools.cache
def take_step(coords, steps_remaining):
    y, x = coords
    down = (0, x) if y + 1 >= len(input) else (y + 1, x)
    up = (len(input) - 1, x) if y - 1 < 0 else (y - 1, x)
    left = (y, len(input[0]) - 1) if x - 1 < 0 else (y, x - 1)
    right = (y, 0) if x + 1 >= len(input[0]) else (y, x + 1)
    final_positions = set()
    if steps_remaining == 0:
        if input[y][x] == '.':
            final_positions.update({coords})
        return frozenset(final_positions)
    for direction in [up, down, left, right]:
        if input[direction[0]][direction[1]] == '.':
            final_positions.update(take_step(direction, steps_remaining - 1))
    return frozenset(final_positions)


print(len(take_step(start, 6)))