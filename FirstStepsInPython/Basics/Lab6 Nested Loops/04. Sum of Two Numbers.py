start = int(input())
stop = int(input())
magic_num = int(input())
counter = 0
pas = False
for i in range(start, stop + 1):
    for j in range(start, stop + 1):
        counter += 1
        if (i + j) == magic_num:
            print(f"Combination N:{counter} ({i} + {j} = {magic_num})")
            pas = True
            break
    if pas:
        break

if not pas:
    print(f"{counter} combinations - neither equals {magic_num}")
