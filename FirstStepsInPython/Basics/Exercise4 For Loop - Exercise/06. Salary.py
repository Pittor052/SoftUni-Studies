n = int(input())
payment = int(input())
deduction = payment
if deduction > 0:
    for i in range(1, n + 1):
        site = str(input())
        if site == "Facebook":
            deduction -= 150
        elif site == "Instagram":
            deduction -= 100
        elif site == "Reddit":
            deduction -= 50

        if deduction <= 0:
            print("You have lost your salary.")
            break

if 0 < deduction <= payment:
    print(deduction)
