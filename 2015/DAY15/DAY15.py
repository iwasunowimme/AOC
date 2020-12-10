'''https://adventofcode.com/2015/day/15'''
import re
import time
# Input data from file
with open("input.txt", "r") as f:
    vals = f.read()

# Max teaspoons given by specs
maxTeaspoons = 100

# Test cases
# vals = "Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8\n " \
#       "Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3"

# RE to extract information from input
regex = re.compile(r"(\w+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)")

# Extract the food data from the input and add to dictionary, keep a list for the food names
foods = {}
foodList = []
for food, capacity, durability, flavour, texture, calories in regex.findall(vals):
    foods[food] = [int(capacity), int(durability), int(flavour), int(texture), int(calories)]
    foodList.append(food)

t1 = time.time()
b = []


def generateList(foodList, teaspoonsleft) -> list:
    '''
    Generates a list of lists for all combinations of the items in foodList with list size teaspoonsleft
    :param foodList: A list of items that will be included in each list
    :param teaspoonsleft: The length of the list required
    :return:
    '''
    if not foodList:
        return []
    if len(foodList) == 1:
        return [[foodList[0]] * teaspoonsleft]
    permList = []
    for i in range(teaspoonsleft):
        recursed = generateList(foodList[1:], teaspoonsleft - i)
        for recurse in recursed:
            permList.append([foodList[0]] * i + recurse)

    return permList

b = generateList(foodList,maxTeaspoons)

# Set initial max values at 0 as it can not be negative
max_score = 0
max_score_healthy = 0

# For each combination of ingredients calculate score
for each in b:
    score = 0
    cap = sum([foods[x][0] for x in each])
    dur = sum([foods[x][1] for x in each])
    fla = sum([foods[x][2] for x in each])
    tex = sum([foods[x][3] for x in each])
    cal = sum([foods[x][4] for x in each])
    if cap > 0 and dur > 0 and fla > 0 and tex > 0:
        score = cap*dur*fla*tex  # Score is product of all bases

        # Part2 require calories less than 500
        if cal <= 500:
            max_score_healthy = max(max_score_healthy, score)
    max_score = max(max_score, score)

print("Part1: ", max_score)
print("Part2: ", max_score_healthy)

t2 = time.time()
b = []
# # Hard coded loop generator,
for i in range(101):
   for j in range(101-i):
       for k in range(101-j-i):
           b.append([foodList[0]]*i+[foodList[1]]*j + [foodList[2]]*k + [foodList[3]]*(100-k-j-i))
# Hard coded loop generator for test case
# for i in range(101):
#     b.append([foodList[0]] * i + [foodList[1]] * (100-i))



# Set initial max values at 0 as it can not be negative
max_score = 0
max_score_healthy = 0

# For each combination of ingredients calculate score
for each in b:
    score = 0
    cap = sum([foods[x][0] for x in each])
    dur = sum([foods[x][1] for x in each])
    fla = sum([foods[x][2] for x in each])
    tex = sum([foods[x][3] for x in each])
    cal = sum([foods[x][4] for x in each])
    if cap > 0 and dur > 0 and fla > 0 and tex > 0:
        score = cap*dur*fla*tex  # Score is product of all bases

        # Part2 require calories less than 500
        if cal <= 500:
            max_score_healthy = max(max_score_healthy, score)
    max_score = max(max_score, score)
print()
print("Part1: hardcoded: ", max_score)
print("Part2: hardcoded", max_score_healthy)
t3 = time.time()

print()
print("The first method has a recursive function to generate all possible combinations")
print("The second method is hard-coded to generate all possible combinations")
print("Recursive: ", t2-t1)
print("hardcoded: ", t3-t2)
print()
print("There is little time difference between the two, however the recursive method should work with varying inputs")