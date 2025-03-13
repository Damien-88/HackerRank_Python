# Read an integer input for the number of operations
N = int(input())

# Initialize an empty list to perform operations on
new_list = []

# Initialize variables to store numbers and positions
num = 0
pos = 0

# Loop through the range of N to perform N operations
for i in range(N):
    # Split the input into a list of strings
    split_list = input().split()
    
    # The first element is the action to be performed
    action = str(split_list[0])
    
    # If there is a second element, convert it to an integer and store in num
    if len(split_list) >= 2:
        num = int(split_list[1])
    
    # If there is a third element, convert it to an integer and store in pos
    if len(split_list) >= 3:
        pos = int(split_list[2])

    # Perform the action based on the value of 'action'
    match action:
        # Insert 'pos' at index 'num' in the list
        case "insert":
            new_list.insert(num, pos)
        # Print the current state of the list
        case "print":
            print(new_list)
        # Remove the first occurrence of 'num' from the list
        case "remove":
            new_list.remove(num)
        # Append 'num' to the end of the list
        case "append":
            new_list.append(num)
        # Sort the list in ascending order
        case "sort":
            new_list.sort()
        # Remove and return the last element of the list
        case "pop":
            new_list.pop()
        # Reverse the elements of the list
        case "reverse":
            new_list.reverse()