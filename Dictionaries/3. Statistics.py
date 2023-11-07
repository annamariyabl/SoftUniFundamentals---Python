element = input()
bakery = {}
while element != 'statistics':
    element = element.split(": ")
    product = element[0]
    quantity = int(element[1])
    if product in bakery:
        bakery[product] += quantity
    else:
        bakery[product] = quantity
    element = input()

print("Products in stock:")
for product, quantity in bakery.items():
    print(f'- {product}: {quantity}')
print(f'Total Products: {len(bakery.keys())}')
print(f'Total Quantity: {sum(bakery.values())}')

