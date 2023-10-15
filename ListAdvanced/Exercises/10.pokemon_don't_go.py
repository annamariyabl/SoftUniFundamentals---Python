my_list = list(map(int, input().split()))
index = int(input())
new_list = []
while len(my_list) > 0:
    if 0 <= index < len(my_list):
        element = my_list[index]
        new_list.append(element)
        for i in range(len(my_list)):
            if my_list[i] <= element:
                my_list[i] += element
            else:
                my_list[i] -= element
        my_list.pop(index)

    elif index < 0:
        new_list.append(my_list[0])
        element = my_list[0]
        for i in range(len(my_list)):
            if my_list[i] <= element:
                my_list[i]+= element
            else:
                my_list[i]-= element
        my_list.pop(0)
        last_element = my_list[len(my_list)-1]
        my_list.insert(0, last_element)

    elif index >= len(my_list):
        element = my_list[-1]
        new_list.append(my_list[-1])
        for i in range(len(my_list)):
            if my_list[i] <= element:
                my_list[i] += element
            else:
                my_list[i] -= element
        my_list.pop(-1)
        my_list.append(my_list[0])


    if len(my_list) == 0:
        break
    index = int(input())

print(sum(new_list))
