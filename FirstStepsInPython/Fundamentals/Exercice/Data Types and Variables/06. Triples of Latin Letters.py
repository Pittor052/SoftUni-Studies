# from itertools import product
# # # 01 solution using itertools.product(*iterables, repeat=)
# # # https://docs.python.org/3/library/itertools.html#itertools.product
# num = int(input())
# result = []
# keywords = ""
# for number in range(97, 97 + num):
#     result += chr(number)
# keywords = ["".join(i) for i in product(result, repeat=3)]
# for i in list(keywords):
#     print(i)
# # 02 solution
num = int(input())
for i in range(0, num):
    for j in range(0, num):
        for k in range(0, num):
            print(f"{chr(97+i)}{chr(97+j)}{chr(97+k)}")
