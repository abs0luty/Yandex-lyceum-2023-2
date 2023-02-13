b = []
for i in range(3):
    a = []

    while True:
        s = input()

        if s == "":
            break

        if s not in a:
            a.append(s)

    for e in a:
        b.append(e)

for e in b:
    if b.count(e) == 1:
        print(e)
