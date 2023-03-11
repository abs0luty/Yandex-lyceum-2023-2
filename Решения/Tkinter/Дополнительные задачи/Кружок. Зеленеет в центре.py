import tkinter


def key_pressed(event):
    dx, dy = 0, 0
    match event.keysym:
        case 'space':
            canvas.coords(oval, (300, 300, 310, 310))
            canvas.itemconfig(oval, fill='green')
        case 'Up':
            dx, dy = 0, -10
        case 'Down':
            dx, dy = 0, 10
        case 'Left':
            dx, dy = -10, 0
        case 'Right':
            dx, dy = 10, 0

    canvas.move(oval, dx, dy)

    middle = (300 + 310) / 2

    if canvas.coords(oval)[0] < (middle - 100) or canvas.coords(oval)[0] > (middle + 100) \
            or canvas.coords(oval)[1] < (middle - 100) or canvas.coords(oval)[1] > (middle + 100):
        canvas.itemconfig(oval, fill='red')
    else:
        canvas.itemconfig(oval, fill='green')


master = tkinter.Tk()
canvas = tkinter.Canvas(master, bg='blue', height=600, width=600)
oval = canvas.create_oval((300, 300), (310, 310), fill='green')
canvas.pack()
master.bind("<KeyPress>", key_pressed)
master.mainloop()
