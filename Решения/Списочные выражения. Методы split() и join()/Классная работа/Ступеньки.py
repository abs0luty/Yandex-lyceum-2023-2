a, b = int(input()), int(input())
print(', '.join([str(i) if i % a !=
      0 else 'БОСИКОМ' for i in range(1, b+1)]))
