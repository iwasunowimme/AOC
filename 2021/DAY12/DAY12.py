# The Advent of Code challenge for day 12
""" https://adventofcode.com/2021/day/12 """
import time
from collections import defaultdict
from collections import deque 
#Read in the file and return a list of all the integers
def readFile():
    with open("DAY12/input.txt", "r") as f:
        return [line.strip("\n") for line in f.readlines()]

vals = readFile()

graph = defaultdict(list)
for each in vals:
    start,end = each.split("-")
    graph[start].append(end)
    graph[end].append(start)

# paths = set()

# Use queue to add completed passes to go through
def solve(part2):
    # Only need to keep track of the small seen
    start =  ('start',set(['start']),True)
    count = 0
    dqueue = deque([start])
    while dqueue:
        point, small_seen, twice = dqueue.popleft()
        if point == 'end':  # we have reached the end
            count += 1
            continue
        for each in graph[point]:
            if each not in small_seen:
                new_seen = set(small_seen)
                if each.islower(): # If it is lower we care if it is seen
                    new_seen.add(each)
                dqueue.append((each,new_seen,twice))        
            elif each in small_seen and twice and each not in ['start','end'] and part2:  # if it is smaller and seen but is part 2 check if it is seen once
                dqueue.append((each, small_seen, False))
    return count

t1 = time.perf_counter() 
print(f"Part 1: {solve(False)}")
t2 = time.perf_counter() 
print(f"Part 2: {solve(True)}")
t3 = time.perf_counter() 


# Traverse through the list recursively
def traverse(x,visisted,triggered,part2):
    pathings = []
    if x == 'end': # end
        return [[x]]
    if x == 'start' and visisted != []:  # first start to initialise
        return []
    if x in visisted:  # if we have gone through it before
        if not x.isupper():
            if triggered or not part2:
                return []
            else:
                triggered = True
    # find all that the subsequent can go through
    for path in graph[x]:
            for each in traverse(path,visisted + [x],triggered,part2):
                pathings.append([x] + each)
    return pathings

t4 = time.perf_counter() 
h = traverse('start',[],False,False)
t5 = time.perf_counter() 
print(f"Part 1: {len(h)}")
traversed = traverse('start',[],False,True)
t6 = time.perf_counter() 
print(f"Part 2: {len(traversed)}")
print(f"Part 1 dequeue timing {t2-t1}")
print(f"Part 1 recursive list timing {t5-t4}")
print(f"Part 2 dequeue timing {t3-t2}")
print(f"Part 2 recursive list timing {t6-t5}")