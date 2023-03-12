sick = set()
vaccine = set()
exemption = set()

while True:
    s = input()
    if not s:
        break
    sick.add(s)

    s = input()
    vaccine.add(s)

    s = input()
    exemption.add(s)

n = int(input())
codes = set()
for i in range(n):
    code = input()
    if code in sick or code in vaccine or code in exemption:
        codes.add(code)

for code in codes:
    print(code)
