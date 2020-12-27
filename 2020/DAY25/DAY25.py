# Import data from text file
with open("input.txt", "r") as f:
    values = [int(lines[:-1]) for lines in f.readlines()]

# Set the card public key and door public key as the input values
card_pub_key = values[0]
door_pub_key = values[1]
# Examples
# card_pub_key = 5764801
# door_pub_key = 17807724
# Set the loop size as 0
card_loop_size = 0
door_loop_size = 0
# subject number as required
subject_number = 7
# modulus value as required
mod_by = 20201227

# Set subject value at 1
value = 1
x = 0
# Loop whilst door loop size and card loop size are unknown
while door_loop_size == 0 or card_loop_size == 0:
    # Multiple value by subject number
    value *= subject_number
    # Value equals remainder of mod
    value = value % mod_by
    # If card loop size unknown and value is public key, set loop size
    if card_loop_size == 0:
        if value == card_pub_key:
            card_loop_size = x + 1
    # If door loop size unknown and value is public key, set loop size
    if door_loop_size == 0:
        if value == door_pub_key:
            door_loop_size = x + 1

    x += 1

# Reset value to 1
value = 1
if card_loop_size > door_loop_size:
    # Loop through door size and apply handshake with card public key
    for _ in range(door_loop_size):
        value *= card_pub_key
        value = value % mod_by
    print(value)
else:
    # Loop through card size and apply handshake with door public key
    for _ in range(card_loop_size):
        value *= door_pub_key
        value = value % mod_by
    print(value)
