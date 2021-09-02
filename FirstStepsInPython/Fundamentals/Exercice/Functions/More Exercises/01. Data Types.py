def manipulation(command_type, value):
    if command_type == "int":
        return f"{int(value) * 2}"
    elif command_type == "real":
        return f"{float(value) * 1.5:.2f}"
    elif command_type == "string":
        return f"${value}$"


command_input = input()
value_ = input()
print(manipulation(command_input, value_))
