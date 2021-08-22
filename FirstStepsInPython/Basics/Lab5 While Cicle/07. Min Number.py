import sys

n = input()
smallest = sys.maxsize
while n != "Stop":
    s = int(n)

    if s < smallest:
        smallest = s
    n = input()

print(smallest)
