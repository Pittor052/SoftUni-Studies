import sys

n = int(input())
odd_sum = float()
odd_min = sys.maxsize
odd_max = -sys.maxsize
even_sum = float()
even_min = sys.maxsize
even_max = -sys.maxsize

for i in range(1, n + 1):
    num = float(input())
    if i % 2 == 0:
        even_sum += num

        if num < even_min:
            even_min = num

        if num > even_max:
            even_max = num

    if i % 2 == 1:
        odd_sum += num

        if num < odd_min:
            odd_min = num

        if num > odd_max:
            odd_max = num

print(f"OddSum={float(odd_sum):.2f},")
if odd_min == sys.maxsize:
    print("OddMin=No,")
else:
    print(f"OddMin={float(odd_min):.2f},")
if odd_max == -sys.maxsize:
    print("OddMax=No,")
else:
    print(f"OddMax={float(odd_max):.2f},")
print(f"EvenSum={float(even_sum):.2f},")
if even_min == sys.maxsize:
    print("EvenMin=No,")
else:
    print(f"EvenMin={float(even_min):.2f},")
if even_max == -sys.maxsize:
    print("EvenMax=No")
else:
    print(f"EvenMax={float(even_max):.2f}")
