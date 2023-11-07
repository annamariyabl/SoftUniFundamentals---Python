elements = input().split()
bakery = {}

for i in range (0, len(elements), 2):
    key = elements[i]
    value = elements[i+1]
    bakery[key] = int(value)

search_products = input().split()

for i in search_products:
    if i in bakery:
        print(f"We have {bakery[i]} of {i} left")
    else:
        print(f"Sorry, we don't have {i}")