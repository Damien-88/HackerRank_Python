# Function to split a string into substrings of length k, Return substrings sans duplicates
def merge_the_tools(string, k):

    n = len(string) # Get the length of the input string
    new_strings = [] # Initialize a list to store the substrings
    # Initialize start and end indices for slicing the string
    start = 0
    end = k
    
    # Loop to divide the string into substrings of length k
    while start < n:
        # If the remaining string is longer than k, slice it and add to the list
        if len(string) > end:
            new_strings.append(string[start:end])
            # Move the start and end indices forward by k
            start += k
            end += k
        else:
            # If the remaining string is shorter than k, add the rest of the string and end the loop
            new_strings.append(string[start::])
            break

    # Print the list of substrings (for debugging purposes)
    print(new_strings)

    # Loop through each substring in the list
    for i in new_strings:
        # Initialize a list to store unique characters
        unique = []
        # Initialize an index counter (not used in this implementation)
        index = 0

        # Loop through each character in the substring
        for n in i:
            # If the character is not already in the unique list, add it
            if n not in unique:
                unique.append(n)
                index += 1

        # Print the substring with unique characters
        print(''.join(unique))

# Example usage of the function
merge_the_tools('AABCAAADA', 3)