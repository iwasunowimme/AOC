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
# values =['mxmxvkd kfcds sqjhc nhms (contains dairy, fish)','trh fvjkl sbzzf mxmxvkd (contains dairy)','sqjhc fvjkl (contains soy)','sqjhc mxmxvkd sbzzf (contains fish)']
ingredients = []
allergens = []
for v in values:
    v_split = v.split("(")
    ingredients.append(set(v_split[0].split()))
    allergens.append(v_split[1].strip("contains").strip(")").strip().split(", "))
allergy = set()
for al in allergens:
    for x in al:
        allergy.add(x)
print(allergy)
print(ingredients)
nothing = set()
bad = {}
for a in allergy:
    a_set = set()
    for i, every in enumerate(ingredients):
        if a in allergens[i]:
            if a_set == set():
                a_set = every
            else:
                a_set = a_set.intersection(every)
    nothing = nothing.union(a_set)
    bad[a] = list(a_set)

print(nothing)
counts = 0

for each in ingredients:
    counts += sum([1 for z in each if z not in nothing])

print("Part1: ", counts)
new_bad = {}
while bad:
    keys = list(bad.keys())
    for key in keys:
        if len(bad[key]) == 1:
            found = bad.pop(key, None)[0]
            new_bad[key] = found
            for key2 in bad:
                if found in bad[key2]:
                    new_key2 = []
                    for zz in bad[key2]:
                        if zz != found:
                            new_key2.append(zz)
                    bad[key2] = new_key2
    print(new_bad)

names = list(new_bad.keys())
names.sort()
print(names)
for na in names:
    print(new_bad[na],end=',')
