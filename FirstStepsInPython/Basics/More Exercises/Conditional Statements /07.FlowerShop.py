import math

magnolii = int(input()) * 3.25
ziymbiyl = int(input()) * 4
rozi = int(input()) * 3.50
cactys = int(input()) * 8
gift_price = float(input())

total_price = magnolii + ziymbiyl + rozi + cactys
tax = total_price * 0.05
total_price = total_price - tax

if total_price >= gift_price:
    print(f"She is left with {math.floor(total_price - gift_price)} leva.")
else:
    print(f"She will have to borrow {math.ceil(gift_price - total_price)} leva.")
