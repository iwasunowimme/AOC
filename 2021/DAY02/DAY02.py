# The Advent of Code challenge for day 1
""" https://adventofcode.com/2021/day/1 """
import time
import re

#Read in the file and return a list of all the integers
def readFile() -> list:
    with open("DAY02/input.txt", "r") as f:
        return [line.strip("\n") for line in f.readlines()]

# Find the sum of all changes in the slope (i to i+1)
def part1(vals) -> int:
    test_str = ",".join(vals)
    forward_m = sum([int(match.groups()[0]) for match in re.finditer(r"forward (\d+)", test_str, re.MULTILINE)])
    down_m = sum([int(match.groups()[0]) for match in re.finditer(r"down (\d+)", test_str, re.MULTILINE)])
    up_m = sum([int(match.groups()[0]) for match in re.finditer(r"up (\d+)", test_str, re.MULTILINE)])
    return(forward_m * (down_m-up_m))
   

# Find the sum of all changes in the slope (i[x:x+2] to i[x+1:x+1+2])
def part2(vals) -> int:
    aim = 0
    hor = 0
    vert = 0
    for line in vals:
        value = int(line.split(" ")[-1])
        if 'forward' in line:
            hor += value
            vert += value * aim
        if 'up' in line:
            aim -= value
        if 'down' in line:
            aim += value
    return(hor*vert)

def test():
    test_input = ['forward 5','down 5','forward 8','up 3','down 8','forward 2']
    assert part1(test_input) == 150
    assert part2(test_input) == 900

if __name__ == "__main__":
    print("Running tests: Start")
    test()
    print("Running tests: Success")

    print("Reading input file: Start")
    vals = readFile()
    print("Reading input file: Success")

    start_part1 = time.perf_counter()
    print(f"Answer for part1 is {part1(vals)}")
    stop_part1 = time.perf_counter()
    start_part2 = time.perf_counter()
    print(f"Answer for part2 is {part2(vals)}")
    stop_part2 = time.perf_counter()
    print(f"Finished Part 1 version 1 in {stop_part1-start_part1:0.4f}")
    print(f"Finished Part 2 version 1 in {stop_part2-start_part2:0.4f}")