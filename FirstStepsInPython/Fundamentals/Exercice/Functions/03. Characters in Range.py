def part_of_ascii(start, stop):
    for number in range(ord(start) + 1, ord(stop)):
        print(chr(number), end=" ")


part_of_ascii(input(), input())
