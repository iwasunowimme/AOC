'''https://adventofcode.com/2015/day/19'''

import re
from copy import deepcopy

# Load file
with open("input.txt", "r") as f:
    values = [lines[:-1] for lines in f.readlines()]

# Test input values
#values = ['H => HO','H => OH','O => HH','e => O','e => H','HOH']

# re for splitting molecule
regex = re.compile(r'\w[a-z]?')
combinations = {}
substitutes = set()

for value in values[:-2]:  # Only combinations
    temp = value.split()
    # Add to dictionary
    if temp[0] not in combinations:
        combinations[temp[0]] = [temp[2]]
    else:
        combinations[temp[0]].append(temp[2])
    substitutes.add(temp[0])
molecule = values[-1]

# Go through all molecule substitutions and add to list
moleculeList = []
for i in regex.findall(molecule):
    moleculeList.append(i)

# Blank set fro holding combinations
allMolecules = set()
keys = combinations.keys()
for i in range(len(moleculeList)):
    # For all molecules with a substitution
    if moleculeList[i] in keys:
        temp = deepcopy(moleculeList)
        # Aplly all substitutions and add to set
        for subs in combinations[moleculeList[i]]:
            temp[i] = subs
            allMolecules.add(''.join(temp))
# Since set is only unique entries, print count
print("Part1: ", len(allMolecules))


# Since the "Ar" ending is unique and always a terminator, we use that as a starting point instead
# This means we reverse it, used over Y and Rn because they are used internally instead.
# We don't use "C" because all "C" are terminated with "Ar" and there are more "Ar"
molecule_reversed = molecule[::-1]  # Reverse molecule
# create a dictionary with the keys as the final combination reversed and the value as the initial reversed
# We reverse here since we want to make it smaller
reps = {m[1][::-1]: m[0][::-1]
        for m in re.findall(r'(\w+) => (\w+)', '\n'.join(values))}
print(reps)
# Create a way to get the list based on the match values
def rep(x):
    return reps[x.group()]

count = 0
# While not a single electron
while molecule_reversed != 'e':
    molecule_reversed = re.sub('|'.join(reps.keys()), rep, molecule_reversed, 1)  # 1 for 1 step at a time
    count += 1

print(count)
