# # 01 solution
number = list(input())
number = sorted(number)
for i in range(len(number)):
    if number[i] == "-":
        number = "".join(number[:i:-1])
        print(f"-{number}")
        break
    else:
        print("".join(number[::-1]))
        break
# # 02 solution
# num = list(input())
# num.sort(reverse=True)
# print("".join(num))
