pirate_ship = list(map(int, input().split('>')))
war_ship = list(map(int, input().split('>')))
max_health_capacity = int(input())
command = input()
bul = True
while command != 'Retire':
    command = command.split()
    if 'Fire' in command:
        index = int(command[1])
        damage = int(command[2])
        if 0 <= index < len(war_ship):
            war_ship[index] -= damage
            if war_ship[index] <= 0:
                print('You won! The enemy ship has sunken.')
                break
    elif "Defend" in command:
        start_index = int(command[1])
        end_index = int(command[2])
        damage = int(command[3])
        if start_index >= 0 and end_index < len(pirate_ship):
            for i in range(start_index, end_index+1):
                pirate_ship[i] -= damage
                if pirate_ship[i] <= 0:
                    print('You lost! The pirate ship has sunken.')
                    bul = False
                    break
            if bul == False:
                break
    elif 'Repair' in command:
        index = int(command[1])
        health = int(command[2])
        if 0<= index < len(pirate_ship):
            pirate_ship[index] += health
            if pirate_ship[index] > max_health_capacity:
                pirate_ship[index] = max_health_capacity
    elif 'Status' in command:
        counter = 0
        for i in pirate_ship:
            if i < max_health_capacity*0.2:
                counter+=1
        print(f'{counter} sections need repair.')

    command = input()
else:
    print(f'Pirate ship status: {sum(pirate_ship)}')
    print(f'Warship status: {sum(war_ship)}')



