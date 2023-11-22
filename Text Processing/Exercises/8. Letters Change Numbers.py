string = input().split()
total_sum = 0
num = ''
number = 0

for word in string:
    for i in word:
        if i.isdigit():
            num+=i
    first_letter = word[0]
    last_letter = word[len(word)-1]
    num = int(num)
    if 65<=ord(first_letter)<=90:
        first_letter = first_letter.lower()
        first_letter = ord(first_letter) - 96
        total_sum += num / first_letter
    else:
        first_letter = ord(first_letter) - 96
        total_sum += num * first_letter
    if 65 <= ord(last_letter) <= 90:
        last_letter = last_letter.lower()
        last_letter = ord(last_letter) - 96
        total_sum -= last_letter
    else:
        last_letter = ord(last_letter) - 96
        total_sum += last_letter

    number += total_sum
    total_sum=0
    num = ''

print(f'{number:.2f}')


