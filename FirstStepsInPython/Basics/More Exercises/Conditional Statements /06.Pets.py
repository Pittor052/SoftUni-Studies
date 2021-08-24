from math import floor, ceil

days = int(input())
food = int(input())
dog_food_kg = days * float(input())
cat_food_kg = days * float(input())
turtle_food_kg = (days * float(input())) / 1000

total_food = dog_food_kg + cat_food_kg + turtle_food_kg

if total_food <= food:
    print(f"{floor(food - total_food)} kilos of food left.")
else:
    print(f"{ceil(total_food - food)} more kilos of food are needed.")


