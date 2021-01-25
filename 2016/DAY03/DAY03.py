'''https://adventofcode.com/2016/day/3'''


# Import data from text file
with open("input.txt", "r") as f:
    values = [lines[:-1] for lines in f.readlines()]

# PART 1
# Set empty counter for valid triangles
valid = 0
# Set a column array to add all the edges to it
cols = []

# For each value in the input
for v in values:
    # Get the edges from the input by splitting on white spaces and mapping to int
    edges = [int(x) for x in v.split()]
    # Find if valid triangle by seeing if the two smaller edges add to larger than the larges
    # Formula is largest < smallest + second smallest, the smallest and second smallest sum to all edges minus the max
    # can rearrange to 2*larges < sum of all
    if 2 * max(edges) < sum(edges):
        valid += 1  # increase counter
    # Append the edges to array
    cols.append(edges)
print("Part1:", valid)

# PART 2
# Reset counter
valid = 0
for i in range(3):  # for 3 columns
    # Iterate through the length of the edges
    # Assumes that there is a multiple of 3 column lengths and does not wrap to next column
    for j in range(0, len(cols), 3):
        # Create an edges list to be able to use same format as part 1
        edges = [cols[j][i], cols[j+1][i], cols[j+2][i]]
        if 2 * max(edges) < sum(edges):
            valid += 1
print("Part2:", valid)



