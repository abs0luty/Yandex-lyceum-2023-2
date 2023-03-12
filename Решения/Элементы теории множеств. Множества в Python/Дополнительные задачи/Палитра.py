kv = {}
r = set()

for i in range(int(input())):
    for j in range(int(input())):
        tmp = input()
        kv[tmp] = kv.get(tmp, 0) + 1
        if kv[tmp] > 1:
            r.add(tmp)

print(len(r), sum(map(kv.get, r)))
