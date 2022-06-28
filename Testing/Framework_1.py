from tkinter import *


def undo(button: Button):
    global f
    button.destroy()
    f -= 1


def do(a: str):
    global f, root
    f += 1
    r = Button(root, text=a + " " + str(f), command=lambda: undo(r))
    r.pack()


def paint(event):
    x1, y1 = (event.x - 2), (event.y - 2)
    x2, y2 = (event.x + 2), (event.y + 2)
    cv.create_oval(x1, y1, x2, y2, fill="#ff0000", outline="#0000ff")


f = 0
root = Tk()
root.title("test")
cv = Canvas(root, width=800, height=500)
cv.bind("<B1-Motion>", paint)
cv.create_bitmap(50, 50, bitmap="questhead")
img = PhotoImage(file="C:\\Users\\Dominik Lovetinsky\\Desktop\\MatlabExport_1.png")
cv.create_image(0, 0, image=img, anchor=NW)
cv.pack()
bt1 = Button(root, text="click me", command=lambda a='destroy': do(a))
bt1.pack()

root.mainloop()
