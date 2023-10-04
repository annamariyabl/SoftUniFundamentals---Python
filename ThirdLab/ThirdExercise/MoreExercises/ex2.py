numbers = input().split()
message = input()
message_as_list = list(message)

for i in range (len(numbers)):
    number = list(numbers[i])
    int_list = [eval(i) for i in number]
    sum_of_list = sum(int_list)
    index = sum_of_list % len(message_as_list)
    print(message_as_list[index], end="")
    message_as_list.pop(index)

