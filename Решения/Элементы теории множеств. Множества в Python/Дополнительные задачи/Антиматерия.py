r1, r2, r3 = set(), set(), set()

while True:
    x = input()

    if x == "":
        break

    if x == "-1":
        r3 = r3 | (r1 & r2)
        r1 = r1 ^ r2
        r2 = set()
        continue

    r2.add(x)

print(*r1 - r3)
