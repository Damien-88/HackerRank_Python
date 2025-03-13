# Define function that changes whitespace to - in a string
def split_and_join(line):
    split_line = line.split(" ") # Split the line by whitespace
    return "-".join(split_line) # Join the split line with -

line = input() # Get input from user
result = split_and_join(line) # Call function
print(result) # Print result