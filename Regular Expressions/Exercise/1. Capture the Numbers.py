import re
lines = []
pattern = "\d+"
while True:
    text = input()
    if text == '':
        break
    else:
        matches = re.findall(pattern, text)
        lines += matches
print(" ".join(lines))

