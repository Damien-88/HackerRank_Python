x, y, z = 1, 1, 1 # Variables used in list comprehension
n = 2 # Variable to stop loop

# List comprehension to generate all permutations of i, j, k in the range of x, y, z
all_perms = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n]

# Print the list of all permutations
print(all_perms)