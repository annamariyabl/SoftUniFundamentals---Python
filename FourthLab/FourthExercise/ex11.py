number = int(input())

def percent(a):
    perc = a // 10
    if a < 100:
        print(f'{a}% [', end ='')
        for i in range(perc):
            print('%', end='')
        for i in range(perc+1, 11):
            print('.', end='')
    elif a == 100:
        print(f'{a}% Complete!')
        print('[',end='')
        for i in range(perc):
            print('%', end='')

percent(number)
print(']')
if number < 100:
    print('Still loading...')
