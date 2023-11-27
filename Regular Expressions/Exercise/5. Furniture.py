import re
text = input()
matches = []
total_cost = 0
while text != "Purchase":
    pattern = r">>([A-Za-z]+)<<(\d+\.?\d*)!(\d+)"
    match = re.search(pattern, text)
    if match:
        furniture, price, quantity = match.groups()
        matches.append(furniture)
        total_cost += float(price)*int(quantity)
    text = input()
print('Bought furniture:')
for i in matches:
    print(i)

print(f'Total money spend: {total_cost:.2f}')