import math

budget = float(input())
students = int(input())
price_flour = float(input())
price_egg = float(input())
price_apron = float(input())

price_eggs = students*10*price_egg
aprons = math.ceil(students*1.2)
price_aprons = aprons*price_apron

flour = students - students // 5
price_flour = price_flour*flour
total_cost = price_eggs+price_aprons+price_flour
if budget >= total_cost:
    print(f"Items purchased for {total_cost:.2f}$.")
else:
    print(f"{(total_cost-budget):.2f}$ more needed.")
