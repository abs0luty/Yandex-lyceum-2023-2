s = input()

in_word = False
word = ""

for c in s:
    if c == ' ':
        if in_word:
            print(word)
            word = ""
        in_word = False
    else:
        in_word = True
        word += c

if in_word:
    print(word)
