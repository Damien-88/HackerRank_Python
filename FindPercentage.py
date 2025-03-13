# Read an integer input for the number of students
n = int(input())

# Initialize an empty dictionary to store student names and their scores
student_marks = {}

# Loop over the range of number of students
for _ in range(n):
    # Read the input, split by spaces, and unpack into name and scores
    name, *line = input().split()
    # Convert the scores from strings to floats and store in a list
    scores = list(map(float, line))
    # Add the name and scores to the dictionary
    student_marks[name] = scores

# Read the name of the student to query
query_name = input()

# Initialize a variable to store the total grade
grade = 0

# Loop over the scores of the queried student
for i in student_marks[query_name]:
    # Sum up the scores
    grade += i

# Calculate the average score
average = grade / len(student_marks[query_name])

# Format the average to 2 decimal places
for_grade = "%.2f" % average

# Print the formatted average
print(for_grade)