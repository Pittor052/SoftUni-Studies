resources = {}
resource = input()
while not resource == "stop":
    value = int(input())
    if resource not in resources:
        resources[resource] = value
    else:
        resources[resource] += value
    resource = input()
for resource, value in resources.items():
    print(f"{resource} -> {value}")
