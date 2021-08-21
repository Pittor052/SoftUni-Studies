text = input()
s = 0
for i in range(0, len(text)):
    if text[i] == "a":
        s += 1
    if text[i] == "e":
        s += 2
    if text[i] == "i":
        s += 3
    if text[i] == "o":
        s += 4
    if text[i] == "u":
        s += 5
print(s)
