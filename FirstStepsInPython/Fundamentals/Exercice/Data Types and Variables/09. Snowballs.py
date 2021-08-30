snowballs = int(input())
snowball_value = 0
a_list = []
for i in range(snowballs):
    snowball_snow = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    score = (snowball_snow / snowball_time) ** snowball_quality
    if score > snowball_value:
        a_list = []
        a_list.append(snowball_snow)
        a_list.append(snowball_time)
        snowball_value = int(score)
        a_list.append(snowball_value)
        a_list.append(snowball_quality)
print(f"{a_list[0]} : {a_list[1]} = {a_list[2]} ({a_list[3]})")

# 1
# 1
# 10
# 2

# 1
# 8
# 10
# 2

# 2
# 10
# 2
# 3
# 5
# 5
# 5

# 3
# 10
# 5
# 7
# 16
# 4
# 2
# 20
# 2
# 2

# 4
# 10
# 5
# 7
# 16
# 4
# 2
# 20
# 2
# 2
# 10
# 5
# 7
