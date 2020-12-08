'''https://adventofcode.com/2015/day/6'''

with open("input.txt", "r") as f :
    vals = [lines[:-1] for lines in f.readlines()]

lights = {}
for i in range(1000):
    for j in range(1000):
        lights[i,j] = 0
for val in vals:
    instructions = val.split()
    if instructions[0] == "turn":
        new = 0
        start = instructions[2].split(",")
        finish = instructions[4].split(",")
        if instructions[1] == 'on':
            new = 1
        for i in range(int(start[0]),int(finish[0])+1):
            for j in range(int(start[1]),int(finish[1])+1):
                lights[i,j] = new
    else:
        start = instructions[1].split(",")
        finish = instructions[3].split(",")
        for i in range(int(start[0]),int(finish[0])+1):
            for j in range(int(start[1]),int(finish[1])+1):

                lights[i,j] = (lights[i,j]+1)%2
count = 0
for item in lights:
    count += lights[item]
print("part1: ", count)

lights = {}
for i in range(1000):
    for j in range(1000):
        lights[i,j] = 0
for val in vals:
    instructions = val.split()
    if instructions[0] == "turn":
        new = -1
        start = instructions[2].split(",")
        finish = instructions[4].split(",")
        if instructions[1] == 'on':
            new = 1
        for i in range(int(start[0]),int(finish[0])+1):
            for j in range(int(start[1]),int(finish[1])+1):
                lights[i, ] += new
                if lights[i, j] < 0:
                    lights[i, j] = 0
    else:
        start = instructions[1].split(",")
        finish = instructions[3].split(",")
        for i in range(int(start[0]),int(finish[0])+1):
            for j in range(int(start[1]),int(finish[1])+1):

                lights[i,j] += 2

count = 0
for item in lights:
    count += lights[item]
print("part2: ", count)

