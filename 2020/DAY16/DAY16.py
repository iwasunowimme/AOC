# https://adventofcode.com/2020/day/16

import re

# Import data from text file
with open("input.txt", "r") as f:
    values = [lines[:-1] for lines in f.readlines()]

# Create extraction regex for numbers
numbers = re.compile(r'(\d+)')

# Create blank values for the fields, nearby tickets, and my ticket
fields = {}
nearby = []
my_ticket = []

# Create the index of the values for which they start with "departure" for use in part 2
departure_indexes = []
departure_indexes_pointer = 0
# Hard coded booleans to match formatting on input to know which section we are up to
section = 0
for value in values:

    # After every empty line increment section counter
    if value == '':
        section += 1
    else:
        if section == 0:  # Fields
            data = value.split(":")
            fields[data[0]] = [int(i) for i in numbers.findall(data[1])]
            # If the field is a "departure" field, add the index to the list
            if value.startswith("departure"):
                departure_indexes.append(departure_indexes_pointer)
        elif section == 1:  # Your ticket
            if value != 'your ticket:':
                # Add the values of the data to the my_ticket field
                my_ticket = [int(i) for i in value.split(',')]
        elif section == 2:  # Nearby tickets
            if value != 'nearby tickets:':  # Ignore text
                # Add the data to the nearby field
                nearby.append([int(i) for i in value.split(',')])
    departure_indexes_pointer += 1

# Find the complete range of numbers that is serviced by the ranges of the fields
complete_range = set()
# For every field
for key in fields:
    val = fields[key]
    # Add the first range, inclusive
    for i in range(val[0], val[1]+1):
        complete_range.add(i)
    # Add the second range, inclusive
    for i in range(val[2], val[3]+1):
        complete_range.add(i)

# Add the scanning rates
scanning_rate = 0
# Create a set of invalid ticket fields
invalid = set()
for ticket in [item for sublist in nearby for item in sublist]:
    # For each ticket in the nearby area, check if it is in a valid range anywhere
    # If not valid, add the number to the scanning rate and add the ticket to the invalid set
    if ticket not in complete_range:
        invalid.add(ticket)
        scanning_rate += ticket

print("Part1: ", scanning_rate)

# Set the total fields as the length of fields given from the input
total_fields = len(fields.keys())

# Find a list of only valid tickets
valid_tickets = [valid for valid in nearby if not any(x in valid for x in invalid)]

# Transpose the list so all the lists in the list are all the ith section on the ticket
columns = list(map(list, zip(*valid_tickets)))


trues = []

# Iterate each column to see if it can be valid for that data type
for column in columns:
    truth = []
    for key in fields:
        data = fields[key]
        count = 0
        #  Each row has a list of the 20 field types and if the ticket value is a valid range for all of it
        for row in column:
            if data[0] <= row <= data[1] or data[2] <= row <= data[3]:
                count += 1
        # If the number of valid values for the field type are all of them, it is True, otherwise False
        truth.append(count == len(column))
    # Add the columns truth table to the list
    trues.append(truth)

# We want to find all correct fields
correct_fields = {}
# Whilst there is still an unknown continue
while len(correct_fields) < total_fields:
    # It is possible to infinite loop if there are no valid options, this can be fixed by applying additional rules,
    # Such as transposing the list and looking at what field can only have a certain row

    # We look at each row of the trues and see if it can only be 1 specific field
    # The specific field will be equal to the ith position of the only true
    for count in range(total_fields):
        if sum(1 for z in trues[count] if z) == 1:  # Sum all the Trues, if exactly 1 it can only be the field
            for index, isTrue in enumerate(trues[count]):
                # Find the index of the true field, since there is only one
                if isTrue:
                    correct_fields[index] = count
                    # Set all values at the current truth index to false
                    for c_trues in trues:
                        c_trues[index] = False
                    # There is only one, no need to go further
                    break

# Product starts at 1
total = 1
# iterate through the departure indexes and multiply the ticket values together
for idx in departure_indexes:
    total *= my_ticket[correct_fields[idx]]

print("part2: ", total)
