'''https://adventofcode.com/2015/day/16'''

import re

# Load file from input file
with open("input.txt", "r") as f:
    val = f.read()

# Create re for the input file and the information given by the spec
regex = re.compile(r'(\d+): (\w+):.(\d+), (\w+): (\d+), (\w+): (\d+)')
regex2 = re.compile(r'(\w+): (\d+)')
# The information given by the spec
results = "children: 3 cats: 7 samoyeds: 2 pomeranians: 3 akitas: 0 vizslas: 0 goldfish: 5 trees: 3 cars: 2 perfumes: 1"

# Create a dictionary for all the information given
information = {}
for key, value in regex2.findall(results):
    information[key] = int(value)

def match(key, value, part) -> bool:
    '''
    Checks the global information dictionary to find if the value given matches the information value
    adds additional functionality for part 2
    :param key: The key for the dictionary for which to compare
    :param value: The comparator variable
    :param part: A string for the part of the exercise
    :return: a boolean based on the key/value pair and part
    '''
    if part == 'part2':
        if key in ('cats', 'trees'):
            return information[key] < value
        elif key in ('pomeranians', 'goldfish'):
            return information[key] > value
    return information[key] == value


# Cycles through each input to find if there is a match with both parts
for auntNo, key1, value1, key2, value2, key3, value3 in regex.findall(val):
    if match(key1, int(value1), 'part1') and match(key2, int(value2), 'part1') and match(key3, int(value3), 'part1'):
        print("Part1: ", auntNo)
    if match(key1, int(value1), 'part2') and match(key2, int(value2), 'part2') and match(key3, int(value3), 'part2'):
        print("Part2: ", auntNo)
