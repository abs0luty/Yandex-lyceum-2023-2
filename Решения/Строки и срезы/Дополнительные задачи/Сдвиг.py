s1 = input()
s2 = input()

if len(s1) != len(s2):
    print("NO")
else:
    if s1 in s2 * 2:
        print(s2.index(s1))
    else:
        print("NO")
