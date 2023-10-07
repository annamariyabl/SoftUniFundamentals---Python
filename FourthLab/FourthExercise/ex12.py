num1 = int(input())
num2 = int(input())


def factorial (a):
    fact = 1
    for i in range (1, a+1):
        fact = fact * i
    return fact

print(f'{factorial(num1)/factorial(num2):.2f}')

