s = input()

mn = 999999
mx = 0

for i in s:
    mn, mx = min(mn, ord(i)), max(mx, ord(i))

print(f'{mn}, {mx}')

result = 'НЕ ХВАТИТ'
symbols = set(list(s))
if len(symbols) <= 32:
    result = 'ХВАТИТ'

print(result)
