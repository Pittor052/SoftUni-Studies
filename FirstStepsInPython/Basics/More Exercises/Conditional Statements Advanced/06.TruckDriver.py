season = str(input())
km_month = float(input())

summer = False
winter = False
spring_autumn = False
small = False
average = False
huge = False

if (season == "Spring") or (season == "Autumn"):
    spring_autumn = True
if season == "Summer":
    summer = True
if season == "Winter":
    winter = True
if km_month <= 5000:
    small = True
if 5000 < km_month <= 10000:
    average = True
if 10000 < km_month <= 20000:
    huge = True

if spring_autumn:
    if small:
        print(f"{((km_month * 0.75) * 4) * 0.90:.2f}")
    if average:
        print(f"{((km_month * 0.95) * 4) * 0.90:.2f}")
    if huge:
        print(f"{((km_month * 1.45) * 4) * 0.90:.2f}")

if summer:
    if small:
        print(f"{((km_month * 0.90) * 4) * 0.90:.2f}")
    if average:
        print(f"{((km_month * 1.10) * 4) * 0.90:.2f}")
    if huge:
        print(f"{((km_month * 1.45) * 4) * 0.90:.2f}")

if winter:
    if small:
        print(f"{((km_month * 1.05) * 4) * 0.90:.2f}")
    if average:
        print(f"{((km_month * 1.25) * 4) * 0.90:.2f}")
    if huge:
        print(f"{((km_month * 1.45) * 4) * 0.90:.2f}")
