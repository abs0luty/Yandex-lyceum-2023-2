s = input()
s2 = ""

for e in s:
    if e != " ":
        s2 += e

print(s2 == s2[::-1])
