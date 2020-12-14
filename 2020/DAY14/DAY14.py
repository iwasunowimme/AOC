

import re
from itertools import combinations
from itertools import permutations
from collections import defaultdict
from collections import deque
from copy import deepcopy


with open("input.txt", "r") as f:
    values = [lines[:-1] for lines in f.readlines()]
#values = ['mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X','mem[8] = 11','mem[7] = 101','mem[8] = 0']
#values = ['mask = 000000000000000000000000000000X1001X','mem[42] = 100','mask = 00000000000000000000000000000000X0XX','mem[26] = 1']
reg = re.compile(r'(\d+)')
mem = defaultdict(int)
mask = ''
for line in values:
    if line.startswith('mask'):
        mask = line.split()[2]
    else:
        m = reg.findall(line)
        mem_slot = m[0]
        towrite = str(bin(int(m[1]))[2:].zfill(36))
        new_string =''
        for i in range(len(towrite)):
            if mask[i] != 'X':
                new_string += mask[i]
            else:
                new_string += towrite[i]

        mem[mem_slot] = int(new_string,2)
print("Part1: ", sum(mem.values()))
print(mem)
mem2 = defaultdict(int)
for line in values:
    if line.startswith('mask'):
        mask = line.split()[2]
    else:
        address = []
        m = reg.findall(line)
        mem_slot = str(bin(int(m[0]))[2:].zfill(36))
        towrite = str(bin(int(m[1]))[2:].zfill(36))
        new_string =''
        for i in range(len(mask)):
            new_add = []
            if mask[i] == '1':
                if address == []:
                    new_add = ['1']
                else:
                    for add in address:
                        new_add.append(add +'1')
            elif mask[i] == '0':
                if address == []:
                    new_add = [mem_slot[i]]
                else:
                    for add in address:
                        new_add.append(add + mem_slot[i])
            elif mask[i] == 'X':
                if address == []:
                    new_add = ['1','0']
                else:
                    for add in address:
                        new_add.append(add+'1')
                        new_add.append(add+'0')
            address = new_add



        for add in address:
            mem2[add] = int(towrite, 2)

print("Part2: ", sum(mem2.values()))

