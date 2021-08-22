# Производителите на вендинг машини искали да направят машините си да връщат възможно най-малко
# монети ресто. Напишете програма, която приема сума - рестото, което трябва да се върне и изчислява с
# колко най-малко монети може да стане това.
change = float(input())
coins = [2.0, 1.0, 0.50, 0.20, 0.10, 0.05, 0.02, 0.01]
biggest = 0.0
coins_returned = 0
while change > 0:
    for i in range(len(coins)):
        if coins[i] <= change:
            biggest = coins[i]
            # print(f"biggest {biggest}")
            coins_returned += 1
            change = round((change - biggest), 2)
            # print(f"coins returned {coins_returned}")
            # print(f"change {change}")
            break

print(coins_returned)
