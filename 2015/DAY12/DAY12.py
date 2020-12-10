'''https://adventofcode.com/2015/day/12'''

import re
import json

# Open and add to value
with open("input.txt", "r") as f:
    vals = [line[:-1] for line in f.readlines()][0]

# Find all digits or digits with a '-' preceding them
numbers = [int(m) for m in re.findall(r'\d+|-\d+', vals)]
print("part1: ", sum(numbers))

# Or as 1 line
print("part1: ", sum(map(int, re.findall(r'-?\d+', open("input.txt", "r").read()))))

# Create an object hook method to refuse any objects with red in them
def hook(obj):
    if "red" in obj.values():
        return {}
    else:
        return obj

# imports into a json using object hook to parse only non "red" containing
json_vals = str(json.loads(vals, object_hook=hook))
print("part1: ", sum(map(int, re.findall(r'-?\d+', json_vals))))

