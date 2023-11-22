str1, str2 = input().split()
total_sum = 0
for i in range(len(str1)):
    if i < len(str2):
        total_sum += (ord(str1[i])*ord(str2[i]))
    else:
        total_sum += ord(str1[i])

if len(str1) < len(str2):
    for i in range(len(str1), len(str2)):
        total_sum += ord(str2[i])

print(total_sum)
