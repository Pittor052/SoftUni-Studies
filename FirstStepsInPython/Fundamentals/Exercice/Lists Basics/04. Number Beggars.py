# # 01 solution not working properly https://judge.softuni.bg/Contests/Compete/Index/1725#3
line1 = input().split(", ")
beggars = int(input())
profit = []
search = []
equal = False
if len(line1) == beggars:
    for i in range(len(line1)):
        line1[i] = int(line1[i])
    equal = True
    print(line1)
else:
    while beggars:  # chek here for err
        beggar_sum = 0
        search = []
        for i in range(0, len(line1), beggars):
            current_element = line1[i]
            beggar_sum += int(current_element)
            search.append(current_element)
        while True:  # works properly
            found = False
            for i in range(len(line1)):
                element = line1[i]
                for j in range(len(set(search))):
                    if element == search[j]:
                        line1.remove(element)
                        found = True
                        break
                if found:
                    break
            if not found:
                break
        profit.append(beggar_sum)
        beggars -= 1
if not equal:
    print(profit)
# # 02 solution prsnr
# nums_str = input().split(', ')
# count = int(input())
# nums = []
# for num in nums_str:
#     nums.append(int(num))
#
# result_sum = [0] * count
#
# for i in range(len(nums)):
#     index = i % count
#     result_sum[index] += nums[i]
#
# print(result_sum)
# # 03 solution Rumen Grozdanov
# numbers = [int(n) for n in input().split(", ")]
# beggar = int(input())
# beggar_sums_list = []
# index = 0
#
# for iteration in range(beggar):
#     current_list = []
#
#     for index in range(0, len(numbers) + 1, beggar):
#         index += iteration
#         if index < len(numbers):
#             current_list.append(numbers[index])
#
#     beggar_sums_list.append(sum(current_list))
#
# print(beggar_sums_list)
# # INPUT 1
# 1, 2, 3, 4, 5
# 2
# # INPUT 2
# 3, 4, 5, 1, 29, 4
# 6
# # INPUT 3
# 3, 4, 5, 1, 29, 4
# 3
# # INPUT 4
# 100, 94, 24, 99
# 5
# # INPUT 5
# 100, 94, 24, 99
# 7
# # INPUT END
