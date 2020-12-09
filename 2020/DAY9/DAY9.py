'''https://adventofcode.com/2020/day/9'''

# Input the values as ints into a list
with open("input.txt", "r") as f:
    vals = [int(line) for line in f.readlines()]

# Set the preamble to the first 25 digits
pre = vals[:25]

# Loop starting at the first digit post preamble to the end
for val in vals[25:]:
    acceptable = False
    for i in range(len(pre)):
        if val - pre[i] in pre[i+1:]:
            acceptable = True
            pre.pop(0)
            pre.append(val)
            break
    if not acceptable:
        weak = val
        print("Part1: ", val)
        break

# Loop Through the entire list of values
for i in range(len(vals)):
    sum = 0
    nums = []
    equals = False
    for v in vals[i:]:
        sum += v
        nums.append(v)
        if sum == weak:
            equals = True
            break
        elif sum > weak:
            break
    if equals:
        print("Part2: ", min(nums) + max(nums))
        break
