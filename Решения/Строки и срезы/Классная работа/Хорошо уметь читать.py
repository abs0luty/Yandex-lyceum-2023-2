s = input()
initials = 'ESM'

j, c = 0, True
d, e = '', 0

pr = False

for i in s:
    j += 1
    if i in initials and not c and not pr:
        f = j - e - 1
        if f >= 0:
            print(f)
        else:
            print(len(s[e:]))
        pr = True
    if i in initials and c:
        print(j)
        e = j
        c = False
    if i not in d:
        d += i

if c:
    print(0)
    print(len(s))
    pr = True

if not pr:
    print(len(s[e:]))

g = set()

for i in d:
    if i not in initials and i != ' ':
        g.add(i)

print(len(g))
