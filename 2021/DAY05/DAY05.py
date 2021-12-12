# The Advent of Code challenge for day 5
""" https://adventofcode.com/2021/day/5 """
from collections import defaultdict
#Read in the file and return a list of all the integers
def readFile() -> list:
    with open("DAY05/input.txt", "r") as f:
        return [line.strip("\n") for line in f.readlines()]
vals = readFile()


boards = []

def play(part):
    board = defaultdict(int)
    for row in vals:
        start,finish = row.split(" -> ")
        x1,y1 = start.split(',')
        x2,y2 = finish.split(',')
        # Lable start and end positions, flip so the line runs left to right
        if int(x1) > int(x2):
            startx = int(x2)
            endx = int(x1)
            starty = int(y2)
            endy =int(y1)
        else:
            startx = int(x1)
            endx = int(x2)
            starty = int(y1)
            endy =int(y2)
        
        if int(x1) == int(x2) or int(y1) == int(y2):  # IF it is a straight line
            if endy > starty:  # If line goes down
                for i in range(startx,endx+1):
                    for j in range(starty,endy+1):
                        board[f"{i},{j}"] +=1
            else:  # if line goes up
                for i in range(startx,endx+1):
                    for j in range(starty,endy-1,-1):  # Reverse y direction
                        board[f"{i},{j}"] +=1
        else:  # A diagonal line
            if part == 2:  # Only needed in part 2
                # Zip together so they always incrememnt ast the same time sinze it is a guaranteed 45 degree
                if endy > starty:
                    for i,j in zip(range(startx,endx+1),range(starty,endy+1)):
                        board[f"{i},{j}"] +=1
                else:
                    for i,j in zip(range(startx,endx+1),range(starty,endy-1,-1)): # Reverse y direction
                        board[f"{i},{j}"] +=1

    counter = sum(1 for v in board.values() if v > 1)
    print(counter)
play(1)
play(2)
# for i in range(10):
#     for j in range(10):
#         print(board[f"{j},{i}"],end="")
#     print()