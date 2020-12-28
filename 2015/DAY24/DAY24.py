'''https://adventofcode.com/2015/day/24'''
from itertools import combinations
from functools import reduce


# Input the values from the file
def readValues():
    with open("input.txt", "r") as f:
        return [int(lines[:-1]) for lines in f.readlines()]


def solve(values, split) -> int:
    # Get the weight as the sum of all divided by the split
    weight = sum(values) // split
    # We get the max numbers, which is the smallest combination of numbers, as the length divided by the split
    max_numbers = len(values) // split
    # Set the min as really high
    minz = float('inf')
    # For combination length i in range 1 to max numbers inclusive
    for i in range(1, max_numbers + 1):
        # For combinations of values
        for comb in combinations(values, i):
            # If the sum is the weight
            if sum(comb) == weight:
                # Comapre the minimums
                minz = min(minz, reduce((lambda x, y: x * y), comb))
    return(minz)


if __name__ == '__main__':
    values = readValues()
    print("Part1: ", solve(values, 3))
    print("Part2: ", solve(values, 4))