import re
from collections import defaultdict
from itertools import combinations
from itertools import permutations
from copy import deepcopy

# Import data from text file
with open("input.txt", "r") as f:
    values = [lines[:-1] for lines in f.readlines()]

#values = ['2 * 3 + (4 * 5)','5 + (8 * 3 + 9 + 3 * 4 * 3)','5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))','((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2']
#values = ['((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2']

def calc(val):
    sum = 0
    i=0
    symbol = ''
    while i < len(val):
        if val[i] !=' ':
            if val[i].isdigit():
                if sum == 0:
                    sum = int(val[i])
                elif symbol == '+':
                    sum += int(val[i])
                    symbol = ''
                elif symbol == '*':
                    sum *= int(val[i])
                    symbol = ''
            elif val[i] == ")":
                return sum, i
            elif val[i] == '+' or val[i] == '*':
                symbol = val[i]
            elif val[i] == "(":
                if symbol == '+':
                    s, j = calc(val[i + 1:])
                    sum += s
                    symbol = ''
                elif symbol == '*':
                    s, j = calc(val[i + 1:])
                    sum *= s
                    symbol = ''
                elif symbol == '':
                    s, j = calc(val[i + 1:])
                    sum += s
                i += j + 1
        i += 1
    return sum, i



total = 0
for v in values:
    x, _ = calc(v)
    print(x)
    total += x

print(total)

def calc2(val):
    sum = 0
    i=0
    symbol = ''
    pro = []
    while i < len(val):
        if val[i] !=' ':
            if val[i].isdigit():
                if sum == 0:
                    sum = int(val[i])
                elif symbol == '+':
                    sum += int(val[i])
                    symbol = ''
                elif symbol == '*':
                    pro.append(sum)
                    sum = int(val[i])
                    symbol = ''
            elif val[i] == ")":

                for p in pro:
                    sum *= p
                return sum, i
            elif val[i] == '+' or val[i] == '*':
                symbol = val[i]
            elif val[i] == "(":
                if symbol == '+':
                    s, j = calc2(val[i + 1:])
                    sum += s
                    symbol = ''
                elif symbol == '*':
                    s, j = calc2(val[i + 1:])
                    pro.append(sum)
                    sum = s

                    symbol = ''
                elif symbol == '':
                    s, j = calc2(val[i + 1:])
                    sum += s
                i += j + 1
        i += 1
    for p in pro:
        sum *= p
    return sum, i



total = 0
for v in values:
    x, _ = calc2(v)
    print(x)
    total += x

print(total)

