string = input().split()

command = input()
while command != "3:1":
    command = command.split()
    if 'merge' in command:
        start_index = int(command[1])
        end_index = int(command[2])
        if start_index < 0:
            start_index = 0
        if end_index>len(string)-1:
            end_index = len(string)-1
        new_string = ''.join(string[start_index:end_index+1])
        string[start_index:end_index+1] = [new_string]

    if 'divide' in command:
        index = int(command[1])
        partitions = int(command[2])
        element = string[index]
        partitions_length = len(element) // partitions
        divided_partition = []
        for i in range (partitions):
            if i != partitions-1:
                divided_partition.append(element[i*partitions_length:(i + 1) * partitions_length])
            else:
                divided_partition.append(element[i*partitions_length:])
        string[index:index+1] = divided_partition

    command = input()

print(*string)