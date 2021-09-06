num = int(input())
number_list = []
result_list = []
for _ in range(num):
    number_list.append(int(input()))
command = input()
if command == "even":
    for number in number_list:
        if number % 2 == 0:
            result_list.append(number)
    print(result_list)
if command == "odd":
    for number in number_list:
        if not number % 2 == 0:
            result_list.append(number)
    print(result_list)
if command == "negative":
    for number in number_list:
        if number < 0:
            result_list.append(number)
    print(result_list)
if command == "positive":
    for number in number_list:
        if number >= 0:
            result_list.append(number)
    print(result_list)

# INPUT 1
# 5
# 33
# 19
# -2
# 18
# 998
# even
# INPUT 2
# 3
# 111
# -4
# 0
# negative
# INPUT 3
# 5
# 33
# 19
# -2
# 18
# 998
# odd
# INPUT 4
# 5
# 33
# 19
# -2
# 18
# 998
# negative
# INPUT 5
# 5
# 33
# 19
# -2
# 18
# 998
# positive
# INPUT END