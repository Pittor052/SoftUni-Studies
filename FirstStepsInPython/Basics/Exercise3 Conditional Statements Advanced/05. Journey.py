budget = float(input())
season = str(input())

region = str()
final_budget = 0
accommodation = str()

if budget <= 100:
    region = "Bulgaria"
    if season == "summer":
        accommodation = "Camp"
        final_budget = budget * 0.7
    else:
        accommodation = "Hotel"
        final_budget = budget * 0.30
elif 100 < budget <= 1000:
    region = "Balkans"
    if season == "summer":
        accommodation = "Camp"
        final_budget = budget * 0.6
    else:
        accommodation = "Hotel"
        final_budget = budget * 0.20
else:
    region = "Europe"
    accommodation = "Hotel"
    if season == "summer":
        final_budget = budget * 0.1
    else:
        final_budget = budget * 0.1

print(f"Somewhere in {region}")
print(f"{accommodation} - {budget - final_budget:.2f}")
