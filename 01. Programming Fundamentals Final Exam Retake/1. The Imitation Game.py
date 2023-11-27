text = input()
command = input()
new_text = ''
while command != 'Decode':
    activity = command.split('|')
    if "Move" in command:
        number_of_letters = int(activity[1])
        text = text[number_of_letters:] + text[:number_of_letters]
    elif "Insert" in command:
        index = int(activity[1])
        value = activity[2]
        text = text[:(index)] + value + text[(index):]
    elif "ChangeAll" in command:
        substring = activity[1]
        replacement = activity[2]
        text = text.replace(substring,replacement)

    command = input()

print(f'The decrypted message is: {text}')