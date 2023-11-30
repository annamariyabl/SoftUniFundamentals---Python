import re
text = input()
total_calories = 0
pattern = r"(?i)([|#])([a-z\s]+)(\1)(\d{2}/\d{2}/\d{2})(\1)(\d+)(\1)"
match = re.findall(pattern, text)
for i in match:
    calories = int(i[5])
    if calories <= 10000:
        total_calories+=calories
days = total_calories//2000
print(f'You have food to last you for: {days} days!')
if days != 0:
    for i in match:
        print(f'Item: {i[1]}, Best before: {i[3]}, Nutrition: {i[5]}')

