s = input()
l = [s[0], s[len(s) // 2], s[len(s) - 2], s[len(s) - 1]]
for i in l:
    print(chr(ord(i) - 3), end="")
