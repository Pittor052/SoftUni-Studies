# # 01 solution
# stack = input().split()
#
# for i in range(len(stack) - 1, -1, -1):
#     print(stack[i], end=' ')

# # 02 solution
# stack = input().split()
#
# print(*list(reversed(stack)), sep=' ', end='')

# # 03 solution
stack = list(map(lambda x: int(x), input().split()))
while stack:
    print(stack.pop(), end=" ")

# # 04 solution example
# text = input().split()
# stack = []
#
# for i in range(len(text)):
#     stack.append(text.pop())
#
# print(" ".join(stack))
