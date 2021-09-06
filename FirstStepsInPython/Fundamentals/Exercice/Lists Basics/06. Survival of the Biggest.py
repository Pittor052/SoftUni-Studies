# # 01 solution
line_nums = input().split()
remove = int(input())
line_nums_list = [int(x) for x in line_nums]
for i in range(remove):
    line_nums_list.remove(min(line_nums_list))
line_nums = ", ".join([str(x) for x in line_nums_list])
print(line_nums)
# # INPUT 1
# 10 9 8 7 6 5
# 3
# # INPUT 2
# 1 10 2 9 3 8
# 2
# # INPUT END