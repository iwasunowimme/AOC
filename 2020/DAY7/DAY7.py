# The Advent of Code challenge for day 7
""" https://adventofcode.com/2020/day/7 """

def readFile() -> list:
    with open("input.txt","r") as f:
        return [line[:-1] for line in f.readlines()]

def part1(vals):
    bags = {}
    numbers = [str(i) for i in range(10)]
    deadwords = ["bags","bag","contain","bags,","bag,","bags.","bag."]
    for val in vals:
        bagList = []
        rules = val.split()
        key = rules[0]+" "+ rules[1]
        value = []
        for rule in rules[2:]:
            if rule in deadwords  or rule in numbers:
                continue
            else:
                value.append(rule)
        for i in range(0,len(value),2):
            bagList.append(value[i]+" "+value[i+1])
        bags[key] = bagList
    gold = "shiny gold"
    step = set()
    for item in bags:
        if gold in bags[item]:
            step.add(item)
    visited = set()
    tovisit = ["shiny gold"]
    while tovisit:
        tester = tovisit.pop(0)
        for item in bags:
            if tester in bags[item]:
                if item not in visited:
                    tovisit.append(item)
                    visited.add(item)

    print(len(visited))
    print("shiny gold" in visited)

def part2(vals):
    bags = {}
    bagsN = {}
    numbers = [str(i) for i in range(10)]
    deadwords = ["bags", "bag", "contain", "bags,", "bag,", "bags.", "bag."]
    for val in vals:
        bagList = []
        nlist = []
        rules = val.split()
        key = rules[0] + " " + rules[1]
        value = []
        for rule in rules[2:]:
            if rule in deadwords:
                continue
            elif rule in numbers:
                nlist.append(rule)
            else:
                value.append(rule)
        for i in range(0, len(value), 2):
            bagList.append(value[i] + " " + value[i + 1])
        bags[key] = bagList
        bagsN[key] = nlist
    tovisit = ["shiny gold"]
    count = -1
    while tovisit:
        count += 1
        tester = tovisit.pop(0)
        search = bags[tester]
        for j in range(len(search)):
            print(j,search,tester)
            if search[j] != 'no other':
                for _ in range(int(bagsN[tester][j])):
                    tovisit.append(search[j])

    print(count)


if __name__ == "__main__":
    vals = readFile()
    #part1(vals)
    part2(vals)
