'''https://adventofcode.com/2015/day/13'''

import re
from itertools import permutations

# Read data from import file
with open("input.txt", "r") as f:
    vals = [lines[:-1] for lines in f.readlines()]

# Set a dictionary to conatin the happiness
happiness = {}
names = set()
# Use a RE to extract the data needed
p1 = re.compile("(\w+) would (\w+) (\d+) happiness units by sitting next to (\w+)")
for v in vals:
    name1, direction, value, name2 = p1.match(v).groups()
    if direction == "gain":  # Gain makes number positive, lose a negative
        happiness[name1, name2] = int(value)
    else:
        happiness[name1, name2] = -int(value)

    # Add names to set to get a list of all unique names
    names.add(name1)
    names.add(name2)

# Uses -inf for the case when the max gain is negative
max_gain = float("-inf")
for x in permutations(names, len(names)):  # Find all permutations of the names
    gain = []
    for i in range(len(x)):  # Add both directions of happiness
        gain.append(happiness[x[i], x[(i + 1) % len(x)]])
        gain.append(happiness[x[(i + 1) % len(x)], x[i]])
    # Keep only the largest
    max_gain = max(max_gain, sum(gain))

print("Part1: ", max_gain)

# Part2 we can insert ourself at the head of every combination and make it non-cyclic
max_gain = float("-inf")
for x in permutations(names, len(names)):  # Find all permutations of the names, same as part 1
    gain = []
    for i in range(len(x) - 1):  # Only go to the one before the end
        # This will get a-b,b-a for a so only need to go to len - 1
        gain.append(happiness[x[i], x[i + 1]])
        gain.append(happiness[x[i + 1], x[i]])
    max_gain = max(max_gain, sum(gain))

print("Part2: ", max_gain)
