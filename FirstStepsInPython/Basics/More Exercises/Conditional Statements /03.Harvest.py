import math

square_meters_field = int(input())
grape_square_meter = float(input())
wine_litres_needed = int(input())
workers = int(input())

grape_kg = square_meters_field * grape_square_meter
wine = (grape_kg * 0.4) / 2.5

if wine_litres_needed <= wine:
    print(f"Good harvest this year! Total wine: {math.floor(wine)} liters.")
    wine_left = wine - wine_litres_needed
    print(f"{math.ceil(wine_left)} liters left -> {math.ceil(wine_left / workers)} liters per person.")
else:
    wine_needed = wine_litres_needed - wine
    print(f"It will be a tough winter! More {math.floor(wine_needed)} liters wine needed.")
