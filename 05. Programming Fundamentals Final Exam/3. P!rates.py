command = input()
dictionary = {}
while command != 'Sail':
    city, population, gold = command.split('||')
    if city not in dictionary:
        dictionary[city] = []
        dictionary[city].append(int(population))
        dictionary[city].append(int(gold))
    else:
        dictionary[city][0]+=int(population)
        dictionary[city][1]+=int(gold)
    command = input()

text = input()
while text != 'End':
    text = text.split('=>')
    if 'Plunder' in text:
        town = text[1]
        people = int(text[2])
        gold = int(text[3])
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
        dictionary[town][0] -= people
        dictionary[town][1] -= gold
        if dictionary[town][0] == 0 or dictionary[town][1] == 0:
            dictionary.pop(town)
            print(f"{town} has been wiped off the map!")
    elif 'Prosper' in text:
        town = text[1]
        gold = int(text[2])
        if gold <= 0:
            print("Gold added cannot be a negative number!" )
        else:
            dictionary[town][1] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {dictionary[town][1]} gold.")
    text = input()

if len(dictionary)>0:
    print(f'Ahoy, Captain! There are {len(dictionary)} wealthy settlements to go to:')
    for city in dictionary:
        print(f'{city} -> Population: {dictionary[city][0]} citizens, Gold: {dictionary[city][1]} kg')
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")