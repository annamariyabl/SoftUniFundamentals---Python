n = int(input())
dictionary = {}
for i in range(n):
    string = input().split()
    command = string[0]
    username = string[1]
    if command == 'register':
        license_plate_number = string[2]
        if username not in dictionary:
            dictionary[username] = license_plate_number
            print(f"{username} registered {license_plate_number} successfully")
        else:
            print(f"ERROR: already registered with plate number {license_plate_number}")
    elif command == 'unregister':
        if username not in dictionary:
            print(f"ERROR: user {username} not found")
        else:
            print(f"{username} unregistered successfully")
            dictionary.pop(username)

for i in dictionary:
    print(f'{i} => {dictionary[i]}')

