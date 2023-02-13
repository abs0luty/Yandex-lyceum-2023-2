n = int(input())
s = [set(), set(), set()]

for i in range(n):
    j = int(input())

    if j > 40:
        s[0].add(j)
    if j % 2 == 0:
        s[1].add(j)
    if j % 3 == 0:
        s[2].add(j)

print(*((s[0] & s[1] | s[1] & s[2] | s[0] & s[2]) - (s[0] & s[1] & s[2])))
