input = input().split(', ')
dictionary = {}
for i in input:
    key = i
    value = ord(i)
    dictionary[key] = value

print(dictionary)
