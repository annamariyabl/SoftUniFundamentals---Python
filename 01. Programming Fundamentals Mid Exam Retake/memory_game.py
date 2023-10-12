my_list = input().split()
integers = input()
moves = 0
while integers != 'end':
    moves += 1
    integers_split = integers.split()
    first = int(integers_split[0])
    second = int(integers_split[1])
    if first == second or not 0 <= second < len(my_list) or not 0 <= first < len(my_list):
        my_list.insert(len(my_list)//2, '-'+ str(moves) +'a')
        my_list.insert(len(my_list)//2, '-' + str(moves) + 'a')
        print("Invalid input! Adding additional elements to the board")
        integers = input()
        continue
    if my_list[first] == my_list[second]:
        print(f'Congrats! You have found matching elements - {my_list[first]}!')
        if first > second:
            my_list.pop(first)
            my_list.pop(second)
        else:
            my_list.pop(second)
            my_list.pop(first)
        if len(my_list) == 0:
            print(f"You have won in {moves} turns!")
            break
        integers = input()
        continue
    else:
        print("Try again!")
        integers = input()
        continue
if my_list:
    print('Sorry you lose :(')
    print(*my_list, sep=" ")
