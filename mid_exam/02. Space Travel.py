string = input().split("||")
flue = int(input())
ammunition = int(input())

for word in string:
    command = word.split()

    if 'Travel' in command:
        num = int(command[1])
        if flue >= num:
            print(f"The spaceship travelled {num} light-years.")
            flue -= num
        else:
            print("Mission failed.")
            break
    elif 'Enemy' in command:
        num = int(command[1])
        if ammunition >= num:
            print(f'An enemy with {num} armour is defeated.')
            ammunition-=num
        else:
            if flue >= num*2:
                print(f'An enemy with {num} armour is outmaneuvered.')
                flue = flue - num*2
            else:
                print("Mission failed.")
                break
    elif 'Repair' in command:
        num = int(command[1])
        flue += num
        ammunition = num*2
        print(f"Ammunitions added: {num*2}.")
        print(f"Fuel added: {num}.")
    elif 'Titan' in command:
        print("You have reached Titan, all passengers are safe.")


