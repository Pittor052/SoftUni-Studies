# # 01 solution basics
# lines = int(input())
# balanced = False
# count_brackets = 0
# save = ""
# for i in range(lines):
#     command = input()
# # Check if the current input equals the previous input. Closing bracket should follow an opening one.
#     if command == save:
#         balanced = False
#         break
#     if (command == "(") or (command == ")"):  # Check if input matches a bracket
#         balanced = True
#         count_brackets += 1
#         save = command  # Save current input
# if balanced and count_brackets % 2 == 0:  # Check if balanced is equal to True and if number of brackets is even
#     print("BALANCED")
# else:
#     print("UNBALANCED")
# 02 Solution
lines = int(input())
command_list = []
open_bracket = "("
save = ""
for i in range(lines):
    command = (input())
    if command == save:
        print("UNBALANCED")
        break
    elif (command == "(") or (command == ")"):
        command_list.append(command)
    save = command
if (len(command_list)) % 2 == 0:
    x = command_list.count("(")
    if (len(command_list) / 2) == x:
        print("BALANCED")
else:
    print("UNBALANCED")
# print(len(command_list) / 2)
# print((len(command_list)) % 2)
# INPUT 1
# 6
# 12 *
# )
# 10 + 2 -
# (
# 5 + 10
# )
# INPUT 2
# 8
# (
# 5 + 10
# )
# * 2 +
# (
# 5
# )
# -12
# INPUT 3
# 3
# a
# (
# )
# --- INPUT END
