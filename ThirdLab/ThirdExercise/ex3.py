string = input()
my_list = list(string.split(" "))
teamA = []
teamB = []

for i in range (len(my_list)):
    if 'A' in my_list[i]:
        teamA.append(my_list[i])
        teamA = list(set(teamA))
        if (11 - len(teamA)) < 7:
            print(f"Team A - {11 - len(teamA)}; Team B - {11 - len(teamB)}")
            print('Game was terminated')
            break
    elif 'B' in my_list[i]:
        teamB.append(my_list[i])
        teamB = list(set(teamB))
        if (11 - len(teamB)) < 7:
            print(f"Team A - {11 - len(teamA)}; Team B - {11 - len(teamB)}")
            print('Game was terminated')
            break
else:
    print(f"Team A - {11 - len(teamA)}; Team B - {11 - len(teamB)}")


