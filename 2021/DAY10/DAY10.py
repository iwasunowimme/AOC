# The Advent of Code challenge for day 10
""" https://adventofcode.com/2021/day/10 """

#Read in the file and return a list of all the integers
def readFile():
    with open("DAY10/input.txt", "r") as f:
        return [line.strip("\n") for line in f.readlines()]

vals = readFile()
#  Points assinged from task Part1
points = {')': 3,']': 57,'}': 1197,'>': 25137}
pairs ={'{':'}',"[":"]",'<':'>','(':')'}

#  Points assinged from task Part2
all_score = []
points_2 ={'(': 1 ,'[': 2 ,'{': 3 ,'<': 4 }

incomplete = []
score_part1 = 0
# For each line create a stack and find if there is any corruption
for line in vals:
    stack = []
    incompleted = True
    for char in line: # iterate through each charater
        if char in pairs.keys():  # Open so add to stack
            stack.append(char)
        elif char in pairs.values(): # Close so remove from stack
            check = stack.pop() # Pop the last item
            if pairs[check] != char: # If the corresponding close is not valid it is corrupt
                score_part1 += points[char]  # add score
                incompleted = False
                break
    
    if incompleted: # Not corrupt just incomplete
        score_part2 = 0
        while stack:  # Untill the end of stack calculate score
            score_part2 *= 5 
            score_part2 += points_2[stack.pop()]
        all_score.append(score_part2) # add score to list

all_score = sorted(all_score)  # Sort scores then find the middle to get part 2 answer

print(f"Part 1: {score_part1}")
print(f"Part 2: {all_score[len(all_score)//2]}")
