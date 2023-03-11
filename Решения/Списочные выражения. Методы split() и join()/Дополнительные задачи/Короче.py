n = input()
print('\n'.join([n[i:len(n) - i] for i in range(len(n) // 2 + 1)]))
