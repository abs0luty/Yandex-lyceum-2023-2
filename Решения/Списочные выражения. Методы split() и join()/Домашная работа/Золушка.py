substring, words = input(), input()
print(*[word for word in words.split() if substring in word])
