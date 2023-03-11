delimiter, n, words = input().split()
n = int(n)
print(delimiter[::-1].join(
    [word for word in words.split(delimiter) if len(set(word)) >= n]))
