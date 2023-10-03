a = int(input())
for i in range (a):
    number = int(input())
    if number % 2 != 0:
        print (f'{number} is odd!')
        break
    if i == a-1:
        print("All numbers are even.")