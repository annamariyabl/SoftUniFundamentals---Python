list = input().split("!")
command = input()
while command != 'Go Shopping!':
    if 'Urgent' in command:
        command = command.split()
        if command[1] not in list:
            list.insert(0,command[1])
    elif 'Unnecessary' in command:
        command1 = command.split()
        if command1[1] in list:
            list.remove(command1[1])
    elif 'Correct' in command:
        command1 = command.split()
        if command1[1] in list:
            index = list.index(command1[1])
            list.pop(index)
            list.insert(index,command1[2])
    elif 'Rearrange' in command:
        command1 = command.split()
        if command1[1] in list:
            list.remove(command1[1])
            list.append(command1[1])
    command = input()

print(*list, sep=", ")