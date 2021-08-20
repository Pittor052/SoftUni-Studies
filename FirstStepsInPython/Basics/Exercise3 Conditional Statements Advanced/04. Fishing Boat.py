budget = int(input())
season = str(input())
fisherman = int(input())

boat = 0
cost = 0
discount = 0
money_left = 0

if fisherman <= 6:
    discount = 0.9
elif 6 < fisherman <= 11:
    discount = 0.85
elif fisherman >= 12:
    discount = 0.75

if season == "Spring":
    boat = 3000
    if fisherman % 2 == 0:
        cost = (boat * discount) * 0.95
        money_left = budget - cost
    else:
        cost = boat * discount
        money_left = budget - cost

elif (season == "Summer") or (season == "Autumn"):
    boat = 4200
    if season == "Summer":
        if fisherman % 2 == 0:
            cost = (boat * discount) * 0.95
            money_left = budget - cost
        else:
            cost = boat * discount
            money_left = budget - cost
    else:
        cost = boat * discount
        money_left = budget - cost

elif season == "Winter":
    boat = 2600
    if fisherman % 2 == 0:
        cost = (boat * discount) * 0.95
        money_left = budget - cost
    else:
        cost = boat * discount
        money_left = budget - cost

if money_left >= 0:
    print(f"Yes! You have {money_left:.2f} leva left.")
else:
    print(f"Not enough money! You need {money_left * -1:.2f} leva.")
