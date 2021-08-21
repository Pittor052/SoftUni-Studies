n = int(input())
count1 = 0
p1 = 0
count2 = 0
p2 = 0
count3 = 0
p3 = 0
count4 = 0
p4 = 0
count5 = 0
p5 = 0

for i in range(1, n + 1):
    num = int(input())
    if num < 200:
        count1 += 1
        p1 = (count1 / n) * 100
    elif 200 <= num <= 399:
        count2 += 1
        p2 = (count2 / n) * 100
    elif 400 <= num <= 599:
        count3 += 1
        p3 = (count3 / n) * 100
    elif 600 <= num <= 799:
        count4 += 1
        p4 = (count4 / n) * 100
    elif num >= 800:
        count5 += 1
        p5 = (count5 / n) * 100

print(f"{p1:.2f}%")
print(f"{p2:.2f}%")
print(f"{p3:.2f}%")
print(f"{p4:.2f}%")
print(f"{p5:.2f}%")
