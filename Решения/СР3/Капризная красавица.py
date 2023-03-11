a = set()
b = set()

current = 0

while True:
    n = int(input())

    if n % 10 == 0:
        current += 1

    if current == 2:
        break

    if current == 0:
        a.add(n)
    else:
        b.add(n)

for i in b.difference(a):
    if i % 10 != 0 and i % 2 != 0:
        print(i, end='#')
