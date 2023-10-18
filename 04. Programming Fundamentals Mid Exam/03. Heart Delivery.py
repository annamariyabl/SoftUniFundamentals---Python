neighborhood = list(map(int, input().split('@')))
jump_command = input()
new_index = 0
while jump_command != 'Love!':
    jump_command = jump_command.split()
    index = int(jump_command[1])
    new_index = new_index + index
    if new_index >= len(neighborhood):
        new_index = 0
        if neighborhood[new_index] == 0:
            print(f"Place {new_index} already had Valentine's day.")
        else:
            neighborhood[new_index] -= 2
            if neighborhood[new_index] <= 0:
                neighborhood[new_index] = 0
                print(f"Place {new_index} has Valentine's day.")
    else:
        if neighborhood[new_index] == 0:
            print(f"Place {new_index} already had Valentine's day.")
        else:
            neighborhood[new_index] -= 2
            if neighborhood[new_index] <= 0:
                neighborhood[new_index] = 0
                print(f"Place {new_index} has Valentine's day.")
    jump_command = input()

print(f"Cupid's last position was {new_index}.")
house_count = 0
for i in neighborhood:
    if not i == 0:
        house_count += 1

if house_count == 0:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {house_count} places.")








