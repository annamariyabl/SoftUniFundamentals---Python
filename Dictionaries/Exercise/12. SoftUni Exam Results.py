students = {}
submissions = {}
command = input()
while command != 'exam finished':
    if 'banned' not in command:
        username, language, points = command.split('-')
        if username not in students:
            students[username] = points
        else:
            if int(students[username]) < int(points):
                students[username] = points
        if language not in submissions:
            submissions[language] = 1
        else:
            submissions[language] += 1
    else:
        username = command.split('-')
        username = username[0]
        students.pop(username)
    command = input()


print('Results:')
for i in students:
    print(f'{i} | {students[i]}')
print('Submissions:')
for i in submissions:
    print(f'{i} - {submissions[i]}')



