import statistics

n = int(input())
students = {}
for i in range(n):
    name = input()
    grade = float(input())
    if name not in students:
        students[name] = []
    students[name].append(grade)


for i in students:
    if statistics.mean(students[i]) >= 4.50:
        print(f'{i} -> {statistics.mean(students[i]):.2f}')