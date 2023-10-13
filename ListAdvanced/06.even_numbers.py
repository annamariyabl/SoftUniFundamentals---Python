string_number = input().split(', ')
even_numbers_indexes = []
for i in range(len(string_number)):
    if int(string_number[i]) % 2 == 0:
        even_numbers_indexes.append(i)

print(even_numbers_indexes)