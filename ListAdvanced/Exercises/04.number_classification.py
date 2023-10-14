list = list(map(int, input().split(', ')))
list_positive = [i for i in list if i>=0]
list_negative = [i for i in list if i <0]
list_even = [i for i in list if i%2 == 0]
list_odd = [i for i in list if i%2 != 0]

print(f'Positive:', end = ' ')
print(*list_positive, sep=", ")
print(f'Negative:', end=' ')
print(*list_negative, sep=", ")
print(f'Even:', end=' ')
print(*list_even, sep=", ")
print(f'Odd:', end=' ')
print(*list_odd, sep=", ")



