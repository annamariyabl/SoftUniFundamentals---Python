targets = list(map(int, input().split()))
command = input()
while command != 'End':
    command1 = command.split()
    index = int(command1[1])
    if "Shoot" in command1:
        power = int(command1[2])
        if 0 <= index < len(targets):
            targets[index] -= power
            if targets[index]<=0:
                targets.pop(index)
        else:
            command = input()
            continue
    elif "Add" in command1:
        value = int(command1[2])
        if 0 <= index < len(targets):
            targets.insert(index,value)
        else:
            print("Invalid placement!")
            command = input()
            continue
    elif 'Strike' in command1:
        radius = int(command1[2])
        if 0 <= index-radius and index+radius<=len(targets):
            remove = radius*2+1
            counter = 0
            while counter < remove:
                targets.pop(index-radius)
                counter+=1
        else:
            print("Strike missed!" )
            command = input()
            continue
    command = input()
print(*targets, sep='|')






