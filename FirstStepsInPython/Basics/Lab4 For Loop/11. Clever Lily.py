age = int(input())
washer = float(input())
price_toy = int(input())

money = 0
toys = 0
sum_money = 0
a = []

for i in range(1, age, 2):
    money += 10
    a.append(money)

for i in range(0, len(a)):
    sum_money = sum_money + a[i]

for i in range(1, age, 2):
    sum_money -= 1

for i in range(0, age, 2):
    toys += 1

price_toy *= toys
total_money = price_toy + sum_money

if total_money >= washer:
    left_money = total_money - washer
    print(f"Yes! {left_money:.2f}")
else:
    s = washer - total_money
    print(f"No! {s:.2f}")
