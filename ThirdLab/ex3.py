positive_list = []
negative_list = []
n = int(input())

for i in range (n):
    data = int(input())
    if data >= 0:
        positive_list.append(data)
    else:
        negative_list.append(data)


print(positive_list)
print(negative_list)
print(f'Count of positives: {len(positive_list)}')
print(f'Sum of negatives: {sum(negative_list)}')

