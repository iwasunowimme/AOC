'''https://adventofcode.com/2015/day/21'''

from math import ceil
# Add the player starting stats
player = {'HP': 100, 'damage': 0, 'armor': 0}

# Import file
with open("input.txt", "r") as f:
    values = [lines[:-1] for lines in f.readlines()]

# Set the dictionary for the boss' stats
boss = {'HP': int(values[0].split(": ")[1]), 'damage': int(values[1].split(": ")[1]),
        'armor': int(values[2].split(": ")[1])}

# Manually add the shop
# Added additional armor and ring to signify no selection
weapons = {'Dagger': [8, 4, 0], 'Shortsword': [10, 5, 0], 'Warhammer': [25, 6, 0], 'Longsword': [40, 7, 0],
           'Greataxe': [74, 8, 0]}
armor = {'Leather': [13, 0, 1], 'Chainmail': [31, 0, 2], 'Splintmail': [53, 0, 3], 'Bandedmail': [75, 0, 4],
         'Platemail': [102, 0, 5], 'Nothing': [0, 0, 0]}
rings = {'D1': [25, 1, 0], 'D2': [50, 2, 0], 'D3': [100, 3, 0], 'DE1': [20, 0, 1], 'DE2': [40, 0, 2],
         'DE3': [80, 0, 3], 'Nothing1': [0, 0, 0], 'Nothing2': [0, 0, 0]}

# Create arrays to store the cost of wins and loses
wins = []
loss = []
# Go through all weapons
for wep_key in weapons:
    # all armor
    for arm_key in armor:
        # All accessories
        for acc_key in rings:
            # All accessories again
            for acc2_key in rings:
                if acc2_key != acc_key:  # Only continue if both accessories are different
                    # Play the game by comparing how many turns it takes to defeat the other
                    # The first play to have their HP reduced to 0 or bellow loses
                    if ceil(player['HP']/(max(boss['damage']
                                              - (armor[arm_key][2]+rings[acc_key][2]+rings[acc2_key][2]), 1)))\
                          >= ceil(boss['HP']/max(weapons[wep_key][1]+rings[acc_key][1]+rings[acc2_key][1]
                                                 - boss['armor'], 1)):
                        # Append cost to wins
                        wins.append(weapons[wep_key][0]+rings[acc_key][0]+rings[acc2_key][0]+armor[arm_key][0])
                    else:
                        # Append cost to losses
                        loss.append(weapons[wep_key][0]+rings[acc_key][0]+rings[acc2_key][0]+armor[arm_key][0])

print("Part1: ", min(wins))
print("Part2: ", max(loss))

