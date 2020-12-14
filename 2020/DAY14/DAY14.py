'''https://adventofcode.com/2020/day/14'''

import re

# Input from text file
with open("input.txt", "r") as f:
    values = [lines[:-1] for lines in f.readlines()]
#values = ['mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X','mem[8] = 11','mem[7] = 101','mem[8] = 0']
#values = ['mask = 000000000000000000000000000000X1001X','mem[42] = 100','mask = 00000000000000000000000000000000X0XX','mem[26] = 1']

# Used to get the two numbers
reg = re.compile(r'(\d+)')
# Use dictionary to store values to keep list small
def solve(values, part_one):
    mem = {}
    mask = ''
    # For each input
    for line in values:
        if line.startswith('mask'):  # Is a Mask
            # Get mask value as string
            mask = line.split()[2]

        else:  # Is not a mask
            address = []
            m = reg.findall(line)  # Find all numbers
            # First number is the memory slot
            mem_slot = str(bin(int(m[0]))[2:].zfill(36))
            # Second number is the string to write, convert to 36 bit binary number, padded with 0's sans '0b'
            towrite = str(bin(int(m[1]))[2:].zfill(36))
            new_string = ''

            # If part one
            if part_one:
                # For each value in to write memory and mask as pairs
                # We can use pairs since we are comparing them bitwise
                for (writing, masking) in zip(towrite, mask):
                    # If bit is overwritten by mask
                    if masking != 'X':
                        new_string += masking
                    # If bit is not masked
                    else:
                        new_string += writing
                # Convert back to decimal
                mem[mem_slot] = int(new_string, 2)

            # If part Two
            else:
                # Iterate through the mask and memory bit
                for (memory_bit, masking) in zip(mem_slot, mask):
                    # Create empty list to add memory addresses
                    new_add = []
                    # If masking is '1', bit is overwritten as 1
                    if masking == '1':
                        if address:
                            for add in address:  # For all current addresses up to this bit
                                new_add.append(add + '1')
                        else:  # If empty
                            new_add = ['1']
                    # If masking is '0', bit is written as the bit in the given address
                    elif masking == '0':
                        if address:
                            for add in address:  # For all current addresses up to this bit
                                new_add.append(add + memory_bit)
                        else:  # If empty
                            new_add = [memory_bit]
                    # If masking is 'X', bit becomes schrodinger's bit, both 0 and 1 at the same time.
                    # This adds all combinations of the address with this bit being 0 and 1 to the list
                    elif masking == 'X':
                        if address:
                            for add in address:  # For all current addresses up to this bit
                                new_add.append(add + '1')
                                new_add.append(add + '0')
                        else:  # If empty
                            new_add = ['1', '0']

                    # Address list is reinstated as the working ones
                    address = new_add

                # For all addresses write the memory value
                for add in address:
                    mem[add] = int(towrite, 2)
    # We want the some of all address values, so we return this
    return sum(mem.values())


print("Part1: ", solve(values, True))
print("Part2: ", solve(values, False))


