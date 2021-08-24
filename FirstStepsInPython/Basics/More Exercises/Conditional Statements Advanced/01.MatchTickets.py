budget = float(input())
category = str(input())
people = int(input())
vip_tickets = people * 499.99
normal_tickets = people * 249.99

if category == "VIP":

    if people <= 4:

        budget -= (budget * 0.75)

    elif 5 <= people <= 9:

        budget -= (budget * 0.6)

    elif 10 <= people <= 24:

        budget -= (budget * 0.5)

    elif 25 <= people <= 49:

        budget -= (budget * 0.4)

    elif people >= 50:

        budget -= (budget * 0.25)
#
# new_budget = budget - vip_tickets
#
# if new_budget >= budget:
#     print(f"Yes! You have {new_budget - normal_tickets:.2f} leva left.")
#
# else:
#     print(f"Not enough money! You need {normal_tickets - new_budget:.2f} leva.")

if category == "Normal":

    if people <= 4:

        budget -= (budget * 0.75)

    elif 5 <= people <= 9:

        budget -= (budget * 0.6)

    elif 10 <= people <= 24:

        budget -= (budget * 0.5)

    elif 25 <= people <= 49:

        budget -= (budget * 0.4)

        if budget >= normal_tickets:
            print(f"Yes! You have {budget - normal_tickets:.2f} leva left.")

        else:
            print(f"Not enough money! You need {normal_tickets - budget:.2f} leva.")

    elif people >= 50:

        budget -= (budget * 0.25)

new_budget = budget - normal_tickets
print(normal_tickets)
if new_budget >= budget:
    print(f"Yes! You have {new_budget - normal_tickets:.2f} leva left.")

else:
    print(f"Not enough money! You need {normal_tickets - new_budget:.2f} leva.")