# Initialize an empty list to store the nested lists of names and scores
nest = []
# Initialize an empty list to store unique grades
grades = []

# Loop to read input for the number of students
for _ in range(int(input())):
    # Read the student's name
    name = input()
    # Read the student's score and convert it to a float
    score = float(input())
    # Append the name and score as a list to the nest list
    nest.append([name, score])
    # If the score is not already in the grades list, add it
    if score not in grades:
        grades.append(score)

# Print the list of students with their scores
print(nest)

# Find the lowest grade in the grades list
lowest = min(grades)
# Remove the lowest grade from the grades list
grades.remove(lowest)
# Find the second lowest grade in the grades list
second_lowest = min(grades)
# Initialize an empty list to store names of students with the second lowest grade
names = []

# Loop through each student in the nest list
for student in nest:
    # If the student's score is equal to the second lowest grade, add their name to the names list
    if student[1] == second_lowest:
        names.append(student[0])

# Sort the names list alphabetically
names.sort()

# Print each name in the sorted names list
for name in names:
    print(name)

"""
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39
"""