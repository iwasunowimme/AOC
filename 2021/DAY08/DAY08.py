# The Advent of Code challenge for day 8
""" https://adventofcode.com/2021/day/8 """
import time
import re
from collections import defaultdict
from functools import lru_cache
#Read in the file and return a list of all the integers
def readFile() -> list:
    with open("DAY08/input.txt", "r") as f:
        return [line.strip("\n") for line in f.readlines()]

# Decode outputs based on inputs
def decode(ins,outs):
    # Create a dictionary of length to coded message, only need numbers 1 and 4 though
    coded = {len(code): set(code) for code in ins if len(code) in [2,4]}
    num = ''
    # For each output build answer based on set operations
    for out in outs:
        l = len(out)
        if   l == 2: num += '1'
        elif l == 3: num += '7'
        elif l == 4: num += '4'
        elif l == 7: num += '8'
        elif l == 5:
            if   len(coded[2] & set(out)) == 2: num += '3'
            elif len(coded[4] & set(out)) == 3: num += '5'
            else                              : num += '2'
        else:
            if   len(coded[4] & set(out)) == 4: num += '9'
            elif len(coded[2] & set(out)) == 2: num += '0'
            else                              : num += '6'

    return int(num)





vals = readFile()

count = 0
summer = 0
for each in vals:
    i, o = each.split(" | ")  # Split the input and outputs
    #Part 1
    # For each output, split into it sections and sum how many have length 2,3,4,7
    count += sum(1 for item in o.split() if len(item) in [2,3,4,7])
    
    #part 2
    # Return the value of the decode for each input and output
    summer += decode(i.split(),o.split())

print(f"Part 1: {count}")
print(f"Part 2: {summer}")
