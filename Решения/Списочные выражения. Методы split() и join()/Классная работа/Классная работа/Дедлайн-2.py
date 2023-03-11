n = int(input())
print(' '.join([str(i - 2) for i in range(n + n % 2, 13, 2)]))
