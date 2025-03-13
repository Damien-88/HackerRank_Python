# Read an integer input from the user and assign it to variable 'a'
a = int(input())

# Read another integer input from the user and assign it to variable 'b'
b = int(input())

# Check if both 'a' and 'b' are within the range from 1 to 10^10
if a >= 1 and a <= 10**10 and b >= 1 and b <= 10**10:
    # Print the sum of 'a' and 'b'
    print(a + b)
    # Print the difference of 'a' and 'b'
    print(a - b)
    # Print the product of 'a' and 'b'
    print(a * b)
else:
    # Print an error message if the inputs are out of the specified range
    print("incorrect input")