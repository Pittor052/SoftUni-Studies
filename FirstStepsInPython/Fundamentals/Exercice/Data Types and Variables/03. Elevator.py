# solution thanks to Nikola Aleksandrov
people = int(input())
capacity = int(input())
trips = people // capacity
people -= trips * capacity
if 0 < people <= capacity:
    trips += 1
print(trips)

