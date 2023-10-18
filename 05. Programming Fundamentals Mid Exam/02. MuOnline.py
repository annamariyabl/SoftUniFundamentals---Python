health = 100
bitcoins = 0
rooms = input().split('|')
max = 0
best_room = 0
for room in rooms:
    command = room.split()
    number = int(command[1])
    if 'potion' in command:
        h = health
        health += number
        if health > 100:
            health = 100
            h = 100 - h
            print(f'You healed for {h} hp.')
        else:
            print(f'You healed for {number} hp.')
        print(f'Current health: {health} hp.')
    elif 'chest' in command:
        bitcoins += number
        print(f'You found {number} bitcoins.')
    else:
        health -= number
        if health <= 0:
            print(f'You died! Killed by {command[0]}.')
            best_room = rooms.index(room)+1
            print(f"Best room: {best_room}")
            break
        else:
            print(f'You slayed {command[0]}.')
else:
    print("You've made it!")
    print(f'Bitcoins: {bitcoins}')
    print(f'Health: {health}')



