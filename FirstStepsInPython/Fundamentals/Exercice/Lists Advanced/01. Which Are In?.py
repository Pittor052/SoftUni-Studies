# # 01 solution using find(): finds the first occurrence of the specified value. returns -1 if the value is not found.
find = input().split(", ")
here = input().split(", ")
result = []

for element_from_find in find:
    for element_from_here in here:
        if element_from_here.find(element_from_find) > -1:
            result.append(element_from_find)
            break
print(result)

# # 02 solution Радослав Георгиев
# string_1, string_2 = input().split(", "), input().split(", ")
# print(sorted(set([str_1 for str_1 in string_1 for str_2 in string_2 if str_1 in str_2]), key=string_1.index))
#
# # 03 solution Dimitar Dzhapunov
# first_string = input().split(', ')
# second_string = input().split(', ')
#
# matched_list = []
#
# for j in range(len(first_string)):
#
#     for i in range(len(second_string)):
#
#         if str(first_string[j]) in str(second_string[i]):
#
#             if first_string[j] not in matched_list:
#
#                 matched_list.append(first_string[j])
#
# print(matched_list)
# # INPUT 1
# arp, live, strong
# lively, alive, harp, sharp, armstrong
# # OUTPUT 1
# ['arp', 'live', 'strong']
# # INPUT 2
# tarp, mice, bull
# lively, alive, harp, sharp, armstrong
# # OUTPUT 2
# []
