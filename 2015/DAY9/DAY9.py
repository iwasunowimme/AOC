'''https://adventofcode.com/2015/day/9'''
import re
from itertools import permutations

with open("input.txt", "r") as f:
    vals = [lines[:-1] for lines in f.readlines()]


# Create a re compiler to get
p1 = re.compile('(\w+) to (\w+) = (\d+)')

# Create a dictionary for the routes
routes = {}
places = set()  # Create a set of all places that are possible
for i in [p1.match(val).groups() for val in vals]:
    routes[i[0], i[1]] = int(i[2])
    routes[i[1], i[0]] = int(i[2])  # Added in with keys reversed to save on having to compare keys for neatness
    places.add(i[0])
    places.add(i[1])

minDistance = float("inf")  # Set min distance to a really large number
maxDistance = 0  # Set max distance to 0 as we can never go negative

# Use a permutation of all places to brute force, every point connects to one another
for perm in permutations(places, len(places)):  # Find all permutations that uses all of the places
    dist = 0
    for p in range(len(perm) - 1):  # For each pair in the permutation
        dist += routes[perm[p + 1], perm[p]]
    minDistance = min(minDistance, dist)
    maxDistance = max(maxDistance, dist)
print("Part1: ", minDistance)
print("Part2: ", maxDistance)





