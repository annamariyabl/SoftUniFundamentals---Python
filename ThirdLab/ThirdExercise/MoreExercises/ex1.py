string = input().split(", ")
int_list = [eval(i) for i in string]
for i in range (len(int_list)):
    if int_list[i] == 0:
        int_list.remove(int_list[i])
        int_list.append(0)


print(int_list)