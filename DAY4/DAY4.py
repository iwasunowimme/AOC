# The Advent of Code challenge for day 4
""" https://adventofcode.com/2020/day/4 """
import re

#Read in the file and return a list of all the integers
def readFile() -> list:
    with open("input.txt", "r") as f:
        return [line[:-1] for line in f.readlines() ]

def part1(vals):
    count = 0
    temp = set()
    masterSet = {"byr","iyr","eyr","hgt","hcl","ecl","pid"}
    for val in vals:
        if val == "":
            if  masterSet - temp ==  set():
                count+=1
            temp = set()
        else:
            for each in val.split(" "):
                temp.add(each.split(":")[0])
    if masterSet - temp == set():
        count += 1
    return count

#check the validity using the metrics stated
def part2(vals):
    count = 0
    temp = set()
    tempDict = {}
    allPassports = []
    masterSet = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
    for val in vals:
        if val == "":
            if masterSet - temp == set():
                allPassports.append(tempDict)
            temp = set()
            tempDict = {}
        else:
            for each in val.split(" "):
                tempSplit = each.split(":")
                temp.add(tempSplit[0])
                tempDict[tempSplit[0]] = tempSplit[1]
    if masterSet - temp == set():
        allPassports.append(tempDict)
    eclMaster = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}
    hclMaster = "0123456789abcdef"
    for passport in allPassports:
        if int(passport["byr"]) >= 1920 and int(passport["byr"]) <=2002:
            if int(passport["iyr"]) >= 2010 and int(passport["iyr"]) <=2020:
                if int(passport["eyr"]) >= 2020 and int(passport["eyr"]) <= 2030:

                    hgt = passport["hgt"]
                    validHgt = False
                    hgtValue = int(re.sub('\D', '', hgt))
                    hgtMetric = re.sub('[^a-z]', '', hgt)

                    if hgtMetric == "cm":
                        if hgtValue >= 150 and hgtValue <= 193:
                            validHgt = True
                    elif hgtMetric == "in":
                        if hgtValue >= 59 and hgtValue <= 76:
                            validHgt = True
                    if validHgt:

                        hcl = passport["hcl"]
                        validHcl = True
                        if len(hcl) != 7:
                            validHcl = False
                        else:
                            if hcl[0] != "#":
                                validHcl = False
                            else:
                                for hc in hcl[1:]:
                                    if hc not in hclMaster:
                                        validHcl = False
                        if validHcl:
                                if passport["ecl"] in eclMaster:
                                    if len(passport["pid"]) == 9:
                                        count += 1



    return(count)

def test():
    test_vars = ["ecl:gry pid:860033327 eyr:2020 hcl:#fffffd","byr:1937 iyr:2017 cid:147 hgt:183cm","","iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884","hcl:#cfa07d byr:1929","","hcl:#ae17e1 iyr:2013","eyr:2024","ecl:brn pid:760753108 byr:1931","hgt:179cm","","hcl:#cfa07d eyr:2025 pid:166559648","iyr:2011 ecl:brn hgt:59in"]
    assert part1(test_vars) == 2
    assert part2(test_vars) == 2

if __name__ == "__main__":
    test()
    vals = readFile()
    print(part1(vals))
    print(part2(vals))
