def count_substring(string, substring):
    # Initialize a counter to keep track of the number of occurrences
    occurance = 0

    # Loop through each character in the string
    for char in range(len(string)):
        # Check if the current character matches the first character of the substring
        if string[char] == substring[0]:
            # Check if the substring matches the slice of the string
            if string[char:char + len(substring)] == substring:
                # Increment the counter if a match is found
                occurance += 1

    # Return the total number of occurrences
    return occurance

# Read the main string from user input and remove any leading/trailing whitespace
string = input().strip()
# Read the substring from user input and remove any leading/trailing whitespace
substring = input().strip()

# Call the function
count = count_substring(string, substring)
# Print the result
print(count)