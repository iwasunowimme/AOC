'''https://adventofcode.com/2015/day/10'''

vals = "1321131112"

# Iterate till desired range
def findLength(vals, n) -> int:
    '''
    Takes the input and applies the look and see
    :param vals:
    :param n:
    :return:
    '''
    res = ""
    for _ in range(n):

        # Set nill data for the string vale and the count of letters
        res = ""
        count = 0
        letter = ""
        for j in range(len(vals)):
            if vals[j] != letter:  # If the current number does not match the previous it ends the chain
                if count != 0:  # This is used to avoid the null condition of the first letter
                    res += str(count) + letter  # Add the count and the digit to the end of the string
                letter = vals[j]  # new letter to count is current
                count = 1  # count starts off at 1
            else:  # Current chain continues
                count += 1

        # Do once more for last stored values
        res += str(count) + letter
        vals = res

    return len(res)


print("part1: ", findLength(vals, 40))
print("part2: ", findLength(vals, 50))

