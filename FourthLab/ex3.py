operation = input()
first_number = int(input())
second_number = int(input())

def multiply (a, b):
    result = a*b
    return result

def divide (a, b):
    result = a // b
    return result

def add (a, b):
    result = a+b
    return result

def subtract (a, b):
    result = a - b
    return result

if operation == 'multiply':
    print(multiply(first_number,second_number))
elif operation == 'divide':
    print(divide(first_number, second_number))
elif operation == 'add':
    print(add(first_number, second_number))
elif operation == 'subtract':
    print(subtract(first_number, second_number))