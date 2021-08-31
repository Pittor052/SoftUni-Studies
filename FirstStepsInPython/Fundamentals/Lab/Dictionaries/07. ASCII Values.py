# Write program that receives a list of characters separated by ", " and creates a dictionary with each character
# as a key and its ASCII value as a value.
# Try solving that problem using comprehensions.
# # 01 solution
# line_input = dict()
# for letter in input().split(', '):
#     line_input[letter] = ord(letter)
# print(line_input)
# # 02 solution dictionary comprehension
line_input = {letter: ord(letter) for letter in input().split(', ')}
print(line_input)
# # INPUT 0
# a, b, c, a
#
# # OUTPUT 0
# {'a': 97, 'b': 98, 'c': 99}
# # INPUT 1
# d, c, m, h
#
# # OUTPUT 1
# {'d': 100, 'c': 99, 'm': 109, 'h': 104}

