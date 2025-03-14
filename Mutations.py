def mutate_string(string, position, character):
    # Convert the string to a list to allow mutation
    string_list = list(string)
    # Replace the character at the specified position
    string_list[position] = character
    # Join the list back into a string
    new_string = "".join(string_list)
    # Return the mutated string
    return new_string

# Read the original string from input
s = input()
# Read the position and character from input, split by space
i, c = input().split()
# Call the mutate_string function with the inputs
s_new = mutate_string(s, int(i), c)
# Print the mutated string
print(s_new)