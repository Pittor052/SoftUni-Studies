def perfect_number(num):
    result = []
    count = 1
    for divisor in range(1, num):
        if num % count == 0:
            result.append(count)
            count += 1
        else:
            count += 1
    if not sum(result) == num:
        print("It's not so perfect.")
    else:
        print("We have a perfect number!")


perfect_number(int(input()))


