number = int(input())
for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            for m in range(1, 10):
                if (number % m == 0) and (number % k == 0) and (number % j == 0) and (number % i == 0):
                    print(f"{i}{j}{k}{m}", end=" ")
