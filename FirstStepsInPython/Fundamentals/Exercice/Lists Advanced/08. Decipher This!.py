secret_message = input().split()
result = []
for word in secret_message:
    num = ''
    num += ''.join([n for n in word if n.isdigit()])
    word = list(chr(int(num)) + word[len(num):])
    word[1], word[len(word) - 1] = word[len(word) - 1], word[1]
    result.append(''.join([n for n in word]))
for j in result:
    print(j, end=" ")
