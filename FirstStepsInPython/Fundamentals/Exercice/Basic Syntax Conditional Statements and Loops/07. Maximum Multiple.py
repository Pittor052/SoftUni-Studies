start = int(input())
stop = int(input())
maximum_multiple = 0
while True:
    for i in range(stop):
        if start * i <= stop and not start * i == 0:
            maximum_multiple = start * i
    print(maximum_multiple)
    break
