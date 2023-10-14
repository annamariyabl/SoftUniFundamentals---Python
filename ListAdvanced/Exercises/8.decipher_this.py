message = input().split()

new_string = []
for word in message:
    number = ''.join((x for x in word if x.isdigit()))
    word = ''.join((x for x in word if not x.isdigit()))
    num = int(number)
    number = str()
    first_letter = chr(num)
    word = first_letter+word
    word_letters = [*word]
    word_letters[1], word_letters[-1] = word_letters[-1],  word_letters[1]
    word = ''.join((x for x in word_letters))
    new_string.append(word)


print(*new_string, sep=" ")



