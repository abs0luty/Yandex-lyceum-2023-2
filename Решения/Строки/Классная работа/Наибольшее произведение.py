num = input()
max_product = 0

for i in range(len(num) - 4):
    product = 1
    for j in range(i, i + 5):
        product *= int(num[j])

    max_product = max(max_product, product)

print(max_product)
