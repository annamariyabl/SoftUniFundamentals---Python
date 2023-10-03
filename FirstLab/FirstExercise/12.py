quantity = int(input())
days = int(input())
points = 0
spend = 0
for i in range (1,days+1):
    if i % 11 == 0:
        quantity+=2
    if i % 2 == 0:
        points+=5
        spend += 2*quantity
    if i % 3 == 0:
        points +=13
        spend+=8*quantity
        if i % 5 == 0:
            points += 30
    if i % 5 == 0:
        points +=17
        spend+=15*quantity
    if i % 10 == 0:
        points-=20
        spend+=23


if days % 10 == 0:
    points -= 30

print(f'Total cost: {spend}')
print(f'Total spirit: {points}')
