product = str(input())
city = str(input())
quantity = float(input())

coffee = False
water = False
beer = False
sweets = False
peanuts = False

if product == "coffee":
    coffee = True
elif product == "water":
    water = True
elif product == "beer":
    beer = True
elif product == "sweets":
    sweets = True
elif product == "peanuts":
    peanuts = True

if city == "Sofia":
    if coffee:
        print(f"{quantity * 0.5}")
    if water:
        print(f"{quantity * 0.8}")
    if beer:
        print(f"{quantity * 1.2}")
    if sweets:
        print(f"{quantity * 1.45}")
    if peanuts:
        print(f"{quantity * 1.6}")

elif city == "Plovdiv":
    if coffee:
        print(f"{quantity * 0.4}")
    if water:
        print(f"{quantity * 0.7}")
    if beer:
        print(f"{quantity * 1.15}")
    if sweets:
        print(f"{quantity * 1.30}")
    if peanuts:
        print(f"{quantity * 1.5}")

elif city == "Varna":
    if coffee:
        print(f"{quantity * 0.45}")
    if water:
        print(f"{quantity * 0.7}")
    if beer:
        print(f"{quantity * 1.10}")
    if sweets:
        print(f"{quantity * 1.35}")
    if peanuts:
        print(f"{quantity * 1.55}")
