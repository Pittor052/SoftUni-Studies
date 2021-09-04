employee_status = input().split()
improvement_factor = int(input())
employee_status = list(map(lambda x: int(x) * improvement_factor, employee_status))
result = list(filter(lambda x: x >= sum(employee_status) / len(employee_status), employee_status))
if len(result) >= len(employee_status)/2:
    print(f"Score: {len(result)}/{len(employee_status)}. Employees are happy!")
else:
    print(f"Score: {len(result)}/{len(employee_status)}. Employees are not happy!")

# 1 2 3 4 2 1
# 3
