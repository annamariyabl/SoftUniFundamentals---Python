message = input()
command = input()
while command != 'Reveal':
    operation = command.split(":|:")
    if "InsertSpace" in command:
        index = int(operation[1])
        message = message[:index] + " " + message[index:]
        print(message)
    elif "Reverse" in command:
        substring = operation[1]
        if substring in message:
            message = message.replace(substring,'')
            substring = substring[::-1]
            message += substring
            print(message)
        else:
            print('error')
    elif 'ChangeAll' in command:
        substring = operation[1]
        replacement = operation[2]
        while substring in message:
            message = message.replace(substring, replacement)
        print(message)
    command = input()

print(f"You have a new text message: {message}")
