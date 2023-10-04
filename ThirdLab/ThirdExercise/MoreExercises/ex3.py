car_race = input().split()
middle_index = (len(car_race)) // 2
left_car = car_race[0 : middle_index]
right_car = car_race[middle_index+1:][::-1]
left_time = 0
right_time = 0
for i in range (len(left_car)):
    num = int(left_car[i])
    if num == 0:
        left_time = left_time*0.8
    left_time += num
    num1 = int(right_car[i])
    if num1 == 0:
        right_time = right_time*0.8
    right_time += num1

if left_time < right_time:
    print(f'The winner is left with total time: {left_time:.1f}')
elif right_time < left_time:
    print(f'The winner is right with total time: {right_time:.1f}')


