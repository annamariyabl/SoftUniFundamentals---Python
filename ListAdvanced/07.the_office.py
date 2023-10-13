happiness = input().split()
factor = int(input())
happiness = [factor*int(i) for i in happiness]

happy = [human for human in happiness if human >= sum(happiness)/len(happiness)]

if len(happy) >= len(happiness)/2:
    print(f'Score: {len(happy)}/{len(happiness)}. Employees are happy!')
else:
    print(f'Score: {len(happy)}/{len(happiness)}. Employees are not happy!')