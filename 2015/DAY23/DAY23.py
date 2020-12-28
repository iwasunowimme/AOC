'''https://adventofcode.com/2015/day/23'''

# Input the values from the file
def readValues():
    values = {}
    with open("input.txt", "r") as f:
        for i, lines in enumerate(f.readlines()):
            values[i] = lines[:-1]
    return values


def solve(register_a, register_b, values) -> int:
    '''
    Solves using the given instructions
    :param register_a: the initial value of the register
    :param register_b: the initial value of the register
    :param values: the instruction set
    :return:  The value of register b
    '''
    # Find the total number of index instructions, assumes no missing indexes
    length = len(values)
    i = 0  # Program counter
    # Loop whilst index is in range 0 - length
    while i < length:
        instruction = values[i]  # Get instruction
        # Test the start of instruction for which to do
        if instruction.startswith('hlf'):  # To half the value
            if 'a' in instruction:  # If register 'a'
                register_a //= 2
            else:  # If register 'b'
                register_b //= 2
        elif instruction.startswith('tpl'):  # To triple the value
            if 'a' in instruction:
                register_a *= 3
            else:
                register_b *= 3
        elif instruction.startswith('inc'):  # To increment value by 1
            if 'a' in instruction:
                register_a += 1
            else:
                register_b += 1
        elif instruction.startswith('jmp'):  # Jumps to the offset instruction
            i += int(instruction.split()[-1]) - 1  # Subtracts 1 due to the auto increment
        elif instruction.startswith('jie'):  # Jump if register is even
            if 'a' in instruction:
                if register_a % 2 == 0:
                    i += int(instruction.split()[-1]) - 1  # Subtracts 1 due to the auto increment if not found
            else:
                if register_b % 2 == 0:
                    i += int(instruction.split()[-1]) - 1
        elif instruction.startswith('jio'):  # Jumps if register value is 1
            if 'a' in instruction:
                if register_a == 1:
                    i += int(instruction.split()[-1]) - 1  # Subtracts 1 due to the auto increment if not found
            else:
                if register_b == 1:
                    i += int(instruction.split()[-1]) - 1

        i += 1  # Auto increment counter
    # Returns the value of the 'b' register
    return register_b


if __name__ == '__main__':
    values = readValues()
    print("Part1: ", solve(0, 0, values))
    print("Part2: ", solve(1, 0, values))
