population = list(map(int, input().split(', ') ))
minimum_wealth = int(input())
max_wealth = max(population)
index_max = population.index(max_wealth)
for i in range(len(population)):
    if population[i] < minimum_wealth:
        diff = minimum_wealth - population[i]
        population[i] = minimum_wealth
        population[index_max] = max_wealth - diff
        if population[index_max] < minimum_wealth:
            print("No equal distribution possible")
            break
        else:
            max_wealth = max(population)
            index_max = population.index(max_wealth)
else:
    print(population)
