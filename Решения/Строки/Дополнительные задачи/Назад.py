s = input()
ls = [s[0], s[len(s) // 2], s[len(s) - 2], s[len(s) - 1]]
for i in ls:
    print(chr(ord(i) - 3), end="")
