'''https://adventofcode.com/2015/day/19'''

import re
from copy import deepcopy
import time
with open("input.txt", "r") as f:
    values = [lines[:-1] for lines in f.readlines()]
#values = ['H => HO','H => OH','O => HH','e => O','e => H','HOH']
regex = re.compile(r'\w[a-z]?')
combinations = {}
substitutes = set()

for value in values[:-2]:
    temp = value.split()
    if temp[0] not in combinations:
        combinations[temp[0]] = [temp[2]]
    else:
        combinations[temp[0]].append(temp[2])
    substitutes.add(temp[0])
molecule = values[-1]


moleculeList = []
for i in regex.findall(molecule):
    moleculeList.append(i)
allMolecules = set()
keys = combinations.keys()
for i in range(len(moleculeList)):
    if moleculeList[i] in keys:
        temp = deepcopy(moleculeList)
        for subs in combinations[moleculeList[i]]:
            temp[i] = subs
            allMolecules.add(''.join(temp))

print("Part1: ", len(allMolecules))



molecule_reversed = molecule[::-1]
reps = {m[1][::-1]: m[0][::-1]
        for m in re.findall(r'(\w+) => (\w+)', '\n'.join(values))}
def rep(x):
    return reps[x.group()]

count = 0
print(molecule_reversed)
while molecule_reversed != 'e':
    molecule_reversed = re.sub('|'.join(reps.keys()), rep, molecule_reversed, 1)
    print(molecule_reversed)
    count += 1

print(count)
