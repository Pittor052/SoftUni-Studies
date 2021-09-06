# # 01 solution using 2 lists and 1 for loop
# lines = int(input())
# key = input()
# word_list = []
# found_match = []
# for _ in range(lines):
#     words = input()
#     word_list.append(words)
#     if key in words:
#         found_match.append(words)
# print(word_list)
# print(found_match)
# 02 solution using 1 list and 2 for loops
lines = int(input())
key = input()
word_list = []
for _ in range(lines):
    words = input()
    word_list.append(words)
print(word_list)
for i in range(len(word_list) - 1, -1, -1):
    element = word_list[i]
    if key not in element:
        word_list.remove(element)
print(word_list)
