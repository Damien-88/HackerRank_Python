# Function to capitalize the first letter of each word in a string
def capitalize_words(s):
    # Split the input string into a list of words
    words = s.split(" ")
    # Initialize an empty list to store the modified words
    new_words = []
 
    # Iterate through each word in the list
    for word in words:
        if word == "":
            new_words.append(" ")
        # If the first character of the word is an alphabetic character
        elif word[0].isalpha():
            # Capitalize the first letter of the word and add it to the new list
            new_words.append(word.title())
        else:
            # If the first character is not alphabetic, add the word as is
            new_words.append(word)

    # Join the modified words back into a single string with spaces
    answer = " ".join(new_words)
    # Return the final capitalized string
    return answer

# Take user input
name = input()
# Print the result of the capitalize_words function
print(capitalize_words(name))