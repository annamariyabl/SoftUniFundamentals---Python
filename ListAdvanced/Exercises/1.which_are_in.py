string1 = input().split(', ')
string2 = input().split(', ')
new_string = []

for word in string1:
    for i in string2:
        if word in i:
            if word not in new_string:
                new_string.append(word)

print((new_string))
