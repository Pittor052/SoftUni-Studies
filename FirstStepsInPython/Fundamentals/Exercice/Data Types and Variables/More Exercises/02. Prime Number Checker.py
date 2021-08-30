num = int(input())
flag = False
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            flag = True
            break
if not flag:
    print("True")
else:
    print("False")

