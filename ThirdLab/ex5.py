n = int(input())
my_list = []
for i in range (n):
    number = int(input())
    my_list.append(number)

command = input()
if command == 'even':
    for i in range(len(my_list)-1, -1, -1):
        element = my_list[i]
        if element % 2 != 0:
            my_list.remove(element)
elif command == 'odd':
    for i in range(len(my_list)-1, -1, -1):
        element = my_list[i]
        if element % 2 == 0:
            my_list.remove(element)
elif command == 'negative':
    for i in range(len(my_list) - 1, -1, -1):
        element = my_list[i]
        if element >= 0:
            my_list.remove(element)
elif command == 'positive':
    for i in range(len(my_list) - 1, -1, -1):
        element = my_list[i]
        if element < 0:
            my_list.remove(element)

print(my_list)