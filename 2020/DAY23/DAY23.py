import re
from collections import defaultdict
from itertools import combinations
from itertools import permutations
from copy import deepcopy
import math
from collections import deque


class MyLLNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

values = 198753462
# values = 389125467

circle = [int(x) for x in str(values)]
print(circle)
m = max(circle)
l = len(circle)
last = circle[-1]
for z in range(100):
    i = (circle.index(last) + 1) % l
    destination = circle[i] - 1
    last = circle[i]
    # print(z,destination,circle,circle[i])

    snapshot = []
    snapshot.append(circle[ (i + 1)%l])
    snapshot.append(
        circle[ (i + 2)%l])
    snapshot.append(
        circle[ (i + 3)%l])
    # print(destination, snapshot)
    while destination in snapshot or destination == 0:
        # print(destination)
        destination -= 1
        if destination <= 0:
            destination = m
        # print(destination)
    # print(destination)
    new= []
    for lz in snapshot:
        new.append(circle.pop(circle.index(lz)))
    # print(i, new,  circle)
    place = circle.index(destination)

    # print(circle,circle[:place + 1],circle[place + 1:])
    circle = circle[:place + 1] + new + circle[place + 1:]

    # print(circle)




print(''.join([str(x) for x in circle]))

circle = [int(x) for x in str(values)]
nodes = {}
last = None
for c in circle:
    new_node = MyLLNode(c)
    nodes[c] = new_node
    if last is not None:
        last.right = new_node
        new_node.left = last
    last = new_node


for number in range(max(circle) + 1, 1_000_000 + 1):
    new_node = MyLLNode(number)
    nodes[number] = new_node
    if last is not None:
        last.right = new_node
        new_node.left = last
    last = new_node

first = nodes[circle[0]]
last.right = first
first.left = last

current = first
# print("part2: ", nodes[1].right.right.val *  nodes[1].right.val,nodes[1].left.val)
for z in range(10_000_000):
    if z%1_000_000 == 0:
        print(z)
    current_val = current.val

    three_1 = current.right
    three_2 = three_1.right
    three_3 = three_2.right

    current.right = three_3.right
    three_3.right.left = current

    destination_value = current_val - 1  or 1_000_000
    while destination_value in (three_1.val, three_2.val, three_3.val, 0):
        destination_value -= 1
        if destination_value <= 0:
            destination_value = 1_000_000

    destination_node = nodes[destination_value]

    three_3.right = destination_node.right
    three_3.right.left = three_3
    destination_node.right = three_1
    three_1.left = destination_node

    current = current.right

print("part2: ", nodes[1].right.right.val *  nodes[1].right.val)




