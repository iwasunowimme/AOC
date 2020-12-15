'''https://adventofcode.com/2015/day/22'''

from copy import deepcopy

# Import boss data from file
with open("input.txt", "r") as f:
    values = [lines[:-1] for lines in f.readlines()]

# Set boss stats from input
boss = {"HP": int(values[0].split()[-1]), "damage": int(values[1].split()[-1])}

# Set play stats as defaults
player = {'mana': 500, 'armor': 0, 'HP': 50}

spells = {'Missile':53, 'Drain':73, 'Shield':113, 'Poison':173, 'Recharge':229}


# Simulate the battle
def battle(player_stats, boss_stats, skills, difficulty):
    '''
    Simulates a boss battle using the skills in order that it was given
    :param player_stats: The player's starting stats
    :param boss_stats: The boss' starting stats
    :param skills: The list of skills to be used in order
    :param difficulty: "hard" or "easy" mode
    :return: <0 for loss, mana spent for win
    '''

    # Reset timers and mana spent
    poison_timer = 0
    shield_timer = 0
    recharge_timer = 0
    mana = 0

    # Iterate through the skills list
    for skill in skills:
        # If difficulty is set to hard, reduce HP by 1 per player turn
        if difficulty == 'hard':
            player_stats['HP'] -= 1

        # Check timers and apply effects
        player_stats['mana'] += recharge(recharge_timer)
        player_stats['armor'] = shield(shield_timer)
        boss_stats['HP'] += poison(poison_timer)

        # Spend mana to cast
        player_stats['mana'] -= spells[skill]
        mana += spells[skill]

        # Player loses, player no mana
        if player_stats['mana'] < 0:
            return -1

        # Player loses, player no HP
        if player_stats['HP'] <= 0:
            return -1

        # Reduce timers
        poison_timer -= 1
        shield_timer -= 1
        recharge_timer -= 1

        # Cast spell
        if skill == 'Drain':
            player_stats['HP'] += 2
            boss_stats['HP'] -= 2
        elif skill == 'Missile':
            boss_stats['HP'] -= 4
        elif skill == 'Shield':
            shield_timer = 6
        elif skill == 'Poison':
            poison_timer = 6
        elif skill == 'Recharge':
            recharge_timer = 5

        # Check timers and apply effects
        player_stats['mana'] += recharge(recharge_timer)
        player_stats['armor'] = shield(shield_timer)
        boss_stats['HP'] += poison(poison_timer)

        # Player wins, boss no HP
        if boss_stats['HP'] <= 0:
            return mana

        # Player hit by boss
        player_stats['HP'] -= max(1, boss_stats['damage'] - player_stats['armor'])

        # Reduce timers
        poison_timer -= 1
        shield_timer -= 1
        recharge_timer -= 1

        # Player loses, player no HP
        if player_stats['HP'] <= 0:
            return -1

    # No more moves, match undecided
    return -2


def shield(shield_timer):
    '''
    Returns the value of the shield at a specific time
    :param shield_timer: # The current shield time
    :return: The new shield value
    '''
    if shield_timer > 0:
        return 7
    else:
        return 0


def poison(poison_timer):
    '''
    Returns the damage dealt by the poison at a specific counter
    :param poison_timer: The counter for the poison
    :return: Th damage done by the poison
    '''
    if poison_timer > 0:
        return -3
    else:
        return 0


def recharge(recharge_time):
    '''
    The value of additional mana to gain at a certain recharge time
    :param recharge_time: The recharge timer
    :return: the value of mana to gain
    '''
    if recharge_time > 0:
        return 101
    else:
        return 0


spell = ['Recharge', 'Shield', 'Drain', 'Poison', 'Missile']
attackset = [['Recharge'], ['Shield'], ['Drain'], ['Poison'], ['Missile']]
mana_saver = []
i = 0
# Attack for a large amount of simulations
# Memoization implementation would increase speed
while i < 200000:
    moveset = attackset.pop(0)
    # Battle
    result = battle(deepcopy(player), deepcopy(boss), moveset, 'easy')
    # If result inconclusive
    if result == -2:
        # Add the same moveset plus 1 spell to the rotation
        for sp in spell:
            temp = deepcopy(moveset)
            temp.append(sp)
            attackset.append(temp)
    # If win add the mana spent to list
    elif result >= 0:
        mana_saver.append(result)
    # If loss, continue to next
    i += 1

print("part1: ", min(mana_saver))

# Attack for a large amount of simulations
# Memoization implementation would increase speed
attackset = [['Recharge'], ['Shield'], ['Drain'], ['Poison'], ['Missile']]
mana_saver = []
i = 0
while i < 200000:
    moveset = attackset.pop(0)
    # Battle
    result = battle(deepcopy(player), deepcopy(boss), moveset, 'hard')
    # If result inconclusive
    if result == -2:
        # Add the same moveset plus 1 spell to the rotation
        for sp in spell:
            temp = deepcopy(moveset)
            temp.append(sp)
            attackset.append(temp)
    # If win add the mana spent to list
    elif result >= 0:
        mana_saver.append(result)
    # If loss, continue to next
    i += 1
print("part2: ", min(mana_saver))
