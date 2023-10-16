courses = input().split(', ')
command = input()
while command != 'course start':
    command = command.split(":")
    if 'Add' in command:
        if command[1] not in courses:
            courses.append(command[1])
    elif 'Insert' in command:
        if command[1] not in courses:
            index = int(command[2])
            courses.insert(index, command[1])
    elif 'Remove' in command:
        if command[1] in courses:
            courses.remove(command[1])
    elif 'Swap' in command:
        if command[1] and command[2] in courses:
            index1 = courses.index(command[1])
            index2 = courses.index(command[2])
            courses[index1], courses[index2] = courses[index2], courses[index1]
            ex = command[1] + '-Exercise'
            if ex in courses:
                courses.remove(ex)
                courses.insert(index2+1, ex)
            ex = command[2] + '-Exercise'
            if ex in courses:
                courses.remove(ex)
                courses.insert(index1+1, ex)
    elif 'Exercise' in command:
        ex = command[1]+'-Exercise'
        if ex not in courses:
            if command[1] in courses:
                index = courses.index(command[1])
                courses.insert(index+1, ex)
            else:
                courses.append(command[1])
                courses.append(ex)

    command = input()


for i in range (0, len(courses)):
    print(f'{i+1}.{courses[i]}')