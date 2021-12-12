# The Advent of Code challenge for day 9
# https://adventofcode.com/2021/day/9

from itertools import combinations
import numpy as np
#Read in the file and return a list of all the integers
def readFile():
    with open("DAY09/input.txt", "r") as f:
        return [line.strip("\n") for line in f.readlines()]

vals = readFile()
rows = len(vals)
cols = len(vals[0])

# Craeate a 2d array of points using tuple assinged dict
m = {}
for i,line in enumerate(vals):
    for j,num in enumerate(line):
        m[i,j] = int(num)

    

lows = []
lows_cords = []

# Solve for the surounding values
def solve(i,j):
    x = [i + x for x in [-1,0,1]]
    y = [j + x for x in [-1,0,1]]   
    for xx in x:
        if xx >= 0 and xx < rows: # if xx in grid
            for yy in y:
                if yy >= 0 and yy < cols: # If yy in grid
                    if not(xx == i and yy == j): # if not the value we are looking at
                        if m[xx,yy] < m[i,j]:  # Return false if there is a surrouding point lower
                            return False
    return True  # No surrounding points lower

# For each number in the grid
for i in range(rows):
    for j in range(cols):
        if solve(i,j): # Find if it is a low point
            lows.append(m[i,j]) # iF lowpoint add it to the list
            lows_cords.append((i,j))  # add coords for part 2

print(f"Part 1: {sum(lows)+len(lows)}")


# Helper function to find all non-9 values that this point can see
# Return list of all values that can be see from here in NSEW cardinal directions
def r_around(i,j):
    visible = []
    checks = [(i,j-1),(i,j+1),(i-1,j),(i+1,j)]
    for check in checks:
        xx,yy = check[0],check[1]
        if xx >= 0 and xx < rows: # If xx in grid
            if yy >= 0 and yy < cols: # If yy in grid
                if m[xx,yy] != 9:  # If the point isn't a 9
                    visible.append(check)
    return visible 

# Part 2 solver to use breath first approach to find size of basin
def solve_2(i,j):
    # Keep track of where we have gone
    visited = set()
    # Starting point at the basins
    to_visit = [(i,j)]
    while to_visit:  # While there is alist of places to visit left
        curr = to_visit.pop()  # remove from list
        visited.add(curr)
        new_to = r_around(curr[0],curr[1])  # Find all values that can be seen from here
        for n in new_to:
            if n not in visited:  # We will visit only if we havent seen it yet
                to_visit.append(n)
    return len(visited)



# # Since each basin only has 1 low point, use the them as the starting coords
basins = [solve_2(low[0],low[1]) for low in lows_cords]

print(f"Part 2: {np.prod(sorted(basins)[-3:])}")

