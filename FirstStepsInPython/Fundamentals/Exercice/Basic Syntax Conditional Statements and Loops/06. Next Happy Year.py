# # 01 solution using set(): a method to convert any of the iterable to sequence of iterable elements
# # with distinct elements, commonly called Set.
# year = int(input())
# while True:
#     year += 1
#     # # compare the length of the year with the number of unique elements
#     if len(str(year)) == len(set(str(year))):
#         print(year)
#         break
# # 02 solution with loops with knowledge from programming basics only
year = int(input())
while True:  # loop the whole process for the year
    year += 1  # change the year to begin new search
    some_str = str(year)  # must work with str to take every element on current position
    found = True  # value for breaking the while loop
    for i in range(len(some_str)):  # loop the whole str (0, end of str)
        test_digit = some_str[i]  # take the element on the current position
        for j in range(len(some_str)):  # loop the whole str for the comparison with the element and the whole str
            if test_digit == some_str[j] and (not i == j):  # compare the element in test_digit with the current one
                # not including same positions because elements are equal
                # (e.g. 8989: test_digit[1] is 8  and some_str[1] is 8)
                found = False
                break
    if found:
        print(year)
        break
