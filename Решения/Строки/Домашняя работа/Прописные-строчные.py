code = ord(input())
if code >= ord('A') and code <= ord('Z'):
    print(chr(code + 32))
elif code >= ord('a') and code <= ord('z'):
    print(chr(code - 32))
