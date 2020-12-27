'''https://adventofcode.com/2020/day/24'''

from collections import defaultdict
from copy import deepcopy

# Import data from text file
with open("input.txt", "r") as f:
# with open("example.txt", "r") as f:
    values = [lines[:-1] for lines in f.readlines()]

# Create a default dictionary for the tile colours
tiles = defaultdict(int)
# Find the max values of the x and y
maxx = 0
maxy = 0
# For each input
for v in values:
    # We set the hex grid up as normal then slide the y + 1 row over,
    # so 'ne' is directly above and 'nw' is one across
    # We do the converse on the y - 1 row, so 'sw' is directly bellow and 'se' is one across

    # Calculate the x but finding the difference of east and west
    # Since the slide of rows, east = (count(e) - (count(ne) + count(se)) + count(se)
    # Since the slide of rows, west = (count(e) - (count(nw) + count(sw)) + count(nw)
    x = (v.count('e') - v.count('ne')) - (v.count('w') - v.count('sw'))
    y = v.count('n') - v.count('s')
    # Alternate 1 and 0 on the x, y tile
    tiles[x, y] = 1 - tiles[x, y]
    # Keep track of the max values
    maxx = max(maxx, abs(x))
    maxy = max(maxy, abs(y))

print("Part1: ", sum(tiles.values()))

# List of direction offsets to be used
dirs = [(-1, 1), (0, 1), (-1, 0), (1, 0), (0, -1), (1, -1)]
# For 100 iterations
for _ in range(100):
    # Increase max x and y, increased at start due to us needing to start +1 from the max
    maxx += 1
    maxy += 1
    # Create deepcopy of current values
    current = deepcopy(tiles)
    # for all in range [-maxx,-maxy] to [maxx+1, maxy+1]
    for row in range(-maxx, maxx+1):
        for col in range(-maxy, maxy + 1):
            # Since we saved the black state as 1 we can just sum the 1,s to find
            total = sum([current[k] for k in [(x + row, y + col) for x, y in dirs]])

            # If is black, and neighbours == 1 or > 2, flip to white (0)
            if current[row, col] == 1:
                if total == 0 or total > 2:
                    tiles[row, col] = 0
            # If is white, and neighbours = 2  flip to black (1)
            else:
                if total == 2:
                    tiles[row, col] = 1

print("Part2: ", sum(tiles.values()))

