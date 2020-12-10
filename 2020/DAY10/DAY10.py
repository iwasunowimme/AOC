'''https://adventofcode.com/2020/day/10'''
from collections import defaultdict

# Import data from file, list of ints
with open("input.txt", "r") as f:
    vals = [int(lines[:-1]) for lines in f.readlines()]

# Test values
# vals = [28,33,18,42,31,14,46,20,48,47,24,23,49,45,19,38,39,11,1,32,25,35,8,17,7,9,4,2,34,10,3]
# vals = [16,10,15,5,1,11,7,19,6,12,4]

# Add 0 to the list and the outlet value (max + 3)
vals.append(0)
vals.sort()
vals.append(vals[-1] + 3)

# Initialise counters for differences of 1 and 3
dif1 = 0
dif3 = 0

# Iterate through all values till last - 1 due to looking at i and i++ at the same time
for i in range(len(vals) - 1):
    if vals[i+1] - vals[i] == 1:
        dif1 += 1
    elif vals[i + 1] - vals[i] == 3:
        dif3 += 1
dif3 += 1
print("part1: ", dif1*dif3)


# Initially this was completed using a recursive method and memoization
# This method counts backwards from the end of the list
def valid(valus, combos) -> int:
    '''
    Recursively finds all combinations of first value in list by find all availble to
    the ones it can reach, difference of 1, 2, or 3
    :param valus: A List of ints
    :param combos: A memory for combinations that have been found, uses a hash based on the values in the list
    this is ''.join([str(m)+"-" for m in valus[x:]])
    :return: The amount of combinations that the sub-array can do
    '''

    #

    ways = 0
    # Base case, return 1 as a single number can only be in 1 combination
    if len(valus) == 1 or isinstance(valus, str):
        return 1

    # if there are only 2 numbers left in the array, only need to check the difference of the first 2
    if len(valus) == 2:
        # If the value has a certain difference find the combinations
        if valus[1] - valus[0] == 1 or valus[1] - valus[0] == 2 or valus[1] - valus[0] == 3:
            if ''.join([str(m)+"-" for m in valus[2:]]) not in combos.keys():  # Not known so calculate
                ways += valid(valus[1:], combos)
            else:  # Combinations of sub-array are known, retrieve the known value
                ways += combos[''.join([str(m)+"-" for m in valus[2:]])]

    # if there are only 3 numbers left in the array, only need to check the difference of the first 3
    if len(valus) == 3:

        if valus[2] - valus[0] == 2 or valus[2] - valus[0] == 1:
            if ''.join([str(m)+"-" for m in valus[2:]]) not in combos.keys():
                ways += valid(''.join([str(m)+"-" for m in valus[2:]]), combos)
            else:
                ways += combos[valus[2:]]
        if valus[1] - valus[0] == 1 or valus[1] - valus[0] == 2 or valus[1] - valus[0] == 3:
            if ''.join([str(m)+"-" for m in valus[2:]]) not in combos.keys():
                ways += valid(valus[1:], combos)
            else:
                ways += combos[''.join([str(m)+"-" for m in valus[2:]])]

    # if there are only more than 2 numbers left, find which ones are available
    if len(valus) > 3:
        if valus[3] - valus[0] == 3:
            if ''.join([str(m)+"-" for m in valus[3:]]) not in combos.keys():
                ways += valid(valus[3:], combos)
            else:
                ways += combos[''.join([str(m)+"-" for m in valus[3:]])]
        if valus[2] - valus[0] == 2 or valus[2] - valus[0] == 1:
            if ''.join([str(m)+"-" for m in valus[2:]]) not in combos.keys():
                ways +=valid(valus[2:], combos)
            else:
                ways += combos[''.join([str(m)+"-" for m in valus[2:]])]
        if valus[1] - valus[0] == 1 or valus[1] - valus[0] == 2 or valus[1] - valus[0] == 3:
            if ''.join([str(m)+"-" for m in valus[1:]]) not in combos.keys():
                ways +=valid(valus[1:], combos)
            else:
                ways += combos[''.join([str(m)+"-" for m in valus[1:]])]

    # Store this in the dictionary
    combos[''.join([str(m)+"-" for m in valus])] = ways
    return ways

# Create empty dictionary to be used
combos = {}
# Run the method and print it's results
print("part2: ", valid(vals, combos))

# Part 2 repeated using a default dictionary
# Create the dictionary
options = defaultdict(int)
# Only 1 combination for 0
options[0] = 1
# Iterates for all values after the initial 0
for v in vals[1:]:
    # sums the possible combination of all predecessors that can be reached in 1, 2, 3 steps
    options[v] = options[v-1] + options[v-2]+options[v-3]

print("my dynamic programing part2: ", options[vals[-1]])
