'''https://adventofcode.com/2015/day/22'''

from copy import deepcopy

with open("input.txt", "r") as f:
    values = [lines[:-1] for lines in f.readlines()]
#values = ['Hit Points: 14', 'Damage: 8']
boss = {}
boss["HP"] = int(values[0].split()[-1])
boss["damage"] = int(values[1].split()[-1])

player = {}
player['mana'] = 500
player['armor'] = 0
player['HP'] = 50

spells = {'Missile':53, 'Drain':73, 'Shield':113, 'Poison':173, 'Recharge':229}

def battle(player, boss, skills):
    poison_timer = 0
    shield_timer = 0
    recharge_timer = 0
    mana = 0
    for skill in skills:
        # print("start player", boss, player)
        player['mana'] += recharge(recharge_timer)
        player['armor'] = shield(shield_timer)
        boss['HP'] += poison(poison_timer)
        player['mana'] -= spells[skill]
        player['HP'] -= 1

        mana += spells[skill]
        if player['mana'] < 0:
            #print("mana exhausted")
            return -1
        if player['HP'] <= 0:
            return -1
        poison_timer -= 1
        shield_timer -= 1
        recharge_timer -= 1
        if skill == 'Drain':
            player['HP'] += 2
            boss['HP'] -= 2
        elif skill == 'Missile':
            boss['HP'] -= 4
        elif skill == 'Shield':
            shield_timer = 6
        elif skill == 'Poison':
            poison_timer = 6
        elif skill == 'Recharge':
            recharge_timer = 5
        # print("end player", boss, player)
        player['mana'] += recharge(recharge_timer)
        player['armor'] = shield(shield_timer)
        boss['HP'] += poison(poison_timer)
        # print("start boss", boss, player)
        if boss['HP'] <= 0:
            #print('PLAYER 1 WINS')
            return mana
        player['HP'] -= max(1, boss['damage'] - player['armor'])
        poison_timer -= 1
        shield_timer -= 1
        recharge_timer -= 1
        # print("end boss", boss, player)
        if player['HP'] <= 0:
            #print("BOSS WINS")
            return -1
    #print("no contest")
    return -2



def shield(shield_timer):
    if shield_timer > 0:
        return 7
    else:
        return 0

def poison(poison_timer):
    if poison_timer > 0:
        return -3
    else:
        return 0

def recharge(recharge_time):
    if recharge_time > 0:
        return 101
    else:
        return 0

spell = ['Recharge', 'Shield', 'Drain', 'Poison', 'Missile']
attackset = [['Recharge'], ['Shield'], ['Drain'], ['Poison'], ['Missile']]
mana_saver = []
i = 0
while i < 200000:
    moveset = attackset.pop(0)
    #print(attackset)
    result = battle(deepcopy(player), deepcopy(boss), moveset)
    if result == -2:
        for sp in spell:
            temp = deepcopy(moveset)
            temp.append(sp)
            #print(temp)
            attackset.append(temp)
    elif result >= 0:
        print(result, moveset)
        mana_saver.append(result)
    i += 1

print("part1: ",min(mana_saver) , mana_saver)
