number = int(input())
sum = 0
for i in range (number):
    letter = input()
    sum += ord(letter)

print(f'The sum equals: {sum}')