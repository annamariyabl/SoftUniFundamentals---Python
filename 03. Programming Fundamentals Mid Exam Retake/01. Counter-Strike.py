energy = int(input())
counter = 0

while energy >= 0:
    distance = input()
    if distance == 'End of battle':
        print(f'Won battles: {counter}. Energy left: {energy}')
        break
    else:
        distance = int(distance)
        if energy >= distance:
            counter+=1
            energy -= distance
            if counter % 3 == 0:
                energy+=counter
        else:
            print(f"Not enough energy! Game ends with {counter} won battles and {energy} energy")
            break