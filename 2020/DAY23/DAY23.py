# Create a doubly linked list node class
class MyLLNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# Input values
values = 198753462  # Actual values
# values = 389125467  # Example values

# Create the circle from the values as each int
circle = [int(x) for x in str(values)]
# Find the max value of the circle
m = max(circle)

# Create a dictionary to be used with the node object
nodes = {}
last = None
# For each value in circle add to list
for c in circle:
    # create node
    new_node = MyLLNode(c)
    # Append node to list
    nodes[c] = new_node
    # If not the first one set up left and right
    if last is not None:
        last.right = new_node
        new_node.left = last
    last = new_node

# Create a circle by connecting the first to the last
first = nodes[circle[0]]
last.right = first
first.left = last

# Start looping from the first node
current = first
for i in range(100):
    # Find the destination value
    destination_value = current.val - 1

    # Create the three neighbours
    three_1 = current.right
    three_2 = three_1.right
    three_3 = three_2.right

    # Separate the three from the rest of the list by attaching the current to the one after the third
    current.right = three_3.right
    three_3.right.left = current

    # Find the destination value if it is in the list of the three
    while destination_value in (three_1.val, three_2.val, three_3.val, 0):
        destination_value -= 1
        if destination_value <= 0:  # If the value goes down to 0, wraps to the highest number
            destination_value = m

    # Find the node that we want to go to
    destination_node = nodes[destination_value]

    # Append the three into the middle of the destination and destination right
    three_3.right = destination_node.right
    three_3.right.left = three_3
    destination_node.right = three_1
    three_1.left = destination_node

    # Move to the next node in the circle
    current = current.right

# start at the node next to the one of value 1
start = nodes[1].right
print("Part1: ", end='')
# For each node up until the node of value 1 print the value with no space
while start.val != 1:
    print(start.val, end='')
    start = start.right
print()

# Create a new set of nodes
nodes = {}
last = None
# Append the circle the same as before
for c in circle:
    new_node = MyLLNode(c)
    nodes[c] = new_node
    if last is not None:
        last.right = new_node
        new_node.left = last
    last = new_node

# Append all numbers from the max to 1 million
for number in range(m + 1, 1_000_000 + 1):
    # Create new node of the number
    new_node = MyLLNode(number)
    # Append to nodes
    nodes[number] = new_node
    # Set up double links
    last.right = new_node
    new_node.left = last
    last = new_node

# Create the circle of the linked list
first = nodes[circle[0]]
last.right = first
first.left = last
current = first

# Takes about 30 seconds to complete all 10,000,000
for z in range(10_000_000):
    # Find the destination value
    destination_value = current.val - 1

    # Create the three neighbours
    three_1 = current.right
    three_2 = three_1.right
    three_3 = three_2.right

    # Separate the three from the rest of the list by attaching the current to the one after the third
    current.right = three_3.right
    three_3.right.left = current

    # Find the destination value if it is in the list of the three
    while destination_value in (three_1.val, three_2.val, three_3.val, 0):
        destination_value -= 1
        if destination_value <= 0:
            destination_value = 1_000_000  # 1 million is the max based off range

    # Find the node that we want to go to
    destination_node = nodes[destination_value]

    # Append the three into the middle of the destination and destination right
    three_3.right = destination_node.right
    three_3.right.left = three_3
    destination_node.right = three_1
    three_1.left = destination_node

    # Move to the next node in the circle
    current = current.right

# Print the product of the two numbers to the right of node 1
print("part2:", nodes[1].right.right.val * nodes[1].right.val)




