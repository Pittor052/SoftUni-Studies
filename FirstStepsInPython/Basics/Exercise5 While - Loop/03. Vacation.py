money_trip = float(input())
current_money = float(input())
days = 0
spend = 0
go_on_trip = False

while not go_on_trip:
    action = input()
    money = float(input())
    days += 1
    if action == "spend":
        spend += 1
        current_money -= money
        if current_money < 0:
            current_money = 0
    if action == "save":
        spend = 0
        current_money += money
    if spend == 5:
        break
    if current_money >= money_trip:
        go_on_trip = True
        break

if go_on_trip:
    print(f"You saved the money for {days} days.")
else:
    print(f"You can\'t save the money.")
    print(days)
