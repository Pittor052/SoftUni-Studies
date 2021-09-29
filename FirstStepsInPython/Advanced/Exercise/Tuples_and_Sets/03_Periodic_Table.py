num_lines_input = int(input())
elements = []
while num_lines_input > 0:
    items = input().split()
    while items:
        elements.append(items.pop())
    num_lines_input -= 1

unique_elements = {element for element in elements}
print(*unique_elements, sep='\n')
