def check_please(command, quantity):
    if command == "coffee":
        return quantity * 1.50
    elif command == "water":
        return quantity
    elif command == "coke":
        return quantity * 1.40
    elif command == "snacks":
        return quantity * 2.00


print(f"{check_please(input(), float(input())):.2f}")
