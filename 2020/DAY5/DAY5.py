# The Advent of Code challenge for day 5
""" https://adventofcode.com/2020/day/5 """

def readFile() ->list:
    with open('input.txt','r') as f:
        return [line[:-1] for line in f.readlines()]

def part1(vals):
    highestID = 0
    for val in vals:
        binNumber = ""
        binRow = ""
        for v in val[:-3]:
            if v == "F":
                binNumber += "0"
            else:
                binNumber += "1"
        for w in val[-3:]:
            if w == "R":
                binRow += "1"
            else:
                binRow += "0"
        seatId = int(binNumber,2)*8+int(binRow,2)
        if seatId > highestID:
            highestID = seatId
    return highestID

def part2(vals):
    seatIds = []
    for val in vals:
        binNumber = ""
        binRow = ""
        for v in val[:-3]:
            if v == "F":
                binNumber += "0"
            else:
                binNumber += "1"
        for w in val[-3:]:
            if w == "R":
                binRow += "1"
            else:
                binRow += "0"
        seatIds.append(int(binNumber, 2) * 8 + int(binRow, 2))
    seatIds.sort()
    for i in range(len(seatIds)):
        if seatIds[i] != seatIds[i+1] - 1:
            return seatIds[i] + 1


def test():
    test_vals = ["BFFFBBFRRR","FFFBBBFRRR","BBFFBBFRLL"]
    assert part1(test_vals) == 820

if __name__ == "__main__":
    vals = readFile()
    test()
    print(part1(vals))
    print(part2(vals))