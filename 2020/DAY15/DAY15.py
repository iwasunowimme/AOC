'''https://adventofcode.com/2020/day/15'''

# Part1 is till 2020, part2 is till 3x10**7
for part in [2020, 30000000]:
    # Import values
    values = [2, 15, 0, 9, 1, 20]  # Since the array is used need to be reinstated

    # Generate a dictionary of all values with turn spoken as value
    # Add 1 to increase turn counter
    nums = {num: i+1 for i, num in enumerate(values)}

    # Last number is the last number on the list, last added+
    last = values[-1]
    # iterate till the part end number
    for j in range(len(nums), part):

        # The current spoken number is this current turn less the last turn the last word was spoken,
        # If the last word had only been spoken then, the value is 0
        speak = j - nums[last] if last in nums else 0

        # Set the last spoken number as the jth position
        # This is done after the assigning of current spoken number due to the first spoken rule
        nums[last] = j
        # Last number is the last number spoken
        last = speak

    # Print the last spoken number
    print(last)




