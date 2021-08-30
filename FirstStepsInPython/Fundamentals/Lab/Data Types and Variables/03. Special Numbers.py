num = int(input())
for i in range(1, num +1):
    result = 0
    digit = i
    while digit > 0:
        result += digit % 10
        digit = int(digit / 10)
    if (result == 5) or (result == 7) or (result == 11):
        print(f"{i} -> True")
    else:
        print(f"{i} -> False")
