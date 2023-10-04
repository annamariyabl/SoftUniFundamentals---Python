list_of_people = input().split()
sequence = int(input())
new_list = []
index = sequence-1

while len(list_of_people) > 0:
    if index < len(list_of_people):
        new_list.append(list_of_people[index])
        list_of_people.pop(index)
        index+=sequence-1
    else:
        index = index-len(list_of_people)

for i in range (len(new_list)):
    new_list[i] = int(new_list[i])
print('[', end='')
print(*new_list, sep=',' ,end='')
print(']')


