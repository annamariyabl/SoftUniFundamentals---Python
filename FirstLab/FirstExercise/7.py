while True:
    word = input()
    if word == 'End':
        break
    if word == 'SoftUni':
        continue
    for i in range (len(word)):
        print(word[i]*2, end="")
    print()

