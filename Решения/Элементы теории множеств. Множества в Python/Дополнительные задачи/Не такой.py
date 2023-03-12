control_char = input().strip()
n = int(input())

max_count = -1
max_string = None

for i in range(n):
    s = input().strip()
    count = len(set(s) - set(control_char))
    if count > max_count:
        max_count = count
        max_string = s

if max_count == 0:
    print("-1")
else:
    for c in set(max_string) - set(control_char):
        print(c, end='')
