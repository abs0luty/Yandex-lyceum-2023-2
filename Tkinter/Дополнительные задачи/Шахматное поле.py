import tkinter

master = tkinter.Tk()
canvas = tkinter.Canvas(master, bg='white', height=600, width=600)
scale = 600 / 8

for i in range(8):
    canvas.create_line([0, i * scale], [600, i * scale])
    canvas.create_line([i * scale, 0], [i * scale, 600])

canvas.pack()
master.mainloop()
