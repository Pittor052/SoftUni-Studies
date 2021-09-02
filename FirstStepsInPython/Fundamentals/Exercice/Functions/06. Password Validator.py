# # 01 solution
def password_validator(password):

    numbers = [int(word) for word in password if word.isdigit()]
    small_letter = range(97, 122, 1)  # range of decimal values of a - z letters in the ASCII table
    capitol_letter = range(65, 90, 1)  # range of decimal values of A - Z letters in the ASCII table
    nums = range(48, 57, 1)  # range of decimal values of numbers from 0 to 9 in the ASCII table
    fail = False
    if not 5 < len(password) < 11:
        fail = True
        print("Password must be between 6 and 10 characters")
    if len(numbers) < 2:
        fail = True
        print("Password must have at least 2 digits")
    for element in password:
        if (ord(element) not in small_letter) and (ord(element) not in capitol_letter) and (ord(element) not in nums):
            fail = True
            print("Password must consist only of letters and digits")
    if not fail:
        print("Password is valid")


password_validator(input())
# # INPUT 1
# logIn22
# # INPUT 2
# MyPass123
# # INPUT 3
# Pa$s$s
# INPUT END
