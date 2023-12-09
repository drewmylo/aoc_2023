import functools
import math


f = open("input.txt", "r")
lines = [list(map(lambda x: int(x), line.split(' '))) for line in f.read().splitlines()]

def get_rate_of_change(fst, array):
    if len(array) == 0:
        return []
    return [array[0] - fst] + get_rate_of_change(array[0], array[1:])

def get_next_number(line):
    next_number = line[0]
    rate_of_change = line
    alternator = 1
    while not all(x == 0 for x in rate_of_change):
        alternator *= -1
        rate_of_change = get_rate_of_change(rate_of_change[0], rate_of_change[1:])
        next_number += rate_of_change[0] * alternator
    return next_number

print(functools.reduce(lambda a, b: a + b, map(lambda x: get_next_number(x), lines)))
