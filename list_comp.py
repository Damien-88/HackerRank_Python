# Assign values to variables x, y, and z
x, y, z = 1, 1, 1

# Assign value to variable n which will be used to filter permutations
n = 2

# List comprehension to generate all permutations of i, j, k in the range of 0 to x, y, z respectively
# Only include permutations where the sum of i, j, k is not equal to n
all_perms = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n]

# Print the list of all valid permutations
print(all_perms)