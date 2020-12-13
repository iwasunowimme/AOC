'''https://adventofcode.com/2020/day/12'''
from collections import deque


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
    '''
    Iterates through the instructions and moves the ship accordingly to part 1 instructions
    :param values: The instruction list
    :return: the sum of the abs values of the North and East directions
    '''

    # Creates a double edged queue to cycle through the direction it is travelling
    direction = deque("ESWN")
    # Sets a dictionary of imaginary numbers to be able to do complex addition
    movement = {'N': 1j, 'E': 1, 'S': -1j, 'W': -1}
    # Our starting point is at the origin
    position = 0

    # Start going through the instruction list
    for value in values:
        # Separate out the instruction and the value
        instruction, arg = value[0], int(value[1:])

        # Rotate the ship
        if instruction == "L":
            direction.rotate(arg//90)  # Assumes that rotation can only be done by 90 degrees at a time
        elif instruction == "R":
            direction.rotate(-(arg // 90))
        # If ship moves forward, change the instruction to the direction the ship is facing
        elif instruction == "F":
            instruction = direction[0]

        # Move the ship forward the correct amount
        if instruction in direction:
            position += movement.get(instruction) * arg

    return int(abs(position.real)) + int(abs(position.imag))



def part2(values) -> int:
    '''
    Iterates through the instructions and moves the ship accordingly to part 2 instructions
    :param values: The instruction list
    :return: the sum of the abs values of the North and East directions of the ship
    '''

    # Sets a dictionary of imaginary numbers to be able to do complex addition
    movement = {'N': 1j, 'E': 1, 'S': -1j, 'W': -1}

    # Our starting point is at the origin
    position = 0
    # Way point starting point is at 10 east and 1 north
    waypoint_position = 10 + 1j

    # Start going through the instruction list
    for value in values:
        # Separate out the instruction and the value
        instruction, arg = value[0], int(value[1:])

        # Rotate the waypoint by transposing the coordinates around the circle
        if instruction == "L":
            for _ in range(arg//90):
                waypoint_position = complex(-waypoint_position.imag, waypoint_position.real)
        elif instruction == "R":
            for _ in range(arg//90):
                waypoint_position = complex(waypoint_position.imag, -waypoint_position.real)

        # If ship moves forward move the ship by the waypoint multiplied by args
        elif instruction == "F":
            position += waypoint_position * arg
        # If the waypoint moves by direction then increase by that amount
        else:
            waypoint_position += movement.get(instruction) * arg

    return int(abs(position.real)) + int(abs(position.imag))


if __name__ == "__main__":
    # Read in values
    values = readText("input.txt")

    # Run the test cases
    test()

    # Run the excercises
    print("Part1: ", part1(values))
    print("Part2: ", part2(values))
