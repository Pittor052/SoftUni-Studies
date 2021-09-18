# # Solution 01
# line_input = input()
# result = line_input[0]
# for ch in range(len(line_input)):
#     if ch < len(line_input) - 1:
#         if not line_input[ch] == line_input[ch + 1]:
#             result += line_input[ch + 1]
#
# print(result)
# # Solution 02
line_input = input()
result = line_input[0]
ch = 0
while ch < len(line_input) - 1:
    if not line_input[ch] == line_input[ch + 1]:
        result += line_input[ch + 1]
    ch += 1
print(result)
# aaaaabbbbbcdddeeeedssaa
