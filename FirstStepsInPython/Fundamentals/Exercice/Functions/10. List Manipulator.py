# # 01 solution NOT complete! https://judge.softuni.bg/Contests/Compete/Index/1728#9
def odd_even(line):
    for some_element in range(0, len(line)):
        if int(line[some_element]) % 2 == 0:
            even.append(line[some_element])
        else:
            odd.append(line[some_element])


def exchange(line, marker):
    line_sliced = line[int(marker) + 1:] + line[:int(marker) + 1]
    return line_sliced


def max_odd_even(line, command):
    if command[0] == "max":
        if command[1] == "odd" and (not len(odd) == 0):
            for element_odd in range(len(line) - 1, 0, -1):
                if int(line[element_odd]) == int(max(odd)):
                    return element_odd
        elif command[1] == "even" and (not len(even) == 0):
            for element_even in range(len(line) - 1, 0, -1):
                if int(line[element_even]) == int(max(even)):
                    return element_even
        else:
            return "No matches"


def min_odd_even(line, command):
    if command[0] == "min":
        if command[1] == "odd" and (not len(odd) == 0):
            for el in range(len(line) - 1, -1, -1):
                if int(line[el]) == int(min(odd)):
                    return el
        elif command[1] == "even" and (not len(even) == 0):
            for j in range(len(line) - 1, -1, -1):
                if int(line[j]) == int(min(even)):
                    return j
        else:
            return "No matches"


def show_first_elements(num_elements, type_element):
    first_elements = []
    if type_element == "odd":
        for odd_element in range(len(line_input)):
            if not int(line_input[int(odd_element)]) % 2 == 0 and len(first_elements) < int(num_elements):
                first_elements.append(int(line_input[int(odd_element)]))
        return first_elements
    elif type_element == "even":
        for even_element in range(len(line_input)):
            if int(line_input[int(even_element)]) % 2 == 0 and len(first_elements) < int(num_elements):
                first_elements.append(int(line_input[int(even_element)]))
        return first_elements


def show_last_elements(num_elements, type_element):
    last_elements = []
    backwards_line = line_input[::-1]
    if type_element == "odd":
        for num_odd in range(len(backwards_line)):
            if not int(backwards_line[int(num_odd)]) % 2 == 0 and len(last_elements) < int(num_elements):
                last_elements.append(int(backwards_line[int(num_odd)]))
        return last_elements[::-1]
    elif type_element == "even":
        for num_even in range(len(backwards_line)):
            if int(backwards_line[int(num_even)]) % 2 == 0 and len(last_elements) < int(num_elements):
                last_elements.append(int(backwards_line[int(num_even)]))
        return last_elements[::-1]


odd = []
even = []
line_input = input().split()
command_input = input().split()
odd_even(line_input)
while not command_input[0] == "end":
    if command_input[0] == "exchange":
        if not -1 < int(command_input[1]) <= len(line_input):
            print("Invalid index")
        else:
            line_input = exchange(line_input, command_input[1])
    elif command_input[0] == "max":
        print(max_odd_even(line_input, command_input))
    elif command_input[0] == "min":
        print(min_odd_even(line_input, command_input))
    elif command_input[0] == "first":
        if not -1 < int(command_input[1]) <= len(line_input):
            print("Invalid count")
        else:
            print(show_first_elements(command_input[1], command_input[2]))
    elif command_input[0] == "last":
        if not -1 < int(command_input[1]) <= len(line_input):
            print("Invalid count")
        else:
            print(show_last_elements(command_input[1], command_input[2]))

    command_input = input().split()

final_line_input = []
for i in range(0, len(line_input)):
    final_line_input.append(int(line_input[i]))

print(final_line_input)
# # INPUT 1
# 1 3 5 7 9
# exchange 1
# max odd
# min even
# first 2 odd
# last 2 even
# exchange 3
# end
#
# # OUTPUT 1
# # 2
# # No matches
# # [5, 7]
# # []
# # [3, 5, 7, 9, 1]
#
# # INPUT 2
# 1 10 100 1000
# max even
# first 5 even
# exchange 10
# min odd
# exchange 0
# max even
# min even
# end
#
# # INPUT 3
# 1 10 100 1000
# exchange 3
# first 2 odd
# last 4 odd
# end
#
# # TEST
# 1 2 2
# first 3 even
# end
