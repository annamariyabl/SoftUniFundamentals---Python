i = 0
number = int(input())
while i <2:
    new_number = int(input())
    if new_number > number:
        number=new_number
    i+=1

print(number)