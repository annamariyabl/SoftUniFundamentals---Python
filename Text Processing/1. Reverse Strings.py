word = input()
while word != 'end':
    reversed_string = ""
    for i in reversed(word):
        reversed_string += i
    print(f'{word} = {reversed_string}')
    word = input()