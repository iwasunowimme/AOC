# The Advent of Code challenge for day 1
""" https://adventofcode.com/2021/day/1 """
import time

#Read in the file and return a list of all the integers
def readFile() -> list:
    with open("DAY01/input.txt", "r") as f:
        return [int(line) for line in f.readlines()]

# Find the sum of all changes in the slope (i to i+1)
def part1(vals) -> int:
    return sum(x < y for x,y in zip(vals,vals[1:]))


# Find the sum of all changes in the slope (i[x:x+2] to i[x+1:x+1+2])
def part2(vals) -> int:
    return sum(x < y for x,y in zip(vals,vals[3:]))

# Find the sum of all changes in the slope (i to i+1)
def part1_loop(vals) -> int:
    slope = 0
    for i in range(len(vals)-1):
        if vals[i] < vals[i+1]:
            slope += 1
    return slope

# Find the sum of all changes in the slope (i[x:x+2] to i[x+1:x+1+2])
def part2_loop(vals) -> int:
    slope = 0
    for i in range(len(vals)-3):
        if vals[i] < vals[i+3]:
            slope += 1
    return slope

# Find the sum of all changes in the slope (i to i+1)
def part1_loop_full(vals) -> int:
    slope = 0
    last = float('inf')
    for item in vals:
        if item > last:
            slope += 1
        last = item
    return slope


# Find the sum of all changes in the slope (i[x:x+2] to i[x+1:x+1+2])
def part2_loop_window(vals) -> int:
    slope = 0
    window = vals[:3]
    # Uses a window by creating a queue and moving forward
    for item in vals[3:]:
        window_sum = sum(window)        
        window.pop(0)
        window.append(item)
        new_window_sum = sum(window)
        if new_window_sum > window_sum:
            slope += 1
    return(slope)

def test():
    test_input = [199,200,208,210,200,207,240,269,260,263]
    assert part1(test_input) == 7
    assert part2(test_input) == 5
    assert part1_loop(test_input) == 7
    assert part2_loop(test_input) == 5
    assert part1_loop_full(test_input) == 7
    assert part2_loop_window(test_input) == 5

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

    start_part1 = time.perf_counter()
    print(f"Answer for part1 is {part1_loop(vals)}")
    stop_part1 = time.perf_counter()
    start_part2 = time.perf_counter()
    print(f"Answer for part2 is {part2_loop(vals)}")
    stop_part2 = time.perf_counter()
    print(f"Finished Part 1 version 2 in {stop_part1-start_part1:0.4f}")
    print(f"Finished Part 2 version 2 in {stop_part2-start_part2:0.4f}")

    start_part1 = time.perf_counter()
    print(f"Answer for part1 is {part1_loop_full(vals)}")
    stop_part1 = time.perf_counter()
    start_part2 = time.perf_counter()
    print(f"Answer for part2 is {part2_loop_window(vals)}")
    stop_part2 = time.perf_counter()
    print(f"Finished Part 1 version 3 in {stop_part1-start_part1:0.4f}")
    print(f"Finished Part 2 version 3 in {stop_part2-start_part2:0.4f}")