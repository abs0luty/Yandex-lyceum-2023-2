[a, b, c] = [set(input()), set(input()), set(input())]
r = set()
r.update(a & b)
r.update(a & c)
r.update(b & c)
print("".join(r))
