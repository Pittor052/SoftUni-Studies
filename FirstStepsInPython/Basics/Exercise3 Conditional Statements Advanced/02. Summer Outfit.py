degrees = int(input())
part_of_day = str(input())

morning = False
afternoon = False
evening = False

if part_of_day == "Morning":
    morning = True
elif part_of_day == "Afternoon":
    afternoon = True
elif part_of_day == "Evening":
    evening = True

cold = False
warm = False
hot = False

if 10 <= degrees <= 18:
    cold = True
elif 18 < degrees <= 24:
    warm = True
elif degrees >= 25:
    hot = True

outfit = str()
shoes = str()

if cold:
    if morning:
        outfit = "Sweatshirt"
        shoes = "Sneakers"
    elif afternoon:
        outfit = "Shirt"
        shoes = "Moccasins"
    elif evening:
        outfit = "Shirt"
        shoes = "Moccasins"

elif warm:
    if morning:
        outfit = "Shirt"
        shoes = "Moccasins"
    elif afternoon:
        outfit = "T-Shirt"
        shoes = "Sandals"
    elif evening:
        outfit = "Shirt"
        shoes = "Moccasins"
elif hot:
    if morning:
        outfit = "T-Shirt"
        shoes = "Sandals"
    elif afternoon:
        outfit = "Swim Suit"
        shoes = "Barefoot"
    elif evening:
        outfit = "Shirt"
        shoes = "Moccasins"

print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")
