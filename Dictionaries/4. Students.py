student = input()
students = []

while ":" in student:
    name, ID, course = student.split(':')
    ID = int(ID)
    if " " in course:
        course = course.replace(" ", "_")
    students.append({'name' : name, 'ID' : ID, 'course' : course})
    student = input()

for i in students:
    if student == i['course']:
        print(f"{i['name']} - {i['ID']}")





