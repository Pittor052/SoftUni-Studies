month = str(input())
days = int(input())

studio_discount = 1
apartment_discount = 1

if 7 < days <= 14:
    studio_discount = 0.95
if days > 14:
    apartment_discount = 0.90
    if (month == "May") or (month == "October"):
        studio_discount = 0.70
    elif (month == "June") or (month == "September"):
        studio_discount = 0.80

if (month == "May") or (month == "October"):
    print(f"Apartment: {days * (65 * apartment_discount):.2f} lv.")
    print(f"Studio: {days * (50 * studio_discount):.2f} lv.")

if (month == "June") or (month == "September"):
    print(f"Apartment: {days * (68.70 * apartment_discount):.2f} lv.")
    print(f"Studio: {days * (75.20 * studio_discount):.2f} lv.")

if (month == "July") or (month == "August"):
    print(f"Apartment: {days * (77 * apartment_discount):.2f} lv.")
    print(f"Studio: {days * (76 * studio_discount):.2f} lv.")
