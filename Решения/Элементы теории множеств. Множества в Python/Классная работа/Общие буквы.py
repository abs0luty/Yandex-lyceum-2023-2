[a, b, c] = [set(input()), set(input()), set(input())]
print("".join(a & b | a & c | b & c))
