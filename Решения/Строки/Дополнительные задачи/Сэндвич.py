s = input()
n = len(s)

n1 = n // 2 + n % 2

for i in range(n1):
    print(s[i], end='')
    if i + n1 < n:
        print(s[i + n1], end='')
