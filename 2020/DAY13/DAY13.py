

import re
from copy import deepcopy
from collections import defaultdict
from itertools import permutations
from itertools import combinations

with open("input.txt", "r") as f:
    values = [lines[:-1] for lines in f.readlines()]
#values = ['939','7,13,x,x,59,x,31,19']

earlytime = int(values[0])
earliest = float('inf')
name = 0
bus = []
i = 0
for each in values[1].split(','):
    if each != 'x':
        bus.append((int(each) - i, int(each)))
        early = int(each)-(earlytime)%int(each)
        if early < earliest:
            earliest = early
            name = int(each)
    i +=1
print(name * earliest)

print(bus)

def crt(doubles):
    M = 1
    for rem, mod in doubles:
        M *= mod
    total = 0
    for rem, mod in doubles:
        b = M // mod
        total += rem * b * pow(b, mod-2, mod)
        total %= M
    return total

print(crt(bus))









