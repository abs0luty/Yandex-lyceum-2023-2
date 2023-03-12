import sys
sys.set_int_max_str_digits(0)

n = int(input())
print(*[int('1' * i) ** 2 for i in range(1, n) if int('1' * i) <= n], sep=', ')
