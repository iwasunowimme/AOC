"""https://adventofcode.com/2016/day/13"""
from copy import deepcopy

# Values given by brief
value = 1350
dest = (31, 39)

rows = []
for x in range(100):
    column = []
    for y in range(100):
        v = x*x + 3*x + 2*x*y + y + y*y + value
        str_v = bin(v)[2:]
        column.append(1 - str_v.count('1') % 2)
    rows.append(column)

paths = [[(1, 1)]]
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
max_col = len(rows[0])
max_row = len(rows[1])
found = False
while paths and not found:
    p = paths.pop(0)
    # print(type(p))
    # print(p)
    for m in moves:
        new = (p[-1][0]+m[0], p[-1][1]+m[1])
        # print(new)
        if 0 <= new[0] < max_col and 0 <= new[1] < max_row:
            if new == dest:
                found = True
                print("Part1:", len(p))
                break
            elif new not in p:
                if rows[new[0]][new[1]]:
                    temp = deepcopy(p)
                    temp.append(new)
                    paths.append(temp)

visited = set()
visited.add((1, 1))
paths = [[(1, 1)]]

while paths:
    p = paths.pop(0)
    if len(p) > 50:
        break
    for m in moves:
        new = (p[-1][0]+m[0], p[-1][1]+m[1])
        if 0 <= new[0] < max_col and 0 <= new[1] < max_row:

            if rows[new[0]][new[1]]:
                visited.add(new)
                if new not in p:
                    temp = deepcopy(p)
                    temp.append(new)
                    paths.append(temp)

print("Part2:", len(visited))
print(visited)


# Some smart guy on reddit, learn from it, godarderik
# frontier = [(1,1,0)]
# explored = {}
#
# def get_wall(tup):
#     num = tup[0] * tup[0] + 3 * tup[0] + 2 * tup[0] * tup[1] +tup[1] + tup[1] * tup[1] + 1350
#     return bin(num)[2:].count("1") % 2 == 0 and tup[0] >= 0 and tup[1] >= 0
#
# def get_next(tup):
#     cand = [(0,1), (0,-1), (1,0), (-1,0)]
#     return [(x[0] + tup[0], x[1] + tup[1], tup[2] + 1) for x in cand if get_wall((x[0] + tup[0], x[1] + tup[1]))]
#
# while len(frontier) > 0:
#     new = frontier.pop()
#     explored[(new[0], new[1])] = new[2]
#     frontier += [x for x in get_next(new) if not (x[0], x[1]) in explored or explored[(x[0], x[1])] > x[2]]
#
# print(explored[(31,39)], len([explored[x] for x in explored.keys() if explored[x] <= 50]))