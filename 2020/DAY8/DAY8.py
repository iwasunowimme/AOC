# The Advent of Code challenge for day 8
""" https://adventofcode.com/2020/day/8 """


# Input data from text files
def readfile() -> list:
    with open("input.txt", "r") as f:
        return [line[:-1] for line in f.readlines()]


def part1(vals):
    # set the accumulator to starting point (0)
    acc = 0
    # Create a set of visited to see if it has been visited
    visited = set()
    # I is the program counter
    i = 0
    while i not in visited:  # Continue until we reach an instruction already visited
        visited.add(i)
        # Store the instructions as the given counter
        ints = vals[i].split()
        if ints[0] == "nop":  # If 'nop' operation
            i += 1  # move forward by 1
        elif ints[0] == "acc":  # If 'acc' operation
            acc += int(ints[1])  # increase acc as needed
            i += 1
        else:  # 'jmp' instruction, move forward counter
            i += int(ints[1])

    return acc


def part2(vals):
    val_length = len(vals)
    # Iterate through every value
    for j in range(val_length):

        # Set loop values as defaults
        visited = set()
        acc = 0
        i = 0
        k = 0
        # Set booleans for exit conditions
        infloop = False
        done = True

        while done:  # Iterate until we find the exit conditions
            if i in visited:  # If an infinite loop is found
                infloop = True
                done = False

            visited.add(i)
            ints = vals[i].split()

            # If at instruction 'j' flip the instruction
            if j == k:
                if ints[0] == "nop":
                    ints[0] = "jmp"
                elif ints[0] == "jmp":
                    ints[0] = "nop"
            k += 1

            # Complete instruction as normal
            if ints[0] == "nop":
                i += 1
            elif ints[0] == "acc":
                acc += int(ints[1])
                i += 1
            else:
                i += int(ints[1])
            # See if we have gone over the instruction limit
            if i >= val_length - 1:
                done = False

        # If we do not have an infinite loop print the accumulator value
        if not infloop:
            return acc

    return 0  # No non infinite loop was found


if __name__ == "__main__":
    vals = readfile()
    print("Part1:", part1(vals))
    print("Part2:", part2(vals))
