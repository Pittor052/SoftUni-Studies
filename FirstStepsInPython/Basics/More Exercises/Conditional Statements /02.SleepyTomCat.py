import math

vacation = int(input())

vacation_petting = vacation * 127
workdays_petting = (365 - vacation) * 63

petting_time = vacation_petting + workdays_petting
over_petting = petting_time - 30000
if petting_time > 30000:
    print("Tom will run away")
    print(f"{math.floor(over_petting / 60)} hours and {over_petting % 60} minutes more for play")
else:
    petting_time = (30000 - (vacation_petting + workdays_petting))
    print(f"Tom sleeps well")
    print(f"{math.floor(petting_time / 60)} hours and {petting_time % 60} minutes less for play")
