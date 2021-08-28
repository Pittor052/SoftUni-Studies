budget = float(input())
price_flour = float(input())
price_eggs = price_flour * 0.75
price_milk = (price_flour * 1.25) / 4
price_easter_bread = price_flour + price_eggs + price_milk
easter_bread = 0
eggs = 0
while budget > price_easter_bread:
    budget -= price_easter_bread
    easter_bread += 1
    eggs += 3
    if easter_bread % 3 == 0:
        eggs -= easter_bread - 2
print(f"You made {easter_bread} cozonacs! Now you have {eggs} eggs and {budget:.2f}BGN left.")


