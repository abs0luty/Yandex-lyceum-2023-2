expression = input().strip()

tokens = []
start = 0
for i in range(len(expression)):
    if expression[i] in ['+', '-']:
        tokens.append(int(expression[start:i]))
        tokens.append(expression[i])
        start = i + 1

tokens.append(int(expression[start:]))

result = tokens[0]
for i in range(1, len(tokens), 2):
    if tokens[i] == '+':
        result += tokens[i + 1]
    else:
        result -= tokens[i + 1]

print(result)
