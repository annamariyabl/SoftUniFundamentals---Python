my_list = ['0']*10
counter = 0
while True:
    command = input().split('-')
    if 'End' in command:
        break
    index = int(command[0])
    note = command[1]
    my_list.pop(index-1)
    my_list.insert(index-1,note)
    counter+=1

my_list = [i for i in my_list if i != '0']

print(my_list)


