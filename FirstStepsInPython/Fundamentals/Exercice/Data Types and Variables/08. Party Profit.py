import math

party_size = int(input())
days = int(input())
money_spent = 0
total_money = 0
count = 0
while days > 0:
    days -= 1
    count += 1
    total_money += 50
    if count % 10 == 0:
        party_size -= 2
    if count % 15 == 0:
        party_size += 5
    if count % 3 == 0:
        money_spent += 3 * party_size
    if count % 5 == 0:
        total_money += 20 * party_size
        if count % 3 == 0:
            money_spent += 2 * party_size
    money_spent += 2 * party_size
print(f"{party_size} companions received {math.floor((total_money - money_spent) / party_size)} coins each.")
