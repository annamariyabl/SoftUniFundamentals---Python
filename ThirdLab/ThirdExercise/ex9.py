collection_of_items = input().split('|')
budget = float(input())
a = budget
new_list = []
profit = 0
for i in range (len(collection_of_items)):
    item = collection_of_items[i].split('->')
    if 'Clothes' in item:
        if float(item[1]) <= 50:
            if budget >= float(item[1]):
                new_list.append(float(item[1]))
                budget -= float(item[1])
        else: continue
    elif 'Shoes' in item:
        if float(item[1]) <= 35:
            if budget >= float(item[1]):
                new_list.append(float(item[1]))
                budget -= float(item[1])
        else: continue
    elif 'Accessories' in item:
        if float(item[1]) <= 20.50:
            if budget >= float(item[1]):
                new_list.append(float(item[1]))
                budget -= float(item[1])
        else: continue

for i in range(len(new_list)):
    new_list[i] += new_list[i]*0.4

formatted_new_list = [f'{price:.2f}' for price in new_list]

print(*formatted_new_list)
profit = sum(new_list)-a+budget
print(f'Profit: {profit:.2f}')
if (profit+a)>=150:
    print("Hello, France!")
else:
    print("Not enough money.")

