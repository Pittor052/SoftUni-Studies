# # 01 solution
def palindrome(sequence):
    result = []
    for element in range(len(sequence)):
        backwards_number = ''.join(reversed(sequence[element]))
        if sequence[element] == backwards_number:
            result.append(sequence[element])
    return print(result)


line = input().split(" ")
search_for = input()
palindrome(line)
print(f"Found palindrome {line.count(search_for)} times")
# # 02 solution
# strings = input().split(" ")
# search_for = input()
# counter = 0
# result = []
# for element in range(len(strings)):
#     if strings[element] == ''.join(reversed(strings[element])):
#         result.append(strings[element])
# print(result)
# print(f"Found palindrome {result.count(search_for)} times")
# wow father mom wow shirt stats
# wow
