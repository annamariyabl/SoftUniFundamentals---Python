string = input()
dictionary = {}
while string != 'buy':
    row = string.split()
    name = row[0]
    price = row[1]
    quantity = float(row[2])
    if name not in dictionary:
        dictionary[name] = []
        dictionary[name].append(float(quantity))
        dictionary[name].append(float(price))
    else:

        dictionary[name].pop(1)
        dictionary[name].append(float(price))
        dictionary[name][0] += quantity


    string = input()

for i in dictionary:
    total_price = dictionary[i][0]*dictionary[i][1]
    print(f"{i} -> {total_price:.2f}")
