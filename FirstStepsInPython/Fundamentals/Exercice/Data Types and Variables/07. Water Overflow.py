fill = int(input())
capacity = 255
pour = 0
for litres in range(fill):
    command = int(input())
    pour += command
    if pour > capacity:
        print()
        print("Insufficient capacity!")
        pour -= command
        continue
print(pour)
