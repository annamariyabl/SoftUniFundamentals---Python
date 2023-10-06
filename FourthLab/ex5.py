product = input()
quantity = int(input())

def total_price (p , q):
    if p == 'coffee':
        return  q*1.5
    elif p == 'water':
        return q*1
    elif p == 'coke':
        return q*1.4
    elif p == 'snacks':
        return q*2

print(f'{total_price(product,quantity):.2f}')