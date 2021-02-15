"""https://adventofcode.com/2016/day/12"""

# Import input from text file
with open("input.txt", "r") as f:
    values = [lines[:-1] for lines in f.readlines()]


def run_instruction(instructions, register) -> int:
    """
    Run through the instructions to calculate the registers. Only accepts 'cpy', 'inc', 'dec', and 'jnz' instructions
    :param instructions: a set of valid instructions
    :param register: the initial values of all needed registers
    :return: the int value of register 'a'
    """
    # Get keys of all register values
    keys = register.keys()
    v = 0  # Set instruction counter to 0
    while v < len(instructions):  # Whilst a valid instruction
        # Split the instruction into its components
        ins = instructions[v].split()
        if ins[0] == 'cpy':  # If cpy instruction
            if ins[1] in keys:  # If copy from register
                register[ins[2]] = register[ins[1]]
            else:  # If copy from integer
                register[ins[2]] = int(ins[1])
        elif ins[0] == 'inc':  # If increment instruction
            register[ins[1]] += 1
        elif ins[0] == 'dec':  # If decrement instruction
            register[ins[1]] -= 1
        elif ins[0] == 'jnz':  # If jump instruction
            if ins[1] in keys:  # If jump compares to instruction
                if register[ins[1]] != 0:
                    v += int(ins[2]) - 1   # Subtract 1 due to adding it for auto-increment
            elif int(ins[1]) != 0:  # If jump compares to int
                v += int(ins[2]) - 1
        # auto-increment
        v += 1
    return register['a']


# Part1, about 2 seconds for execution
part1_reg = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
print("Part1:", run_instruction(values, part1_reg))

# Part2, about 15 seconds for execution
part2_reg = {'a': 0, 'b': 0, 'c': 1, 'd': 0}
print("Part2:", run_instruction(values, part2_reg))
