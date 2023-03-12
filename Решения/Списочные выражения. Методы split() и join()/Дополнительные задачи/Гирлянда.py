a = input().split()
m = max([len(i) for i in a])
c = []
for h in enumerate([[j[i] if i <= len(j) - 1 else " " for j in a] for i in range(m)]):
    c.append(" " + " ".join(h[1]) if h[0] !=
             0 else "_" + "_".join(h[1]) + "_")
print(*c, sep='\n')
c = []
print()
for h in enumerate([[j[i] if i <= len(j) - 1 else " " for j in a] for i in range(m - 1, - 1, -1)]):
    c.append(" " + " ".join(h[1]) if h[0] !=
             m - 1 else "_" + "_".join(h[1]) + "_")
print(*c, sep='\n')
