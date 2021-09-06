lines = int(input())
positive_list = []
negative_list = []
for _ in range(lines):
    value = int(input())
    if value >= 0:
        positive_list.append(value)
    else:
        negative_list.append(value)
print(positive_list)
print(negative_list)
print(f"Count of positives: {len(positive_list)}. Sum of negatives: {sum(negative_list)}")