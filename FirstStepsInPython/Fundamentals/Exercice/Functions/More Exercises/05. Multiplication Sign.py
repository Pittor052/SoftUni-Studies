# # # 01 solution using function
# def result(input_list):
#     neg_count = 0
#     for num in input_list:
#         if num < 0:
#             neg_count += 1
#         elif num == 0:
#             return "zero"
#     if neg_count % 2 == 0:
#         return "positive"
#     else:
#         return "negative"
#
#
# list1 = [float(input()), float(input()), float(input())]
# print(result(list1))
#
# # 02 solution
list1 = [float(input()) for num in range(3)]
neg_count = [num for num in list1 if num < 0]

if [num != 0 for num in list1 if num == 0]:
    print("zero")
elif neg_count == [] or len(neg_count) % 2 == 0:
    print("positive")
else:
    print("negative")

