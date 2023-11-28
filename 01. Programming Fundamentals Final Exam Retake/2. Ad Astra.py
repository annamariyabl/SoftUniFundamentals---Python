import re
text = input()
total_calories = 0
pattern1 = r"[|#]([a-zA-Z\s]+)[|#](\d{2}/\d{2}/\d{2})[|#](\d+)[|#]"
match1 = re.findall(pattern1, text)
for i in match1:
    calories = int(i[2])
    if calories <= 10000:
        total_calories+=calories
days = total_calories//2000
print(f'You have food to last you for: {days} days!')
if days != 0:
    for i in match1:
        print(f'Item: {i[0]}, Best before: {i[1]}, Nutrition: {i[2]}')

