year = int(input())
new_year = year+1
while True:
    for i in str(new_year):
        if str(new_year).count(i) != 1:
            new_year += 1
            break
    else:
        print(new_year)
        break