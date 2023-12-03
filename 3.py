# import functools
# f = open("input.txt", "r")
#
# lines = [line for line in f.read().splitlines()]
#
# def is_special(char):
#     return (not char is None) and (not char.isalnum()) and (char != '.')
#
# def get_char_from_coordinates_safely(y, x):
#     try:
#         return lines[y][x]
#     except IndexError:
#         return None
#
# def search_for_special_character(x, y, already_has_special_character):
#     # top
#     # bottom
#     # left
#     # right
#     # top left diagonal
#     # top right diagonal
#     # bottom left diagonal
#     # bottom right diagonal
#     return already_has_special_character or \
#         is_special(get_char_from_coordinates_safely(y - 1, x)) or \
#         is_special(get_char_from_coordinates_safely(y + 1, x)) or \
#         is_special(get_char_from_coordinates_safely(y, x - 1)) or \
#         is_special(get_char_from_coordinates_safely(y, x + 1)) or \
#         is_special(get_char_from_coordinates_safely(y - 1, x - 1)) or \
#         is_special(get_char_from_coordinates_safely(y - 1, x + 1)) or \
#         is_special(get_char_from_coordinates_safely(y + 1, x - 1)) or \
#         is_special(get_char_from_coordinates_safely(y + 1, x + 1))
#
#
# my_nums = []
# for y in range(len(lines)):
#     current_number = ''
#     has_special_character = False
#     for x in range(len(lines[y])):
#         if lines[y][x].isdecimal():
#             current_number += lines[y][x]
#             has_special_character = search_for_special_character(x, y, has_special_character)
#         elif ((not lines[y][x].isdecimal()) or x > len(lines[y][x]) - 1) and current_number != '':
#             if has_special_character:
#                 my_nums.append(int(current_number))
#             current_number = ''
#             has_special_character = False
#     if has_special_character:
#         my_nums.append(int(current_number))
#
# print(functools.reduce((lambda x, y: x + y), my_nums))


import functools
f = open("input.txt", "r")

lines = [line for line in f.read().splitlines()]

def is_special(y, x):
    if y < 0 or x < 0:
        return None
    try:
        return (not lines[y][x] is None) and (lines[y][x] == '*')
    except IndexError:
        return None

def search_for_special_character(x, y, already_has_special_character):
    # top
    # bottom
    # left
    # right
    # top left diagonal
    # top right diagonal
    # bottom left diagonal
    # bottom right diagonal
       if is_special(y - 1, x):
            return (y - 1, x)
       if is_special(y + 1, x):
            return (y + 1, x)
       if is_special(y, x - 1):
            return (y, x - 1)
       if is_special(y, x + 1):
            return (y, x + 1)
       if is_special(y - 1, x - 1):
            return (y - 1, x - 1)
       if is_special(y - 1, x + 1):
            return (y - 1, x + 1)
       if is_special(y + 1, x - 1):
            return (y + 1, x - 1)
       if is_special(y + 1, x + 1):
            return (y + 1, x + 1)
       return already_has_special_character

my_gears = {}
for y in range(len(lines)):
    current_number = ''
    curr = (None, None)

    for x in range(len(lines[y])):
        if lines[y][x].isdecimal():
            current_number += lines[y][x]
            curr = search_for_special_character(x, y, curr)
        elif ((not lines[y][x].isdecimal()) or x > len(lines[y][x]) - 1) and current_number != '':
            if curr:
                my_gears.setdefault(curr, []).append(int(current_number))
                curr = (None, None)
            current_number = ''
    if curr != (None, None):
        my_gears.setdefault(curr, []).append(int(current_number))
        current_number = ''
        curr = (None, None)

del my_gears[(None, None)]
gears_multiplied = []
for key in my_gears.keys():
    if len(my_gears[key]) > 1:
        gears_multiplied.append(functools.reduce((lambda x, y: x * y), my_gears[key]))

print(functools.reduce((lambda x, y: x + y), gears_multiplied))
