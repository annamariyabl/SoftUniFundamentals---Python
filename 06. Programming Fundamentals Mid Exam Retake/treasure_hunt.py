loots = input().split('|')
command = input()
while command != "Yohoho!":
    command = command.split()
    if "Loot" in command:
        command.remove('Loot')
        for i in command:
            if i not in loots:
                loots.insert(0,i)
    elif "Drop" in command:
        index = int(command[1])
        if 0 <= index < len(loots):
            add = loots[int(command[1])]
            loots.pop(int(command[1]))
            loots.append(add)
    elif 'Steal' in command:
        index = int(command[1])
        if index<len(loots):
            new_list = loots[(len(loots)-index):]
            print(*new_list, sep=', ')
            loots = loots[:(len(loots)-index)]
        else:
            new_list = loots
            print(*new_list, sep=", ")
            loots = []
    command = input()

if loots == []:
    print('Failed treasure hunt.')
else:
    length = 0
    for i in loots:
        length += len(i)
    length = length / len(loots)
    print(f'Average treasure gain: {length:.2f} pirate credits.')

