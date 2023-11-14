contact = input()
phonebook = {}
while '-' in contact:
    contact = contact.split('-')
    phonebook[contact[0]] = contact[1]
    contact = input()

n = int(contact)
for i in range (n):
    name = input()
    if name in phonebook:
        print(f"{name} -> {phonebook[name]}")
    else:
        print(f"Contact {name} does not exist.")

