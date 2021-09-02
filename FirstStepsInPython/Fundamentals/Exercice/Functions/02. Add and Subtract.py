def sum_numbers(a, b):
    return a + b


def subtract(a, b):
    return a - b


def add_and_subtract(a, b, c):
    return subtract(sum_numbers(a, b), c)


print(add_and_subtract(int(input()), int(input()), int(input())))
