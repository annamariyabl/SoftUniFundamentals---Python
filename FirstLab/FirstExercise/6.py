n = int(input())
for i in range(n):
    word = str(input())
    is_pure = True
    for j in range(len(word)):
        if word[j] == ',' or word[j] == '_' or word[j] == '.':
            is_pure = False
            break

    if is_pure == True:
        print(f'{word} is pure.')
    else:
        print(f'{word} is not pure!')
