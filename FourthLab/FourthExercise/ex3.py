a = input()
b = input()

def recurtion (a, b):
    number = ord(a)
    result = chr(number+1)
    print(result, end = " ")
    if number < ord(b)-2:
        a = chr(number+1)
        recurtion(a, b)

recurtion(a,b)
