def even_and_odd_sum(num):
    even = 0
    odd = 0
    for element in range(0, len(num)):
        if int(num[element]) % 2 == 0:
            even += int(num[element])
        else:
            odd += int(num[element])
    return f"Odd sum = {odd}, Even sum = {even}"


print(even_and_odd_sum(input()))


