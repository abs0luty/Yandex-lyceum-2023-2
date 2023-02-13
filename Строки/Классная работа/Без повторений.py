while True:
    s = input()
    if s == "":
        break

    if len(s) == len(set(s)):
        print(s)
