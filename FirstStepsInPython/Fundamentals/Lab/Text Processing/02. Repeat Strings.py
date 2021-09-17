line_input = input().split()
result = ""
for word in line_input:
    result += word * len(word)
print(result)