n = int(input())
heroes = {}
for i in range(n):
    hero_name, HP, MP = input().split( )
    if int(HP) <= 100 and int(MP) <= 200:
        heroes[hero_name]=[]
        heroes[hero_name].append(int(HP))
        heroes[hero_name].append(int(MP))

command = input()
while command != 'End':
    command = command.split(' - ')
    if 'CastSpell' in command:
        hero_name = command[1]
        MP_needed = int(command[2])
        spell_name = command[3]
        if heroes[hero_name][1] >= MP_needed:
            heroes[hero_name][1] -= MP_needed
            print(f"{hero_name} has successfully cast {spell_name} and now has {heroes[hero_name][1]} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")
    elif 'TakeDamage' in command:
        hero_name = command[1]
        damage = int(command[2])
        attacker = command[3]
        heroes[hero_name][0] -= damage
        if heroes[hero_name][0] > 0:
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {heroes[hero_name][0]} HP left!")
        else:
            print(f"{hero_name} has been killed by {attacker}!")
            heroes.pop(hero_name)
    elif 'Recharge' in command:
        hero_name = command[1]
        amount = int(command[2])
        heroes[hero_name][1]+=amount
        if heroes[hero_name][1] > 200:
            amount_recovered = amount - (heroes[hero_name][1]-200)
            heroes[hero_name][1] = 200
            print(f"{hero_name} recharged for {amount_recovered} MP!")
        else:
            print(f"{hero_name} recharged for {amount} MP!")
    elif 'Heal' in command:
        hero_name = command[1]
        amount = int(command[2])
        heroes[hero_name][0] += amount
        if heroes[hero_name][0] > 100:
            amount_recovered = amount - (heroes[hero_name][0] - 100)
            heroes[hero_name][0] = 100
            print(f"{hero_name} healed for {amount_recovered} HP!")
        else:
            print(f"{hero_name} healed for {amount} HP!")
    command = input()

for hero_name in heroes:
    print(f'{hero_name}')
    print(f'  HP: {heroes[hero_name][0]}')
    print(f'  MP: {heroes[hero_name][1]}')


