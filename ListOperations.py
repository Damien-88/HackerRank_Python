# Function to capitalize the first letter of each word in a string
def capitalize_name(s):

    # Initialize an empty string to store the result
    result = ''
    # Flag to indicate whether the next character should be capitalized
    capitalize_next = True

    # Iterate through each character in the input string
    for char in s:
        # If the character is a space, add it and set the flag to capitalize the next character
        if char == ' ':
            result += char
            capitalize_next = True 
        # If the flag is set and the character is alphabetic, capitalize it and reset the flag
        elif capitalize_next and char.isalpha():
            result += char.upper()
            capitalize_next = False
        # Otherwise, add the character as is and reset the flag
        else:
            result += char
            capitalize_next = False

    # Return the resulting string with capitalized words
    return result

# Take input from the user
s = input()
# Print the result of the capitalize_name function
print(capitalize_name(s))