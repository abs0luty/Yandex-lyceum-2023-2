[n, m] = [int(input()), int(input())]

r = set()

for i in range(n):
    k = int(input())
    s = input()

    a = str(s[0:m:k])
    r.add(a)

for e in r:
    print(e)
