command = input()
companies = {}
while command != 'End':
    employee = command.split(" -> ")
    company = employee[0]
    id = employee[1]
    if company not in companies:
        companies[company] = []
        companies[company].append(id)
    else:
        if id not in companies[company]:
            companies[company].append(id)
    command = input()

for i in companies:
    print(i)
    for j in range(len(companies[i])):
        print(f'-- {companies[i][j]}')

