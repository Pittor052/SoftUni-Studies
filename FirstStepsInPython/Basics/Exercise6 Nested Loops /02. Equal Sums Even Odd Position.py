start = int(input())
stop = int(input())

for i in range(start, stop + 1):
    num_str = str(i)
    even = 0
    odd = 0
    for j, v in enumerate(num_str):
        if j % 2 == 0:
            even += int(v)
        else:
            odd += int(v)

    if even == odd:
        print(i, end=" ")
