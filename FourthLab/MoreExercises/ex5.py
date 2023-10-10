num1 = int(input())
num2 = int(input())
num3 = int(input())

def is_positive(a, b, c):
    if a == 0 or b == 0 or c == 0:
        result = 'zero'
        return result
    elif a > 0 and b > 0 and c > 0:
        result = 'positive'
        return result
    elif a > 0 and b > 0 and c < 0:
        result = 'negative'
        return result
    elif a > 0 and b < 0 and c > 0:
        result = 'negative'
        return result
    elif a < 0 and b > 0 and c > 0:
        result = 'negative'
        return result
    elif a < 0 and b < 0 and c > 0:
        result = 'positive'
        return result
    elif a < 0 and b > 0 and c < 0:
        result = 'positive'
        return result
    elif a > 0 and b < 0 and c < 0:
        result = 'positive'
        return result
    elif a < 0 and b < 0 and c < 0:
        result = 'negative'
        return result

print(is_positive(num1,num2,num3))