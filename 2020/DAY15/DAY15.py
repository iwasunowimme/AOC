
import re
from copy import deepcopy
from collections import defaultdict
from itertools import combinations
from itertools import permutations


values = [2,15,0,9,1,20]
# values = [3,1,2]

spoken = defaultdict(int)
said =  defaultdict(int)
last = 0
for j, val in enumerate(values):
    if said[val] == 0:
        spoken[val] = j + 1
        said[val] = 1
    else:
        spoken[val] = j + 1
        said[val] += 1
    last = val
for i in range(j + 1, 30000000):
    # print(spoken[last], said[last], last)
    if said[last] == 0:
        spoken[last] = i
        said[last] = 1
        last = 0
    else:
        last2 = i - spoken[last]
        spoken[last] = i
        last = last2

print(last)




