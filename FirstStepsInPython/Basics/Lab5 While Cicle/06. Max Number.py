import sys

n = input()
biggest = -sys.maxsize
while n != "Stop":
    s = int(n)

    if s > biggest:
        biggest = s
    n = input()

print(biggest)
