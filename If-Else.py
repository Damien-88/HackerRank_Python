# Read an integer input from the user and remove any leading/trailing whitespace
n = int(input().strip())

# Check if the number is odd
if n % 2 != 0:
    # Print "Weird" if the number is odd
    print("Weird")
# Check if the number is even
elif n % 2 == 0:
    # Check if the number is in the range 2 to 5 (inclusive)
    if n >= 2 and n <= 5:
        # Print "Not Weird" if the number is in the range 2 to 5
        print("Not Weird")
    # Check if the number is in the range 6 to 20 (inclusive)
    elif n >= 6 and n <= 20:
        # Print "Weird" if the number is in the range 6 to 20
        print("Weird")
    # Check if the number is greater than 20
    elif n > 20:
        # Print "Not Weird" if the number is greater than 20
        print("Not Weird")