import string

# Function to print the alphabet rangoli of a given size
def print_rangoli(size):
    # Get all lowercase alphabets
    alpha = string.ascii_lowercase
    # Initialize an empty list to store each line of the rangoli
    l = []

    # Loop to create each line of the rangoli
    for i in range(size):
        # Create a string with letters joined by '-' in reverse order and forward order
        s = "-".join(alpha[i:size])
        # Append the mirrored and centered string to the list
        l.append((s[::-1] + s[1:]).center(4 * size - 3, "-"))

    # Print the rangoli by combining the reversed list (excluding the first line) and the original list
    print('\n'.join(l[:0:-1] + l))

# Take input for the size of the rangoli
n = int(input())
# Call the function to print the rangoli
print_rangoli(n)