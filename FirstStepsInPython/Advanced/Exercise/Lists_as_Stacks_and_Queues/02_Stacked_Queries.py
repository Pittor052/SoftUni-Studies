count = int(input())
stack = []
output = []

while not count == 0:
    command = input().split()

    if command[0] == '1':
        stack.append(int(command[1]))

    elif command[0] == '2':
        if len(stack) > 0:
            stack.pop()
        else:
            count -= 1
            continue
    elif len(stack) > 0:
        if command[0] == '3':
            output.append(max(stack))

        elif command[0] == '4':
            output.append(min(stack))

    count -= 1

print(*output, sep="\n")
result = []
for i in range(len(stack) - 1, -1, -1):
    result.append(stack[i])

print(*result, sep=", ")
# # 02 solution
# lines_num = int(input())
# stack = []
#
# while not lines_num == 0:
#     command = input().split()
#     action = int(command.pop(0))
#     if action == 1:
#         x = int(command[0])
#         stack.append(x)
#     elif action == 2 and not len(stack) == 0:
#         stack.pop()
#     elif action == 3 and not len(stack) == 0:
#         print(max(stack))
#     if action == 4 and not len(stack) == 0:
#         print(min(stack))
#     lines_num -= 1
# if not len(stack) == 0:
#     print(*(reversed(stack)), sep=", ")
# 10
# 2
# 1 47
# 1 66
# 1 32
# 4
# 3
# 1 25
# 1 16
# 1 8
# 4
