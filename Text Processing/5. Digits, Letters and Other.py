text = input()
digits = ""
letters = ''
characters = ''
for i in text:
    if 48<=ord(i)<=57:
        digits+=i
    elif 65 <= ord(i) <= 90 or 97 <= ord(i) <= 122:
        letters += i
    else:
        characters += i

print(digits)
print(letters)
print(characters)