# The Advent of Code challenge for day 4
# https://adventofcode.com/2021/day/4 
import numpy as np
#Read in the file and return a list of all the integers
def readFile():
    with open("DAY04/input.txt", "r") as f:
        return [line.strip("\n") for line in f.readlines()]


vals = readFile()
CALLED = [int(x) for x in vals[0].split(',')]


boards = []
curr = []
# Read the input for the boards and add to list
for row in vals[2:]:
    if row == '':
        boards.append(curr)
        curr = []
    else:
        curr.append([int(x) for x in row.split()])


# Create a method to play the entire bingo per board
def play(board):
    # Initialise a win board to find wining spots
    win = [[0,0,0,0,0] for _ in range(5)]
    for z,num in enumerate(CALLED):  # for each number in the bingo called list
        for i,row in enumerate(board):  # For each row in playing board
            for j,item in enumerate(row):  # for each number in row
                if item == num:
                    win[i][j] = 1
        if did_win(win):
            return z,num,win
    return 5000


# Find if there are any rows/column bingos
def did_win(board):
    if any(all(row) for row in board):   # If there is any row where all are 1 return true
        return True
    return any(all(row) for row in list(zip(*board))) # If there is any column where all are 1 return true else return

# Calculate the score of the board as sum of all non found digits times the multiplier
def calc_score(board,mask,multiplier):
    # Use numpy array to be able to use a truth list as a mask
    l = sum([sum(np.array(board_row)[[ o == 0 for o in mask_row]])  for board_row,mask_row in zip(board,mask)])
    return l*multiplier


high = float('inf')
winner = 0
low = 0
loser = 0
results = {}
# play through each board and keep track of winners, losers and a list of all boards masks and multipliers
for z,board in enumerate(boards):
    score, number, mask = play(board)
    if score > low:
        low = score
        loser = z
    if score < high:
        high = score
        winner = z
    results[z] = {"mask":mask,"number":number}

print(f"Part1: {calc_score(boards[winner],results[winner]['mask'],results[winner]['number'])}")
print(f"Part2: {calc_score(boards[loser],results[loser]['mask'],results[loser]['number'])}")