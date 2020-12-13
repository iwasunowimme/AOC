'''https://adventofcode.com/2020/day/13'''

# Import file
with open("input.txt", "r") as f:
    values = [lines[:-1] for lines in f.readlines()]

# Test values
# values = ['939','7,13,x,x,59,x,31,19']

# Set the start time
earlytime = int(values[0])
# Set the
earliest = float('inf')
name = 0
bus = []
# counter for offset for residuals
i = 0
# Iterate through all the buses
for each in values[1].split(','):
    if each != 'x':  # Ignore label 'x'
        bus.append((int(each) - i, int(each)))  # For use in part 2, add as pairs (offset, value)
        early = int(each) - earlytime % int(each)  # Calculates the specific buses earliest time
        if early < earliest:  # Keep track of the earlier
            earliest = early
            name = int(each)
    i +=1
print("Part1: ", name * earliest)


def crt2(doubles) -> int:
    '''
    Finds the first result relating to the Chinese Number Theory of the inputs
    :param doubles: a list of remainder, modulo pairs
    :return: the first integer solution
    '''
    # The product of all numbers
    M = 1
    for rem, mod in doubles:  # Calculate the product
        M *= mod
    total = 0

    # Iterate through all the pairs
    for rem, mod in doubles:
        b = M // mod  # Find the modulus for M using the first in the list

        total += rem * b * pow(b, mod-2, mod)  # Pow is b^(mod-2) % mod
        total %= M
    return total


print("Part2: ", crt2(bus))

# For part can use sympy library
from sympy.ntheory.modular import crt
moduli = []
residuals = []
# Add the moduli and residuals into their own lists
for b in bus:
    moduli.append(b[1])
    residuals.append(b[0])
# Take the first as it returns in the form y = mx+b
print("Part2: ", crt(moduli,residuals)[0])









