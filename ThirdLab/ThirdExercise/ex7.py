gifts = input().split()
command = input()
while command != 'No Money':
    x = command.split()
    if 'OutOfStock' in x:
        for i in range (len(gifts)):
            if gifts[i] == x[1]:
                gifts[i] = 'None'
    elif 'Required' in x:
        if 0 <= int(x[2]) <= len(gifts)-1:
            gifts[int(x[2])] = x[1]
    elif 'JustInCase' in x:
        gifts[-1] = x[1]
    command = input()

while 'None' in gifts:
    gifts.remove('None')
print(*gifts)

