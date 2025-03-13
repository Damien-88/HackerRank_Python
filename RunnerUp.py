# Read an integer input from the user
n = int(input())

# Read a line of input, split it into integers, and map them to a list
arr = map(int, input().split())

# Sort the list of integers in ascending order
list1 = sorted(arr)

# Reverse the sorted list to get it in descending order
list1.reverse()

# Iterate through the list
for i in range(0, len(list1)):
    # If the current element is the same as the first element (the largest), skip it
    if list1[i] == list1[0]:
        continue
    else:
        # Print the first element that is not the largest (the runner-up)
        print(list1[i])
        break