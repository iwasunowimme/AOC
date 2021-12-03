# The Advent of Code challenge for day 3
""" https://adventofcode.com/2021/day/3 """
import time
import re
from collections import defaultdict
#Read in the file and return a list of all the integers
def readFile() -> list:
    with open("DAY03/input.txt", "r") as f:
        return [line.strip("\n") for line in f.readlines()]
vals = readFile()


# vals = ['00100','11110','10110','10111','10101','01111','00111','11100','10000','11001','00010','01010']

# Full expansion and iteration
all = []
for i in range(len(vals[0])):
    row = []
    for item in vals:
        row.append(int(item[i]))
    all.append(row)
ep = ''
for each in all:
    if sum(each) > len(each) // 2:
        ep += '1'
    else:
        ep += '0'

# Transpose list
a=''
for each in list(map(list, zip(*vals))):
    if sum(int(x) for x in each) *2 > len(each):
        a+='1'
    else:
        a+='0'


# One liner
b = ''.join(['1' if sum(int(x) for x in each) *2 > len(each) else '0' for each in list(zip(*vals)) ])

ma = int(''.join('1' for _ in range(len(vals[0]))),2)
print(int(ep,2)*(ma-int(ep,2)))
print(int(a,2)*(ma-int(a,2)))
print(int(b,2)*(ma-int(b,2)))

l = vals.copy()
# while len:
co2_vals = vals.copy()
o2_vals = vals.copy()
o2_ans = ''
co2_ans = ''
for i in range(len(vals[0])):
    row = []
    for item in o2_vals:
        row.append(int(item[i]))
    o2 = ''
    if 2*sum(row) >= len(row):
        o2 = '1'
    else:
        o2 = '0'
    new_vals = []
    for item in o2_vals:
        if item[i] == o2:
            new_vals.append(item)
    if len(new_vals) == 1:
        o2_ans = new_vals[0]
    o2_vals = new_vals.copy()
    
# print(o2_ans)

for i in range(len(vals[0])):
    row = []
    for item in co2_vals:
        row.append(int(item[i]))
    co2 = ''
    if 2*sum(row) < len(row):
        co2 = '1'
    else:
        co2 = '0'
    new_vals = []
    for item in co2_vals:
        if item[i] == co2:
            new_vals.append(item)
    if len(new_vals) == 1:
        co2_ans = new_vals[0]
    co2_vals = new_vals.copy()


print(int(co2_ans,2)*int(o2_ans,2))