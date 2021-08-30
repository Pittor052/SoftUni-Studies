key = int(input())
lines = int(input())
some_list = []
print()
for i in range(lines):
    command = ord(input()) + key
    some_list.append(chr(command))
    print(some_list[i], end="")
