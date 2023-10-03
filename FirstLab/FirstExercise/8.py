coffees = 0
while True:
    activity = input()
    if activity == "END":
        break
    elif activity == 'coding' or activity == 'dog' or activity== 'cat' or activity== 'movie':
        coffees+=1
    elif activity in 'CODING DOG CAT MOVIE':
        coffees+=2
    else: continue

if coffees > 5:
    print('You need extra sleep')
else:
    print(coffees)
