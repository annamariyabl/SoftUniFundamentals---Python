import re
password = input()
command = input()
is_upper = False
is_lower = False
is_digit = False
pattern = '\W'
while command != 'Complete':
    command = command.split()
    if "Upper" in command:
        index = int(command[2])
        password = password[:index] + password[index].capitalize() + password[index+1:]
        print(password)
    elif 'Lower' in command:
        index = int(command[2])
        password = password[:index] + password[index].lower() + password[index + 1:]
        print(password)
    elif 'Insert' in command:
        index = int(command[1])
        char = command[2]
        if index < len(password):
            password = password[:index]+char+password[index:]
            print(password)
    elif 'Replace' in command:
        char = command[1]
        value = int(command[2])
        replace = ord(char) + value
        replace = chr(replace)
        while char in password:
            password = password.replace(char, replace)
        print(password)
    elif 'Validation' in command:
        if len(password) < 8:
            print("Password must be at least 8 characters long!")
        match = re.findall(pattern, password)
        if len(match) > 0:
            print("Password must consist only of letters, digits and _!")
        for i in password:
            if 65 <= ord(i) <= 90:
                is_upper = True
            if 91 <= ord(i) <= 122:
                is_lower = True
            if i.isdigit():
                is_digit = True
        if is_upper == False:
            print("Password must consist at least one uppercase letter!")
        if is_lower == False:
            print("Password must consist at least one lowercase letter!")
        if is_digit == False:
            print("Password must consist at least one digit!")
    command = input()
