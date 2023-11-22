text = input()
new_string = ''
end_string= ''
number = ''
unique_symbols = 0
for i in range(len(text)):
    text_upper = text[i].upper()
    if text_upper not in end_string and not text[i].isdigit():
        unique_symbols += 1
    if text[i].isdigit():
        number = text[i]
        for j in range(i+1, len(text)):
            if text[j].isdigit():
                number+=text[j]
            else:
                break
        number = int(number)
        new_string= new_string*number
        end_string += new_string
        new_string = ''
    else:
        new_string += text_upper

end_string += new_string
print(f'Unique symbols used: {unique_symbols}')
print(end_string)