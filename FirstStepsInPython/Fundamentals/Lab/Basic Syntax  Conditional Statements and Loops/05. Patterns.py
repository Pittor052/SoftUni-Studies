n = int(input())
current = "*"
bigger = False
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(str(current), end="")
    print()
for k in range(n, 1, -1):
    for l in range(k, 1, -1):
        print(str(current), end="")
    print()
