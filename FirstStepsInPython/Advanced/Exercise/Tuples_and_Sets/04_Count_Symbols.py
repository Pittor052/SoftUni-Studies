text_input = input()
letters = []
for el in text_input:
    letters.append(el)
unique_letters = {letter for letter in letters}
for l in sorted(letters):
    if l in unique_letters:
        print(f'{l.strip()}: {letters.count(l)} time/s')
        unique_letters.remove(l)
