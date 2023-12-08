import functools
from enum import Enum
import math

def infinite_array_loop(arr):
    while True:
        for item in arr:
            yield item

def take_next_step(node, step):
    if step == 'R':
        return leaves[node][1]
    return leaves[node][0]

f = open("input.txt", "r")
lines = [line for line in f.read().splitlines()]

leaves = {}
instructions = lines[0]
lines = lines[2:]

for line in lines:
    key, value = line.split(' = ')
    left, right = value.replace("(", "").replace(")", "").split(', ')
    leaves[key] = (left, right)

total_steps = 0
simultaneous_nodes = list(filter(lambda x: x.endswith('A'), leaves.keys()))

def get_steps_to_zed(s):
    steps = 0
    gen = infinite_array_loop(list(instructions))
    while True:
        next_step = next(gen)
        s = take_next_step(s, next_step)
        steps += 1
        if s[2] == 'Z':
            break
    return steps


simultaneous_nodes = list(map(lambda node: get_steps_to_zed(node), simultaneous_nodes))
def find_lcm(x, y):
    return x * y // math.gcd(x, y)

answer = functools.reduce(find_lcm, simultaneous_nodes)
print(answer)

