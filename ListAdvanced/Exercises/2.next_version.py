version = input().split('.')
version = [int(i) for i in version]
if version[2] < 9:
    version[2]+=1
else:
    version[2] = 0
    if version[1] < 9:
        version[1]+=1
    else:
        version[1]=0
        version[0]+=1

print(*version, sep='.')