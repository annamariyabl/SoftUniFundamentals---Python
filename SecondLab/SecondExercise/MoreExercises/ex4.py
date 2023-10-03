lines = int(input())
is_it_true = True
counter1 = 0
counter2 = 0
counter3 = 0
for i in range (lines):
    a = str(input())
    if a == '(':
        counter1 +=1
        counter3 += 1
        is_it_true = False
    elif a == ')':
        counter2 += 1

    if a == ")" and is_it_true == False:
        is_it_true = True
        counter3 -= 1

if counter1 == counter2 and is_it_true == True:
    is_it_true = True
else:
    is_it_true = False
if counter1 == 0 or counter2 == 0:
    is_it_true = False

if counter3 != 0:
    is_it_true = False


if is_it_true == True:
    print('BALANCED')
else:
    print('UNBALANCED')


