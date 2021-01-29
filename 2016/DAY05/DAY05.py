'''https://adventofcode.com/2016/day/5'''
from hashlib import md5

# Input given
input = 'ffykfhsq'
# input = 'abc'  # Test Input

# Blank password for part 1
part1 = ''
# Appended integer
i = 0
# Create an array of 0's to act as an arraylist
part2 = [0 for _ in range(8)]
# Keep counter to see how many positions have been filled
part2_counter = 0
# Loop whilst both part 1 or part 2 are incomplete
while len(part1) < 8 or part2_counter < 8:

    # Uses hashlibs md5 function to find the hash
    hash = md5((input + str(i)).encode('utf-8')).hexdigest()

    # We only interested in ones starting with 5 0's
    if hash.startswith('00000'):
        if len(part1) < 8:  # If part1 is incomplete
            # Append the value to the password
            part1 += hash[5]
        if part2_counter < 8:  # If part2 is incomplete
            # Convert position to hex int
            position = int(hash[5], 16)
            if 8 > position >= 0:  # If valid position
                if part2[position] == 0:  # If position is not yet filled
                    # Position can only be an integer between 0-8 inclusive, no strings can enter
                    part2[position] = str(hash[6])
                    part2_counter += 1
    i += 1  # Increment the append integer

print("Part1: ", part1)
print("Part2: ", ''.join(part2))
