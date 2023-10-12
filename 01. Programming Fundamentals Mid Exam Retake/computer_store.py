price = input()
total_price = 0

while price != 'regular' or price != 'special':
    if price == 'regular' or price == 'special':
        break
    price = float(price)
    if price <= 0:
        print('Invalid price!')
        price = input()
        continue
    else: total_price += price
    price = input()
taxes = total_price*0.2
total_price_without_taxes =total_price
total_price += taxes

if price == 'special':
    total_price*=0.90
if total_price == 0:
    print("Invalid order!" )
else:
    print("Congratulations you've just bought a new computer!")
    print(f'Price without taxes: {(total_price_without_taxes):.2f}$')
    print(f'Taxes: {taxes:.2f}$')
    print('-----------')
    print(f'Total price: {total_price:.2f}$')
