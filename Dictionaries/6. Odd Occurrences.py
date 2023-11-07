string = input().split()
dictionary = {}
for i in string:
    i = i.lower()
    if i not in dictionary:
        dictionary[i] = 1
    else:
        dictionary[i] += 1

for (key, value) in dictionary.items():
    if value % 2 != 0:
        print(key, end = " ")