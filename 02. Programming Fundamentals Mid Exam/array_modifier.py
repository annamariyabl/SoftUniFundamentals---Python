array = list(map(int, input().split()))
command = input()
while command != 'end':
    command = command.split()
    if 'swap' in command:
        index1 = int(command[1])
        index2 = int(command[2])
        array[index1],array[index2]=array[index2],array[index1]
    elif 'multiply' in command:
        index1 = int(command[1])
        index2 = int(command[2])
        array[index1] *= array[index2]
    elif 'decrease' in command:
        array = [array[i]-1 for i in range(len(array))]

    command = input()

print(*array, sep=', ')
