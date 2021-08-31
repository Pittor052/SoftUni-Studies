# Write a program that extracts all elements from a given sequence of words that are present in it an odd number of
# times (case-insensitive).
#    Words are given on a single line, space separated.
#    Print the result elements in lowercase, in their order of appearance.

line_input = input().split()
dictionary = {}
for word in line_input:
    word_lower = word.lower()
    if word_lower not in dictionary:
        dictionary[word_lower] = 0
    dictionary[word_lower] += 1
for key, val in dictionary.items():
    if not val % 2 == 0:
        print(key, end=" ")

# # INPUT
# Java C# PHP PHP JAVA C java
# # OUTPUT
# java c# c
# # INPUT 1
# 3 5 5 hi pi HO Hi 5 ho 3 hi pi
# # OUTPUT 1
# 5 hi
# # INPUT 2
# a a A SQL xx a xx a A a XX c
# # OUTPUT 2
# a sql xx c
