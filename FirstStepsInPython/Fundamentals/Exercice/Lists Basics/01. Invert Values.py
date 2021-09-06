str_nums = input()
some_list = str_nums.split(input())
result = []
for el in some_list:
    result.append((int(el) * -1))
print(result)
# INPUT 1
# 1 2 -3 -3 5
# INPUT 2
# -4 0 2 57 -101
# INPUT END
