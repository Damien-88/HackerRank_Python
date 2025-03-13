# Define a function named is_leap that takes a parameter year
def is_leap(year):
    # Initialize a variable leap to False
    leap = False
    
    # Check if the year is divisible by 4
    if year % 4 == 0:
        # If the year is divisible by 4, check if it is not divisible by 100
        if year % 100 != 0:
            # If the year is not divisible by 100, set leap to True
            leap = True
        # Additionally, check if the year is divisible by 400
        if year % 400 == 0:
            # If the year is divisible by 400, set leap to True
            leap = True
    
    # Return the value of leap
    return leap

# Read an integer input from the user and store it in the variable year
year = int(input())