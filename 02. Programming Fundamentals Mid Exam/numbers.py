numbers = list(map(int, input().split()))
average = sum(numbers) / len(numbers)
bigger_number = [i for i in numbers if i > average]
bigger_number.sort()
bigger_number.reverse()

if len(bigger_number) > 5:
    print(*bigger_number[0:5], sep=' ')
elif len(bigger_number) == 0:
    print('No')
else:
    print(*bigger_number, sep=" ")
