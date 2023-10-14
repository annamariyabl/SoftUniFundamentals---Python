rooms = int(input())
counter = 0
counter_print = True
for i in range(1, rooms+1):
    room = input().split()
    if len(room[0]) >= int(room[1]):
        counter += (len(room[0])-int(room[1]))
    else:
        print(f'{abs((len(room[0])-int(room[1])))} more chairs needed in room {i}')
        counter_print = False

if counter_print:
    print(f'Game On, {counter} free chairs left')

