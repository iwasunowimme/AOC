'''https://adventofcode.com/2015/day/8'''

with open("input.txt", "r") as f:
    vals = [lines[:-1] for lines in f.readlines()]

# Set counters for the total memory and the total count
totalCount = 0
totalMemory = 0
for val in vals:
    totalCount += len(val)
    i = 0
    while i < len(val):
        if val[i] == '"':  # if contains the quotation mark
            i += 1
            continue
        elif val[i] == '\\':  # if contains a backslash
            if val[i + 1] == "x":  # If 'x' follows backslash move forward 3 as it is a a unicode of 4 bytes
                totalMemory += 1
                i += 3
            elif val[i + 1] == '\\' or val[i + 1] == '"':  # if a special character follows it is a special character
                totalMemory += 1
                i += 1
            else:  # If nothing follows then the special character is ignored
                totalMemory += 1
        else:  # Normal character
            totalMemory += 1
        i += 1

print("part1: ", totalCount - totalMemory)

# The total number of extra characters is just the sum of the special characters +2*all the length of the list
totalMemory = 2 * len(vals)
for val in vals:
    for v in val:
        if v == '"' or v == "\\":  # Only special characters in list are " and \
            totalMemory += 1

print("part2: ", totalMemory)
