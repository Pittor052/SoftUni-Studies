# # 02 solution prsnr
string = input().split()
number_out = int(input())
soldiers = [int(i) for i in string]
soldiers_len = len(soldiers)
new_list = []
count = 0
index = 0
while len(new_list) < soldiers_len:

    count += 1
    if count % number_out == 0:
        new_list.append(soldiers.pop(index))
    else:
        index += 1
    if index >= len(soldiers):
        index = 0

print(str(new_list).replace(' ', ''))
# # INPUT 1
# 1 2 3 4 5 6 7
# 3
# # INPUT END
