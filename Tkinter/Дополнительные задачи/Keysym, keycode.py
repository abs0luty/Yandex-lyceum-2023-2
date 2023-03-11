import tkinter


def show_key(event):
    label.config(text=" ".join(
        [event.keysym, event.char, str(event.keycode)]))


master = tkinter.Tk()
label = tkinter.Label(master, text="Hello world!")
label.pack()
master.bind("<KeyPress>", show_key)
master.mainloop()
