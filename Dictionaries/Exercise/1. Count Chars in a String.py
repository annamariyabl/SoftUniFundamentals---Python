string = input()
dictionary = {}
for i in string:
    if i != " ":
        if i not in dictionary:
            dictionary[i] = 1
        else:
            dictionary[i]+=1

for i in dictionary:
    print(f"{i} -> {dictionary[i]}")
