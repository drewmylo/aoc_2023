import functools
import queue
import sys

def get_mapping(dest, src, stp, input):
    if src <= input <= (src + stp):
        return dest + input - src
    return None

f = open("input.txt", "r")

mappings = []
local_mappings = []

lines = [line for line in f.read().splitlines()]
seeds = []
locations = []
iterator = iter(lines)
in_loc = False
try:
    while True:
        line = next(iterator)
        if line.startswith('seeds'):
            seeds = line.split(' ')
            seeds = seeds[1:]
            seeds = [int(x) for x in seeds]
            print(seeds)
        if '-' in line and len(local_mappings) != 0:
            if line.startswith('humidity'):
                in_loc = True
            mappings.append([x for x in local_mappings])
            local_mappings = []
        if line.split(' ')[0].isdigit():
            destination, source, step = line.split(' ')
            local_mappings.append(functools.partial(get_mapping, int(source), int(destination), int(step)))
            if in_loc:
                locations.append((int(destination), int(step)))
except StopIteration:
    mappings.append([x for x in local_mappings])

lowest_location_number = sys.maxsize
mappings.reverse()
seeds_with_range = []
for x in range(0, len(seeds), 2):
    seeds_with_range.append((seeds[x], seeds[x + 1]))

sorted_destinations = sorted(locations, key=lambda x: x[0])

for location in sorted_destinations:
    for location_x in range(location[0], location[0] + location[1]):
        for mapping_set in mappings:
            for mapping_func in mapping_set:
                mapping = mapping_func(location_x)
                if mapping is not None:
                    location_x = mapping
                    break
        for seed in seeds_with_range:
            if seed[0] <= location_x <= seed[0] + seed[1]:
                print(location_x)
                exit()