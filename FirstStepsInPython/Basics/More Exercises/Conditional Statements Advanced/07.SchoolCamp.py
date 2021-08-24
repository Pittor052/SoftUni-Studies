season = str(input())
gender = str(input())
people = int(input())
time = int(input())

winter = False
spring = False
summer = False
girls = False
boys = False
mixed = False
tax = 0
sport = str()
total_price = 0
discount = 0

if season == "Winter":
    winter = True
elif season == "Spring":
    spring = True
elif season == "Summer":
    summer = True

if gender == "boys":
    boys = True
elif gender == "girls":
    girls = True
elif gender == "mixed":
    mixed = True

if people >= 50:
    discount = 0.50
elif 20 <= people < 50:
    discount = 0.85
elif 10 <= people < 20:
    discount = 0.95
else:
    discount = 1

if winter:
    if boys or girls:
        tax = 9.60
        total_price = people * tax
        if boys:
            sport = "Judo"
        if girls:
            sport = "Gymnastics"
    elif mixed:
        tax = 10
        total_price = people * tax
        sport = "Ski"

elif spring:
    if boys or girls:
        tax = 7.20
        total_price = people * tax
        if boys:
            sport = "Tennis"
        if girls:
            sport = "Athletics"
    elif mixed:
        tax = 9.50
        total_price = people * tax
        sport = "Cycling"

elif summer:
    if boys or girls:
        tax = 15
        total_price = people * tax
        if boys:
            sport = "Football"
        if girls:
            sport = "Volleyball"
    elif mixed:
        tax = 20
        total_price = people * tax
        sport = "Swimming"

print(f"{sport} {(total_price * time) * discount:.2f} lv. ")
