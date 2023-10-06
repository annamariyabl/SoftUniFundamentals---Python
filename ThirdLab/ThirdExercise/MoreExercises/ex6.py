my_list = input().split()
command = input()
new_list = []
final_list = my_list
while command != 'end':
    if 'exchange' in command:
        index = command.split()
        index = int(index[1])
        if index < 0 or index >= (len(my_list)):
            print('Invalid index')
        else:
            my_list = my_list[index + 1:] + my_list[:index + 1]
    elif 'max' in command:
        bul_odd = False
        bul_even = False
        max = int(my_list[0])
        max_index=0
        if max % 2 != 0:
            bul_odd = True
        else:
            bul_even = True
        if 'odd' in command:
            for i in range (1,len(my_list)):
                item = int(my_list[i])
                if item % 2 != 0:
                    if item>=max:
                        max = item
                        max_index = i
                        bul_odd = True
            if bul_odd:
                print(max_index)
            else:
                print('No matches')

        elif 'even' in command:
            for i in range(1, len(my_list)):
                item = int(my_list[i])
                if item % 2 == 0:
                    if item >= max:
                        max = item
                        max_index = i
                        bul_even = True
            if bul_even:
                print(max_index)
            else:
                print('No matches')
    elif 'min' in command:
        bul_odd = False
        bul_even = False
        min = int(my_list[0])
        min_index = 0
        if min % 2 != 0:
            bul_odd = True
        else:
            bul_even = True
        if 'odd' in command:
            for i in range (1,len(my_list)-1):
                item = int(my_list[i])
                if item % 2 != 0:
                    if item<=min:
                        min = item
                        min_index = i
                        bul_odd = True
            if bul_odd:
                print(min_index)
            else:
                print('No matches')

        elif 'even' in command:
            for i in range(1, len(my_list)-1):
                item = int(my_list[i])
                if item % 2 == 0:
                    if item <= min:
                        min = item
                        min_index = i
                        bul_even = True
            if bul_even:
                print(min_index)
            else:
                print('No matches')
    elif 'first' in command:
        index = command.split()
        index = int(index[1])
        if index > len(my_list):
            print('Invalid count')

        elif 'even' in command:
            for i in range (len(my_list)):
                if int(my_list[i]) % 2 == 0:
                    new_list.append(my_list[i])
                    if len(new_list) == index:
                        break
            new_list = [eval(i) for i in new_list]
            print(new_list)
            new_list = []
        elif 'odd' in command:
            for i in range (len(my_list)):
                if int(my_list[i]) % 2 != 0:
                    new_list.append(my_list[i])
                    if len(new_list) == index:
                        break
            new_list = [eval(i) for i in new_list]
            print(new_list)
            new_list = []
    elif 'last' in command:
        index = command.split()
        index = int(index[1])
        if index > len(my_list):
            print('Invalid count')

        elif 'even' in command:
            for i in range (len(my_list)-1, -1, -1):
                if int(my_list[i]) % 2 == 0:
                    new_list.append(my_list[i])
                    if len(new_list) == index:
                        break
            new_list = [eval(i) for i in new_list]
            print(new_list)
            new_list = []
        elif 'odd' in command:
            for i in range (len(my_list)-1, -1, -1):
                if int(my_list[i]) % 2 != 0:
                    new_list.append(my_list[i])
                    if len(new_list) == index:
                        break
            new_list = [eval(i) for i in new_list]
            print(new_list)
            new_list=[]

    command = input()
final_list = [eval(i) for i in final_list]
print(final_list)

