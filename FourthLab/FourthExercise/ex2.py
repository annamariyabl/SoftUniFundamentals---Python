a = int(input())
b = int(input())
c = int(input())


def sum_numbers(num1, num2):
    return num1 + num2

def subtract(num1,num2, num3):
    sum1 = sum_numbers(num1, num2)
    return sum1 - num3

def add_and_subtract(num1, num2, num3):
    return (subtract(num1,num2,num3))

print(add_and_subtract(a, b, c))


