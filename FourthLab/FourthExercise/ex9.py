password = input()
bul = True
counter = 0
def is_long_enough(a):
    return 6 <= a <= 10

def is_contains_nums_letters(a):
    return 48 <= ord(a) <= 57 or 65 <= ord(a) <= 90 or 97 <= ord(a) <= 122

def at_least_2_digits(a):
    return 48 <= ord(a) <= 57

if not is_long_enough(len(password)):
    print('Password must be between 6 and 10 characters')

for i in password:
    if not is_contains_nums_letters(i):
        print('Password must consist only of letters and digits')
        bul = False
        break

for i in password:
    if at_least_2_digits(i):
        counter+=1
    if counter == 2:
        break
else: print('Password must have at least 2 digits')

if is_long_enough(len(password)) and bul == True and counter == 2:
    print('Password is valid')

