"""https://adventofcode.com/2016/day/9"""

# Input data from text file
with open("input.txt", "r") as f:
    values = [lines[:-1] for lines in f.readlines()][0]


def decompress(string, recurse):
    """
    A function that decompresses the string using the (XxY) formula duplicating the next X characters Y times
    :param string: The string to decompress
    :param recurse: False if (XxY) are not decompressed if part of another expansion, true if decompresses as well
    :return: the total length of the decompressed string
    """
    # Default values
    count = 0
    i = 0
    # Iterate whilst we haven't reached the end of the string
    while i < len(string):
        if string[i] == "(":
            i += 1  # Skip the '(', it is not included
            make = ''
            # Find the (XxY) form
            while string[i] != ')':
                make += string[i]
                i += 1
            i += 1  # Skip the ')', it is not included
            # Convert (XxY) to [X, Y] as int
            range_coord = [int(x) for x in make.split('x')]
            if recurse:  # Part B
                # Recurse the next portion to find the count that is decompressed again
                count += range_coord[1] * decompress(string[i:i + range_coord[0]], recurse)
            else:  # Part A
                # Count the parts that are decompressed then skip all inclusive (XxY)
                count += range_coord[1] * range_coord[0]
            # Skip forward till the end of the decompressed portion
            i += range_coord[0] - 1
        else:  # If a letter
            count += 1
        i += 1
    return count


print("Part1: ", decompress(values, recurse=False))
print("Part2: ", decompress(values, recurse=True))
