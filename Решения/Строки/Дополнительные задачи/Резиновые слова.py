s = input()
middle, d = len(s) // 2, len(s) % 2

if d != 0:
    middle += 1
    print((s[(middle - 1)]).center(len(s)))

for i in range(d, middle):
    print((s[middle - i - 1] + ' ' * (2 * i - d) +
          s[middle + i - d]).center(len(s)))
