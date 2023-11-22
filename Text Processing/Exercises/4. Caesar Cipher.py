sentence = input()
new_sentence = ''
for i in sentence:
    a = ord(i)+3
    new_sentence += chr(a)

print(new_sentence)