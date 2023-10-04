string1 = input().split()
string2 = input().split()
string3 = input().split()
bul = False
name = 'First'

for player in range (1, 3):
    player = str(player)
    line = [player, player, player]
    if string1 == line or string2 == line or string3 == line:
        bul = True
    for i in range (3):
        if string1[i] == player and string2[i]==player and string3[i]==player:
            bul=True
    if string1[0] == player and string2[1] == player and string3[2] == player:
        bul = True
    elif string1[2] == player and string2[1] == player and string3[0] == player:
        bul = True
    if bul:
        print(f'{name} player won')
        break
    name = 'Second'
else:
    print('Draw!')
