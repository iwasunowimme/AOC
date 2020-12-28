'''https://adventofcode.com/2015/day/25'''
import re


# Input the values from the file
def readValues():
    with open("input.txt", "r") as f:
        return [lines[:-1] for lines in f.readlines()][0]


def part1(values) -> int:
    # Pull the numbers using re expression from the input
    digits = []
    for v in re.findall(r'(\d+)', values):
        digits.append(int(v))
    row = digits[0]  # Set row as first number
    column = digits[1]  # Set column as second number
    # Get the total iterations as the triangle number + the extra columns
    total = sum(range(row + column - 1)) + column - 1

    # Set starting value
    start = 20_151_125

    # Loop through each iteration to find the result
    for _ in range(total):
        start = (start * 252_533) % 33_554_393
    return start


if __name__ == '__main__':
    values = readValues()
    print("Part1: ", part1(values))
