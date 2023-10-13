my_list = input()
my_list = [x for x in my_list if x not in 'a i o u e A I O U E']
print(*my_list, sep='')