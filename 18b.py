import re

get_line_as_tuple = lambda regex_match: (regex_match.group(1), int(regex_match.group(2)), regex_match.group(3))
match_line = lambda line: re.match(r'(\w)\s+(\d+)\s+(.*)', line)
match_hex = lambda hex_code: re.match(r'\(#([0-9A-Fa-f]{5})([0-9]+)\)', hex_code)
get_hex_tuple = lambda regex_match:  (int(regex_match.group(1), 16), int(regex_match.group(2)))

input = [get_line_as_tuple(match_line(line)) for line in open("input.txt", "r").read().splitlines()]
new_instruction = [get_hex_tuple(match_hex(line[2])) for line in input]
print(new_instruction)

y = 0
x = 0
x_coords = []
y_coords = []
for instruction in new_instruction:
    print(instruction)
    distance, direction = instruction
    for i in range(0, distance):
        if direction == 1:
            y += 1
        if direction == 3:
            y -= 1
        if direction == 2:
            x -= 1
        if direction == 0:
            x += 1
        x_coords.append(x)
        y_coords.append(y)

print(len(x_coords) / 2 + 1 + 0.5 * abs(sum(
    x_coords[i] * y_coords[(i + 1) % len(x_coords)] - x_coords[(i + 1) % len(x_coords)] * y_coords[i] for i in
    range(len(x_coords)))))
