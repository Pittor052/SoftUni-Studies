# # Write a program that receives two numbers (factor and count) and creates a list with length of the given count and
# # contains only integer numbers that are multiples of the given factor. The numbers should be only positive, and they
# # should be arranged in ascending order, starting from the smallest multiple number.
# # 01 solution
# factor = int(input())
# count = int(input())
# x = 1
# result = []
# while len(result) < count:
#     if x % factor == 0:
#         result.append(x)
#         x += 1
#     else:
#         x += 1
# print(result)
# # 02 solution ?
# INPUT 1
# 2
# 5
# INPUT 2
# 1
# 10
# INPUT END
