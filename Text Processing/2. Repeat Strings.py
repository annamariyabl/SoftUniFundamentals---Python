strings = input().split()
result = ""
for i in strings:
    result+=i*len(i)
print(result)