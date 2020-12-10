'''https://adventofcode.com/2015/day/17'''
from itertools import combinations

# Import data from file
with open("input.txt", "r") as f:
    vals = [int(lines[:-1]) for lines in f.readlines()]

#vals = [20, 15, 10, 5, 5]  # Test input

# Set eggnog as per specs, total capacity of bags
eggnog = 150

def eggy(vals, egg) -> int:
    '''
    A recursive function that counts all combinations of vals that equal egg
    :param vals: A list of items that contain the values of the containers
    :param egg: the value remaining that can fit i
    :return: Count of all combinations, base case is when current value - remaining value = 0
    '''
    count = 0
    # Loop through all available values
    for i in range(len(vals)):
        if vals[i] < egg:
            count += eggy(vals[i+1:], egg - vals[i])
        elif vals[i] == egg:  # Base case, no more eggnog left
            count += 1
    return count


print("part1: ", eggy(vals, eggnog))
# A one liner using combinations and list comprehension
print("part1: ", sum(1 for x in range(len(vals)) for perm in combinations(vals, x) if sum(perm) == eggnog))

# Use combinations of increasing size to find the minimum size that is available
for x in range(len(vals)):  # Max size is the full list
    count = 0
    # Find all combinations of x digits in the values
    for perm in combinations(vals, x):
        if sum(perm) == eggnog:
            count += 1
    # Breaks out whenever there is more than 0 combinations at a specific x
    if count:
        break
print("Part2: ", count)
