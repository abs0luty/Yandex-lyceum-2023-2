s = input()
print("\n".join(s[i:i + 1 + (i != len(s))] for i in range(0, len(s), 2)))
