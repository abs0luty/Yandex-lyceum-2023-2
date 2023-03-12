print(*[f"{i}, " + ("; АХ! " if i % 4 == 0 else "")
      for i in range(1, int(input())+1)], end="")
