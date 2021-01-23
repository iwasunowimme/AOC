'''https://adventofcode.com/2016/day/2'''

# Import data from text file
with open("input.txt", "r") as f:
    values = [lines[:-1] for lines in f.readlines()]
# Test input
# values = ['ULL', 'RRDDD', 'LURDL', 'UUUUD']

# Set up keypads for both parts based on their configuration
# in the form (x, y) where (0, 0) is the centre,
# x is the vertical, increasing in the "U" and decreasing in the "D",
# y is the horizontal, increasing in the "R" direction and decreasing in the "L" direction
keypad_part1 = {(1, -1): 1, (1, 0): 2, (1, 1): 3, (0, -1): 4, (0, 0): 5, (0, 1): 6, (-1, -1): 7, (-1, 0): 8, (-1, 1): 9}
keypad_part2 = {(2, 0): 1, (1, -1): 2, (1, 0): 3, (1, 1): 4, (0, -2): 5, (0, -1): 6, (0, 0): 7, (0, 1): 8, (0, 2): 9,
                (-1, -1): "A", (-1, 0): "B", (-1, 1): "C", (-2, 0): "D"}


def print_password(instructions, keypad) -> str:
    '''
    This function prints the password based on the instruction set given and the appropriate keypad layout
    Method assumes instructions are written to start at the number 5
    :param instructions: A list of strings where each string is the movement on the keypad
    :param keypad: the keypad layout will all valid coordinates, as a dictionary
    :return: a string which is the password
    '''
    # Get a list of the keys to know valid inputs
    keys = keypad.keys()
    # Find the starting location, always starts at 5
    start = list(keys)[list(keypad.values()).index(5)]
    x = start[0]
    y = start[1]
    # Create blank password
    password = ''
    # Iterate through each instruction
    for value in instructions:
        # iterate through each movement in the instruction
        for d in value:
            if d == "L":  # If moving Left
                # Set temporary value
                newy = y - 1
                # Check if it is a valid values
                if (x, newy) in keys:
                    y = newy  # If valid update the original
            elif d == "U":  # If moving up
                newx = x + 1
                if (newx, y) in keys:
                    x = newx
            elif d == "R":  # If moving Right
                newy = y + 1
                if (x, newy) in keys:
                    y = newy
            elif d == "D":  # If moving Down
                newx = x - 1
                if (newx, y) in keys:
                    x = newx

        # Save the value at the end of the instruction
        password += str(keypad[x, y])
    return password


print("Part1: ", print_password(values, keypad_part1))
print("Part2: ", print_password(values, keypad_part2))
