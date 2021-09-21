# # 01 solution
# num_names = int(input())
# unique_names = []
# [unique_names.append(input()) for _ in range(num_names)]
# print(*set(unique_names), sep='\n')
# # 02 solution
# num_names = int(input())
# unique_names = []
# while num_names > 0:
#     name = input()
#
#     if name not in unique_names:
#         unique_names.append(name)
#
#     num_names -= 1
# print(*unique_names, sep='\n')
# # 03 solution
from collections import deque

num_names = int(input())
names = deque(input() for _ in range(num_names))

while names:
    name = names.pop()
    if name not in names:
        print(name)
