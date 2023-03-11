import tkinter

master = tkinter.Tk()
canvas = tkinter.Canvas(master, bg='white', height=600, width=600)
scale = 600 / 8

for i in range(8):
    canvas.create_line([0, i * scale], [600, i * scale])
    canvas.create_line([i * scale, 0], [i * scale, 600])

for i in range(3):
    for j in range(8):
        if (i + j) & 1:
            continue

        canvas.create_oval((j * scale, i * scale),
                           ((j + 1) * scale, (i + 1) * scale), fill="red")
        canvas.create_oval(((8 - j) * scale, (8 - i) * scale),
                           ((7 - j) * scale, (7 - i) * scale), fill="blue")

canvas.pack()
master.mainloop()
