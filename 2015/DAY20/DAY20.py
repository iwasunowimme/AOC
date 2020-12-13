'''https://adventofcode.com/2015/day/20'''

from math import sqrt
from collections import defaultdict
import time

# The input data
target = 33100000
t1 = time.time()

# Set a total for the count
total = 0
# estimated lower bound from trial and error (Start at 1 for brute force)
z = 700000
# Find the first value that is greater than the total
while total < target:
    z += 1
    total = 0
    # Find the sqrt to limit range and addition
    sqr = int(sqrt(z))
    # Only go to sqrt as we are adding both sides of the factor
    # For example, if z is 16 we add 8 when we reach 2 so no need to go above 4
    for i in range(1, sqr + 1):
        if z % i == 0:
            if i == sqr:  # Only want to add the sqr once
                total += 10*sqr
            else:  # Add both size of the fraction
                total += 10*(i + z // i)

print("Part1:", z)


t2 = time.time()


total = 0
z = 700000
while total < target:
    z += 1
    total = 0
    sqr = int(sqrt(z))
    for i in range(1, sqr + 1):
        if z % i == 0:
            if i == sqr and z % sqr == 0:
                total += 11 * sqr
            else:
                if z < 50 * i:
                    total += 11 * i

                if z < 50 * (z // i):
                    total += 11 * (z // i)

print("Part2: ", z)

t3 = time.time()


# Choose a relatively high upper bound
upper_bound = 1000000
# Create a default dictionary to add houses
houses = defaultdict(int)

# Go from 1 to target as target will 100% include the value
for elf in range(1, target):
    # Go from the elf number to the upper bound in range of the number elf that we are on
    for house in range(elf, upper_bound, elf):
        # Increase the value at that house by 10 times the number of the eld
        houses[house] += elf * 10

    # check the value at the house we are on and leave if it is right
    if houses[elf] >= target:
        print("DD part 1: ", elf)
        break

t4 = time.time()

houses = defaultdict(int)
# Go from 1 to target as target will 100% include the value
for elf in range(1, target):
    for house in range(elf, min(elf * 50 + 1, upper_bound), elf):  # Only go to the first 50
        houses[house] += elf * 11

    # check the value at the house we are on and leave if it is right
    if houses[elf] >= target:
        print("DD part 2: ", elf)
        break
t5 = time.time()
print("Part1 time for finding factors", t2-t1)
print("Part2 time for finding factors", t3-t2)
print("Part1 time with default dictionary DP approach: ", t4-t3)
print("Part2 time with default dictionary DP approach: ", t5-t4)
print("We can see that the default dictionary approach is a lot faster.")
print("If we started the factor finding approach from 1 instead of 700,000 it would be a lot slower than this.")
print("Part 2 for the DD apraoch is a lot faster due to the fact we are only adding the first 50 instead of close to 1 mil")


