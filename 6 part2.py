import functools
from sympy import symbols, Eq, solve
import math

f = open("input.txt", "r")
lines = [line for line in f.read().splitlines()]
times_and_distances = list(zip([int(x) for x in lines[0].split()[1:]], [int(x) for x in lines[1].split()[1:]]))

def get_max_distance_for_charge_time_and_race_time(charge_time, race_time):
    time_left = (race_time - charge_time)
    return time_left * charge_time

a, b, c, x = symbols('a b c x')

x1, y1 = 0, get_max_distance_for_charge_time_and_race_time(0, times_and_distances[0][0])
x2, y2 = 2, get_max_distance_for_charge_time_and_race_time(2, times_and_distances[0][0])
x3, y3 = 3, get_max_distance_for_charge_time_and_race_time(3, times_and_distances[0][0])

eq1 = Eq(a * x1**2 + b * x1 + c, y1)
eq2 = Eq(a * x2**2 + b * x2 + c, y2)
eq3 = Eq(a * x3**2 + b * x3 + c, y3)

solution = solve((eq1, eq2, eq3), (a, b, c))

# Create the quadratic equation
quadratic_equation = solution[a] * x**2 + solution[b] * x + solution[c] - times_and_distances[0][1]
a = solution[a]
b = solution[b]
c = -times_and_distances[0][1]

discriminant = b ** 2 - 4 * a * c

if discriminant >= 0:
    # Calculate the two roots
    x1 = (-b + math.sqrt(discriminant)) / (2 * a)
    x2 = (-b - math.sqrt(discriminant)) / (2 * a)

    distance = abs(x1 - x2)
    print( distance)
