import functools

f = open("input.txt", "r")
lines = [line for line in f.read().splitlines()]
times_and_distances = list(zip([int(x) for x in lines[0].split()[1:]], [int(x) for x in lines[1].split()[1:]]))

def get_max_distance_for_charge_time_and_race_time(charge_time, race_time):
    time_left = (race_time - charge_time)
    return time_left * charge_time

global_ways_to_win = []

for race in times_and_distances:
    ways_to_win = 0
    for charge_time in range(0, race[0]):
        if get_max_distance_for_charge_time_and_race_time(charge_time, race[0]) > race[1]:
            ways_to_win += 1
    global_ways_to_win.append(ways_to_win)
    ways_to_win = 0

print(functools.reduce(lambda x, y: x * y, global_ways_to_win))