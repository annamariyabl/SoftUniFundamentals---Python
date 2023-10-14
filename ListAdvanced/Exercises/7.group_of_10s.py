my_list = list(map(int, input().split(', ')))
max_value = max(my_list)
new_list = []

max_number1 = max_value // 10
max_number2 = max_value % 10
if max_number2 != 0:
    for i in range (10, (max_number1+2)*10, 10):
        for num in my_list:
            if num <= i and num > i-10:
                new_list.append(num)
        print(f"Group of {i}'s: {new_list}")
        new_list = []
else:
    for i in range (10, (max_number1+1)*10, 10):
        for num in my_list:
            if num <= i and num > i-10:
                new_list.append(num)
        print(f"Group of {i}'s: {new_list}")
        new_list = []
