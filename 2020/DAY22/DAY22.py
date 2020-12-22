import re
from collections import defaultdict
from itertools import combinations
from itertools import permutations
from copy import deepcopy
import math
from collections import deque

# Import data from text file
with open("input.txt", "r") as f:
# with open("example.txt", "r") as f:
    values = [lines[:-1] for lines in f.readlines()]

player1 = []
player2 = []

p1 = True
for v in values:
    if v != '':
        if v == "Player 1:":
            p1 = True
        elif v == "Player 2:":
            p1 = False
        elif p1:
            player1.append(int(v))
        else:
            player2.append(int(v))
print(len(player1),len(player2))
p1_2 = deepcopy(player1)
p2_2 = deepcopy(player2)
print(player1)
while len(player1) != 0 and len(player2) != 0:
    one = player1.pop(0)
    two = player2.pop(0)
    if one > two:
        player1.append(one)
        player1.append(two)
    else:
        player2.append(two)
        player2.append(one)
total = 0
print(player1)
print(player2)
if len(player1) == 0:
    for i, number in enumerate(player2):
        total += (len(player2) - i) * number
else:
    for i, number in enumerate(player1):
        total += (len(player1) - i) * number

print(total)


def recursive_game(p1, p2):
    while len(p1) > 0 and len(p2)> 0:

        one = p1.pop(0)
        two = p2.pop(0)

        if len(p1) >= one and len(p2) >= two:
            winner = sub(deepcopy(p1[:one]), deepcopy(p2[:two]))
            # print(winner)
            if winner == 1:
                p1.append(one)
                p1.append(two)
            else:
                p2.append(two)
                p2.append(one)
            continue
        else:
            # print(one,two)
            if one > two:
                p1.append(one)
                p1.append(two)
            else:
                p2.append(two)
                p2.append(one)
        if len(p1) == 0:
            return p1, p2, 2
        elif len(p2) == 0:
            return p1, p2, 1
    return p1, p2, 0

def sub(p1, p2):
    oldgames2 = set()
    while len(p1) > 0 and len(p2) > 0:
        game = ','.join([str(x) for x in p1]) + "-" + ','.join([str(x) for x in p2])
        if game in oldgames2:
            return 1
        oldgames2.add(game)
        one = p1.pop(0)
        two = p2.pop(0)

        if len(p1) >= one and len(p2) >= two:
            winner = sub(deepcopy(p1[:one]), deepcopy(p2[:two]))
            if winner == 1 :
                p1.append(one)
                p1.append(two)
            else:
                p2.append(two)
                p2.append(one)
            continue
        else:
            # print(one,two)
            if one > two:
                p1.append(one)
                p1.append(two)
            else:
                p2.append(two)
                p2.append(one)
        if len(p1) == 0:
            return 2
        elif len(p2) == 0:
            return 1
    return 'hacker'


p11, p22, winnerr = recursive_game(p1_2, p2_2)
print(p11,p22)
print(len(p11))
total = 0
if winnerr == 2:
    for i, number in enumerate(p22):
        total += (len(p22) - i) * number
else:
    for i, number in enumerate(p11):
        total += (len(p11) - i) * number
print(total)
