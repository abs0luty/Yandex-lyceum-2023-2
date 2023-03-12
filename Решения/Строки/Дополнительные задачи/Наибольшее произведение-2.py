num = input()
n = int(input())
max_product = 0

for i in range(len(num) - n + 1):
    product = 1

    for j in range(n):
        product *= int(num[i + j])

    max_product = max(max_product, product)

print(max_product)
