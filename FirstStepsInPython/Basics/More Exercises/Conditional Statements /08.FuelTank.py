fuel_type = str(input())
fuel_left = int(input())

if fuel_left < 25:
    if fuel_type == "Diesel" or fuel_type == "Gasoline" or fuel_type == "Gas":
        print(f"Fill your tank with {fuel_type.lower()}!")
    else:
        print("Invalid fuel!")
elif fuel_left >= 25 and fuel_type == "Diesel" or fuel_type == "Gasoline" or fuel_type == "Gas":
    print(f"You have enough {fuel_type.lower()}.")
else:
    print("Invalid fuel!")
