string = input()

my_list = list(string.split(" "))

for i in range (len(my_list)):
    my_list[i] = int(my_list[i])
    my_list[i] = -my_list[i]


print(my_list)