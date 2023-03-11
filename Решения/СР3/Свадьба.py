s0 = input()
i = set()

while True:
    s = input()

    if s == "":
        break

    j = s.rfind(s0)

    if j != -1:
        i.add(j)

if i != set():
    print("\n".join(map(str, i)))
else:
    print("-1")
