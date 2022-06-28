import os
import sys
from tkinter import *
from tkinter import filedialog


def fileOpen():
    fd = filedialog.askopenfile()
    print(fd)


path = os.scandir('C:\\Users\\Dominik Lovetinsky\\Coding')
root = Tk()
n = []
scroll = Scrollbar(root)
scroll.pack(side=RIGHT, fill=Y)
listedItems = Listbox(root, yscrollcommand=scroll.set)
for i in path:
    # if 'r' in i.name:
    n.append(i.name)
    listedItems.insert(END, i.name)
listedItems.pack()
Button(root, text='Click me', command=fileOpen).pack()
var = StringVar()
var.set('Select folder: ')

drop = OptionMenu(root, var, *n)
drop.pack()
root.mainloop()
