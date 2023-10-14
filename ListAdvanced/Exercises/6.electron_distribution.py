electrons = int(input())
list = []
position = 0
while electrons > 0:
    position += 1
    empty_space = 2*position**2
    if electrons >= empty_space:
        list.append(empty_space)
    else:
        list.append(electrons)
    electrons -= empty_space

print(list)