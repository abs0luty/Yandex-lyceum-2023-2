n = int(input())

a, b = set(), set()

for i in range(n):
    a.add(input())

m = int(input())

for i in range(m):
    b.add(input())

print("\n".join(a.intersection(b)))
