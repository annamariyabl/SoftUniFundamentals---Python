n = int(input())
dictionary = {}
for i in range(n):
    plant, rarity = input().split('<->')
    dictionary[plant] = []
    dictionary[plant].append(int(rarity))
command = input()
while command != 'Exhibition':
    com = command.split(': ')
    com = com[1]
    if "Rate" in command:
        com = com.split(" - ")
        plant = com[0]
        if plant not in dictionary.keys():
            print('error')
            command = input()
            continue
        rating = int(com[1])
        dictionary[plant].append(rating)
    elif 'Update' in command:
        com = com.split(" - ")
        plant = com[0]
        if plant not in dictionary.keys():
            print('error')
            command = input()
            continue
        new_rarity = com[1]
        dictionary[plant].pop(0)
        dictionary[plant].insert(0, int(new_rarity))
    elif "Reset" in command:
        if com not in dictionary.keys():
            print('error')
            command = input()
            continue
        for i in range(len(dictionary[com])-1):
            dictionary[com].pop(1)
    command = input()
print('Plants for the exhibition:')
for i in dictionary:
    if len(dictionary[i])-1 > 0:
        average_rating = (sum(dictionary[i])-dictionary[i][0])/(len(dictionary[i])-1)
        print(f"- {i}; Rarity: {dictionary[i][0]}; Rating: {average_rating:.2f}")
    else: print(f"- {i}; Rarity: {dictionary[i][0]}; Rating: {0:.2f}")

