'''https://adventofcode.com/2015/day/4'''

import hashlib
i = 0
million = 1000000
tenmillion = 10000000
secret = "yzbqklnj"
while i < million:  # force a high loop vale
    # Implements the md5 hash from hashlib to find the first i that will give 5 leading zeros
    if hashlib.md5((secret+str(i)).encode('utf-8')).hexdigest()[:5] == '00000':  # 5 leading 0's
        print(i)
        break
    i += 1

i = 0
while i < tenmillion:  # force a high loop vale
    # Implements the md5 hash from hashlib to find the first i that will give 6 leading zeros
    if hashlib.md5((secret+str(i)).encode('utf-8')).hexdigest()[:6] == '000000':  # 6 leading 0's
        print(i)
        break
    i += 1
