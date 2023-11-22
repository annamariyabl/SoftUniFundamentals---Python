sentence = input()
for i in range(len(sentence)):
    if sentence[i] == ":":
        print(sentence[i] + sentence[i+1])