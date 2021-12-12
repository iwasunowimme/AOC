# The Advent of Code challenge for day 11
""" https://adventofcode.com/2021/day/11 """

#Read in the file and return a list of all the integers
def readFile():
    with open("DAY11/input.txt", "r") as f:
        return [line.strip("\n") for line in f.readlines()]

vals = readFile()
octs = {}
rows = len(vals)
cols = len(vals[0])
total = rows*cols # total numbers on the board

# Crate the board as a dictionary of tuple coordinates
for i,row in enumerate(vals):
    for j,col in enumerate(row):
        octs[i,j] = int(col)


# If  something flashed return all the valid surrounding points
def flashed(i,j):
    rlist = []
    for x in [-1,0,1]:
        for y in [-1,0,1]:
            xx = i + x
            yy = j + y
            if (xx >= 0 and xx < rows) and (yy>=0 and yy < cols) and not (x == 0 and y == 0): # If point within valid grid
                rlist.append((xx,yy))
    return rlist


# simulate one iteration
def play():
    flashes = []
    flash_count = 0
    # Go through everypoint and increase by 1
    for i in range(rows):
        for j in range(cols):
            temp = octs[i,j]
            if temp == 9: # If there is a flash  set value to 0, take count, save coords
                octs[i,j] = 0
                flashes.append((i,j))
                flash_count += 1
            else:
                octs[i,j] += 1

    while flashes:  # Whilst there is flashes left
        to_burn = [] 
        for flash in flashes:
            to_burn = to_burn + flashed(flash[0],flash[1]) # find list of all points to flash including duplicates
        flashes = [] # Reset flashes

        # Iterate through all flashed points and increment
        for each in to_burn:
            i = each[0]
            j = each[1]
            temp = octs[i,j]
            if temp == 9: # If it has then been flashed add to list
                octs[i,j] = 0
                flashes.append((i,j))
                flash_count += 1
            elif temp != 0: # Do nothing if it has already flashed this round, else increment 
                octs[i,j] += 1
    return flash_count

total_flash_count = 0
i = 0
winner= 0
while winner == 0 or i < 100:  # play whilst there is no full flash and for at least the first 100 iterations
    bu = play()
    if bu == total:  # Everything flashed
        winner = 1 + i
    if i < 100: # Only count the first 100
        total_flash_count += bu
    i += 1
    
print(f"Part 1: {total_flash_count}")
print(f"Part 2: {winner}")
