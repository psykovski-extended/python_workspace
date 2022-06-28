from PacMan.Labyrinth import *
from PIL import Image
from PIL import ImageTk


class Entity:

    def __init__(self, origin: Point2D, canvas: Canvas, name: str):
        self.origin = origin
        self.canvas = canvas
        self.name = name


class Ghost(Entity):

    def __init__(self, origin, canvas, name):
        super().__init__(origin, canvas, name)

        self.myself = self.canvas.create_bitmap(origin.x, origin.y, bitmap='questhead')


class Pac(Entity):

    def __init__(self, origin, canvas, name):
        super().__init__(origin, canvas, name)


if __name__ == '__main__':

    def move(event):
        if event.keysym == 'Right':
            cv.move(g.myself, 10, 0)
        elif event.keysym == 'Left':
            cv.move(g.myself, -10, 0)
        elif event.keysym == 'Up':
            cv.move(g.myself, 0, -10)
        elif event.keysym == 'Down':
            cv.move(g.myself, 0, 10)


    root = Tk()
    cv = Canvas(root, width=200, height=200, bg='#a1a1a1')
    width = 50
    height = 50
    img = Image.open("C:\\Users\\Dominik Lovetinsky\\Desktop\\Python\\PacMan\\Blinky.jpg")
    img = img.resize((width, height), Image.ANTIALIAS)
    photoImg = ImageTk.PhotoImage(img)
    b = Button(root, image=photoImg, width=50)
    b.pack()
    po = Point2D(50, 50)
    cv.pack(fill=BOTH)
    g = Ghost(po, cv, 'linda')
    root.bind('<KeyPress-Right>', lambda e: move(e))
    root.bind('<KeyPress-Left>', lambda e: move(e))
    root.bind('<KeyPress-Up>', lambda e: move(e))
    root.bind('<KeyPress-Down>', lambda e: move(e))
    root.mainloop()
