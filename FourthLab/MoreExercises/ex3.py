import math

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())
x4 = float(input())
y4 = float(input())


def line (a, b, c, d):
    import math
    if (a >= 0 and c >= 0) or (a<0 and c<0):
        ac = abs(a-c)
    elif (a<0 and c >0) or (a>0 and c<0):
        ac = abs(a)+abs(c)
    if (b >= 0 and d >= 0) or (b<0 and d<0):
        bd = abs(b-d)
    elif (b<0 and d >0) or (b>0 and d<0):
        bd = abs(b)+abs(d)
    line = math.sqrt(ac**2+bd**2)
    return line

def line_closer (a, b):
    import math
    c = math.sqrt(a**2 + b**2)
    return c

if line(x1,y1, x2,y2)>=line(x3,y3,x4,y4):
    if line_closer(x1, y1) <= line_closer(x2, y2):
        print(f'({math.floor(x1)}, {math.floor(y1)})({math.floor(x2)}, {math.floor(y2)})')
    else:
        print(f'({math.floor(x2)}, {math.floor(y2)})({math.floor(x1)}, {math.floor(y1)})')
else:
    if line_closer(x3, y3) <= line_closer(x4, y4):
        print(f'({math.floor(x3)}, {math.floor(y3)})({math.floor(x4)}, {math.floor(y4)})')
    else:
        print(f'({math.floor(x4)}, {math.floor(y4)})({math.floor(x3)}, {math.floor(y3)})')