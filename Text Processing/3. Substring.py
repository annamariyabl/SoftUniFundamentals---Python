word = input()
strings = input()
while word in strings:
    strings = strings.replace(word, "")
print(strings)