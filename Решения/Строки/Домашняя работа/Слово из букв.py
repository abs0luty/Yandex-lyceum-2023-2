words = [input() for i in range(int(input()))]

result = ""

for i, word in enumerate(words):
    if len(word) >= i + 1:
        result += word[-(i + 1)]
    else:
        result = "None"
        break

print(result)
