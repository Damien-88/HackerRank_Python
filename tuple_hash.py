# Read an integer input from the user and assign it to the variable 'n'
n = int(input())

# Read a line of input, split it into a list of integers, and convert it to a tuple
t = tuple(map(int, input().split()))

# Print the hash value of the tuple 't'
print(hash(t))