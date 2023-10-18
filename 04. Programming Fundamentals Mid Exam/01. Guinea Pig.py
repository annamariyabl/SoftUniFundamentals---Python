food = float(input())
hay = float(input())
cover = float(input())
weight = float(input())

for i in range(1, 31):
    food = food - 0.3
    food = round(food,2)
    if food <= 0:
        print("Merry must go to the pet store!")
        break
    if i % 2 == 0:
        hay -= food*0.05
        if hay <= 0:
            print("Merry must go to the pet store!")
            break
        if i % 3 == 0:
            cover -= 1/3*weight
            if cover <= 0:
                print("Merry must go to the pet store!")
                break
    elif i % 3 == 0:
            cover -= weight/3
            if cover <= 0:
                print("Merry must go to the pet store!")
                break
else:
    print(f'Everything is fine! Puppy is happy! Food: {food:.2f}, Hay: {hay:.2f}, Cover: {cover:.2f}.')