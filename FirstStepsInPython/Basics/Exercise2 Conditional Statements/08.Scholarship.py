from math import floor

income = float(input())
average_grades = float(input())
min_wage = float(input())

social_scholarship = floor(min_wage * 0.35)
scholarship = floor(average_grades * 25)

if average_grades <= 4.50 or average_grades < 5.50 and income >= min_wage:
    print("You cannot get a scholarship!")
elif average_grades >= 5.50 and income >= min_wage:
    print(f"You get a scholarship for excellent results {scholarship} BGN")
elif 4.50 < average_grades < 5.50 and income <= min_wage:
    print(f"You get a Social scholarship {social_scholarship} BGN")
elif average_grades >= 5.50 and income <= min_wage:
    if social_scholarship <= scholarship:
        print(f"You get a scholarship for excellent results {scholarship} BGN")
    else:
        print(f"You get a Social scholarship {social_scholarship} BGN")
