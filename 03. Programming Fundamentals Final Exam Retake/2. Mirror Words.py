import re
text = input()
pattern = r'([@#])([A-Za-z]{3,})(\1)(\1)([A-Za-z]{3,})(\1)'
matches = re.findall(pattern,text)
mirror_words = []

if len(matches) == 0:
    print("No word pairs found!")
else:
    print(f"{len(matches)} word pairs found!")
    for i in matches:
        reverse = i[4][::-1]
        if i[1] == reverse:
            mirror_words.append(i[1] + " <=> " + i[4])

if len(mirror_words) == 0:
    print("No mirror words!")
else:
    print(f"The mirror words are:")
    print(f"{', '.join(mirror_words)}")