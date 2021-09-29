first_num_elements, second_num_elements2 = [int(num) for num in input().split()]
first_set = {input() for _ in range(first_num_elements)}
second_set = {input() for _ in range(second_num_elements2)}

print(*first_set.intersection(second_set), sep='\n')


# 4 3
# 1
# 3
# 5
# 7
# 3
# 4
# 5