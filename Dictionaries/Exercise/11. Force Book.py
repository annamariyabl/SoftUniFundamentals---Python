command = input()
dictionary = {}
counter =0
while command !="Lumpawaroo":
    if ' | ' in command:
        command = command.split(" | ")
        force_side = command[0]
        force_user = command[1]
        for i in dictionary:
            if force_user in dictionary[i]:
                counter += 1
                break
        if counter == 1:
            break
        if force_side not in dictionary:
            dictionary[force_side] = []
            dictionary[force_side].append(force_user)
        elif force_side in dictionary:
            if counter == 0:
                dictionary[force_side].append(force_user)
    elif " -> " in command:
        command = command.split(" -> ")
        force_side = command[1]
        force_user = command[0]
        for i in dictionary:
            if force_user in dictionary[i]:
                dictionary[i].remove(force_user)

        else:
            if force_side not in dictionary:
                dictionary[force_side] = []
                dictionary[force_side].append(force_user)
                print(f"{force_user} joins the {force_side} side!")
            else:
                dictionary[force_side].append(force_user)
                print(f"{force_user} joins the {force_side} side!")
    command = input()

for i in dictionary:
    if len(dictionary[i])>0:
        print(f'Side: {i}, Members: {len(dictionary[i])}')
        for j in range(len(dictionary[i])):
            print(f'! {dictionary[i][j]}')



