# Write a function that receives two integer numbers.
# Calculate factorial of each number.
# Divide the first result by the second and print the division formatted to the second decimal point.
# # Solution 01
def factorial_division(num1, num2):
    factor1 = 1
    factor2 = 1
    for i in range(1, num1 + 1):
        factor1 *= i
    for i in range(1, num2 + 1):
        factor2 *= i
    print(f"{factor1 / factor2:.2f}")


factorial_division(int(input()), int(input()))


# # Solution 02 Mario Georgiev
# def factorial_division(num_1: int, num_2: int):
#     multiplication_first = 1
#     multiplication_second = 1
#     for numbers_from_num_1 in range(num_1, 0, -1):
#         multiplication_first *= numbers_from_num_1
#     for numbers_from_num_2 in range(num_2, 0, -1):
#         multiplication_second *= numbers_from_num_2
#
#     return f"{multiplication_first / multiplication_second:.2f}"
#
#
# number_1 = int(input())
# number_2 = int(input())
#
# print(factorial_division(number_1, number_2))
