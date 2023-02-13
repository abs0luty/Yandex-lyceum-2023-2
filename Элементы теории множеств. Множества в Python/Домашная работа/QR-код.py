a = [set(), set(), set()]

for i in range(3):
    while True:
        b = input()
        if b == "":
            break

        a[i].add(b)

n = int(input())
r = set()
for i in range(n):
    c = input()
    if c in a[0] or c in a[1] or c in a[2]:
        r.add(c)

print("\n".join(r))
