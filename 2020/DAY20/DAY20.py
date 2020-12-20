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
def isqrt(n):
    if n > 0:
        x = 1 << (n.bit_length() + 1 >> 1)
        while True:
            y = (x + n // x) >> 1
            if y >= x:
                return x
            x = y
    elif n == 0:
        return 0
    else:
        raise ValueError("square root not defined for negative numbers")
diagram = defaultdict(list)

tile = 0
while values:
    v = values.pop(0)
    if v != '':
        if v.startswith("Tile"):
            tile = int(v.split()[1][:-1])
        else:
            diagram[tile].append(v)
print(diagram)
size = isqrt(len(diagram))
print(size,len(diagram))
dq = deque('LURD')
megaset = set()
corners = []
shape = {}
for key in diagram:
    count = 0
    edges = {}
    for key2 in diagram:
        key1_set = set()
        key2_set = set()
        if key != key2:

            item1 = diagram[key]
            item2 = diagram[key2]
            key1_set.add(item1[0])
            key1_set.add(item1[-1])
            key1_set.add(''.join([x[0] for x in item1]))
            key1_set.add(''.join([x[-1] for x in item1]))
            key2_set.add(item2[0])
            key2_set.add(item2[-1])
            key2_set.add(item2[0][::-1])
            key2_set.add(item2[-1][::-1])
            key2_set.add(''.join([x[0] for x in item2]))
            key2_set.add(''.join([x[-1] for x in item2]))
            key2_set.add(''.join([x[0] for x in item2][::-1]))
            key2_set.add(''.join([x[-1] for x in item2][::-1]))
            if item1[0] in key2_set:
                edges['top'] = key2
            if item1[-1] in key2_set:
                edges['bottom'] = key2
            if ''.join([x[0] for x in item1]) in key2_set:
                edges['left'] = key2
            if ''.join([x[-1] for x in item1]) in key2_set:
                edges['right'] = key2

            count += len(key1_set.intersection(key2_set))
    if count == 2:
        corners.append(key)
    shape[key] = edges

total = 1
for c in corners:
    total *= c
    if 'right' in shape[c]:
        if 'bottom' in shape[c]:
            start = c
print(corners)
print("part1: ", total)

# print(shape)
def rotate(left,right):
    rotatations = 0
    if 'left' in shape[right]:
        if shape[right]['left'] == left:
            rotatations = 0
    if 'top' in shape[right]:
        if shape[right]['top'] == left:
            rotatations = 3
    if 'right' in shape[right]:
        if shape[right]['right'] == left:
            rotatations = 2
    if 'bottom' in shape[right]:
        if shape[right]['bottom'] == left:
            rotatations = 1
    for _ in range(rotatations):
        new = {}
        if 'left' in shape[right]:
            new['top'] = shape[right]['left']
        if 'top' in shape[right]:
            new['right'] = shape[right]['top']
        if 'right' in shape[right]:
            new['bottom'] = shape[right]['right']
        if 'bottom' in shape[right]:
            new['left'] = shape[right]['bottom']
        shape[right] = new


        diagram[right] = list(zip(*diagram[right][::-1]))
    ZZ = ''.join([x[-1] for x in diagram[left]])
    YY = ''.join([x[0] for x in diagram[right]])
    # print(left,right)
    # print(ZZ,YY)
    if  ZZ != YY:
        if 'top' in shape[right]:
            if 'bottom' in shape[right]:
                shape[right]['top'], shape[right]['bottom'] = shape[right]['bottom'], shape[right]['top']
            else:
                shape[right]['bottom'] = shape[right]['top']
        elif 'bottom' in shape[right]:
            if 'top' in shape[right]:
                shape[right]['top'], shape[right]['bottom'] = shape[right]['bottom'], shape[right]['top']
            else:
                shape[right]['top'] = shape[right]['bottom']
        diagram[right] = diagram[right][::-1]
    return shape, diagram

def rotate2(top,bottom):
    rotatations = 0
    if 'left' in shape[bottom]:
        if shape[bottom]['left'] == top:
            rotatations = 1
    if 'top' in shape[bottom]:
        if shape[bottom]['top'] == top:
            rotatations = 0
    if 'right' in shape[bottom]:
        if shape[bottom]['right'] == top:
            rotatations = 3
    if 'bottom' in shape[bottom]:
        if shape[bottom]['bottom'] == top:
            rotatations = 2
    for _ in range(rotatations):
        new = {}
        if 'left' in shape[bottom]:
            new['top'] = shape[bottom]['left']
        if 'top' in shape[bottom]:
            new['right'] = shape[bottom]['top']
        if 'right' in shape[bottom]:
            new['bottom'] = shape[bottom]['right']
        if 'bottom' in shape[bottom]:
            new['left'] = shape[bottom]['bottom']
        shape[bottom] = new
        diagram[bottom] = list(zip(*diagram[bottom][::-1]))

    zzzz = ''.join(diagram[top][-1])
    yyyy = ''.join(diagram[bottom][0])
    if zzzz != yyyy:
        if 'left' in shape[bottom]:
            if 'right' in shape[bottom]:
                shape[bottom]['left'], shape[bottom]['right'] = shape[bottom]['right'], shape[bottom]['left']
            else:
                shape[bottom]['right'] = shape[bottom]['left']
        elif 'right' in shape[bottom]:
            if 'left' in shape[bottom]:
                shape[bottom]['left'], shape[bottom]['right'] = shape[bottom]['right'], shape[bottom]['left']
            else:
                shape[bottom]['left'] = shape[bottom]['right']
        diagram[bottom] = [x[::-1] for x in diagram[bottom]]
    return shape, diagram

next = start
first = start
direction = "right"
direction2 = "bottom"

j = 0
spots = [[0 for _ in range(size)] for __ in range(size)]

# print(shape[first])
while j < size:
    i = 0
    while i < size - 1:
        if i == 0:
            print(i,j,next)
        spots[j][i] = next

        last = next
        next = shape[last]['right']
        shape, diagram = rotate(last, next)

        # print(next)
        i += 1

    spots[j][i] = next
    if "bottom" in shape[first]:
        next = shape[first]['bottom']
        shape, diagram = rotate2(first, next)
        first = next

    j+=1
# print(spots)
print("end")
combines = []
for xx in spots:
    for i in range(1,len(diagram[xx[0]])-1):
        new_x = []
        for xxx in xx:
            new_x.append(''.join(diagram[xxx][i][1:-1]))
        combines.append(''.join(new_x))
    #         print(''.join(diagram[xxx][i]), end=' ')
    #     print()
    # print()
for com in combines:
    print(com)

max_snek = 0
for _ in range(2):
    for _ in range(4):
        for height in range(len(combines) - 3):
            for width in range(18,len(combines[0]) - 1):
                if combines[height][width] == '#':
                    if combines[height + 1][width - 18] == '#':
                        if combines[height + 1][width - 13] == '#':
                            if combines[height + 1][width - 12] == '#':
                                if combines[height + 1][width - 7] == '#':
                                    if combines[height + 1][width - 6] == '#':
                                        if combines[height + 1][width - 1] == '#':
                                            if combines[height + 1][width] == '#':
                                                if combines[height + 1][width + 1] == '#':
                                                    if combines[height + 2][width - 17] == '#':
                                                        if combines[height + 2][width - 14] == '#':
                                                            if combines[height + 2][width - 11] == '#':
                                                                if combines[height + 2][width - 8] == '#':
                                                                    if combines[height + 2][width - 5] == '#':
                                                                        if combines[height + 2][width - 2] == '#':
                                                                            max_snek += 15

        combines = list(zip(*combines[::-1]))
    combines = combines[::-1]
print(max_snek)
print(sum([sum([1 for x in z  if x == "#"]) for z in combines]) - max_snek)
