import math

budget = float(input())
price_flour = float(input())
price_eggs = 0.75*price_flour
price_milk = price_flour*1.25
bread_price = price_eggs+price_milk/4+price_flour
loafs = budget//bread_price
money_left = budget-(price_flour+price_eggs+price_milk/4)*loafs
loafs= int(loafs)
eggs = 0
if loafs <3:
    eggs = loafs*3
else:
    eggs=loafs*3
    for i in range (1,loafs+1):
        if i % 3 == 0:
            loose=(i-2)
            if loose <= 0:
                loose=2
            eggs -=loose

print(f'You made {loafs} loaves of Easter bread! Now you have {eggs} eggs and {money_left:.2f}BGN left.')


