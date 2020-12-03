# The Advent of Code challenge for day 3
""" https://adventofcode.com/2020/day/3 """

#Read in the file and return a list of all the integers
def readFile() -> list:
    with open(f"{__file__.rstrip('DAY3.py')}input.txt", "r") as f:
        return [str(line[:-1]) for line in f.readlines()]

# itterates through the list to find the collisions
def part1(vals) -> int:
    return countTrees(vals, 3, 1)

def countTrees(vals,right,down) -> int:
    yCoord = 0
    yCount = 0
    yCheck = 0
    trees = 0
    for each in vals:
        if yCheck == yCoord:
            xCoord = ( yCount * right ) % len(each) # find the xcoord based on the the formula right*y % max(x)
            trees += each[xCoord] == '#' #if its a tree add 1
            yCoord += down
            yCount += 1
        yCheck += 1

    return trees

def part2(vals) -> int:
    t = countTrees(vals,1,1)*countTrees(vals,3,1)*countTrees(vals,5,1)*countTrees(vals,7,1)*countTrees(vals,1,2)
    return t


def test():
    test_input = ["..##.......","#...#...#..",".#....#..#.","..#.#...#.#",".#...##..#.","..#.##.....",".#.#.#....#",
                  ".#........#","#.##...#...","#...##....#",".#..#...#.#"]
    assert part1(test_input) == 7
    assert part2(test_input) == 336

if __name__ == "__main__":
    test()
    vals = readFile()
    # print(vals)
    # part1(vals)
    print(part1(vals))
    print(part2(vals))

