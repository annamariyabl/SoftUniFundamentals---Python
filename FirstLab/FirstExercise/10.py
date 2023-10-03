str1 = input()
str2 = input()
a = str()
for i in range (len(str2)):
    if str1[i] == str2[i]:
        continue
    else: a = str2[0:i+1]+str1[i+1:len(str2)]
    print(a)
