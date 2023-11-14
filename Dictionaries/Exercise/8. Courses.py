string = input()
courses = {}
while string != 'end':
    string = string.split(" : ")
    course = string[0]
    name = string[1]
    if course not in courses:
        courses[course] = []
    courses[course].append(name)
    string = input()

for i in courses:
    print(f'{i}: {len(courses[i])}')
    for j in range(len(courses[i])):
        print(f'-- {courses[i][j]}')