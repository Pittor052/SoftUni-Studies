search_for = str(input())
found = False
book = input()
num_books = 0
while book != "No More Books":
    if search_for == book:
        found = True
        break

    num_books += 1
    book = str(input())

if found:
    print(f"You checked {num_books} books and found it.")
else:
    print("The book you search is not here!")
    print(f"You checked {num_books} books.")
