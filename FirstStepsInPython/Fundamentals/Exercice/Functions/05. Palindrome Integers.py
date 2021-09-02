# # Functions/Exercise/05_palindrome_integers
def palindrome(sequence):
    for element in range(len(sequence)):
        backwards_number = ''.join(reversed(sequence[element]))
        if sequence[element] == backwards_number:
            print("True")
        else:
            print("False")


palindrome(input().split(", "))
# # INPUT 1
# 123, 323, 421, 121
# # OUTPUT 1
# # False
# # True
# # False
# # True
# # INPUT 2
# 32, 2, 232, 1010
# INPUT END
