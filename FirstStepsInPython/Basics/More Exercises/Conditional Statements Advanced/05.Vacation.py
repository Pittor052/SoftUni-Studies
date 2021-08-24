budget = float(input())
season = str(input())
summer = False
a = "Alaska"
m = "Morocco"
c = "Camp"
h = "Hut"
ho = "Hotel"
if season == "Summer":
    summer = True

if budget <= 1000:
    if summer:
        print(f"{a} - {c} - {budget * 0.65:.2f}")
    else:
        print(f"{m} - {c} - {budget * 0.45:.2f}")
if 1000 < budget <= 3000:
    if summer:
        print(f"{a} - {h} - {budget * 0.80:.2f}")
    else:
        print(f"{m} - {h} - {budget * 0.60:.2f}")
if budget > 3000:
    if summer:
        print(f"{a} - {ho} - {budget * 0.90:.2f}")
    else:
        print(f"{m} - {ho} - {budget * 0.90:.2f}")