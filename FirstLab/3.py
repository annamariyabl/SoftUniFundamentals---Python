word = str(input())
reserve_word = ''
for i in range (len(word) -1 , -1, -1):
    reserve_word += word[i]
print(reserve_word)

