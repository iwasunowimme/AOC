'''https://adventofcode.com/2020/day/11'''

from copy import deepcopy


with open("input.txt", "r") as f:
    seats = [lines[:-1] for lines in f.readlines()]

# Test data
# seats =["L.LL.LL.LL","LLLLLLL.LL","L.L.L..L..","LLLL.LL.LL","L.LL.LL.LL","L.LLLLL.LL","..L.L.....","LLLLLLLLLL","L.LLLLLL.L","L.LLLLL.LL"]

# Convert the strings to lists
seats = [list(a) for a in seats]
# Create a deep copy to be used for part 2
seatspart2 = deepcopy(seats)

# Set max values, assumes data it is a rectangle
yMax = len(seats[0])
xMax = len(seats)

# Find convergence by comparing last 3 sums
last = 0
last2 = 0

# Iterate for an arbitrary large number (assume convergence before range ends)
for _ in range(100):
    new_seats = deepcopy(seats)

    # iterate through entire list as a 2d array
    for x in range(xMax):
        for y in range(yMax):
            if seats[x][y] != ".":  # Skip if it is the floor
                total = 0

                # finds neighbours by modifying current x and y with -1, 0, or +1
                for xAxis in range(-1, 2):
                    for yAxis in range(-1, 2):
                        if not (xAxis == 0 and yAxis == 0):  # If not the cell itself (not a neighbour)
                            # Add modifiers
                            xCell = x + xAxis
                            yCell = y + yAxis

                            # If cell is valid and is occupied
                            if 0 <= yCell < yMax and 0 <= xCell < xMax and seats[xCell][yCell] == '#':
                                total += 1

                curr = seats[x][y]  # Find current state
                # If seat is empty and there are no occupied seats, occupy the seat
                if curr == 'L' and total == 0:
                    new_seats[x][y] = '#'
                # If seat is occupied and there are more thant 4 occupied seats, vacate the seat
                elif curr == '#' and total >= 4:
                    new_seats[x][y] = 'L'
                # Keep state same if not met before
                else:
                    new_seats[x][y] = curr

            # If the floor, stay as the floor
            else:
                new_seats[x][y] = seats[x][y]
    # the seats become the new seats
    seats = deepcopy(new_seats)

    # Sum all occupied seat
    tot = sum([row.count('#') for row in seats])
    if tot == last and tot == last2:
        print("Part1: ", tot)
        break
    else:
        last2 = last
        last = tot


last = 0
last2 = 0
# Iterate for an arbitrary large number (assume convergence before range ends)
for _ in range(100):
    new_seats = deepcopy(seatspart2)

    # iterate through entire list as a 2d array
    for x in range(xMax):
        for y in range(yMax):
            if seatspart2[x][y] != ".":  # Skip if it is the floor
                total = 0

                # finds neighbours by modifying current x and y with -1, 0, or +1
                for xAxis in range(-1, 2):
                    for yAxis in range(-1, 2):
                        if not (xAxis == 0 and yAxis == 0):  # If not the cell itself (not a neighbour)
                            # Add modifiers
                            xCell = x + xAxis
                            yCell = y + yAxis
                            while 0 <= yCell < yMax and 0 <= xCell < xMax and seatspart2[xCell][yCell] == '.':
                                xCell += xAxis
                                yCell += yAxis
                            # If cell is valid and is occupied
                            if 0 <= yCell < yMax and 0 <= xCell < xMax and seatspart2[xCell][yCell] == '#':
                                total += 1

                curr = seatspart2[x][y]  # Find current state
                # If seat is empty and there are no occupied seats, occupy the seat
                if curr == 'L' and total == 0:
                    new_seats[x][y] = '#'
                # If seat is occupied and there are more thant 4 occupied seats, vacate the seat
                elif curr == '#' and total >= 5:
                    new_seats[x][y] = 'L'
                # Keep state same if not met before
                else:
                    new_seats[x][y] = curr

            # If the floor, stay as the floor
            else:
                new_seats[x][y] = seatspart2[x][y]
    # the seats become the new seats
    seatspart2 = deepcopy(new_seats)

    # Sum all occupied seat
    tot = sum([row.count('#') for row in seatspart2])
    if tot == last and tot == last2:
        print("Part1: ", tot)
        break
    else:
        last2 = last
        last = tot

