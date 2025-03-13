nest = []
grades = []

for _ in range(int(input())):
    name = input()
    score = float(input())
    nest.append([name, score])
    if score not in grades:
        grades.append(score)

print(nest)

lowest = min(grades)
grades.remove(lowest)
second_lowest = min(grades)
names = []

for student in nest:
    if student[1] == second_lowest:
        names.append(student[0])

names.sort()

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