juniors = int(input())
seniors = int(input())
trail = str(input())
total_trail_income = ((juniors * 5.50) + (seniors * 7)) * 0.95
total_downhill_income = ((juniors * 12.25) + (seniors * 13.75)) * 0.95
total_road_income = ((juniors * 20) + (seniors * 21.50)) * 0.95
total_cross_country_income = ((juniors * 8) + (seniors * 9.50)) * 0.95

if trail == "cross-country":
    if juniors + seniors >= 50:
        tax_junior = (juniors * 8) * 0.75
        tax_senior = (seniors * 9.50) * 0.75
        total_tax_income = (tax_junior + tax_senior) * 0.95
        print(f"{total_tax_income:.2f}")
    else:
        print(f"{total_cross_country_income:.2f}")
elif trail == "trail":
    print(f"{total_trail_income:.2f}")
elif trail == "downhill":
    print(f"{total_downhill_income:.2f}")
elif trail == "road":
    print(f"{total_road_income:.2f}")
