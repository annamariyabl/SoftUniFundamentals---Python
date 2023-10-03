number_of_orders = int(input())
total_price = 0
for i in range(number_of_orders):
    price = float(input())
    days = int(input())
    capsules = int(input())
    if 0.01<=price<=100 and 1<=days<=31 and 1<=capsules<=2000:
        price_of_coffee = price*days*capsules
        print(f'The price for the coffee is: ${price_of_coffee:.2f}')
        total_price += price_of_coffee
    else: continue

print(f'Total: ${total_price:.2f}')
