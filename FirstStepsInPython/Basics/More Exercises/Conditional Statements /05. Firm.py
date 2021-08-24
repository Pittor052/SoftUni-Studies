import math

hours_needed = int(input())
days_available = int(input())
workers_overtime = int(input())
# every worker can work only 2 hours a day overtime
overtime = 2 * workers_overtime * days_available
#                                              time for training
total_hours_available = (((days_available - (days_available * 0.1)) * 8) + overtime)

if total_hours_available >= hours_needed:
    print(f"Yes!{math.floor(total_hours_available) - hours_needed} hours left.")
else:
    print(f"Not enough time!{hours_needed - math.floor(total_hours_available)} hours needed.")
print(hours_needed)