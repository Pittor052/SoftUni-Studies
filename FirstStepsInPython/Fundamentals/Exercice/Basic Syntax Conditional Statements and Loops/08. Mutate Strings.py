string1 = input()
string2 = input()
string_list1 = list(string1)
while not string1 == string2:
    for i in range(len(string2)):
        string3 = string1
        element = string2[i]
        string_list1[i] = element
        string1 = "".join(string_list1)
        if not string1 == string3:
            print(string1)
    break
