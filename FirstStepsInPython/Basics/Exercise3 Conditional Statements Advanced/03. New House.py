flowers_type = str(input())
number_flowers = int(input())
budget = int(input())

final_price = 0

if flowers_type == "Roses":
    if number_flowers > 80:
        final_price = (number_flowers * 5) * 0.90
    else:
        final_price = number_flowers * 5
elif flowers_type == "Dahlias":
    if number_flowers > 90:
        final_price = (number_flowers * 3.8) * 0.85
    else:
        final_price = number_flowers * 3.8
elif flowers_type == "Tulips":
    if number_flowers > 80:
        final_price = (number_flowers * 2.8) * 0.85
    else:
        final_price = number_flowers * 2.8
elif flowers_type == "Narcissus":
    if number_flowers >= 120:
        final_price = number_flowers * 3
    else:
        final_price = number_flowers * 3.45
elif flowers_type == "Gladiolus":
    if number_flowers >= 80:
        final_price = number_flowers * 2.5
    else:
        final_price = number_flowers * 3

final_budget = budget - final_price

if final_budget >= 0:
    print(f"Hey, you have a great garden with {number_flowers} {flowers_type} and {final_budget:.2f} leva left.")
else:
    print(f"Not enough money, you need {final_budget * -1:.2f} leva more.")