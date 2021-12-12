# The Advent of Code challenge for day 6
""" https://adventofcode.com/2021/day/6 """
import time
import re
from collections import defaultdict
from functools import lru_cache
#Read in the file and return a list of all the integers
def readFile():
    with open("DAY06/input.txt", "r") as f:
        return [line.strip("\n") for line in f.readlines()]

vals = [int(x) for x in readFile()[0].split(",")]



# Use caching for memoization and do a recursive method
@lru_cache(maxsize=None)
def life(days_left, counter):
    # Base case, no more days left so return 1 fish, itself
    if days_left == 0:
        return 1
    c = counter - 1
    if c == -1: # if it has a baby return itself reset to 6 and all its babies' offsprings set to 8
        return life(days_left-1,6) + life(days_left-1,8)
    else: # continue
        return life(days_left-1,c)


v = [0,1,2,3,4,5,6]
for n in [80,256]:
    # Find the amount of fish each possible starting point will generate
    # So we only do 6 times in total not len(input) times
    scores = {each: life(n,each) for each in v}
    # For each input fish find the relevant sscore and add to total
    score = sum(scores[each] for each in vals)

    print(n,score)
    



    