import tkinter
import math

master = tkinter.Tk()
canvas = tkinter.Canvas(master, bg='white', height=600, width=600)
canvas.pack()

n = int(input())

for k1 in range(n):
    k2 = ((k1 + n / 2 - 1) % n) if n % 2 == 0 else (k1 + (n - 1) / 2) % n

    canvas.create_line((300 + 50 * math.cos(2 * 3.14 * k1 / n),
                        300 + 50 * math.sin(2 * 3.14 * k1 / n)),
                       (300 + 50 * math.cos(2 * 3.14 * k2 / n),
                        300 + 50 * math.sin(2 * 3.14 * k2 / n)), fill='red')

master.mainloop()
