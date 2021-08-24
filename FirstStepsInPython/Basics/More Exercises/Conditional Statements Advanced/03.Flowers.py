hrizantemi = int(input())
rozi = int(input())
laleta = int(input())
season = str(input())
holiday = str(input())

total_flowers = hrizantemi + rozi + laleta
first_half = 0
second_half = 0
total_price_1 = 0
total_price_2 = 0

if (season == "Spring") or (season == "Summer"):
    first_half = 1
    total_price_1 = (hrizantemi * 2) + (rozi * 4.10) + (laleta * 2.50)


if (season == "Autumn") or (season == "Winter"):
    second_half = 1
    total_price_2 = (hrizantemi * 3.75) + (rozi * 4.50) + (laleta * 4.15)

if first_half and holiday == "Y":
    total_price_1 += (total_price_1 * 0.15)

if first_half and laleta > 7:
    total_price_1 -= (total_price_1 * 0.05)

if first_half and total_flowers > 20:
    total_price_1 *= 0.80

if second_half and holiday == "Y":
    total_price_2 += (total_price_2 * 0.15)

if season == "Winter" and rozi >= 10:
    total_price_2 -= (total_price_2 * 0.1)
if second_half and total_flowers > 20:
    total_price_2 *= 0.80

if first_half == 1:
    print(f"{total_price_1 + 2:.2f}")

else:
    print(f"{total_price_2 + 2:.2f}")
