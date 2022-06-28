import sympy as sp
from tkinter import *
import sys
import time
import threading
import code as cd


class ConsoleHandler:

    def __init__(self, textfield: Text):
        self.textfield = textfield

    def write(self, output):
        self.textfield.insert(END, output)


class InputHandler:

    def __init__(self, entry: Entry):
        self.entry = entry
        self.readableReady = False
        self.entry.bind('<Return>', self.setTrue)

    def setTrue(self, e):
        self.readableReady = True

    def readline(self):
        while not self.readableReady:
            time.sleep(0.5)
        self.readableReady = False
        return self.entry.get()


def inputSth():
    while threading.main_thread().is_alive():
        _contentIn = ""
        try:
            _contentIn = input()
            text.insert(END, ">>>  " + _contentIn + "\n")
            eval(_contentIn)
        except Exception as e:
            try:
                exec(_contentIn)
            except Exception as e1:
                print(e1)


root = Tk()
text = Text(root, font=('JetBrains Mono', 10), fg='#23ea11', bg='#555555')
text.pack(side=TOP)
sys.stdout = ConsoleHandler(text)
entry = Entry(root, font=('JetBrains Mono', 10))
entry.pack(fill=X)
sys.stdin = InputHandler(entry)
x = sp.symbols('x')
expr1 = 2 * x ** 2 + 4 * x - 8
expr2 = sp.cos(x)
sp.solve(expr1, x)
print(sp.evaluate(expr1))
n = eval('x**2 + x - 20')
t = threading.Thread(target=inputSth)
t.start()
# n = eval('2**x + x')
print(sp.latex(sp.integrate(n, x)))
root.mainloop()
