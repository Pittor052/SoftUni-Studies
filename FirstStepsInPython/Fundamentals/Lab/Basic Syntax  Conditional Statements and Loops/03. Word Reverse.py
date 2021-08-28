# 01. basic solution
word = input()
for i in range(len(word) - 1, -1, -1):
    print(word[i], end="")
# # 02. join() method solution
# # initial string
# s = 'Python'
# reversed = ''.join(reversed(s))
# # .join() method merges all of the characters resulting from the reversed iteration into a new string
# print(reversed)  # print the reversed string
# # 03. simplified join() method solution
# s = input()
# print(f"{''.join(reversed(s))}")
