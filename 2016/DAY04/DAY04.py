'''https://adventofcode.com/2016/day/4'''
import collections
import re

# Import data from text file
with open("input.txt", "r") as f:
    val = [lines[:-1] for lines in f.readlines()]

# Set counter to 0
sum_id = 0
# Create a dictionary for valid rooms
room_names = {}
# Compile regex to extract data
regex = re.compile(r'([a-z-]+)(\d+)\[(\w+)\]')
# For each input
for v in val:
    # Use the expression to extract all relevant data
    room, sectorID, checksum = re.findall(regex, v)[0]

    # Remove the "-" and compact the room title
    # For Part2 we can ignore spaces
    room_name = room.replace("-","")

    # Finds the order of which letters are most common and then combines them into a string
    # Collections counter finds the most most common by count n for letter c
    # Then it is added as a tuple to a list in order of -n to c to be able to use ascending sorting to get both alpha
    # And numeric sorting.
    # Then it extracts only the char and joins it to form a string
    decoy = ''.join([b for a, b in sorted([(-n, c) for c, n in collections.Counter(room_name).most_common()])])[:5]

    # If the checksum is valid, the sector ID is incremented
    if checksum == decoy:
        sum_id += int(sectorID)
        # If valid room it is added to list to be deciphered
        room_names[' '.join(room_name)] = int(sectorID)


print("Part1:", sum_id)

# Set the values of a and z as their ordinal values
a = ord('a')
z = ord('z')
for room in room_names:
    cypher = room_names[room]
    # Create my own Ceaser Cypher using the ord values
    temp = ''.join([chr((ord(t) + cypher - a) % (z-a+1) + a) for t in room if t != " "])
    # If the word North appears we know it is the right one (answer is "north pole object storage")
    if "north" in temp:
        print("Part2:", temp, cypher)



