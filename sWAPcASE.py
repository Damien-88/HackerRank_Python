# Define Function that swaps the case of a string
def swap_case(s):
    swapped = "" # Stores swapped characters
    
    # Iterate through each character
    for char in s:
        # Check if character is uppercase
        if char.isupper(): #
            swapped += char.lower() # Convert to lowercase
        elif char.islower(): # Character is lowercase
            swapped += char.upper() # Convert to uppercase
        else: # Character is not a letter
            swapped += char # Add character as is

    return swapped # Return swapped string

s = input() # Input string
result = swap_case(s) # Call function
print(result) # Output swapped string