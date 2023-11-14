cities = input().split(", ")
capitals = input().split(", ")

dict = {cities: capitals for cities,
        capitals in zip(cities,capitals)}

for i in dict:
    print(f"{i} -> {dict[i]}")