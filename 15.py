import re

f = open("input.txt", "r")
input = f.read()
input = input.replace('\n', '').split(',')


def hash(input):
    curr = 0
    for char in input:
        curr += ord(char)
        curr *= 17
        curr %= 256
    return curr


pattern = r'([a-z]+|\W|\d+)'
dict_of_boxes = {}
steps = list(map(lambda y: [(y[0], hash(y[0]))] + y[1:], [list(filter(lambda x: x != '', re.split(pattern, x))) for x in input]))

print(steps)
for index, step in enumerate(steps):
    if step[1] == '=':
        if step[0][1] not in dict_of_boxes.keys():
            dict_of_boxes[step[0][1]] = [[step[0][0], step[2]]]
        else:
            for lens in dict_of_boxes[step[0][1]]:
                if lens[0] == step[0][0]:
                    lens[1] = step[2]
                    break
            else:
                dict_of_boxes[step[0][1]].append([step[0][0], step[2]])
    else:
        try:
            dict_of_boxes[step[0][1]] = list(filter(lambda lens: lens[0] != step[0][0], dict_of_boxes[step[0][1]]))
        except KeyError:
            pass
    print(dict_of_boxes)

answer = 0
for box_number in dict_of_boxes.keys():
    slot_number = 1
    for lens in dict_of_boxes[box_number]:
        answer += (box_number + 1) * slot_number * int(lens[1])
        slot_number += 1

print(answer)