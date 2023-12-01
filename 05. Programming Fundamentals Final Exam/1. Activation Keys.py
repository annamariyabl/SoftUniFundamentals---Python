activation_key = input()
command = input()
while command != 'Generate':
    command = command.split('>>>')
    if 'Contains' in command:
        substring = command[1]
        if substring in activation_key:
            print(f"{activation_key} contains {substring}")
        else:
            print("Substring not found!")
    elif 'Flip' in command:
        upper_lower = command[1]
        startIndex = int(command[2])
        endIndex = int(command[3])
        if upper_lower == 'Upper':
            string = activation_key[startIndex:endIndex]
            activation_key = activation_key.replace(string, string.upper())
            print(activation_key)
        else:
            string = activation_key[startIndex:endIndex]
            activation_key = activation_key.replace(string, string.lower())
            print(activation_key)
    elif 'Slice' in command:
        startIndex = int(command[1])
        endIndex = int(command[2])
        activation_key = activation_key[:startIndex]+activation_key[endIndex:]
        print(activation_key)
    command = input()

print(f"Your activation key is: {activation_key}")


