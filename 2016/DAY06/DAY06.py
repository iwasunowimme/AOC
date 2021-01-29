'''https://adventofcode.com/2016/day/6'''
from collections import Counter

# Import from text file
with open("input.txt", "r") as f:
    values = [lines[:-1] for lines in f.readlines()]

# find the most common of each column
# Zip(*) transposes the array
# Join makes it a string
print("Part1:", ''.join(Counter(''.join(x)).most_common()[0][0] for x in zip(*values)))
print("Part2:", ''.join(Counter(''.join(x)).most_common()[-1][0] for x in zip(*values)))



