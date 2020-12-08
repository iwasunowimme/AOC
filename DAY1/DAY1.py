'''https://adventofcode.com/2015/day/1'''

# Read input from the txt file
with open("input.txt","r") as f:
    vals = f.readline() #input only has one line

# set counter variable
count = 0
for val in vals:
    if val == "(": #go up a floor
        count+=1
    elif val == ")": # Go down a floor
        count-=1
print("Part1: ",count)

#set part 2 counters
count = 0
i = 0 # counter for value position in list
for val in vals:
    i+=1
    if val == "(":
        count+=1
    elif val == ")":
        count-=1
    if count < 0:
        print("part2: ", i)
        break



