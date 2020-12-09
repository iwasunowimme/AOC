"""https://adventofcode.com/2015/day/7"""

# Read the input file
with open("input.txt", "r") as f:
    vals = [lines[:-1] for lines in f.readlines()]

instruction = []
end = []
values = {}
ready = set()  # To hold wires with live signals
# Go through all instruction and split into an instruction set and an output set
for val in vals:
    temp = val.split(" -> ")  # Split to instruction and end
    if temp[0].isdigit():  # For instructions which are input wires
        values[temp[1]] = int(temp[0])
        ready.add(temp[1])
    else:
        instruction.append(temp[0])
        end.append(temp[1])


def readInstructions(instruction, values, end, ready) -> dict:
    '''
    Runs through the instructions and performs the bitwise operators
    :param instructions: A list of strings that denote an instruction that will take place
    :param values: An input list of the current values
    :param end: An input list of the output wires that correspon to the instruction
    :param ready: An input set that contains all wires that have an active output
    :return: A dictionary of wires and their output values
    '''
    # Whilst there are still instructions to run through
    i = 0
    while instruction:
        temp = instruction[i].split()  # Find the values of the instructions
        if "NOT" in temp:  # If 'NOT' Instruction
            if temp[1] in ready:
                values[end[i]] = ~values[temp[1]]
                ready.add(end[i])  # Add to ready to say that the output is live
                instruction.pop(i)  # pop instruction from queue
                end.pop(i)  # Pop output wire from queue, each wire can only have one output
                i = -1
        elif "OR" in temp:  # For 'OR' instructions
            if temp[0] in ready and temp[2] in ready:
                values[end[i]] = values[temp[0]] | values[temp[2]]
                ready.add(end[i])
                instruction.pop(i)
                end.pop(i)
                i = -1
        elif "RSHIFT" in temp:  # For 'RSHIFT' instructions
            if temp[0] in ready:
                values[end[i]] = values[temp[0]] >> int(temp[2])
                ready.add(end[i])
                instruction.pop(i)
                end.pop(i)
                i = -1
        elif "LSHIFT" in temp: # For 'LSHIFT' instructions
            if temp[0] in ready:
                values[end[i]] = values[temp[0]] << int(temp[2])
                ready.add(end[i])
                instruction.pop(i)
                end.pop(i)
                i = -1
        elif "AND" in temp:  # For 'AND' instructions
            if temp[0] in ready and temp[2] in ready:  # Case for both are wire inputs
                values[end[i]] = values[temp[0]] & values[temp[2]]
                ready.add(end[i])
                instruction.pop(i)
                end.pop(i)
                i = -1
            elif temp[0] in ready and temp[2].isdigit():  # Case for left wire input and number input
                values[end[i]] = values[temp[0]] & int(temp[2])
                ready.add(end[i])
                instruction.pop(i)
                end.pop(i)
                i = -1
            elif temp[0].isdigit() and temp[2] in ready:  # Case for right wire input and number input
                values[end[i]] = int(temp[0]) & values[temp[2]]
                ready.add(end[i])
                instruction.pop(i)
                end.pop(i)
                i = -1
        else:  # Case where wire is a straight input
            if temp[0] in ready:
                values[end[i]] = values[temp[0]]
                ready.add(end[i])
                instruction.pop(i)
                end.pop(i)
                i = -1
        i += 1
    return values


ansA = readInstructions(instruction, values, end, ready)['a'] # Find the output of wire 'a'
print("part1: ", ansA)

# reset the instructions
instruction = []
end = []
values = {}
ready = set()
for val in vals:
    temp = val.split(" -> ")
    if temp[0].isdigit():
        if temp[1] == 'b':  # Set the value of the 'b' input wire to the output value of 'a' from previous
            values[temp[1]] = ansA
        else:
            values[temp[1]] = int(temp[0])
        ready.add(temp[1])
    else:
        instruction.append(temp[0])
        end.append(temp[1])
i = 0

ansAPart2 = readInstructions(instruction, values, end, ready)['a']  # Find the output of wire 'a'
print("part2: ", ansAPart2)

