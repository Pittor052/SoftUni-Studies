def calculate(command, num_a, num_b):
    if command == "multiply":
        return num_a * num_b
    elif command == "divide":
        return num_a // num_b
    elif command == "add":
        return num_a + num_b
    elif command == "subtract":
        return num_a - num_b


print(calculate(input(), int(input()), int(input())))
