n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
    
grade = 0
    
for i in student_marks[query_name]:
    grade += i
        
average = grade / len(student_marks[query_name])
    
for_grade = "%.2f" % average
print(for_grade)