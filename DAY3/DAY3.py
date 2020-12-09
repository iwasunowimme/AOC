'''https://adventofcode.com/2015/day/3'''

with open("input.txt","r") as f: # input values
    vals = f.readline()
y = 0
x = 0
visited = set()  # create a set top add house as "x:y" coordinates
visited.add(str(x)+":"+str(y))  # add the starting location


# created a function that is used to determine the outcome of each case
def move(x, y, direction) -> int:
    """
    uses the direction instruction to increment the correct coordinate

    :param x:  A x coordinate
    :param y:  A Y coordinate
    :param direction:  The direction to travel, one of the following ^,>,v,<
    :return both x and y coordinates:
    """
    if direction == "^":  # find the cases
        y += 1
    elif direction == ">":
        x += 1
    elif direction == "v":
        y -= 1
    elif direction == "<":
        x -= 1
    return x, y


for val in vals:
    x, y = move(x, y, val)
    visited.add(str(x) + ":" + str(y))

print("part1: ", len(visited))

# part2 using coordinates for both santas
santay = 0
santax = 0
roboy = 0
robox = 0
realSanta = True  # decides to case
visited = set()
visited.add(str(santax)+":"+str(santay))

for val in vals:
    if realSanta:  # changes between the santas via a boolean
        santax, santay = move(santax, santay, val)
        visited.add(str(santax) + ":" + str(santay))
        realSanta = False
    else:
        robox, roboy = move(robox, roboy, val)
        visited.add(str(robox) + ":" + str(roboy))
        realSanta = True

print("part2: ", len(visited))

