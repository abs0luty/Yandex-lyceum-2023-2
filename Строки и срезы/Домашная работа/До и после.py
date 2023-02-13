s = input()

j = -1
for i in range(len(s)):
    if s[i] == '-':
        j = i

print(f"{s[j+1:]}-{s[:j]}")
