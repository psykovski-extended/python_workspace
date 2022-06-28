import threading
import time
from tkinter import *


root = Tk()
text = StringVar(root)


def mul(a, b):
    time.sleep(1)
    text.set(str(a*b))


for i in range(5):
    threading.Thread(target=mul, args=(i, i*3)).start()


l1 = Label(root, textvariable=text)
l1.pack()
root.mainloop()

