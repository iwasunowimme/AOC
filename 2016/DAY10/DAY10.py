"""https://adventofcode.com/2016/day/10"""
from collections import defaultdict
from functools import reduce
import re

# Read input from text file
with open("input.txt", "r") as f:
    values = [lines[:-1] for lines in f.readlines()]
# Comparator values given from source description
Comparator_values = {17, 61}

# Example data
# with open("example.txt", "r") as f:
#     values = [lines[:-1] for lines in f.readlines()]
# Comparator_values = {2, 5}

# Create default dict to house values that the bot has, list as we are expecting more than 1 value
bots = defaultdict(list)
outputs = defaultdict(list)

# Set re compiled
re_values = re.compile(r'\d+')  #  We assume no negative numbers r'-?/d+' for negative
re_boro = re.compile(r' (bot|output)')  # Only two options, bot and output (need the space to ignore starting bot)

# Treat as a FIFO queue until it is empty, place unused instructions at the end
while values:
    # Get instruction
    v = values.pop(0)
    # Split it at white spaces
    msg = v.split()

    if v.startswith('b'):  # If is a Bot transfer
        # Get the bot values from the input
        bot, low, high = map(int, re_values.findall(v))
        # Find whether the transfer targets are bots or outputs
        low_boro, high_boro = re_boro.findall(v)
        # This assumes that it is impossible for a bot to receive more than 2 microchips ever
        # Does not agree with discrete time
        if len(bots[bot]) == 2:  # If has exactly two microchips to process
            if set(bots[bot]) == Comparator_values:  # If the set we require that compares specific numbers
                print("Part1:", bot)

            # Append the min and max values to their respective bots/outputs
            if low_boro == 'bot':  # If a bot
                bots[low].append(min(bots[bot]))
            else:  # If an output bin
                outputs[low].append(min(bots[bot]))

            if high_boro == 'bot':  # If a bot
                bots[high].append(max(bots[bot]))
            else:  # If an output bin
                outputs[high].append(max(bots[bot]))
            bots[bot] = []  # Clear what the bot is holding
        else:  # Not enough microchips, not ready for instruction -- skip till the end
            values.append(v)

    elif v.startswith('v'):  # If bot receiving initial value
        # Get the values from the input and append to correct bot
        value, bot = map(int, re_values.findall(v))
        bots[bot].append(value)

# Part2, print the product of the outputs 0 1 and 2
print("Part2:", reduce(lambda a, b: a * b, [outputs[i][0] for i in (0, 1, 2)]))
