# # 01 solution
# stack = input()
# 
# for i in range(len(stack) - 1, -1, -1):
#     print(stack[i], end='')
#
# # 02 solution
# stack = input().split()
#
# while stack:
#     print(*list(reversed(stack.pop())), sep='', end=' ')
#
# # 03 solution example
text = list(input())
stack = []

for i in range(len(text)):
    stack.append(text.pop())

print("".join(stack))
