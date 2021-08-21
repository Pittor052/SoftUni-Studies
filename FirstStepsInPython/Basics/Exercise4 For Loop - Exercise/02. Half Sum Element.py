import sys

n = int(input())
max_n = -sys.maxsize
sum_n = 0
for i in range(1, n + 1):
    num = int(input())
    if num > max_n:
        max_n = num
    sum_n += num

sum_others = sum_n - max_n

if max_n == sum_others:
    print("Yes")
    print(f"Sum = {sum_others}")
else:
    print("No")
    print(f"Diff = {abs(max_n - sum_others)}")
