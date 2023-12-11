import functools

f = open("input.txt", "r")
lines = [[char for char in line] for line in f.read().splitlines()]
lines_with_expanded_horizontals = []
#expand horizontals
for index, row in enumerate(lines):
    if all(x == '.' for x in row):
        lines_with_expanded_horizontals.append(['*' for x in row])
    else:
        lines_with_expanded_horizontals.append([x for x in row])

lines_with_expanded_verticals = []
#expand verticals
for x in range(0, len(lines_with_expanded_horizontals[0])):
    column = [row[x] for row in lines_with_expanded_horizontals]
    if all(x in ['.', '*'] for x in column):
        lines_with_expanded_verticals.append(['$' if x != '*' else '&' for x in column])
    else:
        lines_with_expanded_verticals.append([x for x in column])

#rotate back to reduce mental strain
rotated_back = []
for x in range(0, len(lines_with_expanded_verticals[0])):
    column = [row[x] for row in lines_with_expanded_verticals]
    rotated_back.append([x for x in column])

galaxies = set()

for y in range(0, len(rotated_back)):
    for x in range(0, len(rotated_back[0])):
        if rotated_back[y][x] == '#':
            galaxies.add((y, x))

galaxy_target_set = set()

for galaxy in galaxies:
    other_galaxies = galaxies - {galaxy}
    for other_galaxy in other_galaxies:
        galaxy_target_set.add(frozenset((galaxy, other_galaxy)))

def get_shortest_path(source_and_target):
    source_galaxy, target_galaxy = list(source_and_target)
    sy, sx = source_galaxy
    ty, tx = target_galaxy
    steps = 0
    while sx != tx or sy != ty:
        sy, steps = step_closer(steps, sy, ty)
        if rotated_back[sy][sx] in ['*', '&']:
            steps += 999999
        sx, steps = step_closer(steps, sx, tx)
        if rotated_back[sy][sx] in ['$', '&']:
            steps += 999999
    return steps

def step_closer(steps, s, t):
    if s != t:
        if s < t:
            s += 1
        else:
            s -= 1
        steps += 1
    return s, steps

for k in rotated_back:
    print(''.join(k))
print(functools.reduce(lambda a, b: a + b, [get_shortest_path(x) for x in galaxy_target_set]))