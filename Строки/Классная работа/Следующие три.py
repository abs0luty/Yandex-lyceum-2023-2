n = int(input())
s = ''
for i in range(n - 1, n + 3):
    s += chr(ord('A') + i % 26)
print(s)
