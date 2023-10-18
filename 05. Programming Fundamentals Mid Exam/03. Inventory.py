items = input().split(", ")
command = input()
bul = True
while command != 'Craft!':
    command = command.split(' - ')
    if 'Collect' in command:
        if command[1] not in items:
            items.append(command[1])
    elif 'Drop' in command:
        if command[1] in items:
            items.remove(command[1])
    elif 'Combine Items' in command:
        n = command[1].split(':')
        if n[0] in items:
            index = items.index(n[0])
            items.insert(index+1, n[1])
    elif 'Renew' in command:
        if command[1] in items:
            items.remove(command[1])
            items.append(command[1])
    command = input()

print(*items, sep=", ")