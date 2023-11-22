word = input()
last_one = word[0]
print(word[0], end='')
for i in range(1, len(word)):
    if word[i] == last_one:
        continue
    else:
        print(word[i], end='')
        last_one = word[i]