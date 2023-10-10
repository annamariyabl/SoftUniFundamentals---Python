number = int(input())

def tribonacc(n):
    list = [1, 0, 0]
    for i in range (n):
        new_num = sum(list)
        print(new_num, end=' ')
        list.append(new_num)
        list.pop(0)

tribonacc(number)

