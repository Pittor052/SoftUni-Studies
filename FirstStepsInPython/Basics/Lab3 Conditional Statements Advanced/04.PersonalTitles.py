age = float(input())
sex = str(input())

if age < 16:
    if sex == "m":
        print("Master")
    else:
        print("Miss")
elif age >= 16:
    if sex == "m":
        print("Mr.")
    else:
        print("Ms.")