from tkinter import *


class Rectangle:

    def __init__(self, x, y, w, h, color, master):
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.color = color
        self.master = master
        self.master.bind("<KeyPress-Left>", lambda e: self.moveComponent(-5, 0))
        self.master.bind("<KeyPress-Right>", lambda e: self.moveComponent(5, 0))
        self.master.bind("<KeyPress-Up>", lambda e: self.moveComponent(0, -5))
        self.master.bind("<KeyPress-Down>", lambda e: self.moveComponent(0, 5))
        self.master.bind("<KeyPress-R>", lambda e: self.resizeComponent())
        self.cv = Canvas(master, height=400, width=400)
        self.rectangle = self.cv.create_rectangle(self.x, self.y, self.x + self.width,
                                                  self.y + self.height, fill=self.color)

    def resizeComponent(self):
        self.cv.delete(self.rectangle)
        self.height += 10
        self.width += 10
        self.rectangle = self.cv.create_rectangle(self.x, self.y, self.x + self.width,
                                                  self.y + self.height, fill=self.color)

    def moveComponent(self, dx, dy):
        self.x += dx
        self.y += dy
        self.cv.move(self.rectangle, dx, dy)


root = Tk()
rect = Rectangle(30, 30, 25, 25, '#ff00ff', root)
rect.cv.pack()
root.mainloop()
