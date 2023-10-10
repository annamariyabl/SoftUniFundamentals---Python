import math

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())


def line (a, b):
    import math
    c = math.sqrt(a**2 + b**2)
    return c

if line(x1,y1)<=line(x2,y2):
    print(f'({math.floor(x1)}, {math.floor(y1)})')
else:
    print(f'({math.floor(x2)}, {math.floor(y2)})')