n = int(input())
number1 = 0
snowball_weight1 = 0
snowball_time1 = 0
snowball_quality1 = 0
for i in range (n):
    snowball_weight = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    sum = (snowball_weight / snowball_time) ** snowball_quality
    if (sum > number1):
        number1 = sum
        snowball_weight1 = snowball_weight
        snowball_time1 = snowball_time
        snowball_quality1 = snowball_quality

print(f'{snowball_weight1} : {snowball_time1} = {int(number1)} ({snowball_quality1})')



