targets = list(map(int, input().split()))
index = input()
counter = 0
while index != 'End':
    index = int(index)
    if 0 <= index < len(targets):
        if targets[index] != -1:
            counter+=1
            value = targets[index]
            targets[index] = -1
            for i in range(len(targets)):
                if targets[i] != -1:
                    if targets[i] > value:
                        targets[i] -= value
                    else:
                        targets[i] += value
    index = input()

print(f'Shot targets: {counter} -> ', end = '')
print(*targets, sep= " ")
