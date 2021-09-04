version = input().split(".")
version_list = list(map(lambda x: int(x), version))

if -1 < int(version_list[len(version) - 1]) < 9:  # 0.0.1
    increase_version = version_list.pop((int(len(version) - 1))) + 1
    version_list.append(increase_version)

else:  # 0.0.1
    version_list.remove(version_list[int(len(version) - 1)])
    version_list.extend([0])
    if -1 < int(version_list[len(version) - 2]) < 9:  # 0.1.0
        increase_version = version_list.pop((int(len(version) - 2))) + 1
        version_list.insert(version_list[0], increase_version)
    else:  # 0.1.0
        version_list.pop((int(len(version) - 2)))
        version_list.insert(version_list[0], 0)
        increase_version = version_list.pop(0) + 1  # 1.0.0
        version_list.insert(version_list[0], increase_version)

print(f"{version_list[0]}.{version_list[1]}.{version_list[2]}")
# Input 1
# 1.2.3
# Output 1
# 1.2.4
# Input 2
# 1.3.9
# Output 2
# 1.4.0
# Input 3
# 3.9.9
# Output 3
# 4.0.0
