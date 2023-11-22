string = input()
new_string = ''
strenght = 0
for i in range(len(string)):
    if strenght > 0 and string[i] != '>':
        strenght -= 1
    elif string[i] == ">":
        new_string+='>'
        strenght += int(string[i+1])
    else:
        new_string += string[i]
print(new_string)