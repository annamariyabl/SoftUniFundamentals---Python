number = int(input())
wagons = [0 for i in range(number)]
command = input()
while command != 'End':
    command = command.split()
    if 'add' in command:
        wagons[number-1]+=int(command[1])
    elif 'insert' in command:
        wagons[int(command[1])] += int(command[2])
    elif 'leave' in command:
        wagons[int(command[1])] -= int(command[2])
    command = input()

print(wagons)