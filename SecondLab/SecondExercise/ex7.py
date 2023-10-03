n = int(input())
sum = 0
for i in range(n):
    litters = int(input())
    sum+=litters
    if(sum > 255):
        print('Insufficient capacity!')
        sum-=litters

print(sum)
