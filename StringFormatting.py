# Function to print numbers in decimal, octal, hexadecimal, and binary formats
def print_formatted(number):
    # Calculate the width needed for formatting based on the binary representation of the largest number
    width = len(bin(number)) - 2

    # Loop through numbers from 1 to the given number (inclusive)
    for i in range(1, number + 1):
        # Convert to octal
        octal_num = oct(i)
        # Convert to hexadecimal
        hex_num = hex(i)
        # Convert to binary
        bin_num = bin(i)
        # Convert to uppercase
        hex_num = hex_num.upper()

        # Print the number in decimal, octal, hexadecimal, and binary formats
        # Right-aligned with the calculated width
        print(f"{i:>{width}} {octal_num[2:]:>{width}} {hex_num[2:]:>{width}} {bin_num[2:]:>{width}}")

# Read an integer input from the user
n = int(input())
# Call the function to print the formatted output
print_formatted(n)