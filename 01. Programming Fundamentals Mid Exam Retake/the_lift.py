people = int(input())
wagons = input().split()
wagons = [eval(i) for i in wagons]

for i in range (len(wagons)):
    wagon = wagons[i]
    if wagon < 4:
        empty_space = 4 - wagon
        if people >= empty_space:
            people = people - empty_space
            wagons.pop(i)
            wagons.insert(i, 4)
        else:
            empty_space = empty_space - people
            people = 0
            empty_space = 4 - empty_space
            wagons.pop(i)
            wagons.insert(i, empty_space)
    if people == 0:
        if sum(wagons) == len(wagons)*4:
            print(*wagons)
        else:
            print('The lift has empty spots!')
            print(*wagons)
        break
else:
    print(f"There isn't enough space! {people} people in a queue!")
    print(*wagons)

