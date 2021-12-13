# The Advent of Code challenge for day 13
""" https://adventofcode.com/2021/day/13 """
import time
import re
from collections import defaultdict
from itertools import combinations,zip_longest
from functools import lru_cache
from collections import deque 
from copy import deepcopy
#Read in the file and return a list of all the integers
def readFile():
    with open("DAY13/input.txt", "r") as f:
        return [line.strip("\n") for line in f.readlines()]

vals = readFile()
def print_grid(grid):
    for row in grid:
        for char in row:
            print("█" if char == 1 else ' ',end='')
        print()

numb = True
part1 = True
flips = []
maxy = 0
maxx = 0
points = {}
for line in vals:
    if numb:
        if line: # if valid line
            x,y = map(int, line.split(","))
            maxx=max(x,maxx)
            maxy=max(y,maxy)
            points[x,y] = 1
        else: # INput flips to instructions after first blank line
            numb = False
            # Create a list of points and set to 0 if not in the input
            paper = [[points.get((i,j),0) for i in range(maxx+1)] for j in range(maxy+1)]
    else:
        xy, no = line.split()[-1].split("=")
        no = int(no)

        if xy == 'x':
            # For each row do a or with the row zipped by itself
            paper = [[i or j for i,j in zip(row[:no],row[:no:-1])] for row in paper] 

        elif xy == 'y':
            # For each row find its corresponding flip and check and do an or operation
            paper = [[i or j for i,j in zip(row_top,row_bottom)] for row_top, row_bottom in zip(paper[:no],paper[:no:-1])] 
        if part1:
            print(f"Part 1: {sum([sum(row) for row in paper])}")
            part1 = False

print("Part 2:")
print_grid(paper)