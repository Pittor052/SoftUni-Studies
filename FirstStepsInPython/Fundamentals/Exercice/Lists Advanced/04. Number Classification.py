line_numbers = input().split(", ")
print("Positive:", ", ".join(list(filter((lambda x: int(x) > -1), line_numbers))))
print("Negative:", ", ".join((list(filter((lambda x: int(x) < 0), line_numbers)))))
print("Even:", ", ".join((list(filter((lambda x: int(x) % 2 == 0), line_numbers)))))
print("Odd:", ", ".join((list(filter((lambda x: int(x) % 2 != 0), line_numbers)))))
# # INPUT 1
# 1, -2, 0, 5, 3, 4, -100, -20, 12, 19, -33
# # OUTPUT 1
# Positive: 1, 0, 5, 3, 4, 12, 19
# Negative: -2, -100, -20, -33
# Even: -2, 0, 4, -100, -20, 12
# Odd: 1, 5, 3, 19, -33
