'''https://adventofcode.com/2015/day/18'''
from copy import deepcopy
with open("input.txt", "r") as f:
    values = [lines[:-1] for lines in f.readlines()]
#values = [".#.#.#","...##.","#....#","..#...","#.#..#","####.."]
one_hundred = 100
lights = {}
i = 0
for value in values:
    j = 0
    for light in value:
        if light == "#":
            lights[i, j] = 1
        else:
            lights[i, j] = 0
        j += 1
    i += 1
length = i
def findNeighbours(current, x, y) -> int:
    total = 0
    for xAxis in range(x-1,x+2):
        for yAxis in range(y-1, y+2):
            try:
                if xAxis == x and yAxis == y:
                    continue
                else:
                    total += current[xAxis, yAxis]
            except:
                continue
    return total


part2Lights = deepcopy(lights)
for _ in range(one_hundred):
    current_state = deepcopy(lights)
    for key in lights:
        neighbours = findNeighbours(current_state, key[0], key[1])
        if current_state[key] == 1:
            if neighbours not in (2, 3):
                lights[key] = 0
        else:
            if neighbours == 3:
                lights[key] = 1


print("Part1: ", sum(lights.values()))
corners =[(0, 0), (0, length-1) , (length-1, 0), (length-1, length-1)]
for corner in corners:
    part2Lights[corner] = 1
for _ in range(one_hundred):
    current_state2 = deepcopy(part2Lights)
    for key in part2Lights:

        if key in corners:
            continue
        else:
            neighbours = findNeighbours(current_state2, key[0], key[1])
            if current_state2[key] == 1:
                if neighbours not in (2, 3):
                    part2Lights[key] = 0
            else:
                if neighbours == 3:
                    part2Lights[key] = 1

print("Part1: ", sum(part2Lights.values()))

