s1 = set()
s2 = set()
s3 = set()

while True:
    x = input().strip()
    if x == '':
        break
    s1.add(x)

while True:
    x = input().strip()
    if x == '':
        break
    s2.add(x)

while True:
    x = input().strip()
    if x == '':
        break
    s3.add(x)

n = int(input())
result = set()
for i in range(n):
    query = input().strip()
    if query in s1 or query in s2 or query in s3:
        result.add(query)

for r in result:
    print(r)
