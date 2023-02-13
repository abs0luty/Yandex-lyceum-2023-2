s = input()
prev = chr(0)
f = True
for e in s:
    if e < prev:
        print(e)
        f = False
        break
    prev = e

if f:
    print("(:_0_:)")
