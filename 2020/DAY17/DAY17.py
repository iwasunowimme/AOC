import re
from collections import defaultdict
from itertools import combinations
from itertools import permutations
from copy import deepcopy

# Import data from text file
with open("input.txt", "r") as f:
    values = [lines[:-1] for lines in f.readlines()]

#values = ['.#.','..#','###']

cubes = defaultdict(int)

par2cubes = defaultdict(int)
for i, value in enumerate(values):

    for j, val in enumerate(value):
        if val == "#":
            cubes[i - 1, j - 1, 0] = 1
            par2cubes[i - 1, j - 1, 0, 0] = 1
        else:
            cubes[i - 1, j - 1, 0] = 0
            par2cubes[i - 1, j - 1, 0, 0] = 0

height = i + 1
width = j + 1
depth = 1
height4 = i + 1
width4 = j + 1
depth4 = 1
dimension4 = 1



for _ in range(6):
    current_state = deepcopy(cubes)
    for x in range(-height, height):
        for y in range(-width, width):
            for z in range(-depth, depth+1):
                key = (x, y, z)
                total = 0
                for xAxis in [-1, 0, 1]:
                    for yAxis in [-1, 0, 1]:
                        for zAxis in [-1, 0, 1]:
                            if not (xAxis == 0 and yAxis == 0 and zAxis == 0):
                                total += current_state[xAxis + x, yAxis + y, zAxis + z]
                if current_state[key] == 1:
                    if total not in (2, 3):
                        cubes[key] = 0
                    else:
                        cubes[key] = 1
                else:
                    if total == 3:
                        cubes[key] = 1
    width += 1
    height += 1
    depth += 1

print(sum(cubes.values()))


for _ in range(6):
    current_state = deepcopy(par2cubes)
    for x in range(-height, height):
        for y in range(-width, width):
            for z in range(-depth, depth+1):
                for w in range(-dimension4, dimension4 + 1):
                    key = (x, y, z, w)
                    total = 0
                    for xAxis in [-1, 0, 1]:
                        for yAxis in [-1, 0, 1]:
                            for zAxis in [-1, 0, 1]:
                                for wAxis in [-1, 0, 1]:
                                    if not (xAxis == 0 and yAxis == 0 and zAxis == 0 and wAxis == 0):
                                        total += current_state[xAxis + x, yAxis + y, zAxis + z, wAxis + w]
                    if current_state[key] == 1:
                        if total not in (2, 3):
                            par2cubes[key] = 0
                        else:
                            par2cubes[key] = 1
                    else:
                        if total == 3:
                            par2cubes[key] = 1
    width += 1
    height += 1
    depth += 1
    dimension4 += 1

print(sum(par2cubes.values()))


