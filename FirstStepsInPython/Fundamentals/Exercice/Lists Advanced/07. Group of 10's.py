import math

nums = list(map(lambda x: int(x), input().split(", ")))
max_num = max(nums)

for i in range(1, (math.ceil(max_num / 10)) + 1):
    print(f"Group of {i * 10}'s:",
          list(map(lambda x: int(x), (list(filter((lambda x: (i - 1) * 10 < x <= i * 10), nums))))))

# # INPUT 1
# 8, 12, 38, 3, 17, 19, 25, 35, 50
# # OUTPUT 1
# Group of 10's: [8, 3]
# Group of 20's: [12, 17, 19]
# Group of 30's: [25]
# Group of 40's: [38, 35]
# Group of 50's: [50]
# # INPUT 2
# 1, 3, 3, 4, 34, 35, 25, 21, 33
# # OUTPUT 2
# Group of 10's: [1, 3, 3, 4]
# Group of 20's: []
# Group of 30's: [25, 21]
# Group of 40's: [34, 35, 33]
# # TEST
# 8, 12, 38, 3, 17, 19, 25, 35, 50, 55
