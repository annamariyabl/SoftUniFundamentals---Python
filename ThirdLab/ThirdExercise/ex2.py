factor = int(input())
count = int(input())
my_list = []
counter = 0
i=1

while counter < count:
    if i % factor == 0:
        counter += 1
        my_list.append(i)
    i+=1

print(my_list)