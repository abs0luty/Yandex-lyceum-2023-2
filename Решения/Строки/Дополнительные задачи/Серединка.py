word = input()
mid = len(word) // 2
print(word[mid - (1 - (len(word) % 2))])
