# 01 solution
something = input()
indices = list()
for element in range(len(something)):
    if something[element].isupper():
        indices.append(element)
print(indices)

# # 02 solution found on https://stackoverflow.com/questions/28402480/get-the-indices-of-capital-letters-in-a-string
# # must investigate further
# something = input()
# res = [i for i, element in enumerate(something) if element.isupper()]
# print(res)
