import re
pattern = r"\bwww\.[A-Za-z0-9\-?\.?]+\.[a-z]+\b"
list = []

while True:
    strings = input()
    if strings == "":
        break
    else:
        match = re.findall(pattern, strings)
        if match:
            list.append(match)

for i in list:
    print(*i)

