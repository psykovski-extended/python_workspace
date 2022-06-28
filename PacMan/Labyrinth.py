from tkinter import *
from PacMan.Point2D import Point2D
from PacMan.Border import Border


class Labyrinth:

    def __init__(self, canvas: Canvas, walls: list):
        self.canvas = canvas
        self.walls = walls
        self.wallID = []

    def display(self):
        for i in self.walls:
            self.wallID.append(self.canvas.create_line(i.p1.x, i.p1.y, i.p2.x, i.p2.y, width=6, fill='#1919a6'))


if __name__ == '__main__':
    p1 = Point2D(5, 10)
    p2 = Point2D(5, 200)
    border = Border(p1, p2)
    p3 = Point2D(5, 10)
    p4 = Point2D(100, 10)
    border2 = Border(p3, p4)

    print(border.isOn(Point2D(3, 10)))

    root = Tk()
    background = PhotoImage('C:\\Users\\Dominik Lovetinsky\\Desktop\\Python\\PacMan\\labyrint.png')
    root.geometry("%dx%d+50+30" % (background.width(), background.height()))
    cv = Canvas(root, width=background.width(), height=background.height())
    cv.pack(side='top', fill=BOTH, expand='yes')
    cv.create_image(0, 0, image=background, anchor='nw')
    # cv = Canvas(root, height=200, width=200)
    # cv.pack()
    # l = Labyrinth(cv, [border, border2])
    # l.display()
    root.mainloop()
