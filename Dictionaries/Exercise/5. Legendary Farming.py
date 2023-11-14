dictionary = {'shards': 0, 'fragments':0, 'motes':0 }
word = input()
while True:
    counter = 0
    row = word.split()
    for i in range(0,len(row),2):
        word = row[i+1].lower()
        if word not in dictionary:
            dictionary[word] = int(row[i])
        else:
            dictionary[word] += int(row[i])
        if dictionary['fragments'] >= 250:
            print('Valanyr obtained!')
            dictionary['fragments'] -= 250
            counter +=1
            break
        elif dictionary['shards'] >= 250:
            print('Shadowmourne obtained!')
            dictionary['shards'] -= 250
            counter += 1
            break
        elif dictionary['motes'] >= 250:
            print('Dragonwrath obtained!')
            dictionary['motes'] -= 250
            counter += 1
            break
    if counter == 1:
        break
    word = input()

for i in dictionary:
    print(f"{i}: {dictionary[i]}")
