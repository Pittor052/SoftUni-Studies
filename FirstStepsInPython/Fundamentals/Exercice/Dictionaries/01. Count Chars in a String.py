list_of_letters = list(input())
unique_letters = []
for letter in list_of_letters:
    if letter not in unique_letters:
        unique_letters.append(letter)
for each_letter in unique_letters:
    if not each_letter == " ":
        print(f"{each_letter} -> {list_of_letters.count(each_letter)}")
