'''https://adventofcode.com/2015/day/14'''
import re

# Import values from file
with open("input.txt", "r") as f:
    vals = [lines[:-1] for lines in f.readlines()]

# Manual input from specs
seconds = 2503

# Test inputs
#seconds = 1000
#vals = ["Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.","Dance can fly 16 km/s for 11 seconds, but then must rest for 162 seconds."]

# Create re compiler to pass data
p1 = re.compile(r'(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+).*')

# Create dictionary to store data and a set to store unique names
reindeers = {}
names = set()
# Set a list of distance that all travel
distance = []

# Go through each line in the input
for val in vals:
    # Use the re to split out the important information and store in dictionary
    reindeer, speed, flighttime, resttime = p1.match(val).groups()
    speed = int(speed)
    flighttime = int(flighttime)
    resttime = int(resttime)
    # Add values to dictionary
    reindeers[reindeer, "speed"] = speed
    reindeers[reindeer, "flighttime"] = flighttime
    reindeers[reindeer, "resttime"] = resttime
    # Formula for distance calculates loops of fly rest cycles and remaining seconds for last loop
    distance.append(speed * ((flighttime * (seconds//(flighttime + resttime))) +
                             min(flighttime, seconds % (flighttime + resttime))))
    names.add(reindeer)


print("Part1: ", max(distance))

# Create dictionaries to keep the information of the points and current position for each reindeer
points = {}
position = {}
for n in names:
    points[n] = 0
    position[n] = 0
# Go through each second to calculate distances and points
for second in range(seconds):
    max_name = []
    max_dist = 0
    # For each reindeer
    for name in names:
        kmh = reindeers[name, "speed"]
        ft = reindeers[name, "flighttime"]
        rt = reindeers[name, "resttime"]
        # If they should be flying, increment by speed
        if second % (ft + rt) < ft:
            position[name] += kmh

        # If they are currently further than the lead, add the name to an empty list
        if position[name] > max_dist:
            max_name = [name]
            max_dist = position[name]
        # Else if they are currently in the lead add the name to the list
        elif position[name] == max_dist:
            max_name.append(name)
    # Increase points for all reindeer tied in the lead
    for n in max_name:
        points[n] += 1


print("Part2: ", max(points.values()))


