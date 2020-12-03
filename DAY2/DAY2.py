# The Advent of Code challenge for day 2
""" https://adventofcode.com/2020/day/2 """

#Read in the file and return a list of all the integers
def readFile() -> list:
    with open(f"{__file__.rstrip('DAY2.py')}input.txt", "r") as f:
        return [str(line[:-1]) for line in f.readlines()]

#Find the count of passwords that do fit the criteria
#Input is a list of strings in the form: int-int char : string
#where the two ints provide the upper and lower bounds of the frequency of the char in the str
def part1(vals) -> int:
    count = 0
    for each in vals: # iterate through all list objects
        split = each.split() #split the string
        bounds = [int(i) for i in split[0].split('-')] # extract the bounds
        letter = split[1][0] # extract the letter sans ":"
        pwd = split[2] # extract the password
        freq = pwd.count(letter) # find the frequency of the letter in the pwd
        if freq <= bounds[1] and freq >= bounds[0]: # if the frequency is within bounds increase count
            count += 1
    return count

#Find the count of passwords that do fit the criteria
#Input is a list of strings in the form: int-int char : string
#where the two ints provide the two index of the char in the str as a XAND
def part2(vals):
    count = 0
    for each in vals:  # iterate through all list objects
        split = each.split()  # split the string
        bounds = [int(i) for i in split[0].split('-')]  # extract the bounds
        letter = split[1][0]  # extract the letter sans ":"
        pwd = split[2]  # extract the password
        if pwd[bounds[0]-1] == letter:
            if pwd[bounds[1]-1] != letter:
                count += 1
        elif pwd[bounds[1]-1] == letter:
            count += 1
    return count

def test():
    test_input = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]
    assert part1(test_input) == 2
    assert part2(test_input) == 1

if __name__ == "__main__":
    test()
    vals = readFile()
    print(part1(vals))
    print(part2(vals))