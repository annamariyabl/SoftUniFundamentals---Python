number = int(input())
cars = {}
for i in range (number):
    car, mileage, flue = input().split('|')
    cars[car] = []
    cars[car].append(int(mileage))
    cars[car].append(int(flue))

command = input()
while command != 'Stop':
    command = command.split(" : ")
    if 'Drive' in command:
        car = command[1]
        distance = int(command[2])
        flue = int(command[3])
        if flue > cars[car][1]:
            print("Not enough fuel to make that ride")
        else:
            cars[car][0]+=distance
            cars[car][1]-=flue
            print(f"{car} driven for {distance} kilometers. {flue} liters of fuel consumed.")
            if cars[car][0] >= 100000:
                cars.pop(car)
                print(f"Time to sell the {car}!")
    elif 'Refuel' in command:
        car = command[1]
        flue = int(command[2])
        if cars[car][1]+flue <=75:
            cars[car][1]+=flue
            print(f"{car} refueled with {flue} liters")
        else:
            refuel = 75 - cars[car][1]
            cars[car][1] = 75
            print(f"{car} refueled with {refuel} liters")
    elif 'Revert' in command:
        car = command[1]
        kilometers = int(command[2])
        if cars[car][0] - kilometers <= 10000:
            decrease = cars[car][0] - 10000
            cars[car][0] = 10000
        else:
            cars[car][0] -= kilometers
            print(f"{car} mileage decreased by {kilometers} kilometers")
    command = input()

for car in cars:
    print(f"{car} -> Mileage: {cars[car][0]} kms, Fuel in the tank: {cars[car][1]} lt.")

