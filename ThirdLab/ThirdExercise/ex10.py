string = input().split('|')
energy = 100
coins = 100
for i in range(len(string)):
    day = string[i].split('-')
    if 'rest' in day:
        energy += int(day[1])
        if energy > 100:
            print(f'You gained {int(day[1])-(energy-100)} energy.')
            energy = 100
        else:
            print(f'You gained {int(day[1])} energy.')
        print(f"Current energy: {energy}.")
    elif 'order' in day:
        if energy < 30:
            print('You had to rest!')
            energy += 50
            if energy > 100:
                energy = 100
        else:
            coins += int(day[1])
            energy -= 30
            print(f"You earned {day[1]} coins.")
    else:
        if coins >= int(day[1]):
            print(f"You bought {day[0]}.")
            coins -= int(day[1])
        else:
            print(f"Closed! Cannot afford {day[0]}.")
            break
else:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")




