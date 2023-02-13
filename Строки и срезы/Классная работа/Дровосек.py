s = input()
n = int(input())

while s != "":
    print(s[-n:])
    s = s[:-n]
    print(s[:n])
    s = s[n:]
