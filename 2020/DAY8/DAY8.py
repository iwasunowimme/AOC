# The Advent of Code challenge for day 8
""" https://adventofcode.com/2020/day/8 """

def readfile() -> list:
    with open("input.txt","r") as f:
        return [line[:-1] for line in f.readlines()]

def part1(vals):
    acc = 0
    visited = set()
    i = 0
    while i not in visited:
        visited.add(i)
        ints = vals[i].split()
        if ints[0] == "nop":
            i += 1
        elif ints[0] == "acc":
            acc += int(ints[1])
            # if ints[1][0] == "-":
            #     acc -= int(ints[1][1:])
            # else:
            #     acc += int(ints[1][1:])
            i += 1
        else:
            i += int(ints[1])
            # if ints[1][0] == "-":
            #     i -= int(ints[1][1:])
            # else:
            #     i += int(ints[1][1:])
    return acc
def part2(vals):
    acc = 0
    k = 0
    infloop = False
    done = True
    for j in range(len(vals)):

        visited = set()
        acc = 0
        i = 0
        infloop = False
        done = True
        k=0
        while done:
            if i in visited:
                infloop = True
                done = False
            visited.add(i)
            ints = vals[i].split()

            if j == k:
                if ints[0] == "nop":
                    ints[0] = "jmp"
                elif ints[0] == "jmp":
                    ints[0] = "nop"
            k += 1
            if ints[0] == "nop":
                i += 1
            elif ints[0] == "acc":
                acc += int(ints[1])
                # if ints[1][0] == "-":
                #     acc -= int(ints[1][1:])
                # else:
                #     acc += int(ints[1][1:])
                i += 1
            else:
                i += int(ints[1])
                # if ints[1][0] == "-":
                #     i -= int(ints[1][1:])
                # else:
                #     i += int(ints[1][1:])
            if i >= 600:
                done = False

        if infloop == False:
            return acc

    return 0

if __name__ == "__main__":
    vals = readfile()
    print(part1(vals))
    print(part2(vals))