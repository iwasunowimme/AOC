'''https://adventofcode.com/2020/day/11'''

from copy import deepcopy

with open("input.txt", "r") as f:
    vals = [lines[:-1] for lines in f.readlines()]
#vals =["L.LL.LL.LL","LLLLLLL.LL","L.L.L..L..","LLLL.LL.LL","L.LL.LL.LL","L.LLLLL.LL","..L.L.....","LLLLLLLLLL","L.LLLLLL.L","L.LLLLL.LL"]

seats = {}
i = 0
for value in vals:
    j = 0
    for seat in value:
        seats[i, j] = seat
        j += 1
    i += 1
# for m in range(i):
#     for n in range(j):
#         print(seats[m, n], end="")
#     print()
# print()
part2seats = deepcopy(seats)
def findNeighbours(current, x, y) -> str:
    total = 0

    for xAxis in range(x-1,x+2):
        for yAxis in range(y-1, y+2):
            try:
                if xAxis == x and yAxis == y:
                    continue
                else:
                    if current[xAxis, yAxis] == "#":
                        total += 1
            except:
                continue
    curr =current[x, y]

    if curr == "L" and total == 0:
        return "#"
    elif curr == "#" and total >=4:
        return "L"
    else:
        return curr
last = 0
last2 = 0
seatspart2 = deepcopy(seats)
for _ in range(100):
    current_state = deepcopy(seats)
    for key in seats:
        if current_state[key] != ".":
            seats[key] = findNeighbours(current_state, key[0], key[1])
    tot = sum([1 for v in seats.values() if v == "#"])
    if tot == last and tot == last2:
        print("Part1: ", tot)
        break
    else:
        last2 = last
        last = tot
    # for m in range(i):
    #     for n in range(j):
    #         print(seats[m, n], end="")
    #     print()
    # print()



def findNeighbours2(current, x, y) -> str:
    total = 0

    for xAxis in range(x-1,x+2):
        for yAxis in range(y-1, y+2):
            try:
                if xAxis == x and yAxis == y:
                    continue
                else:
                    xAxis2 = xAxis
                    yAxis2 = yAxis

                    while current[xAxis2, yAxis2] == "." and xAxis2 >=0 and yAxis2 >=0 and xAxis2 < i and yAxis2 < j:
                       # print(x,y,xAxis,yAxis, xAxis2 ,yAxis2)
                        xAxis2 += xAxis - x
                        yAxis2 += yAxis - y
                    if current[xAxis2, yAxis2] == "#":
                        total += 1
            except:
                continue

    curr =current[x, y]

    if curr == "L" and total == 0:
        return "#"
    elif curr == "#" and total >=5:
        return "L"
    else:
        return curr
last = 0
last2 = 0

seats = deepcopy(part2seats)
for m in range(i):
    for n in range(j):
        print(seats[m, n], end="")
    print()
print()
for _ in range(100):
    current_state = deepcopy(seats)
    for key in seats:
        if current_state[key] != ".":
            seats[key] = findNeighbours2(current_state, key[0], key[1])
    tot = sum([1 for v in seats.values() if v == "#"])
    if tot == last and tot == last2:
        print("Part1: ", tot)
        break
    else:
        last2 = last
        last = tot
    for m in range(i):
        for n in range(j):
            print(seats[m, n], end="")
        print()
    print()