days = int(input())
bakers = int(input())
cakes = int(input())
waffles = int(input())
pancakes = int(input())

money_cakes = cakes * 45
money_waffles = float(waffles * 5.8)
money_pancaces = float(pancakes * 3.2)

money_made = float(bakers*(money_cakes + money_waffles + money_pancaces)*days)
expenses = money_made / 8
total = money_made - expenses
print(total)
