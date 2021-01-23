'''https://adventofcode.com/2016/day/1'''
from collections import deque

# Import values
with open("input.txt", "r") as f:
    values = f.readline()

# Create a direction deque to rotate
q = deque("NESW")
# Set default coordinates
x = 0
y = 0
lastx = 0
lasty = 0
# Create an empty set of all visited places
visited = set()
found = False

# For each direction
for v in values.split(", "):
    # Rotate the dq to face the correct direction
    if v[0] == "R":  # If going right
        q.rotate(1)
    else:  # If going left
        q.rotate(-1)

    # Assumes steps are positive integers
    steps = int(v[1:])
    d = q[0]  # Find the direction which is the direction first in the dq
    if d == "N":  # If north
        y += steps  # Increase step counter
        if not found:  # If the intersection has not been found
            # Add each integer increment to the visited set
            for i in range(steps):
                # if the one being added is in the set then it will be the intersect
                if (x, lasty + i) in visited:
                    part2 = abs(x) + abs(lasty + i)
                    found = True
                else:  # no intersect found
                    visited.add((x, lasty + i))
            lasty = y
            
    elif d == "E":  # If east
        x += steps
        if not found:
            for i in range(steps):
                if (lastx + i, y) in visited:
                    part2 = abs(lastx + i) + abs(y)
                    found = True
                else:
                    visited.add((lastx + i, y))
            lastx = x

    elif d == "S":  # If south
        y -= steps
        if not found:
            for i in range(steps):
                if (x, lasty - i) in visited:
                    part2 = abs(x) + abs(lasty - i)
                    found = True
                else:
                    visited.add((x, lasty - i))
            lasty = y

    elif d == "W":  # If west
        x -= steps
        if not found:
            for i in range(steps):
                if (lastx - i, y) in visited:
                    part2 = abs(lastx - i) + abs(y)
                    found = True
                else:
                    visited.add((lastx - i, y))
            lastx = x


print("Part1: ", abs(x) + abs(y))
print("Part2: ", part2)
