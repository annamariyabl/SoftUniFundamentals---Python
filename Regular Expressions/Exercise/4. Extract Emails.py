import re
text = input()
pattern = r"\s(([0-9a-z]+[0-9a-z\.\-\_]*)@([a-z\-]+)(\.[a-z]+)+)\b"
matches = re.findall(pattern, text)

for i in matches:
    print(i[0])
