'''https://adventofcode.com/2016/day/8'''

# Import values from txt file
with open("input.txt", "r") as f:
    values = [lines[:-1] for lines in f.readlines()]

# Set width and height values
width = 50
height = 6

# Create a blank 2d array of 0 (0 for off state and 1 for on state)
lights = [[0 for _ in range(width)] for _ in range(height)]

# For each instruction
for v in values:
    if v.startswith('rect'):  # If rect instruction
        # Maps the values to the instruction to get the dimensions of the rectangle
        inst = list(map(int, v.split()[-1].split('x')))
        # Iterates through both lists for 0 to the instructions
        for i in range(inst[1]):
            for j in range(inst[0]):
                lights[i][j] = 1

    elif 'column' in v:  # If rotate by column
        # Maps the values to the instructions for the row and dimension of the shift
        inst = list(map(int, v.split('=')[-1].split(' by ')))
        # Create a temp which is a copy of the current array to be shifted
        temp = [lights[i][inst[0]] for i in range(height)]
        # For the entire height find the value in the -dimension position which will be the new value
        for i in range(height):
            lights[i][inst[0]] = temp[i - inst[1]]

    elif 'row' in v:  # If rotate by row
        # Maps the values to the instructions for the row and dimension of the shift
        inst = list(map(int, v.split('=')[-1].split(' by ')))
        # return the current instance of the row from -dimension to 0 + 0 to -dimension
        lights[inst[0]] = lights[inst[0]][-inst[1]:] + lights[inst[0]][:-inst[1]]

# Find the sum of all 1's in the array
print("Part1:", sum(sum(l) for l in lights))
# print(sum(map(sum, lights)))

# Part 2
print("Part2:")
# Use '@' and ' ' for readability, can use any symbol
# prints '@' if 1 else, prints ' ' for each row
print('\n'.join(''.join('@' if l else ' ' for l in row) for row in lights))
