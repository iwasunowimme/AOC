'''https://adventofcode.com/2015/day/4'''

import hashlib
i=0
while i < 10000000: # force a high loop vale
    temp = hashlib.md5(("yzbqklnj"+str(i)).encode('utf-8')).hexdigest()
    if temp[:5] == "00000": # five leading 0's
        print(i)
        break
    i+=1

i=0
while i >-1: # force a high loop vale
    temp = hashlib.md5(("yzbqklnj"+str(i)).encode('utf-8')).hexdigest()
    if temp[:6] == "000000": #6 leading 0's
        print(i)
        break
    i+=1