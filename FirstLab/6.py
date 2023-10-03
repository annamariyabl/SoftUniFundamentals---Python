budget = int(input())
price = input()
total = 0
while price != 'End':
    price = int(price)
    total += price
    if total > budget:
        print('You went in overdraft!')
        break
    price= input()

if price == 'End':
    print('You bought everything needed.')