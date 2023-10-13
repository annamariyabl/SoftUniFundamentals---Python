string = input().split()
palindrome = input()
palindromes =[]
for word in string:
    if word == ''.join(reversed(word)):
        palindromes.append(word)

print(palindromes)
print(f'Found palindrome {palindromes.count(palindrome)} times')