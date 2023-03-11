import tkinter
import random


def draw(event):
    (r, x, y) = (random.randint(100, 600),
                 random.randint(0, 600), random.randint(0, 600))

    canvas.create_oval((x, y), (x + r, y + r), fill='red')
    return


master = tkinter.Tk()
canvas = tkinter.Canvas(master, bg='blue', height=600, width=600)
canvas.pack()
master.bind("<KeyPress>", draw)
master.mainloop()
