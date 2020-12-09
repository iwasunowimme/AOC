# The Advent of Code challenge for day 1
""" https://adventofcode.com/2020/day/1 """

#Read in the file and return a list of all the integers
def readFile() -> list:
    with open("input.txt", "r") as f:
        return [int(line[:-1]) for line in f.readlines()]

#Find the two numbers that add up to 2020 in vals and then return the product
def part1(vals) -> int:
    for each in vals:
        if (2020 - each) in vals:
            return((2020-each) * each)

#Find the three numbers that add up to 2020 in vals and then return the product
def part2(vals) -> int:
    for each in vals:
        for each2 in vals:
            if (2020-each-each2) in vals:
                return(each*each2*(2020-each-each2))


def test():
    test_input = [1721, 979, 366, 299, 675, 1456]
    assert part1(test_input) == 514579
    assert part2(test_input) == 241861950

if __name__ == "__main__":
    test()
    vals = readFile()
    print(part1(vals))
    print(part2(vals))
