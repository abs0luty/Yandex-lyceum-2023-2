import tkinter


def key_pressed(event):
    (dx, dy) = (0, 0)
    match event.keysym:
        case 'Up':
            (dx, dy) = (0, -10)
        case 'Down':
            (dx, dy) = (0, 10)
        case 'Left':
            (dx, dy) = (-10, 0)
        case 'Right':
            (dx, dy) = (10, 0)
    canvas.move(oval, dx, dy)


master = tkinter.Tk()
canvas = tkinter.Canvas(master, bg='blue', height=600, width=600)
oval = canvas.create_oval((300, 300), (310, 310), fill='red')
canvas.pack()
master.bind("<KeyPress>", key_pressed)
master.mainloop()
