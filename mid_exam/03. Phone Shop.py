phones = input().split(', ')
com = input()
while com != 'End':
    command = com.split(' - ')
    if "Add" in command:
        if command[1] not in phones:
            phones.append(command[1])
    elif 'Remove' in command:
        if command[1] in phones:
            phones.remove(command[1])
    elif 'Bonus phone' in command:
        bonus = command[1].split(':')
        oldPhone = bonus[0]
        newPhone = bonus[1]
        if oldPhone in phones:
            index = phones.index(oldPhone)
            phones.insert(index+1, newPhone)
    elif 'Last' in command:
        if command[1] in phones:
            phones.remove(command[1])
            phones.append(command[1])
    com = input()
print(*phones, sep=', ')
