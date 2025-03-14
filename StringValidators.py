def string_contains(string):
    # Initialize a list to keep track of the presence of different types of characters
    # check[0] -> alphanumeric, check[1] -> alphabetic, check[2] -> digits, 
    # check[3] -> lowercase, check[4] -> uppercase
    check = [0, 0, 0, 0, 0]
    count = 0

    # Iterate through each character in the string
    for i in string:
        # If all types of characters are found, break the loop
        if count == 5:
            break
        # Check if the character is alphanumeric
        if check[0] == 0 and i.isalnum():
            check[0] = 1
            count += 1
        # Check if the character is alphabetic
        if check[1] == 0 and i.isalpha(): 
            check[1] = 1
            count += 1
        # Check if the character is a digit
        if check[2] == 0 and i.isdigit():
            check[2] = 1
            count += 1
        # Check if the character is lowercase
        if check[3] == 0 and i.islower():
            check[3] = 1
            count += 1
        # Check if the character is uppercase
        if check[4] == 0 and i.isupper():  
            check[4] = 1
            count += 1            
    
    # Print True or False for each type of character found
    for n in check:
        if n == 1:
            print(True)
        else:
            print(False)

# Take input from the user
s = input()
# Call the function with the input string
string_contains(s)