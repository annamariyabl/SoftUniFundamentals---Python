key = int(input())
lines = int(input())
word = str()
for i in range (lines):
    a = input()
    number = ord(a)
    number += key
    letter = chr(number)
    word+= letter

print(word)





