'''https://adventofcode.com/2016/day/7'''
import re

# Import data from text file
with open("input.txt", "r") as f:
    values = [lines[:-1] for lines in f.readlines()]

# Create lists to hold answers
sep = []
# Set to remove duplicates if already found one answer
ssl_ = set()
# For each value
for v in values:

    # Split to two lists for ones inside and outside '[]'
    left = []
    right = []

    # For each value split by '['
    for x in v.split('['):
        # Split again by closing ']'
        y = x.split("]")
        if len(y) > 1:  # If first value
            right.append(y[0])
            left.append(y[1])
        else:  # Other tuples
            left.append(y[0])

    # Create booleans to test if we have the form abba for both left and right lists
    left_count = False
    right_count = False

    # For the left list
    for l in left:
        for i in range(len(l) - 3):  # Got to -3 to avoid index out of bounds
            # if in form 'abba' and not 'aaaa'
            if l[i] == l[i+3] and l[i + 1] == l[i + 2] and l[i] != l[i + 1]:
                left_count = True
    # For the left list
    for r in right:
        for i in range(len(r) - 3):
            # if in form 'abba' and not 'aaaa'
            if r[i] == r[i+3] and r[i + 1] == r[i + 2] and r[i] != r[i + 1]:
                right_count = True

    # If abba in left list and not right
    if left_count and not right_count:
        sep.append(v)

    # Create set of all valid 'aba'
    ssl = set()
    ssl_count = False
    # Go through left first to populate valid ssl
    for l in left:
        for i in range(len(l) - 2):
            if l[i] == l[i+2] and l[i] != l[i+1]:
                ssl.add(l[i+1] + l[i] + l[i+1])  # Add the inverse
    for r in right:
        for i in range(len(r) - 2):
            if r[i] + r[i+1] + r[i + 2] in ssl:  # If  'bab' in the list
                ssl_.add(v)

# Print the count of all valid answers
print("Part1: ", len(sep))
print("Part2: ", len(ssl_))


''' Credit to Reddit user barnybug'''
# a function to determine if 'abba' is in each list
def abba(x):
    return any(a == d and b == c and a != b for a, b, c, d in zip(x, x[1:], x[2:], x[3:]))
# Split the lines based on the regex
lines = [re.split(r'\[([^\]]+)\]', line) for line in open('input.txt')]
# Split the lines list to have a left and right side
parts = [(' '.join(p[::2]), ' '.join(p[1::2])) for p in lines]
# Sum all that have abba in left and not in right list
print("barnybug's Answer #1:", sum(abba(sn) and not(abba(hn)) for sn, hn in parts))
# Sum all that have the aba in left and bab in right
print("barnybug's Answer #2:", sum(any(a == c and a != b and b+a+b in hn for a, b, c in zip(sn, sn[1:], sn[2:])) for sn, hn in parts))
