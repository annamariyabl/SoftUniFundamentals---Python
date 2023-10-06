numbers = list(map(int, input().split(', ')))

def reverse (a):
    b = str(a)[::-1]
    b = int(b)
    return a == b

for i in numbers:
    print(reverse(i))
