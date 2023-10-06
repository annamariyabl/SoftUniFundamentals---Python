number = int(input())
sum_even = 0
sum_odd = 0
def my_number(a):
    num = a % 10
    return num

while number > 0:
    my_num = my_number(number)
    number //= 10
    if my_num % 2 == 0:
        sum_even+=my_num
    else:
        sum_odd +=my_num

print(f"Odd sum = {sum_odd}, Even sum = {sum_even}")

