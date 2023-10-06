number = int(input())
sum_of_number =0

def divisor(a, b):
    return a % b == 0

for i in range (1, number//2+1):
    if divisor(number, i):
        sum_of_number+=i

if sum_of_number == number:
    print('We have a perfect number!')
else:
    print("It's not so perfect.")