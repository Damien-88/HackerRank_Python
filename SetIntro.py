# Function to calculate average of unique elements in an array
def average(array):

    # Convert input array to a set to remove duplicate elements
    unique = set(array)
    # Initialize a variable to store sum of unique elements
    total = 0

    # Iterate through the unique elements. Add it to total
    for i in unique:
        total += i

    # Return average of unique elements
    return total / len(unique)

# Test the function with a sample array and print the result
print(average([161, 182, 161, 154, 176, 170, 167, 171, 170, 174]))