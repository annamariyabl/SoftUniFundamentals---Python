usernames = input().split(", ")
is_true = True
for username in usernames:
    if 3<= len(username) <= 16:
        for i in username:
            if i.isdigit() or i.isalpha() or i == '-' or i == '_':
                is_true = True
            else:
                is_true = False
                break
        if is_true:
            print(username)




