"""
3
11 2 4
4 5 6
10 8 -12
"""
# # # 01 solution
# num_rows = int(input())
# matrix = [[int(x) for x in input().split()] for n in range(num_rows)]
# result = sum([matrix[n][n] for n in range(num_rows)])
# print(result)

# # 02 solution
num_rows = int(input())
matrix = [[int(x) for x in input().split()] for n in range(num_rows)]
result = 0
for n in range(num_rows):
    result += matrix[n][n]
print(result)