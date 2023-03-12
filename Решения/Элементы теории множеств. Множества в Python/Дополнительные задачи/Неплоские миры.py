n = int(input())
r = set()

for i in range(n):
    m = int(input())

    for j in range(m):
        r.add(input())

print("\n".join(r))
