'''https://adventofcode.com/2015/day/6'''

# Import values from file
with open("input.txt", "r") as f :
    vals = [lines[:-1] for lines in f.readlines()]

import re

# set up 2 re commands to separate the string values and int values needed
p1 = re.compile('(turn on|turn off|toggle)')
p2 = re.compile('.* (\d+),(\d+) through (\d+),(\d+)')

lights = {}
# create a blank map for all possible values
for i in range(1000):
    for j in range(1000):
        lights[i, j] = 0

# go through instructions
for val in vals:
    op = ''.join(p1.match(val).groups())
    x1, y1, x2, y2 = tuple([int(m) for m in p2.match(val).groups()])
    if op == "turn on":
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                lights[i, j] = 1  # set light to on (1)
    elif op == "turn off":
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                lights[i, j] = 0  # set light to off (0)
    elif op == "toggle":
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                lights[i, j] = 1 - lights[i, j]  # Toggle light from 1 to 0 or 0 to 1 (1-1=0,1-0=1)
count = 0
for item in lights:
    count += lights[item]  # Add all 1's (on lights)
print("part1: ", count)

# Recreate blank light array
for i in range(1000):
    for j in range(1000):
        lights[i, j] = 0
for val in vals:
    # Get instructions
    op = ''.join(p1.match(val).groups())
    x1, y1, x2, y2 = tuple([int(m) for m in p2.match(val).groups()])
    if op == "turn on":
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                lights[i, j] += 1  # Increment by 1 when light is on
    elif op == "turn off":
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                lights[i, j] -= 1  # Decrement by 1 when light is off
                if lights[i, j] < 0:  # Check if light brightness decreases below 0 and resets if it does
                    lights[i, j] = 0
    elif op == "toggle":
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                lights[i, j] += 2  # If toggle increment by 2

count = 0
for item in lights:
    count += lights[item]
print("part2: ", count)

