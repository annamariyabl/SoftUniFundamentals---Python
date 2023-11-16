words = input().split(", ")
tekst = input()
for i in words:
    if i in tekst:
        tekst = tekst.replace(i,"*"*len(i))

print(tekst)