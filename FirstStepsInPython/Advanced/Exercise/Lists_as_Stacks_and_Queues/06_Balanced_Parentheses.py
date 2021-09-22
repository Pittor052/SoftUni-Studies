open_list = ["[", "{", "("]
close_list = ["]", "}", ")"]
line_input = input()
stack = []
stop = False

for ll in line_input:
    if ll in open_list:
        stack.append(ll)
    elif ll in close_list:
        pos = close_list.index(ll)
        if (len(stack) > 0) and (open_list[pos] == stack[len(stack) - 1]):
            stack.pop()
        else:
            print('NO')
            stop = True
    if stop:
        break

if not stop:
    print('YES')
# # INPUT 1
# {[()]}
# # OUTPUT 1
# # YES
# # INPUT 2
# {[(])}
# # OUTPUT 2
# # NO
# # INPUT 3
# {{[[(())]]}}
# # OUTPUT 3
# # YES
# # TEST
# ()))
# [()()]
# (){}[]
# ]})({[