start = int(input())
stop = int(input())
first_letter = 0
second_letter = 0
for i in range(1, start + 1):
    for j in range(1, start + 1):
        for k in range(stop):
            for m in range(stop):
                for n in range(start + 1):
                    if n > i and n > j:
                        first_letter += 97 + k
                        second_letter += 97 + m
                        if i < start:
                            print(f"{i}{j}{chr(first_letter)}{chr(second_letter)}{n}", end=" ")
                            first_letter = 0
                            second_letter = 0
