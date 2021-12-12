# The Advent of Code challenge for day 7
""" https://adventofcode.com/2021/day/7 """
import time
import re
from collections import defaultdict
#Read in the file and return a list of all the integers
def readFile():
    with open("DAY07/input.txt", "r") as f:
        return [line.strip("\n") for line in f.readlines()]
vals = [int(x) for x in readFile()[0].split(",")]

m_list = [i for i in range(min(vals),max(vals))]  # list of all potential values in the range


part1 = defaultdict(int)
part2 = defaultdict(int)
# Find an array of all values for each value and add it to the corresponding location
for x in vals: 
    for y in m_list:
        diff = abs(x-y)
        part1[y] += diff
        part2[y] += (diff*(diff+1))//2

# Part 1 
part1_small = float('inf')
for _,v in part1.items():
    part1_small = min(part1_small,v)
print(f"Part 1: {part1_small}")
# Part 2
part2_small = float('inf')
for _,v in part2.items():
    part2_small = min(part2_small,v)
print(f"Part 2: {part2_small}")


# Maths approach 
import numpy as np
median = np.median(vals)
print(f"Part 1: use median to find number {sum([int(abs(x-median)) for x in vals])}")
mean = int(np.mean(vals))
max_mean_group = float('inf')
slice = [-2,-1,0,1,2]
for sect in slice:
    max_mean_group = min(max_mean_group,sum([(abs(sect+mean-x)*(abs(sect+mean-x) + 1))//2 for x in vals]))
print(f"Part 2: uses a window around the mean {max_mean_group}")

    