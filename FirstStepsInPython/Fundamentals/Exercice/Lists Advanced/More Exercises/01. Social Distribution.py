population_wealth = list(map(lambda x: int(x), input().split(", ")))
min_wealth_line = int(input())
for wealth in population_wealth:
    if wealth < min_wealth_line:
        add = min_wealth_line - wealth
        population_wealth[population_wealth.index(max(population_wealth))] -= add
        population_wealth[population_wealth.index(wealth)] += add
for border in population_wealth:
    if border < min_wealth_line:
        print("No equal distribution possible")
        break
else:
    print(population_wealth)

# 2, 3, 5, 15, 75
# 5
