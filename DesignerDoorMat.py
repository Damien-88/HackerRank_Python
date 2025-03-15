# Function to generate and print the door mat pattern
def door_mat(rows, columns):
    # Loop to create the top half of the mat
    for i in range(rows//2):
        # Print the pattern for each row in the top half
        print((".|." * i).rjust((columns-3)//2, 
                "-") + ".|." + 
                (".|." * i).ljust((columns-3)//2, "-"))
    
    # Print the middle "WELCOME" row
    print("-" * ((columns-7)//2) + "WELCOME" + "-" * ((columns-7)//2))
    
    # Loop to create the bottom half of the mat
    for n in range(rows//2):
        # Print the pattern for each row in the bottom half
        print((".|." * (rows//2 - n - 1)).rjust((columns-3)//2, 
                "-") + ".|." + 
                (".|." * (rows//2 - n - 1)).ljust((columns-3)//2, "-"))

# Take input for the dimensions of the mat
space = input().split()
# Convert the input dimensions to integers
width = int(space[0])
height = int(space[1])
# Call the function to generate the door mat
door_mat(width, height)