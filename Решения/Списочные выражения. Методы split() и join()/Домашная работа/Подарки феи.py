s = input().split(", ")
result = ["flower" if i % 2 == 0 else "gemstone" for i in range(len(s))]
print("; ".join(result))
