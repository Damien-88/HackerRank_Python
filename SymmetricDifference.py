# Symmetric Difference
def symmetric_difference(a, b):
    # Calculate the symmetric difference between two sets
    sym_dif = a.symmetric_difference(b)
    # Sort the symmetric difference in ascending order
    sym_dif = sorted(sym_dif)

    # Print the sorted symmetric difference
    for i in sym_dif:
        print(i)

# Read the size of the first set and its elements
siza_a = int(input())
set_a = set(map(int, input().split()))

# Read the size of the second set and its elements
siza_b = int(input())
set_b = set(map(int, input().split()))

# Call the function to calculate and print the symmetric difference
symmetric_difference(set_a, set_b)