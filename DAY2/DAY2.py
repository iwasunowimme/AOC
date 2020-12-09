'''https://adventofcode.com/2015/day/2'''

with open("input.txt",'r') as f:
    vals = [[int(x) for x in lines[:-1].split("x")] for lines in f.readlines()]  # split the values on the x and cast to int
total = 0

for val in vals:
    # find the three surface ares
    a = val[0]*val[1]
    b = val[1]*val[2]
    c = val[0]*val[2]
    total += 2*(a+b+c) + min(a, b, c) # find the sum of the all 6 SA (2 of each) add 1* the smallest area

print("part1: ", total)

total = 0
for val in vals:
    val.sort()  # Sort list so that we can access the two smallest numbers, only 3 entries per list so O(n) is small
    total += val[0]*val[1]*val[2]+2*val[0]+2*val[1]  # sum cubic area l*w*h and 2* 2 shortest sides

print("part2: ", total)
