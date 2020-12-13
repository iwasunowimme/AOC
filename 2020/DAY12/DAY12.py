'''https://adventofcode.com/2020/day/12'''


def readText(filename) -> list:
    '''
    A function that reads from the input file
    :return: a list of the line values except new line character
    '''
    # Import file into the return statement
    with open(filename, "r") as f:
        return [lines[:-1] for lines in f.readlines()]


def test():
    '''
    Runs the function using the test data on the webpage
    prints out statements depending on the success of each part using asssert
    '''
    test_values = ['F10', 'N3', 'F7', 'R90', 'F11']

    # Part 1
    assert part1(test_values) == 25
    print("Test part 1 successful")

    # Part 2
    assert part2(test_values) == 286
    print("Test part 2 successful")
    print()


def part1(values) -> int:

    east = 0
    north = 0
    facing = 0

    for value in values:
        instruction = value[0]
        val = int(value[1:])
        if instruction == "F":
            mo = facing % 360
            if mo == 0:
                instruction = 'E'
            elif mo == 90:
                instruction ="N"
            elif mo == 180:
                instruction = "W"
            elif mo == 270:
                instruction = "S"
        if instruction == 'N':
            north += val
        elif instruction == "S":
            north -= val
        elif instruction == "E":
            east += val
        elif instruction == "W":
            east -= val
        elif instruction == "L":
            facing += val
        elif instruction == "R":
            facing -= val
    return abs(east)+abs(north)


def part2(values) -> int:

    node_east = 10
    node_north = 1
    ship_east = 0
    ship_north = 0
    facing = 0

    for value in values:
        instruction = value[0]
        val = int(value[1:])
        if instruction == "F":
            ship_east += val*node_east
            ship_north += val * node_north
        elif instruction == 'N':
            node_north += val
        elif instruction == "S":
            node_north -= val
        elif instruction == "E":
            node_east += val
        elif instruction == "W":
            node_east -= val
        elif instruction == "L":
            for _ in range(val%360//90):
                node_east, node_north = -node_north, node_east
        elif instruction == "R":
            for _ in range(val % 360 // 90):
                node_east, node_north = node_north, -node_east

    return abs(ship_east)+abs(ship_north)

if __name__ == "__main__":
    values = readText("input.txt")
    test()
    print("Part1: ", part1(values))
    print("Part2: ", part2(values))
