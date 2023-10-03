list_of_integer = input().split()
n = int(input())
my_list = []

for i in list_of_integer:
    my_list.append(int(i))

for i in range (n):
    min_num = my_list[0]
    for j in range (1, len(my_list)):
        if my_list[j] < min_num:
            min_num = my_list[j]
    my_list.remove(min_num)

print(*my_list, sep=", ")

