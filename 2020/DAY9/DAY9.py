'''https://adventofcode.com/2020/day/9'''
from itertools import combinations

# Input the values as ints into a list
with open("input.txt", "r") as f:
    vals = [int(line) for line in f.readlines()]

# Set the preamble to the first 25 digits
preamble = 25

for j in range(preamble, len(vals)):
    # Get a set of combinations from the the moving preamble then sum all pairs
    # Then see if the current number is part of the sum, "there" is a boolean to see if it is true at any point
    there = any([sum(i) == vals[j] for i in combinations(vals[j - preamble:j], 2)])
    if not there:  # Number did not have a sum
        weak = vals[j]
        print("Part1: ", weak)
        break


# Loop Through the entire list of values
for i in range(len(vals)):
    total = 0
    nums = i
    equals = False
    for j in range(i, len(vals)):  # Go through all values starting at i and add them and compare to weak number
        total += vals[j]
        if total == weak:  # We found the continuous set of numbers
            equals = True
            break
        elif total > weak:  # Number can not go down as no negative input numbers
            break
    if equals:  # If we have found it
        print("Part2: ", min(vals[i:j]) + max(vals[i:j]))
        break
