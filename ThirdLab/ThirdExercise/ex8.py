fire = input().split('#')
water = int(input())
effort = 0
total_fire = 0
print('Cells:')
for i in range (len(fire)):
    type = fire[i].split(' = ')
    if 'High' in type:
        if 81<=int(type[1])<=125:
            if int(type[1]) <= water:
                print(f' - {type[1]}')
                effort += int(type[1]) * 0.25
                water -= int(type[1])
                total_fire += int(type[1])
            else: continue
    elif 'Medium' in type:
        if 51<=int(type[1])<=80:
            if int(type[1]) <= water:
                print(f' - {type[1]}')
                effort += int(type[1]) * 0.25
                water-=int(type[1])
                total_fire += int(type[1])
            else: continue
    elif 'Low' in type:
        if 1<=int(type[1])<=50:
            if int(type[1]) <= water:
                print(f' - {type[1]}')
                effort += int(type[1]) * 0.25
                water -= int(type[1])
                total_fire += int(type[1])
            else: continue
print(f'Effort: {effort:.2f}')
print(f'Total Fire: {total_fire}')