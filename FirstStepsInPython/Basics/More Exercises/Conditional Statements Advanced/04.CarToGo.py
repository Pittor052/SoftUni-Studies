budget = float(input())
season = str(input())
summer = False
car_type = str()
budget_type = str()

if season == "Summer":
    summer = True

if budget <= 100:
    budget_type = "Economy class"
    if summer:
        car_type = "Cabrio"
        print(budget_type)
        print(f"{car_type} - {budget * 0.35:.2f}")
    else:
        car_type = "Jeep"
        print(budget_type)
        print(f"{car_type} - {budget * 0.65:.2f}")
if 100 < budget <= 500:
    budget_type = "Compact class"
    if summer:
        car_type = "Cabrio"
        print(budget_type)
        print(f"{car_type} - {budget * 0.45:.2f}")
    else:
        car_type = "Jeep"
        print(budget_type)
        print(f"{car_type} - {budget * 0.80:.2f}")
if budget > 500:
    budget_type = "Luxury class"
    car_type = "Jeep"
    print(budget_type)
    print(f"{car_type} - {budget * 0.90:.2f}")


