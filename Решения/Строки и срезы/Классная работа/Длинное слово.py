max_s, max_l = "", -1

s = input()
buffer = ""
for c in s:
    if c == " ":
        if len(buffer) > max_l:
            max_l = len(buffer)
            max_s = buffer

        buffer = ""
    else:
        buffer += c

if len(buffer) > max_l:
    max_l = len(buffer)
    max_s = buffer

print(max_s)
