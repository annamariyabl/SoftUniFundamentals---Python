n = int(input())
dictionary = {}
for i in range(n):
    text = input()
    piece, composer, key = text.split('|')
    dictionary[piece] = []
    dictionary[piece].append(composer)
    dictionary[piece].append(key)
command = input()
while command != 'Stop':
    if 'Add' in command:
        com = command.split('|')
        new_piece = com[1]
        if new_piece not in dictionary:
            new_composer = com[2]
            new_key = com[3]
            dictionary[new_piece] = []
            dictionary[new_piece].append(new_composer)
            dictionary[new_piece].append(new_key)
            print(f'{new_piece} by {new_composer} in {new_key} added to the collection!')
        else:
            print(f"{new_piece} is already in the collection!")
    elif "Remove" in command:
        com = command.split('|')
        new_piece = com[1]
        if new_piece in dictionary:
            dictionary.pop(new_piece)
            print(f"Successfully removed {new_piece}!")
        else:
            print(f"Invalid operation! {new_piece} does not exist in the collection.")
    elif "ChangeKey" in command:
        com = command.split("|")
        new_piece = com[1]
        new_key = com[2]
        if new_piece in dictionary:
            dictionary[new_piece].pop(1)
            dictionary[new_piece].append(new_key)
            print(f"Changed the key of {new_piece} to {new_key}!")
        else:
            print(f"Invalid operation! {new_piece} does not exist in the collection.")
    command = input()

for piece in dictionary:
    print(f"{piece} -> Composer: {dictionary[piece][0]}, Key: {dictionary[piece][1]}")




