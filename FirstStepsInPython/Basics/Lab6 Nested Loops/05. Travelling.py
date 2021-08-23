destination = input()
budget = float(input())
new_income = 0.0
go = False
print()
while destination != "End":
    income = input()
    try:
        new_income += float(income)
        if new_income >= budget:
            go = True
            if go:
                print(f"Going to {destination}!")
                new_income = 0.0
    except:
        destination = str(income)
        if destination != "End":
            go = False
            income = input()
            budget = float(income)
        else:
            break
