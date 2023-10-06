numbers = list(map(int, input().split()))

def is_even(a):
    return a % 2 == 0

even_list = list(filter(is_even, numbers))

print(even_list)



