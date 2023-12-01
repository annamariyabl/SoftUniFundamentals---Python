import re

text = input()
emojis = []
coolThresholdSum = 1
pattern1 = r'([:]{2}|[*]{2})([A-Z][a-z]{2,})(\1)'
pattern2 = r'\d'
match = re.findall(pattern1,text)
numbers = re.findall(pattern2, text)

if numbers != []:
    for i in numbers:
        coolThresholdSum *= int(i)
    print(f"Cool threshold: {coolThresholdSum}")
else:
    print(f"Cool threshold: {0}")

for i in match:
    emojis.append(i[0]+i[1]+i[2])
print(f"{len(emojis)} emojis found in the text. The cool ones are:")

for emoji in emojis:
    coolness = 0
    for i in emoji:
        if i.isalpha():
            coolness += ord(i)
    if coolness >= coolThresholdSum:
        print(emoji)







