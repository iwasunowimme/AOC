'''https://adventofcode.com/2015/day/11'''


vals = "hxbxwxba"  # Import from website
A = ord('a')  # Set the A value as the ord for the letter a, this is the 0 value
Z = ord('z')  # Set the Z value as the ord for the letter z, this is the max value
password = [ord(m) for m in vals]  # convert password to list of numbers


def checkPassword(password) -> bool:
    '''
    Checks the password against given criteria
    Passwords must include one increasing straight of at least three letters
    Passwords may not contain the letters i, o, or l
    Passwords must contain at least two different, non-overlapping pairs of letters.
    :param password: A list of ord numbers that correspond to the text of the password
    :return: True if the password is valid, false otherwise
    '''
    # Sets default straight to false
    straight = False
    # Creates a list of the bad letters in ord form
    badLetters = [ord('i'), ord('o'), ord('l')]

    # Finds if the password contains any bad letters, returns false if it is
    # This is done first as it is the fastest
    if any(x in badLetters for x in password):
        return False

    # Iterates through the password to see if there are any triples
    for i in range(len(password) - 2):
        if password[i + 1] - password[i] == 1 and password[i + 2] - password[i] == 2:
            straight = True
            break

    # Sets a double counter to count unique sets
    double = 0
    # Contains a set of letters that are doubled up, only unique letters are wanted
    completed = set()
    for i in range(len(password) - 1):
        if password[i] == password[i + 1]:
            if password[i] not in completed:  # This will work for 'aaa' only counting once as 'a' is in completed set
                double += 1
                completed.add(password[i])
    # sets the doubles boolean to see if there are more than 1
    doubles = double > 1
    
    return straight and doubles


def passwordIncrement(password) -> list:
    '''
    Incrmements the password by 1, if letter is 'z' wraps to 'a' and increments next letter
    goes from last letter to first
    :param password: A list of ord numbers that correspond to the text of the password
    :return: The next password in ord form incremented by 1
    '''
    password[-1] += 1
    if password[-1] > Z:
        password[-1] = A
        carry = 1
        for p in range(len(password) - 2, -1, -1):
            password[p] += carry
            if password[p] > Z:
                password[p] = A
                carry = 1
            else:
                carry = 0
    return password


def findNextPassword(password) -> list:
    '''
    Finds the next valid password as based by the checkPassword function
    :param password: A list of ord numbers that correspond to the text of the password
    :return: The next valid password in ord form
    '''

    # Used the passwordIncrement function to increase password to next one to be checked
    # Increments once before entering loop in case the current password is a valid one
    password = passwordIncrement(password)
    while not checkPassword(password):
        password = passwordIncrement(password)
    return password


def printPassword(password):
    '''
    Prints the password in plain text
    :param password: A list of ord numbers that correspond to the text of the password
    '''
    print(''.join([chr(m) for m in password]))


# Do part 1 using the given input
part1 = findNextPassword(password)
print("Part1:", end=" ")
printPassword(part1)

# Do part 2 using the result of part 1
part2 = findNextPassword(part1)
print("Part2:", end=" ")
printPassword(part2)
