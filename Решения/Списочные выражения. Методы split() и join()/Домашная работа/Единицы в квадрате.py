n = int(input())
squares = [int('1' * i) ** 2 for i in range(1, n + 1) if int('1' * i) <= n]
print(', '.join(map(str, squares)))
