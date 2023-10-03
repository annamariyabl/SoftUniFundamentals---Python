string= input().split(', ')
beggars = int(input())
my_list = []
new_list = []

for i in string:
    my_list.append(int(i))

start_index = 0
while start_index < beggars:
    current_beggar_sum = 0
    for i in range (start_index, len(my_list), beggars):
        current_beggar_sum += my_list[i]
    new_list.append(current_beggar_sum)
    start_index+=1

print(new_list)

