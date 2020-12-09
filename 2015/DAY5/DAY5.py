'''https://adventofcode.com/2015/day/5'''

with open("input.txt","r") as f:
    vals = [lines[:-1] for lines in f.readlines()]

nice = 0
bad = ['ab', 'cd', 'pq', 'xy']  # list of bad substrings
vowels = ['a', 'e', 'i', 'o', 'u']  # list of vowels
for val in vals:
    double = False
    vow = 0
    if not any(x in val for x in bad):  # see if they contain bad substrings
        if sum(x in vowels for x in val) > 2:  # see if there are more than 2 vowels
            for v in range(len(val)-1):  # compare two neighbouring characters
                if val[v] == val[v+1]:
                    double = True
            if double:  # contains all nice things
                nice += 1
print("part1: ", nice)

nice = 0
for val in vals:
    sando = False
    pair = False
    for v in range(len(val)-2):
        if val[v] == val[v+2]:  # checks if there are two of the same letters separated by n+2
            sando = True
        if v == 0:  # checks if the substring of the first two letters appears in the rest of the string
            if val[:2] in val[2:]:
                pair = True
        else:
            if val[v:v+2] in val[v+2:]:  # breaks the string where we are and checks if the substring is in the rest
                pair = True
    if sando and pair:  # if both are true they are nice
        nice += 1
print("part2: ", nice)

