"""
2
1, 2, 3
4, 5, 6
"""
# # 01 solution
# matrix = []
#
# for x in range(int(input())):
#     line = []
#     for num in (map(int,input().split(', '))):
#         if num % 2 == 0:
#             line.append(num)
#     matrix.append(line)
# print(matrix)

# # 02 solution
n = int(input())
print([[num for num in (map(int, input().split(', '))) if num % 2 == 0] for x in range(n)])
