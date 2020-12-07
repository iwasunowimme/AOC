# The Advent of Code challenge for day 6
""" https://adventofcode.com/2020/day/6 """

def readFile() -> list:
    with open("input.txt","r") as f:
        return [line[:-1] for line in f.readlines()]

def part1(vals):
    count = 0
    temp = set()
    for val in vals:
        if val == "":
            count += len(temp)
            temp = set()
        else:
            for each in val:
                temp.add(each)
    count += len(temp)
    return count
def part2(vals):
    count = 0
    temp = set()
    temp2 = set()
    p = True
    for val in vals:
        print(count)
        temp2 = set()
        if val == "":
            count += len(temp)
            temp = set()
            p = True
        else:
            for each in val:
                temp2.add(each)
            if p:
                temp = temp2
                p = False
                temp = temp & temp2
    count += len(temp)
    return count

if __name__ == "__main__":
    vals = readFile()
    print(part1(vals))
    print(part2(vals))